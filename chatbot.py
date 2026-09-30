import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = []

print("Chat started. Type 'quit' to exit.")
system_prompt = "You are a friendly Premier League football expert. Keep answers under 3 sentences. Only discuss football."

while True:
    user_input = input("\nYou:  ")

    if user_input == "quit":
        print("Goodbye!")
        break

    # Tas1: add the user's message to the list
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            system=system_prompt,
            messages=messages
        )
        reply = response.content[0].text
        print("\nClaude: ", reply)

        #Task 2: add the AI's reply to the list 
        messages.append({"role": "assistant", "content": reply})

        #Task3: print how many messages are in the list now
        print(f"Message count: {len(messages)}")

    except anthropic.APIError as e:
        print(f"API error: {e}")

