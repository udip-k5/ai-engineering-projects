import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

folder = "articles"
files = os.listdir(folder)

print(f"Found {len(files)} files to process\n")

for filename in files:
    if not filename.endswith(".txt"):
        continue
    # TASK1: Build the full path
    file_path = os.path.join(folder, filename)
    # TASK2: Read the file into a variable called content
    with open(file_path, "r") as file:
        content = file.read()
    #TASK 3: Build the prompt
    prompt = f"Summarize this recent football news article in 2-sentence summary:\n\n{content}"

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        print(f" === {filename} === ")
        print(response.content[0].text)
        print()
        output_path = os.path.join("summaries",filename)
        with open(output_path, "w") as output_file:
            output_file.write(response.content[0].text)

    except anthropic.APIError as e:
        print(f"Error processing {filename}: {e}")