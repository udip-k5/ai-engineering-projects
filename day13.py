import os
import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

ticket = "Hi, could you update my email address when you get a chance? Thanks, John."


prompt = f"""Classify this support ticket.

Respond with ONLY valid JSON in exactly this format:
{{"urgency": "HIGH or MEDIUM or LOW", "category": "technical or billing or general", "customer_name": "Customer Name"}}

Do not include any explanation or text outside the JSON.

Ticket: {ticket}"""


try:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    raw_text = response.content[0].text
    print("DEBUG:", raw_text)
    data = json.loads(raw_text)

    print("Urgency:", data.get("urgency", "UNKNOWN"))
    print("Category:", data.get("category", "UNKNOWN"))
    print("Customer:", data.get("customer_name", "UNKNOWN"))

except anthropic.APIError as e:
    print(f"API error: {e}")
    exit()
