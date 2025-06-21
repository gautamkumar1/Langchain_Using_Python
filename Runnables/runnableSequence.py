from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()

model = ChatOpenAI()
prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"],
)
parser = StrOutputParser()
chain = RunnableSequence([prompt, model, parser])
result = chain.invoke({"country": "India"})
print(result)  