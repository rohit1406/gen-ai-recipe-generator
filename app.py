from dotenv import load_dotenv
import openai

# Load environment variables from .env file: OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_VERSION
load_dotenv()

# which model to use
deployment_name = "gpt-4o-mini"
# change this to get more textual output as per your needs
max_tokens = 100
# change this to get more creative/varying output as per your needs where 1 being the most variable and 0 being the most deterministic
temperature = 0.5

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
    messages=messages,
    max_tokens=max_tokens,
    temperature=temperature
)

# Print the result
print(completion.choices[0].message.content)

# Create a new prompt with the result from the previous completion
old_prompt_result= completion.choices[0].message.content
prompt = "Produce a shopping list for the generated recipes and please don't include the ingredients that I already have."

new_prompt = f"{old_prompt_result} {prompt}"
messages = [{"role": "user", "content": new_prompt}]
completion = openai.chat.completions.create(
    model=deployment_name,
    messages=messages,
    max_tokens=max_tokens,
    temperature=temperature
)

# Print the result
print("Shopping List:")
print(completion.choices[0].message.content)