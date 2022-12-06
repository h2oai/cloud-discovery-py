import nox
import nox_poetry


nox.options.sessions = ["lint", "tests"]


@nox_poetry.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
@nox.parametrize(
    "httpx_version_constraint", ["==0.16.*", "==0.21.*", "==0.22.*", "==0.23.*", ""]
)
def tests(session, httpx_version_constraint):
    session.install("pytest", "pytest-asyncio")
    session.poetry.session.install(f"httpx{httpx_version_constraint}", "respx", ".")
    session.run("pytest", *session.posargs)


@nox_poetry.session
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


@nox_poetry.session()
def e2e_tests(session):
    session.install("pytest", "pytest-asyncio", "respx")
    session.poetry.session.install(".")
    session.run("pytest", "-m e2e", *session.posargs)
