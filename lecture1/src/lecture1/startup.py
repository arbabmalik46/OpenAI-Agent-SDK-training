from dotenv import load_dotenv
import os
from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

external_client = AsyncOpenAI(api_key=API_KEY,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
modeldefined = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=external_client)
set_tracing_disabled(True)
def main():
    agent = Agent(name="Arbab",instructions="You are a dotnet instructor",model=modeldefined)
    result = Runner.run_sync(agent,"I want to create a website tell me best thing about why should I develop it in dotnet and not in any other language?. create a readme.md file and Write the answer into the readme.md file")
    print(result.final_output)