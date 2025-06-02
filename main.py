# txmedina
# Thomas Medina
#
# This Artificial Intelligent Agent allows the user to leverage its tools 
# to learn new skills

from dotenv import load_dotenv 
from pydantic import BaseModel
from langchain_openai import ChatOpenAI   # allows communication with llm
#from langchain_anthropic import ChatAnthropic   # for claude/other models
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()   # env api key

# prompt template class:
# contains adjustable fields for desirable output from LLM

class AssistantResponse(BaseModel):   
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model_name="gpt-4o")
# llm2 = ChatAnthropic(<insert claude or other model here>)
parser = PydanticOutputParser(pydantic_object=AssistantResponse)


# prompt template via LangChain website
# configure to change how Agent will interact with user

ai_identity = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI Agent and will answer every request of mine.
            Use necessary tools to answer user query
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())