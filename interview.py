from groq import Groq

client = Groq(
    api_key="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"
)

def generate_question(context):

    prompt = f"""
    Based on the resume information below:

    {context}

    Generate one technical interview question.
    Only return the question.
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