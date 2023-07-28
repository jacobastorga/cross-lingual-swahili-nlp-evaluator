"""
Example: Evaluating Swahili Chain-of-Thought (CoT) Output from Frontier LLM
Demonstrates automated rubric grading for English-to-Swahili technical translation.
"""
from src.cross_lingual_evaluator import CrossLingualEvaluator


def main():
    evaluator = CrossLingualEvaluator()
    
    prompt = "Explain how a computer database organizes relational records."
    
    # Model Candidate A (High Quality, properly localized)
    candidate_a = (
        "Mfumo wa kanzidata hupanga rekodi kwa kutumia jedwali zilizounganishwa "
        "kwa funguo za msingi na funguo geni ili kudumisha uadilifu wa data."
    )
    
    # Model Candidate B (Low Quality, raw English loanwords and code-mixing)
    candidate_b = (
        "Hii database inatumia computer software kuweka tables na algorithm bila utaratibu."
    )
    
    reference = (
        "Kanzidata ya uhusiano hupanga taarifa ndani ya majedwali yenye safu na nguzo, "
        "ikitegemea funguo za msingi kuhakikisha uadilifu na usahihi wa data."
    )
    
    print("==================================================================")
    print("Cross-Lingual Evaluation: English -> Swahili NLP Model Response")
    print("Prompt:", prompt)
    print("==================================================================")
    
    res_a = evaluator.evaluate_translation(prompt, candidate_a, reference)
    print("Candidate A (Localized Kiswahili):")
    print(f"  Overlap:     {res_a['lexical_overlap']}")
    print(f"  Loanwords:   {res_a['unlocalized_loanwords']}")
    print(f"  Fidelity:    {res_a['fidelity_score']}")
    print(f"  Pass:        {res_a['passed_threshold']}")
    
    print("------------------------------------------------------------------")
    res_b = evaluator.evaluate_translation(prompt, candidate_b, reference)
    print("Candidate B (Code-mixed English borrowings):")
    print(f"  Overlap:     {res_b['lexical_overlap']}")
    print(f"  Loanwords:   {res_b['unlocalized_loanwords']}")
    print(f"  Fidelity:    {res_b['fidelity_score']}")
    print(f"  Pass:        {res_b['passed_threshold']}")
    print("==================================================================")


if __name__ == "__main__":
    main()
