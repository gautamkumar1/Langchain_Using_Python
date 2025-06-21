### Chains

- It allows us to connect multiple steps (like prompts, LLMs, tools, etc.) together — this is called a Chain.

### Why Chains?

- Chains help you:

    1. Break a big task into small parts.

    2. Control what happens step by step.

    3. Combine tools (like prompts + LLM + memory).

### Types of Chains in LangChain

- Simple Chain
- Sequential Chain
- Parallel Chain
- Condinational Chain

**1. Simple chain**
- Simple chain means it is goes linear way like this 
    prompt -> model -> parser


**2. Sequential Chain**
- Sequential chains means You want multiple inputs and outputs in steps.
    User input -> Report(Give LLM) -> Print -> One more(LLM Call for Extract 5 main points from report) -> Print -> End
    chain = prompt1 | model | parser | prompt2 | model | parser
    
**3. Parallel Chain**
- Parallel Chain means we have run multiple LLM or same LLM parallel. like when we want to one LLM to generate notes and 2nd LLM will be generate questions based on generated notes then we have use 3rd LLM to merge them. so it is called Parallel Chain.

- In Langchain we can use from **langchain_core.runnables** library .




