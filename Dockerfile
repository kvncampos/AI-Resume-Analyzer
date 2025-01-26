# Use the base image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory in the container
WORKDIR /

# Copy pyproject.toml and uv.lock to the root of the container
COPY pyproject.toml uv.lock ./

# Copy the app directory into the container
COPY app /app/

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the Streamlit app
# CMD ["uv", "run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
