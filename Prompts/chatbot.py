from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
load_dotenv()
model = ChatOpenAI()

chat_history = [SystemMessage(content="You are a helpful chatbot that engages in casual conversation with users.")]

while True:
    user_input = input("Enter your message: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")
print(chat_history)
