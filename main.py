import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py "your prompt here"')
        sys.exit(1)

    prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY is not set in the environment.")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(f"{response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
