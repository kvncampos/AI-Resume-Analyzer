# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory to /streamlit
WORKDIR /streamlit

# Enable bytecode compilation for performance
ENV UV_COMPILE_BYTECODE=1

# Copy pyproject.toml and uv.lock into /streamlit
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the source code into /streamlit
COPY ./app /streamlit/app/

# Set the PATH to include the virtual environment executables
ENV PATH="/streamlit/.venv/bin:$PATH"

# Reset the entrypoint to avoid invoking uv by default
ENTRYPOINT []

# Run Streamlit App
CMD ["streamlit", "run", "app/app.py"]
