from langchain_community.document_loaders import WebBaseLoader

url = "https://daily.dev/blog/node-js-programming-language-basics"
loader = WebBaseLoader(url)
docs = loader.load()
print(len(docs))
print(docs[0].page_content)