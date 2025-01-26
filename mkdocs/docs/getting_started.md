
# Getting Started

Welcome to the **AI Resume Analyzer**! Follow this guide to prepare your environment and get the application up and running.

---

## Prerequisites

Before running the containers, make sure the following are completed:

1. **Install Docker and Docker Compose**
   Ensure that Docker and Docker Compose are installed on your system:
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

2. **Download Required Models**
   The application relies on **Ollama Models**, with the default being `llama3.2:latest`. Follow these steps to download the models:
   ```bash
   ollama pull llama3.2:latest
   ```

---

## Steps to Prepare and Run

### 1. Download and Verify the Model

```python
# Command to download the model
ollama pull llama3.2:latest
```

- Ensure that the model is downloaded correctly.
- Verify the installation using:
  ```bash
  ollama list
  ```

::: details More Information
If you need additional models, visit the [Ollama documentation](https://ollama.ai/docs).
:::

---

### 2. Start the Containers

Use the following commands to build and start the containers:

=== "Docker Compose"
    ```bash
    docker compose up --build
    ```

=== "Alternative Command"
    ```bash
    invoke build
    ```

---

### 3. Access the Application

Once the containers are running, you can access the services via the following URLs:

- **Streamlit App**: [http://localhost:8501](http://localhost:8501)
- **MkDocs Documentation**: [http://localhost:8000](http://localhost:8000)

---

## Troubleshooting

If you encounter any issues, consider the following:

- **Model Not Found**:
    - Double-check that `llama3.2:latest` has been downloaded using `ollama pull`.
    - Verify that your `ollama` service is running.

- **Docker Issues**:
    - Run:
      ```bash
      docker system prune -af
      ```
    - Rebuild the containers:
      ```bash
      docker compose up --build
      ```

---

## Resources

- Ollama Documentation: [https://ollama.ai/docs](https://ollama.ai/docs)
- Docker Compose Reference: [https://docs.docker.com/compose](https://docs.docker.com/compose)
- MkDocs Material: [https://squidfunk.github.io/mkdocs-material](https://squidfunk.github.io/mkdocs-material)

---

## Quick Checklist

- [x] Docker and Docker Compose installed.
- [x] `ollama pull llama3.2:latest` executed successfully.
- [x] Containers started using `docker compose up`.

---

### 🚀 You're Ready to Go!

Enjoy exploring and using the **AI Resume Analyzer**! If you have questions or feedback, feel free to reach out.
