from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def claude_response(prompt: str) -> str:
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
