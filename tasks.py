from invoke import task


@task
def tests(c):
    """
    Run ruff and black to autoformat the codebase.
    """
    print("Running Ruff...")
    c.run("ruff check . --fix")
    print("Running Black...")
    c.run("black .")


@task
def up(c):
    """
    Start the Docker Compose services.
    """
    print("Starting Docker Compose services...")
    c.run("docker compose up")


@task
def build(c):
    """
    Build the Docker Compose services.
    """
    print("Building Docker Compose services...")
    c.run("docker compose up --build")


@task
def stop(c):
    """
    Stop the Docker Compose services.
    """
    print("Stopping Docker Compose services...")
    c.run("docker compose down")


@task
def destroy(c):
    """
    Destroy all Docker volumes, including orphans.
    """
    print("Destroying all Docker volumes, including orphans...")
    c.run("docker compose down -v --remove-orphans")
    print("Removing unused volumes...")
    c.run("docker volume prune -f")
