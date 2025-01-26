import streamlit as st
from backend.pdf_ingestion import load_split_pdf
from backend.vector_store import create_vector_store
from backend.analysis import analyze_resume, analyze_job_description
import os
import shutil

ERROR_ICON = ":material/notification_important:"


def handle_resume_analysis(resume_docs, job_description):
    """
    Handles the resume analysis process by first validating the job description
    and then analyzing the resume if the job description is valid.

    Args:
        resume_docs (list): List of parsed resume document objects.
        job_description (str): The job description to validate.

    Returns:
        None
    """

    def _process_resume(resume_docs):
        """
        Combines the content of parsed resume documents into a single text string.

        Args:
            resume_docs (list): List of parsed resume document objects.

        Returns:
            str: Combined resume text.
        """
        return " ".join(doc.page_content for doc in resume_docs)

    # Step 1: Validate the job description
    try:
        if not analyze_job_description(job_description):
            st.error(
                "The job description is invalid. Please provide a valid description.\n\n**It Must Contain**: \n\n1. Valid Job Role\n\n2. Job Requirements",
                icon=ERROR_ICON,
            )
            return
    except Exception as e:
        st.error(
            f"An error occurred during job description analysis: {str(e)}",
            icon=ERROR_ICON,
        )
        return

    # Step 2: Combine all document contents into one text string
    try:
        full_resume = _process_resume(resume_docs)
    except Exception as e:
        st.error(
            f"An error occurred while processing the resume: {str(e)}", icon=ERROR_ICON
        )
        return

    # Step 3: Analyze the resume
    try:
        analysis = analyze_resume(full_resume, job_description)
        st.session_state.analysis = analysis
        st.success("Resume analysis completed successfully!")
    except Exception as e:
        st.error(f"An error occurred during resume analysis: {str(e)}", icon=ERROR_ICON)


def validate_inputs(resume_file, job_description):
    """
    Validates the inputs for the resume and job description analysis.

    Args:
        resume_file (file): Uploaded resume file.
        job_description (str): The job description text.

    Returns:
        bool: True if inputs are valid, False otherwise.
    """
    if not resume_file:
        st.error("Please upload your resume in PDF format.", icon=ERROR_ICON)
        return False
    if len(job_description) < 100:
        st.error(
            "Job description must be at least 100 characters long.", icon=ERROR_ICON
        )
        return False
    return True


# Main application including "Upload Resume" and "Resume Analysis" sections
def render_main_app():
    # Apply custom CSS to adjust the sidebar width
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            min-width: 25%;
            max-width: 25%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Moving the upload section to the sidebar
    with st.sidebar:
        st.header("Upload Resume")  # Header for the upload section

        # File uploader for PDF resumes
        resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

        # Text area for job description input
        job_description = st.text_area("Enter Job Description", height=300)

        # Check if both inputs are provided
        if resume_file and job_description:
            # Create a temporary directory if it doesn't exist
            temp_dir = "temp"
            os.makedirs(temp_dir, exist_ok=True)

            # Save the uploaded file to the temporary directory
            with open(os.path.join(temp_dir, resume_file.name), "wb") as f:
                f.write(resume_file.getbuffer())

            # Load and split the PDF file into documents and chunks
            resume_file_path = os.path.join("temp", resume_file.name)
            resume_docs, resume_chunks = load_split_pdf(resume_file_path)

            # Create a vector store from the resume chunks
            vector_store = create_vector_store(resume_chunks)
            st.session_state.vector_store = (
                vector_store  # Store vector store in session state
            )

            # Remove the temporary directory and its contents
            shutil.rmtree(temp_dir)

            # Button to trigger resume analysis
            if st.button("Analyze Resume", help="Click to analyze the resume"):
                # Step 1: Validate inputs
                if not validate_inputs(resume_file, job_description):
                    return  # Exit early if inputs are invalid

                # Step 2: Proceed to handle resume analysis
                handle_resume_analysis(resume_docs, job_description)

    # Display the analysis result if it exists in session state
    if "analysis" in st.session_state:
        st.header("Resume-Job Compatibility Analysis")
        st.write(st.session_state.analysis)
    else:
        st.header("Welcome to the Ultimate Resume Analysis Tool!")
        st.subheader("Your one-stop solution for resume screening and analysis.")
        st.info(
            "Do you want to find out the compatibility between a resume and a job description? So what are you waiting for?"
        )

        todo = ["Upload a Resume", "Enter a Job Description", "Click on Analyze Resume"]
        st.markdown("\n".join([f"##### {i+1}. {item}" for i, item in enumerate(todo)]))
