from groq import Groq

client = Groq(
    api_key="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"
)

def evaluate(question, answer):

    prompt = f"""
    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    1. Score out of 10
    2. Strengths
    3. Areas for Improvement
    4. Final Feedback
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content