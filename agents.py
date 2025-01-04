from crewai import Agent, LLM
# from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from tools import tool
import openai
load_dotenv()


#call gemini model
# llm=ChatGoogleGenerativeAI(
#     model="gemini-1.5-pro",
#     verbose=True,
#     temperature=0.5,
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
# )

# Replace ChatGoogleGenerativeAI with Ollama LLM
ollama_llm = LLM(
    model='ollama/llama3.2:1b',  # Use your downloaded Ollama model name here
    base_url='http://localhost:11434',  # Default Ollama server URL
    verbose=True,
    temperature=0.5,  # Adjust temperature if needed
)

openai.api_key=os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    verbose=True,
    temperature=0.5,
    openai_api_key=openai.api_key,
)


#creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
    ),
    tools=[tool],
    llm=ollama_llm, # default --> openai
    allow_delegation=True, #communicate with other agents
)


#creating a writer agent with custom tools responsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=ollama_llm, # default --> openai
    allow_delegation=True, #communicate with other agents
)