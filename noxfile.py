import nox
import nox_poetry


@nox_poetry.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def tests(session):
    session.install("pytest")
    session.poetry.session.install(".")
    session.run("pytest", *session.posargs)


@nox.session()
def lint(session):
    session.install(".")
    session.install("black", "mypy")
    session.install(
        "flake8",
        "flake8-bugbear",
        "flake8-builtins",
        "flake8-deprecated",
        "flake8-eradicate",
    )
    session.run("black", "--check", ".")
    session.run("mypy", "src")
    session.run("flake8", "src", "tests")
