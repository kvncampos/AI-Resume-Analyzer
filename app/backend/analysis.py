from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Set up Groq API key
load_dotenv()  # Load environment variables from .env file

# # ------------------------------------
# # KEEP THIS IF USING GROQ API
# # ------------------------------------
# from langchain_groq import ChatGroq
# os.environ["GROQ_API_KEY"] = os.getenv(
#     "GROQ_API_KEY"
# )  # Set the Groq API key from environment variables

# # Initialize the ChatGroq model with the specified model name
# Initialize the Ollama LLM
llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3,  # Lower value for more deterministic responses
    top_p=0.9,  # Restrict randomness to the top 90% probability mass
    top_k=40,  # Consider top 40 options during generation
)


def analyze_resume(full_resume, job_description):
    # Template for analyzing the resume against the job description
    template = """
    You are an AI assistant specialized in resume analysis and recruitment. Analyze the given resume and compare it with the job description.

    Respond in the following structure:

    **OVERVIEW**:
    - **Match Percentage**: [Provide a percentage value.]
    - **Matched Skills**: [List of skills that match the job description.]
    - **Unmatched Skills**: [List of skills missing from the job description.]

    **DETAILED ANALYSIS**:
    1. Match Percentage: Explain how you calculated the match percentage.
    2. Matched Skills: Provide a detailed explanation of why these skills match.
    3. Unmatched Skills: Explain why these skills are missing.

    **Additional Comments**:
    Include actionable recommendations for the recruiter or HR manager.

    Resume:
    {resume}

    Job Description:
    {job_description}

    ### Analysis:
    """

    prompt = PromptTemplate(  # Create a prompt template with input variables
        input_variables=["resume", "job_description"], template=template
    )

    # Create a chain combining the prompt and the language model
    chain = prompt | llm

    # Invoke the chain with input data
    response = chain.invoke({"resume": full_resume, "job_description": job_description})

    # Return the content of the response
    return response
