import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

model = ChatOpenAI(api_key=api_key,model="gpt-4o-mini")

chain = prompt | model | StrOutputParser()

response = chain.invoke({"topic": "Bear"})
print(response)





