from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant customer support agent for a tech company.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}'),
])

# Load chat history from a file
chat_history = []
with open("chat_history.txt") as file:
    chat_history.extend(file.readlines())

print(chat_history)

# Create a prompt with the chat history and a new user query

prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query': 'What is my refund status?'
})

result = model.invoke(prompt)
print(result.content)