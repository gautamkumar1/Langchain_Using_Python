from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("textpdf.pdf") 
docs = loader.load()
print(len(docs)) 