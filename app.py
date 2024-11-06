from crewai import Crew
from agents import HR_Agents
from tasks import HR_Tasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get user input for the role and description
role = str(input('Enter the role title: '))
inputs = str(input('Enter a brief description for the position: ')) 

class HRCrew:
    def __init__(self, role, inputs):
        self.role = role
        self.inputs = inputs

    def run(self):
        # Instantiate the agents
        hr_agents = HR_Agents()
        
        # Create instances of each agent
        analyst = hr_agents.benchmark(self.role, self.inputs)
        manager = hr_agents.manager(self.role, self.inputs)
        writer = hr_agents.writer(self.role)
        qa = hr_agents.quality_assurance(self.role)

        # Instantiate tasks
        hr_tasks = HR_Tasks()
        
        # Step-by-step instantiation of tasks and setting contexts
        search_task = hr_tasks.search_web(agent=analyst, role=self.role, inputs=self.inputs)
        
        requirements_task = hr_tasks.job_requirements(agent=manager, role=self.role, inputs=self.inputs)
        requirements_task.set_context([search_task])

        writing_task = hr_tasks.writing(agent=writer, role=self.role)
        writing_task.set_context([search_task, requirements_task])

        qa_task = hr_tasks.quality_assurance(agent=qa, role=self.role)
        qa_task.set_context([search_task, requirements_task, writing_task])

        # Define the crew with the agents and tasks
        crew = Crew(
            agents=[analyst, manager, writer, qa],
            tasks=[search_task, requirements_task, writing_task, qa_task],
            verbose=True,
        )

        # Kick off the crew process and return the result
        result = crew.kickoff(inputs={"role": self.role, "description": self.inputs})
        return result

if __name__ == "__main__":
    print("## Welcome to HR Job Description Assistant")
    print('-------------------------------')

    hr_crew = HRCrew(role, inputs)
    result = hr_crew.run()
    print(result)
