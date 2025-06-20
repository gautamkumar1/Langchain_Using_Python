### What is Structured Output?

- Structured Output means when u ask llm to give the any response in specific format like Json.

- There are two types of structure out model

    1. LLM like Openai when give the instruction their system prompt give out in specfic format then it will give the same format response data. so means it is by default support Structured Output. 
    If any LLM model will support Structured Output by default then we can use **with_structured_output()** method. that is only support by models like OpenAI, Anthropic via tool-calling or JSON mode.

    2. Vice versa if any LLM does not support any Structured Output default then we can use **Output parser** to convert the their response in any format. 

### with_structured_output() 

- In with_structured_output() we can format data in 3 ways.
    1. Typedist
    2. Pydantic
    3. Json Schema

**1. TypeDist**

- Typedist is a simple dictionary with support type. but there is one catch it is only define the type. not support the validation. means if using typedist we define the any user type string then if any user enter the name as integer then it will not give the error. 

