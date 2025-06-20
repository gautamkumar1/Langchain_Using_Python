### What is a Prompt?
- Prompt is a set of instruction that you send to LLM.
### Why use Prompts in LangChain?
- We can use the same prompt in different file means reusable.
- It  is clean and easy to maintain.

### There are two types of prompts
- Static Prompt : A prompt is fixed message that does not change.

    Example : 

    prompt = "Write a short poem about the moon."

- Dynamic Prompt : A dynamic prompt is a message that has blanks (placeholders).
    1. You can fill it with different values.
    2. Useful when you want to customize the prompt.

    **Note :** PromptTemplate We can only use when we sending the only single message (without any chat history) means we can only use the PromptTemplate when we sending user input one time as dynamic after that chat is close.Only use for single time conversation.

    **Note:** We can use the chat prompt template when you sending list of message dynamic with chat history and chat going utill we manullay not close. Use for multi time conversation. 

    Example :
    ```
    from langchain.prompts import PromptTemplate

    prompt = PromptTemplate(
        template="Write a short poem about {topic}."
        input_variables=["topic"],
    )
    ```
### How we can give the memory or chat history to the LLM.

- There is 2 way to do this

    **1. Doing Manullay : -**  Means storing the user input and ai response each time in an array then send it to the llm but in this approach when our chat history become long then it is not work properly bcz llm will not able not indentified which message is user input or their himself response. so this is not suitable for prod. we can only use this method only for testing purpose.

    **2. Utilizing  Langchain message functionality :  -** Langchain already solved this problem.(from langchain_core.messages import AIMessage, HumanMessage, SystemMessage).

    - SystemMessage - Predefined ai behaviour.

    - HumanMessage - User input that goes to LLM.

    - AIMessage - LLM resposne.

    Previously in step 1 we are simply storing the user inut and llm reponse without any identifiying which is user input or which is ai response. for above method we can solve this problem. with this llm will able to indentify which message is user or which message is llm. 

    Example  : 

    ```
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
    ```

### MessagesPlaceholder 
- We are MessagesPlaceholder in chat prompts tempalate to adding list of message for chat history. 

