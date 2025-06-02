# txmedina
# Thomas Medina
#
# This Artificial Intelligent Agent allows the user to leverage its tools 
# to learn new skills

from dotenv import load_dotenv 
from pydantic import BaseModel
from langchain_openai import ChatOpenAI   # allows communication with llm
#from langchain_anthropic import ChatAnthropic   # for claude/other models


load_dotenv()   # env api key

llm = ChatOpenAI(model_name="gpt-4o")  # This is guaranteed to work
# llm2 = ChatAnthropic(<insert claude or other model here>)

response = llm.invoke("Why does the moon have craters?")  # sample input
print(response)