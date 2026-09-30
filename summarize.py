import os
from dotenv import load_dotenv
import anthropic


load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# 1. Read the file into a variable called content
try:
    with open("article.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("article.txt was not found")
    exit()

# 2. Build the prompt using an f-string
prompt = f"Summarize this football article in 200 words as bullet points, for someone new to football:\n\n{content}"

# 3. Send it
try:
    response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
    print(response.content[0].text)
    print("---")
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    
except anthropic.AuthenticationError:
    print("Invalid API Key. Check your .env file")
except anthropic.RateLimitError:
    print("Too many requests. Wait a moment and try again.")
except anthropic.APIError as e:
    print(f"An error occurred: {e}")
    exit()

