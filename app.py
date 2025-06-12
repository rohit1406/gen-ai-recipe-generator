from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI()
response = client.responses.create(
    model="gpt-4o-mini",
    input="Once upon a time there was a"
)
print(response.output_text)
