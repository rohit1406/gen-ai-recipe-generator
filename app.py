from dotenv import load_dotenv
import openai

# Load environment variables from .env file: OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_VERSION
load_dotenv()

deployment_name = "gpt-4o-mini"

# Add your completion code
# Number of recipes to generate
no_recipes = input("No of recipes to generate (for example: 3): ")
ingredients = input("List of ingredients (for example: chicken, potatoes, carrots): ")
filter = input("Filter (for example: vegetarian, vegan, gluten-free): ")
# Interpolate the prompt with number of recipes and ingredients
prompt = f"Show me {no_recipes} recipes for a dish with following ingredients: {ingredients}" \
f"Per recipe, list all ingredients used, no instructions, and no {filter}." 
messages = [{"role": "user", "content": prompt}]

# Make Completion
completion = openai.chat.completions.create(
    model=deployment_name,
    messages=messages
)

# print the response
print(completion.choices[0].message.content)
