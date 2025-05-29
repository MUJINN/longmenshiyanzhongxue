from ..core.ai.grading_model import auto_grade_question
import json

def grade_submission(answers, correct_answers):
    total_score = 0.0
    feedback = {}

    for qid, student_answer in answers.items():
        correct_answer = correct_answers.get(qid)
        if not correct_answer:
            continue

        try:
            grading_result = auto_grade_question(qid, student_answer, correct_answer)
            parsed_result = json.loads(grading_result)
        except Exception as e:
            raise RuntimeError(f"Grading failed for question {qid}: {str(e)}")

        total_score += parsed_result["score"]
        feedback[qid] = parsed_result["feedback"]

    average_score = total_score / len(correct_answers) if correct_answers else 0.0
    return {
        "average_score": round(average_score, 2),
        "feedback": feedback
    }