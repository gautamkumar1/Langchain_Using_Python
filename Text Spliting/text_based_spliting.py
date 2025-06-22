from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("textpdf.pdf")
docs = loader.load()
text = docs[0].page_content  # Print the content of the first page
text_spliter = CharacterTextSplitter(
    separator="",
    chunk_size=100, # Size of each chunk
    chunk_overlap=0, # Overlap between chunks
)

 # This will only split the one page content loaded above
result = text_spliter.split_text(text) 

result2 = text_spliter.split_documents(docs)  # This will split all the documents loaded above
print(result2[0])
