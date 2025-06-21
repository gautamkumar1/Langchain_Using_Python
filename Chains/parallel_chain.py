from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
prompt1 = PromptTemplate(
    template="Describe the this topic in detail: {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a 5 five question about the topic: {topic}.",
    input_variables=["topic"],
)

prompt3 = PromptTemplate(
    template="Give the details about the topic: {topic} and the questions: {questions}.",
    input_variables=["topic", "questions"],
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "topic": lambda x: x["topic"], # Pass the topic to both prompts
        "details": prompt1 | model1 | parser,
        "questions": prompt2 | model1 | parser,
    }
)

merged_chain = prompt3 | model1 | parser

chain = parallel_chain | merged_chain

result = chain.invoke({"topic": "nodejs"})
print(result)
chain.get_graph().print_ascii()