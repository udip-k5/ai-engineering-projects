# AI Engineering Projects

Python tools I built while learning to work with the Claude API.

## Projects

### Article Summarizer (summarize.py)
Reads an article from a text file and returns a bullet-point summary
written for a beginner audience.

### Support Ticket Classifier (day13.py)
Takes a free-text support ticket and returns structured JSON with the
urgency level, category, and customer name, so it could be routed
automatically.

### Chatbot with Memory (chatbot.py)
A terminal chatbot that holds a multi-turn conversation. The Claude API
is stateless, so the message history is stored in a list and resent with
every request.

## Tech Used
- Python
- Claude API (Anthropic)
- python-dotenv for environment variables

## Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install anthropic python-dotenv`
4. Create a `.env` file with your API key:
   `ANTHROPIC_API_KEY=your-key-here`
5. Run any script: `python3 summarize.py`
