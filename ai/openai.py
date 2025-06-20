import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
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
        model="gpt-4.1",
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
