import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)
while True:
    message = input("Ask the baby...")
    completion = client.chat.completions.create(
        model="grok-3",
        messages=[
            {
                "role": "system",
                "content": "You are a baby. You talk in baby. That's all.",
            },
            {"role": "user", "content": message},
        ],
        temperature=1.0,
    )

    print(completion.choices[0].message.content)
