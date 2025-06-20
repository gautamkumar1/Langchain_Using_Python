from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant in spefic {domain}'),
    ('human', 'Tell me about {topic}')
])

prompt = chat_template.invoke({
    "domain": "Python programming",
    "topic": "decorators"
})

print(prompt)