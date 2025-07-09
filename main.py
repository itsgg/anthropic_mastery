import os
from dotenv import load_dotenv
from anthropic import Anthropic


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"
    message = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "What is quantum computing? Answer in one sentence."
            }
        ]
    )

    print(message.content[0].text)


if __name__ == "__main__":
    main()
