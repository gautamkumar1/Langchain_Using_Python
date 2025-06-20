from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

'''
PROJECT DESCRIPTION:
User input -> Report(Give LLM) -> Print -> One more(LLM Call for Extract 5 main points from report) -> Print -> End
'''
prompt1 = PromptTemplate(
    template="Generate a detail report about {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Extract 5 main points from the report: {report}.",
    input_variables=["report"],
)

model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Sex"})
print(result)

