
# Understanding the Code

This document explains the key components and functionality of the code that integrates with the Ollama LLM (Large Language Model) for analyzing resumes and job descriptions.

## Overview

The code is structured to:

1. Load environment variables.
2. Initialize the Ollama LLM with a specified model.
3. Provide utility functions for interacting with the LLM.
4. Analyze job descriptions and resumes to produce insights.

## Key Components

### 1. Loading Environment Variables

```python
from dotenv import load_dotenv
load_dotenv()
```

**Purpose**: Loads environment variables from a `.env` file into the application. These variables include the model name for the LLM.

#### Example:

```plaintext
.env file:
OLLAMA_MODEL=llama3.2:latest
```

### 2. Initializing the LLM

```python
LLM_MODEL = os.environ.get("OLLAMA_MODEL", default="llama3.2:latest")
llm = OllamaLLM(
    model=LLM_MODEL,
)
```

- **LLM_MODEL**: Retrieves the model name from the environment variables or uses `"llama3.2:latest"` as the default.- **OllamaLLM**: Initializes the LLM using the specified model.

### 3. Templates for Prompts

```python
from .templates import OLLAMA_TEMPLATES
```

- **OLLAMA_TEMPLATES**: Contains predefined templates for different tasks such as job description validation and resume analysis.Templates define the structure of the input prompts provided to the LLM.

### 4. Invoking the LLM

```python
def invoke_llm(template_name: str, inputs: dict) -> str:
```
This helper function:

- Takes a template name and input variables.
- Validates the template name.
- Constructs a `PromptTemplate` using the template and inputs.
- Executes the chain combining the prompt and the LLM.
- Returns the response from the LLM.

??? info "Example Workflow"
    **Input**:

    ```python
    invoke_llm("RESUME_ANALYSIS", {"resume": "Sample Resume", "job_description": "Sample Job Description"})
    ```

    **Output**:
    The LLM’s analysis of the resume against the job description.

### 5. Job Description Validation

```python
def analyze_job_description(job_description: str) -> bool:
```

**Purpose**: Checks if the job description is valid.

**Process**:

1. Ensures the input is non-empty.
2. Invokes the LLM with the `JOB_DESCRIPTION` template.
3. Validates that the LLM’s response is either `True` or `False`.

**Returns**: `True` if the job description is valid, `False` otherwise.

#### Example:

- **Input**:

    ```python
    analyze_job_description("We are looking for a Python developer with Django experience.")
    ```

- **Output**:

    ```plaintext
    True
    ```

### 6. Resume Analysis

```python
def analyze_resume(full_resume: str, job_description: str) -> str:
```

**Purpose**: Analyzes a resume against a job description.

**Process**:

1. Ensures both inputs are non-empty.
2. Invokes the LLM with the `RESUME_ANALYSIS` template.

**Returns**: A detailed analysis string from the LLM.

#### Example:

- **Input**:

    ```python
    analyze_resume(
        "Experienced Python developer with Django expertise.",
        "Looking for a Python developer with Django and Flask experience."
    )
    ```

- **Output**:

    ```plaintext
    A string containing the LLM’s analysis of the resume compared to the job description.
    ```

### Error Handling

#### Invalid Template Name:

```python
if template_name not in OLLAMA_TEMPLATES:
    raise ValueError(f"Invalid template name: {template_name}")
```

Ensures only valid templates are used.

#### Empty Input Validation:

- `analyze_job_description`: Ensures the job description is non-empty.
- `analyze_resume`: Ensures both resume and job description inputs are non-empty.

#### Unexpected Responses:

```python
if response not in ["True", "False"]:
    raise RuntimeError(f"Unexpected response from LLM: {response}")
```

Ensures the LLM’s response is predictable.

## Summary

This code provides a robust framework for leveraging the Ollama LLM to:

1. Validate job descriptions.
2. Analyze resumes against job descriptions.
3. Return structured and actionable insights.

The use of templates ensures consistency in prompts, while helper functions like `invoke_llm` simplify interaction with the LLM. Error handling and input validation ensure reliability and robustness.
