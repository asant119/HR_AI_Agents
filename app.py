import streamlit as st
from crewai import Crew
from agents import HRAgent
from tasks import HR_Task
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# User inputs through Streamlit
st.title("HR Job Description Generator")
inputs = {}
inputs["role"] = st.text_input("Enter the role:")
inputs["inputs"] = st.text_area("Enter a brief description of the role:")

# Initialize Crew
crew = Crew(
    agents=[HRAgent()],
    tasks=[HR_Task()],
    verbose=2,
    memory=True,
)

# Run the task sequence and display output on button click
if st.button("Generate Job Description"):
    result = crew.kickoff(inputs)
    st.markdown(result)
