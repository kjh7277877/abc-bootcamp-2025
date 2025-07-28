from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input="make python code for factorial",
    stream=True,
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="", flush=True)