from crewai import Task
from agents import Agents


"""The summary of the tasks is as follows:
    - Search the web for job descriptions for positions similar to the {role} position
    - Extract the requirements for the {role} position from the job descriptions
    - Define the requirements for the {role} position
    - Write the job description for the {role} position
    - Review the job description for the {role} position
"""


class HR_Task(Task):
    def __init__(self):
        return
    

    def search_web(self):
        return Task(
            description=(
                "1. Search the web for job descriptions for positions similar to the {role} position\n "
                "2. Evaluate the content for the most relevant web pages.\n"
                "4. Create a complete list with the requirements for the position based on the evaluation.\n"
                "5. Proofread for grammatical errors.\n"
            ),
            expected_output="A complete list of all requirements for the {role}",
            agent=Agents.HRAgent.Benchmark(),
        )
    

    def job_requirements(self):
        return Task(
            description=(
                "1. Assess the {inputs} from the user and create an initial list of requirements for the {role}\n "
                "2. Evaluate and classify the requiment between job accountability, technical skills, and soft skills.\n"
                "4. Create a bullet point list with the requirements for the {role}.\n"
                "5. Proofread for grammatical errors.\n"
                ),
            expected_output="A well-written bullet point list of requirements for the {role}"
            "in markdown format, ready for job description writing",
            agent=Agents.HRAgent.Manager(),
        )
    

    def writing(self):
        return Task(
            description=(
                "1. Review the {inputs} provided by the Hiring Manager, \n"
                "including the list of responsibilities, qualifications, and skills for the {role}.\n"
                "2. Use the information to draft a clear and structured job description \n" 
                "that effectively communicates the role’s key responsibilities and expectations.\n"
                "3. Ensure the description highlights the technical and soft skills required, \n"
                "emphasizing the company’s culture and values.\n"
                "4. Write the job description in a professional yet engaging tone to attract qualified candidates.\n"
                "5. Format the description using clear sections (e.g., responsibilities, qualifications, skills) for readability.\n"
                "6. Proofread for grammar, spelling, and clarity, ensuring that the language is consistent and free from errors.\n"
            ),
            expected_output="A polished and well-structured job description for the {role}, formatted in markdown, "
                    "ready for publishing on job platforms.",
            agent=Agents.HRAgent.Writer(),
        )
    
    
    def quality_assurance(self):
        return Task(
            description=(
                "Review the response drafted by the Senior HR Analyst for the {role} position. \n"
                "Ensure that the answer is comprehensive, accurate, and adheres to the \n"
                "high-quality standards expected for a job position description.\n"
                "Verify that all parts of the Technical Hiring Manager assessment have been addressed\n"
                "Check for references and sources used to \n"
                " find the information, \n"
                "ensuring the response is well-supported"
            ),
            expected_output=(
                "A final, detailed, and informative job description for the {role} position\n"
                "ready to be posted.\n"
                "This response should fully address the hiring manager expectations"
            ),
            agent=Agents.HRAgent.QualityAssurance(),
        )

