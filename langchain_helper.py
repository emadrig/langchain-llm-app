from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.8)

    prompt_template_name = PromptTemplate(
        input_variables = ["animal_type", "pet_color"],
        template="I have a pet {animal_type} that is {pet_color}and I want a cool name for it, Suggest 5 cool names for my pet that are related to it's species"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")
    response = name_chain({"animal_type": animal_type, "pet_color":pet_color})

    return response

def langchain_agent():
    llm = OpenAI(temperature=0.8)
    tools = load_tools(["llm-math", "wikipedia"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.invoke(
        "What is the average age of a dog? Tell me the age of the dog, and then multiply the age by 3"
    )
    print(result)

if __name__ == "__main__":
    # print(generate_pet_name("cow", "blue"))
    langchain_agent()
