from groq import Groq

client = Groq(
    api_key="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"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(response.choices[0].message.content)