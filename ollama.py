from langchain_community.llms import Ollama

llm = Ollama(model='llama3.2')

x=2

while x < 3:

    inp = input('talk to me : ')

    responce = llm.invoke(inp)

    print(responce)
    
