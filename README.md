# Cross-Lingual Swahili NLP Evaluator

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Language: Swahili / Kiswahili](https://img.shields.io/badge/Language-Kiswahili%20(Swahili)-brightgreen.svg)](#)

A cross-lingual evaluation harness and verification pipeline for benchmarking English-to-Swahili foundation model translations, grammatical concord compliance, semantic alignment, and low-resource reasoning fidelity.

---

## Motivation

Frontier LLMs frequently encounter severe degeneration, unnatural code-mixing, and grammatical concord collapse when handling low-resource and African Bantu languages such as Swahili (Kiswahili). This framework provides deterministic scoring, morphological parsing, and bilingual alignment auditing to evaluate and improve AI model outputs for cross-lingual tasks.

---

## Key Capabilities

- **Bantu Grammatical Concord Verification**: Validates noun-class prefixes (Classes 1–10: M/WA, KI/VI, N/N) against verb subject markers ($a-$, $wa-$, $ki-$, $vi-$) to flag hallucinated grammatical structures.
- **Semantic Fidelity & Overlap Scoring**: Calculates lexical n-gram coverage and semantic fidelity against human-annotated references.
- **Unlocalized Borrowing & Code-Mixing Detection**: Detects un-translated English jargon and flags missed domain localizations (e.g., *database* $\to$ *kanzidata*, *artificial intelligence* $\to$ *akili mnemba*).
- **Chain-of-Thought (CoT) Auditing**: Evaluates multi-step mathematical and scientific explanations translated into Swahili for RLHF/DPO preference curation.

---

## Installation & Testing

```bash
git clone https://github.com/jacobastorga/cross-lingual-swahili-nlp-evaluator.git
cd cross-lingual-swahili-nlp-evaluator
pip install -r requirements.txt
python -m unittest discover tests
```

---

## Running the Benchmark Example

```bash
python examples/evaluate_swahili_reasoning.py
```

---

## Author

**Jacob Astorga**  
BS in Mechanical Engineering (UTEP) | BS in Software Development (Dallas College)  
Advanced Swahili (Kiswahili) Bilingual Evaluation Specialist  
GitHub: [@jacobastorga](https://github.com/jacobastorga)
