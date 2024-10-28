from crewai import Crew
from textwrap import dedent
from agents import HRAgent
from tasks import HR_Task


from dotenv import load_dotenv
load_dotenv()

inputs={}
inputs["role"] = str(input("Enter the role: "))
inputs["inputs"] = str(input("Enter a brief description of the role: "))

crew = Crew(
    agents=[HRAgent()],
    tasks=[HR_Task()],
    verbose=2,
    memory=True,
)

result = crew.kickoff(inputs)

from IPython.display import Markdown
Markdown(result)