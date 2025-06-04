Setup in VSCode:

python -m venv .venv  
source .venv\Scripts\activate # or .venv/bin/activate on Linux  
pip install -r requirements.txt  

Also requires a file called .env (no suffix) with text:  

OPENAI_API_KEY={insert OpenAI API key here}
