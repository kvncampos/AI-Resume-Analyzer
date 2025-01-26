from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import os
from .templates import OLLAMA_TEMPLATES

# Load environment variables from .env file
load_dotenv()

LLM_MODEL = os.environ.get("OLLAMA_MODEL", default="llama3.2:latest")

# Initialize the Ollama LLM
llm = OllamaLLM(
    model=LLM_MODEL,
)


def invoke_llm(template_name: str, inputs: dict) -> str:
    """
    Helper function to invoke the Ollama LLM with a given template and inputs.

    Args:
        template_name (str): The name of the template in OLLAMA_TEMPLATES.
        inputs (dict): The input variables for the template.

    Returns:
        str: The response from the LLM.

    Raises:
        ValueError: If the template name is invalid or inputs are empty.
    """
    # Ensure the template name exists
    if template_name not in OLLAMA_TEMPLATES:
        raise ValueError(f"Invalid template name: {template_name}")

    # Get the template
    template = OLLAMA_TEMPLATES[template_name]

    # Initialize the prompt template
    prompt = PromptTemplate(
        input_variables=list(inputs.keys()),
        template=template,
        validate_template=True,
    )

    # Combine the prompt with the language model
    chain = prompt | llm

    # Invoke the chain with the provided inputs
    response = chain.invoke(inputs)

    # Return the content of the response
    return response.strip()


def analyze_job_description(job_description: str) -> bool:
    """
    Verifies the validity of a job description using Ollama LLM.

    Args:
        job_description (str): The full text of the job description.

    Returns:
        bool: True if the job description is valid, False otherwise.

    Raises:
        ValueError: If the job description is empty.
    """
    if not job_description.strip():
        raise ValueError("Job description must be non-empty")

    # Invoke the LLM with the job description validation template
    response = invoke_llm("JOB_DESCRIPTION", {"job_description": job_description})

    response = response.strip().capitalize()

    # Ensure the response is either "True" or "False"
    if response not in ["True", "False"]:
        raise RuntimeError(f"Unexpected response from LLM: {response}")

    return response == "True"


def analyze_resume(full_resume: str, job_description: str) -> str:
    """
    Analyzes a resume against a job description using Ollama LLM.

    Args:
        full_resume (str): The full text of the resume.
        job_description (str): The full text of the job description.

    Returns:
        str: The response from the Ollama LLM analysis.

    Raises:
        ValueError: If either the resume or job description is empty.
    """
    if not full_resume.strip() or not job_description.strip():
        raise ValueError("Both resume and job description must be non-empty")

    # Invoke the LLM with the resume analysis template
    return invoke_llm(
        "RESUME_ANALYSIS", {"resume": full_resume, "job_description": job_description}
    )
