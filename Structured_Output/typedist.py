from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()

model = ChatOpenAI(
    model="gpt-4o",
)

# Schema for structured output

class Review(TypedDict):
    summary: str
    sentiment: str
# Example usage of the model with structured output

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("""This method takes a schema as input which specifies the names, types, and descriptions of the desired output attributes. The method returns a model-like Runnable, except that instead of outputting strings or messages it outputs objects corresponding to the given schema. The schema can be specified as a TypedDict class, JSON Schema or a Pydantic class. If TypedDict or JSON Schema are used then a dictionary will be returned by the Runnable, and if a Pydantic class is used then a Pydantic object will be returned.

""")

print(result)