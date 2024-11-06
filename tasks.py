from crewai import Task

class HR_Tasks:
    
    def search_web(self, agent, role, inputs):
        return Task(
            description=(
                f"""1. Search the web for job descriptions for positions similar to the {role} position.\n
                    2. Evaluate and select the most relevant web pages based on the {role} and {inputs}.\n
                    3. Compile a comprehensive list of requirements for the position based on the analysis.\n
                    4. Proofread the final list for accuracy and grammatical correctness."""
            ),
            expected_output=f"A complete list of all requirements for the {role} position.",
            agent=agent,
        )
    
    def job_requirements(self, agent, role, inputs):
        return Task(
            description=(
                f"""1. Review {inputs} provided by the user to create an initial list of requirements for the {role} position.\n
                    2. Categorize each requirement as either job accountability, technical skills, or soft skills.\n
                    3. Create a bullet point list of categorized requirements for the {role}.\n
                    4. Proofread the list for grammatical errors and clarity."""
            ),
            expected_output=f"A categorized bullet point list of requirements for the {role} in markdown format, ready for use in job description writing.",
            context=[self.search_web],
            agent=agent,
        )
    
    def writing(self, agent, role):
        return Task(
            description=(
                f"""1. Review the list of responsibilities, qualifications, and skills for the {role} provided by the Manager.\n
                    2. Draft a structured and professional job description that communicates the role's key responsibilities and expectations.\n
                    3. Highlight required technical and soft skills while reflecting the company’s culture and values.\n
                    4. Ensure readability with clear sections (e.g., responsibilities, qualifications, skills).\n
                    5. Proofread for grammar, spelling, and consistency."""
            ),
            expected_output=f"A polished and well-structured job description for the {role}, formatted in markdown, ready for publishing.",
            context=[self.search_web, self.job_requirements],
            agent=agent,
        )
    
    def quality_assurance(self, agent, role):
        return Task(
            description=(
                f"""1. Review the job description draft for the {role} created by the Senior HR Analyst.\n
                    2. Verify that all Manager-provided requirements are addressed and that the description meets high-quality standards.\n
                    3. Check that the tone reflects the company's culture and that the description is both detailed and easy to understand.\n
                    4. Confirm that references and sources are accurate and well-documented where applicable."""
            ),
            expected_output=(
                f"A final, high-quality job description for the {role} position, ready for posting and aligned with hiring manager expectations."
            ),
            context=[self.search_web, self.job_requirements, self.writing],
            agent=agent,
        )
