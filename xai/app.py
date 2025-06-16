import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)
chat_messages = []
chat_messages.append(
    {
        "role": "system",
        "content": "You are a baby. You talk in baby. That's all.",
    },
)
while True:
    message = input("Ask the baby...")
    chat_messages.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="grok-3",
        messages=chat_messages,
        temperature=1.0,
    )
    chat_messages.append(
        {
            "role": completion.choices[0].message.role,
            "content": completion.choices[0].message.content,
        }
    )
    print(completion.choices[0].message.content)
