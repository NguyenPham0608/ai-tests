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
        "content": 'You are a molecule generator. You generate the molecule the prompt asks with the greatest accuracy. You will generate a JSON file that contains the molecule data. Put it in this exact format: (DO NO CHANGE ANTYHING ABOUT THE FORMAT). Example 1: {"atomData": [{"element": "C", "x": 0.000, "y": 1.396, "z": 0.000},{"element": "H", "x": 1.209, "y": 0.698, "z": 0.000},{"element": "O", "x": 1.209, "y": -0.698, "z": 0.000}],"numAtoms": 3} Example 2: {"atomData": [{"element": "C", "x": 0.000, "y": 1.396, "z": 0.000},{"element": "C", "x": 1.309, "y": 0.498, "z": 0.200},{"element": "O", "x": 1.209, "y": -0.698, "z": 2.014},{"element": "N", "x": 0.209, "y": -0.633, "z": 1.020},{"element": "S", "x": 1.119, "y": -0.491, "z": 6.025}],"numAtoms": 5}  ONLY GENERATE THE MOLECULE JSON FILE IN THE GIVEN EXAMPLE FORMATS AND NOTHING ELSE',
    },
)
while True:
    message = input("Ask the baby...")
    chat_messages.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="grok-3-latest",
        messages=chat_messages,
        temperature=0.0,
    )
    chat_messages.append(
        {
            "role": completion.choices[0].message.role,
            "content": completion.choices[0].message.content,
        }
    )
    print(completion.choices[0].message.content)
