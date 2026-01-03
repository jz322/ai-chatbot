import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions
from functions.call_function import call_function
from config import MAX_ITERS

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    for i in range(MAX_ITERS):
        response = client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        function_results_list = []
        if args.verbose:
            print(f"User prompt: {messages}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                if not function_call_result.parts:
                    raise Exception("No parts list")
                if function_call_result.parts[0].function_response == None:
                    raise Exception("No response object")
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception("No actual response")
                function_results_list.append(function_call_result.parts[0])

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                
            messages.append(types.Content(role="user", parts=function_results_list))

        else:
            print("Response:")
            print(response.text)
            break
        if i == 19:
            print("AI could not solve.")
            exit(1)


if __name__ == "__main__":
    main()
