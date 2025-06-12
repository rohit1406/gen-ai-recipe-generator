from dotenv import load_dotenv
import openai

# Load environment variables from .env file:: OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_VERSION
load_dotenv()

deployment_name = "gpt-4o-mini"

# Add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

# Make Completion
completion = openai.chat.completions.create(
    model=deployment_name,
    messages=messages
)

# print the response
print(completion.choices[0].message.content)
