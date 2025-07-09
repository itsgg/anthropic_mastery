from dotenv import load_dotenv
from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(client, model, messages):
    message = client.messages.create(
        model=model,
        max_tokens=100,
        messages=messages
    )

    return message.content[0].text


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"

    messages = []

    add_user_message(messages, "Define quantum computing in one sentence")
    answer = chat(client, model, messages)
    print(answer)

    add_assistant_message(messages, answer)
    add_user_message(messages, "Write another sentence")

    print(chat(client, model, messages))


if __name__ == "__main__":
    main()
