### What are Runnables?

- LangChain made everything (like prompts, LLMs, chains, tools) act like a Runnable — so you can connect them like pipes .

###  Why use Runnables?

- Runnables make your code:
    1. Clean
    2. Easy to reuse
    3. Easy to run in parallel, sequence, or with custom logic

###  Basic Runnable Flow
```
Input --> Runnable1 --> Output1 --> Runnable2 --> Final Output
```
- Each step can be:

    ➤ A Prompt

    ➤ A Model

    ➤ A Parser

    ➤ A Function

    ➤ Full Chain
- We can also connect Runnable1 to Runnable2 it will automatically goes Runnable1 output in Runnable2

### Types of Runnables
**1. RunnableSequence**
- Do steps one after another 🔁 (same as chaining using |)
