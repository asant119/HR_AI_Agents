from crewai import Crew
from agents import HR_Agents
from tasks import HR_Tasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

role = str(input('Enter the role title: '))
inputs = str(input('Enter a brief description for the position: ')) 

class HRCrew:
    def __init__(self, role, inputs):
        self.role = role
        self.inputs = inputs

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = HR_Agents()
        tasks = HR_Tasks()

        # Define your custom agents and tasks here
        benchmarker = agents.Benchmark()
        manager = agents.Manager()
        writer = agents.Writer()
        qa = agents.Quality_Assurance()


        # Custom tasks include agent name and variables as input
        web_search = tasks.search_web(
            benchmarker,
            self.role,
            self.inputs,
        )

        job_requirements = tasks.job_requirements(
            manager,
            self.role,
            self.inputs,
        )

        writing = tasks.writing(
            writer,
            self.role,
        )

        qa_review = tasks.quality_assurance(
            qa,
            self.role,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[benchmarker,
                    manager,
                    writer,
                    qa
                    ],
            tasks=[
                web_search,
                job_requirements,
                writing,
                qa_review
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to HR Job Description Assistant")
    print('-------------------------------')


trip_crew = TripCrew(role, inputs)
result = trip_crew.run()