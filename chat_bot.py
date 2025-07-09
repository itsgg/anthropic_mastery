from dotenv import load_dotenv
from anthropic import Anthropic
import anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(client, model, messages):
    try:
        message = client.messages.create(
            model=model,
            max_tokens=100,
            messages=messages
        )
        return message.content[0].text
    except (anthropic.APIError, anthropic.OverloadedError, anthropic.RateLimitError) as e:
        print(f"Error: {e}")
        return "Sorry, I'm having trouble responding right now. Please try again later."


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"

    messages = []

    while True:
        message = input("Enter message: ")
        print(message)
        add_user_message(messages, message)
        answer = chat(client, model, messages)
        add_assistant_message(messages, answer)
        print(answer)


if __name__ == "__main__":
    main()
