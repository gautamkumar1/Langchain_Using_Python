from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
'''
Here:

prompt is a Runnable

model is a Runnable

parser is a Runnable

All connected using | pipe operator!
'''
model = ChatOpenAI()

prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"],
)

parser = StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({"country": "India"})
print(result)
