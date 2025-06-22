### What is text spliting
- Text spliting is a proccess of breaking the large text into small-small chunks that LLM will handle effectly.

**1. Length Based Text Splitter**

- Length based text splitter means we have give the one fixed size to break the chunks. like we give the size of spliting chunks after 20 characters then it will divide the each chunks based on 20 words characters.
- It will not have any meaningfull chunking. we cannnot use this for creating any spefic rag based application.

- split_text : This method only split one page text of any pdf or simple text. it will return list of chunks
- split_documents : This method split all the pages of any pdf. it will also return list of chunks

**2. Recursive Text Splitter**

- It use to create meaningfull chunks. 

- It tries to split text:

    1. First by paragraphs (\n\n)

    2. If not possible, then by lines (\n)

    3. Then by sentences (.)

    4. Then by words ( )

    5. Lastly by characters
    
- Example : 

    If we have any text then if u give the chunk size as 10 then it will 1st break the chunks in paragraph then it will check if the world length will be 10 size or not, if not then this process will be continue until the they not found exact size chunk.


