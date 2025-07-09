from dotenv import load_dotenv
from anthropic import Anthropic
import anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(client, model, messages, system_prompt=None):
    params = {
        "model": model,
        "max_tokens": 100,
        "messages": messages
    }

    if system_prompt is not None:
        params["system"] = system_prompt

    try:
        message = client.messages.create(**params)
        return message.content[0].text
    except (anthropic.APIError,
            anthropic.OverloadedError,
            anthropic.RateLimitError) as e:
        print(f"Error: {e}")
        return "Please try again later."


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"

    messages = []

    system_prompt = """
    You are a patient math tutor. Do not directly answer a student's question.
    Guide them to a solution step by step.
    """

    while True:
        message = input("Enter message: ")
        print(message)
        add_user_message(messages, message)
        answer = chat(client, model, messages, system_prompt)
        add_assistant_message(messages, answer)
        print(answer)


if __name__ == "__main__":
    main()
