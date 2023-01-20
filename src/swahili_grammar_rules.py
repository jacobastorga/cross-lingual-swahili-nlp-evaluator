"""
Swahili (Kiswahili) Grammatical Concord and Morphology Rules
Evaluates Bantu noun classes and agreement concord prefixes in generated text.
"""
from typing import Dict, List, Tuple


# Primary Swahili Noun Classes and characteristic prefixes
NOUN_CLASSES = {
    "Class 1 (M-)": {"prefix": "m", "subject_prefix": "a", "plural": "Class 2 (WA-)"},
    "Class 2 (WA-)": {"prefix": "wa", "subject_prefix": "wa", "singular": "Class 1 (M-)"},
    "Class 7 (KI-)": {"prefix": "ki", "subject_prefix": "ki", "plural": "Class 8 (VI-)"},
    "Class 8 (VI-)": {"prefix": "vi", "subject_prefix": "vi", "singular": "Class 7 (KI-)"},
    "Class 9 (N-)": {"prefix": "", "subject_prefix": "i", "plural": "Class 10 (N-)"},
    "Class 10 (N-)": {"prefix": "", "subject_prefix": "zi", "singular": "Class 9 (N-)"},
}

# Tense Infixes in Standard Swahili
TENSE_MARKERS = {
    "na": "present continuous",
    "li": "past definite",
    "ta": "future",
    "me": "present perfect",
    "ki": "conditional / participle",
    "nge": "hypothetical conditional"
}


def verify_subject_verb_concord(subject_noun: str, verb: str, noun_class: str) -> bool:
    """
    Verifies that the Swahili verb contains the appropriate subject concord prefix
    matching the grammatical noun class.
    Example: 'Mtoto anasoma' -> Class 1 (M-) matches 'a-' prefix.
    """
    if noun_class not in NOUN_CLASSES:
        return False
    
    expected_prefix = NOUN_CLASSES[noun_class]["subject_prefix"]
    verb_lower = verb.lower().strip()
    return verb_lower.startswith(expected_prefix)
