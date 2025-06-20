from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

message = [
    SystemMessage(content="You are a helpful assistant that translates English to Hindi."),
    HumanMessage(content="I love programming."),
]

response = model.invoke(message)
message.append(AIMessage(content=response.content))
print(message)