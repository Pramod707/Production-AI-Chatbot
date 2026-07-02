from dotenv import loadenv
from langchain_google_genai import ChatGoogleGenerativeAI

loadenv()

llm = ChatGoogleGenerativeAI(model="google:genai_2.5-flash", temperature=0.2)
