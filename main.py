import os
from dotenv import load_dotenv
from anthropic import Anthropic


def main():
    load_dotenv()

    client = Anthropic()
    model = "claude-sonnet-4-0"


if __name__ == "__main__":
    main()
