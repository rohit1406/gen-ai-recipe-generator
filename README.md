### Description
**This is a console based Python application and uses OpenAI as a LLM.**  
This application is a recipe generator application responsible to return the recipes for the ingredients you have along with instruction on how to prepare the dish. In the end it also shows the shopping list for the ingredients you don't have.

When run, it asks for following inputs from user:
1. Number of recipes (for example: 5)
2. Ingredients (for example: Milk, Strawberry)
3. Filter some of the ingredients which you don't like, allergic to, don't want, etc(for example: Sugar)

### Create a .env file for Environment variables
Following environment variables are set to run this application.
1. OPENAI_API_KEY=<'API key to use to connect to OpenAI'> --> You need get this key from your OpenAI provider.
2. OPENAI_API_TYPE=openai

### How to Run
1. Clone this repository (https://github.com/rohit1406/genai-recipe-generator.git)
2. Open command prompt -> cd to the project folder where you cloned this repository
3. Create a virtual environment and install dependent libraries
```
python -m venv venv
venv\Scripts\activate ( for windows OS )
pip install openai (Makes it easy to connect to OpenAI LLM)
pip install dotenv (To load environment variables)
```
4. Run the application: python .\app.py


### Prerequisites
1. Python (version 3.13.3 used for this application)
2. Any text editor or Visual Studio Code or any preferred IDE