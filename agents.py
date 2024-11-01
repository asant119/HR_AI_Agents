from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


"""Agents Summary based on the role and backstory:
    - Each agent is specialized in a specific task
    - Each agent has a unique goal and backstory
    - Each agent has a set of tools that it can use to complete its task
    - Each agent can delegate tasks to other agents

    HR Analyst is responsible for searching the web for job postings for similar positions and extract requirements
    Manager is responsible for defining the job description, ensuring it clearly communicates the key responsibilities,
    required skills, and qualifications to attract top talent.
    Writer is responsible for drafting a well-structured job description for the position
    Quality Assurance is responsible for reviewing the job description for the {role} to ensure high quality results
"""

class HR_Agents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)


    def Benchmark(self, role, inputs):
        return Agent(
            role="HR Analyst",
            goal=f"Use the {role} and {inputs} to search the web and find job postings for similar positions and extract requirements",
            backstory=f"""You are a HR analyst with deep understanding on the {role} position.
                You're tasked to search online for positions similar to the {role}.
                Based on your search you will scrape the most relevant options and extract requirements for the position.
                Your result will be passed to the Manager for further refinement and definition of the final requirements for the {role}""",
            allow_delegation=False,
            verbose=True,
            tools=[scrape_tool, search_tool],
            llm=self.OpenAIGPT35
        )
    

    def Manager(self, role, inputs):
        return Agent(
            role="Technical Hiring Manager",
            goal=f"""Define and provide detailed job descriptions, including key responsibilities, qualifications, and required skills based on {inputs} for the {role}""",
            backstory=f"""You are a hiring manager with deep understanding on the {role} position.
                You're tasked with hiring for a critical position in the company: {role}.
                You have a deep understanding of the company’s goals, culture, and the specific needs of the department.
                Your role is to define the job description, ensuring it clearly communicates the key responsibilities, required skills,
                and qualifications to attract top talent. Your work sets the foundation for the recruitment process,
                ensuring only candidates with the right experience and cultural fit are considered for the role.""",
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4
        )
    

    def Writer(self, role):
        return Agent(
            role="Senior HR Analyst",
            goal=f"Write a clear and compelling job description for the position: {role}",
            backstory=f"""You are a HR analyst specialized in writting job descriptions.
                You're responsible for drafting a well-structured job description for the position: {role}.
                You base your writing on the information provided by the Hiring Manager, who has outlined the key responsibilities,
                required skills, and qualifications for the role. Your task is to turn that information into a clear, engaging,
                and precise job description that effectively communicates the expectations of the role and attracts the right candidates.
                You ensure the tone reflects the company's culture, and you make sure the description is both detailed and easy to understand.""",
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4
        )
    

    def Quality_Assurance(self, role):
        return Agent(
            role="Senior Quality Assurance Analyst",
            goal=f"Review the job description for the {role} to ensure high quality results",
            backstory=f"""You are a senior QA analyst specialized in reviewing job descriptions.
                You're responsible to ensure the job description for the {role} addressed the key requirements listed by the technical hiring manager.
                You ensure the tone reflects the company's culture, and you make sure the description is both detailed and easy to understand.
                Assess the results for grammar and factual elements.""",
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT4
        )
