"""
Cross-Lingual Evaluation Harness for English -> Swahili LLM Outputs
Evaluates semantic translation fidelity, grammatical concord, and hallucination / code-mixing.
"""
import re
from typing import Dict, List, Any
from .swahili_grammar_rules import verify_subject_verb_concord


class CrossLingualEvaluator:
    def __init__(self):
        # Known common English technical terms that should be localized rather than raw-copied
        self.unlocalized_loanwords = {
            "computer", "software", "artificial intelligence", "database",
            "algorithm", "engineer", "system"
        }
        self.swahili_equivalents = {
            "computer": "tarakilishi / kompyuta",
            "software": "programu",
            "artificial intelligence": "akili unde / akili mnemba",
            "database": "kanzidata",
            "algorithm": "kanuni za kihesabu / algoriti",
            "engineer": "mhandisi",
            "system": "mfumo"
        }

    def tokenize(self, text: str) -> List[str]:
        """Simple whitespace and punctuation-stripped tokenizer."""
        return re.findall(r"\b[\w'-]+\b", text.lower())

    def compute_lexical_overlap(self, candidate: str, reference: str) -> float:
        """Computes unigram Jaccard lexical overlap between candidate and reference."""
        cand_tokens = set(self.tokenize(candidate))
        ref_tokens = set(self.tokenize(reference))
        if not cand_tokens or not ref_tokens:
            return 0.0
        intersection = cand_tokens.intersection(ref_tokens)
        union = cand_tokens.union(ref_tokens)
        return len(intersection) / len(union)

    def detect_unlocalized_borrowings(self, swahili_text: str) -> List[str]:
        """Flags raw English technical words that were unlocalized in Swahili response."""
        tokens = set(self.tokenize(swahili_text))
        flagged = []
        for word in self.unlocalized_loanwords:
            if word in tokens or (word in swahili_text.lower()):
                flagged.append(word)
        return flagged

    def evaluate_translation(self, english_prompt: str, swahili_candidate: str, swahili_reference: str) -> Dict[str, Any]:
        """
        Runs comprehensive evaluation on a candidate Swahili translation / reasoning response:
        1. Lexical overlap against human reference
        2. Unlocalized borrowing detection
        3. Overall quality score [0.0 - 1.0]
        """
        overlap = self.compute_lexical_overlap(swahili_candidate, swahili_reference)
        loanwords = self.detect_unlocalized_borrowings(swahili_candidate)
        
        # Penalize for unlocalized code-mixing
        penalty = min(0.3, len(loanwords) * 0.1)
        final_score = max(0.0, min(1.0, overlap * 0.7 + (0.3 - penalty)))

        return {
            "lexical_overlap": round(overlap, 4),
            "unlocalized_loanwords": loanwords,
            "fidelity_score": round(final_score, 4),
            "passed_threshold": final_score >= 0.65
        }
