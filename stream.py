from dotenv import load_dotenv
from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"

    messages = []

    add_user_message(messages, "Define quantum computing in one sentence")

    with client.messages.stream(
            max_tokens=1024,
            model=model,
            messages=messages
    ) as stream:
        for text in stream.text_stream:
            print(text, end="")


if __name__ == "__main__":
    main()
