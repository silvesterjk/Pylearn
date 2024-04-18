from langchain_together import Together

llm = Together(
    model="togethercomputer/RedPajama-INCITE-7B-Base",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    together_api_key="eeecd592eb2365831e544995d68830cb357a14bd46283a2de2d965170b29dc6e"
    # TOGETHER_KEY = "eeecd592eb2365831e544995d68830cb357a14bd46283a2de2d965170b29dc6e"

)

input_ = """You are a teacher with a deep knowledge of machine learning and AI. \
You provide succinct and accurate answers. Answer the following question: 

What is a large language model?"""
print(llm.invoke(input_))