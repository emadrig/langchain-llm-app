from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.6)
    name = llm("I have ")
