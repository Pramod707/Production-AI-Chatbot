from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:7b")
stream = llm.stream("what is docker")
for chunk in stream:
    print(chunk.content, flush=True, end="")
