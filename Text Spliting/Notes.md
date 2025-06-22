### What is text spliting
- Text spliting is a proccess of breaking the large text into small-small chunks that LLM will handle effectly.

**1. Length Based Text Splitter**

- Length based text splitter means we have give the one fixed size to break the chunks. like we give the size of spliting chunks after 20 characters then it will divide the each chunks based on 20 words characters.
- It will not have any meaningfull chunking. we cannnot use this for creating any spefic rag based application.

- split_text : This method only split one page text of any pdf or simple text. it will return list of chunks
- split_documents : This method split all the pages of any pdf. it will also return list of chunks

