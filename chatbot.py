import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    print("Error: No API key found in .env file.\nCheck your .env file")
    exit()

client = OpenAI()

print("Hello! I am your simple chatbot. Type 'quit' anytime to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("Chatbot: Bye! Have a great day!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=200
        )
        bot_reply = response.choices[0].message["content"]
        print("Chatbot:", bot_reply)

    except Exception as e:
        print("Oops! Something went wrong:", e)
