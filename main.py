import os
import sys
import argparse
from dotenv import load_dotenv

from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Prompt text to send to LLM model", type=str)
    parser.add_argument(
        "-v",
        "--verbose",
        help="Verbosity: Print user prompt, and user/response tokens in output",
        required=False,
        action="store_true",
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found. Check .env for typos and an API key exists")

    if not api_key:
        print("Error: GEMINI_API_KEY is not set in the environment.")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(f"{response.text}")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
