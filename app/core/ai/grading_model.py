import openai
import os
from app.config import settings

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY
)

def auto_grade_question(question: str, student_answer: str, correct_answer: str = None):
    prompt = f"""
你是一个教师，请根据以下题目和参考答案，对学生的回答进行评分。
题目：{question}
学生回答：{student_answer}
标准答案：{correct_answer}

请返回一个 JSON 格式的结果：
- score: float (0~1)
- feedback: str (评语)
"""

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")