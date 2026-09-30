import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    extra_body={"temperature": 0},
    messages=[
        {"role": "user", "content": "Invent a name for a Premier League podcast."}
    ]
)

print(response.content[0].text)
print("---")
print("Stop reason:", response.stop_reason)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)