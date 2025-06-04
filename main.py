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
from langchain.agents import create_tool_calling_agent, AgentExecutor


load_dotenv()   # env api key

# prompt template class:
# contains adjustable fields for desirable output from LLM

class AssistantResponse(BaseModel):   
    topic: str
    summary: str
    # sources: list[str]   for web search services 
    # tools_used: list[str]   tools that are used in search

llm = ChatOpenAI(model_name="gpt-4o")
# llm2 = ChatAnthropic(<insert claude or other model here>)
parser = PydanticOutputParser(pydantic_object=AssistantResponse)


# prompt template via LangChain website
# configure to change how Agent will interact with user

prompt = ChatPromptTemplate.from_messages(
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
        ("human", "{query}"),  # here we can pass multiple types of data in from user
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = []   # insert AI agent tools from tools.py
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# need for execution of agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # true = see process of Agent
query = input("How may I help you? ")
response = agent_executor.invoke({"query": query})
print(response)

# parses information from class
#
#try:
#    parsed_response = parser.parse( response.get("output")[0]["text"])
#except Exception as e:
#    print("There was an ERROR parsing response", e, "Reponse - ", response  )