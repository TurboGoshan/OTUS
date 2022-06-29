import pytest


@pytest.fixture(scope="module")
def fixture_module():
    print("\n\nTest module started")
    yield
    print("\nTest module finished")

@pytest.fixture(scope="session")
def fixture_session():
    print("\nTest session started")
    yield
    print("\nTest session finished")


@pytest.fixture(scope="function")
def fixture_function():
    print("\nTest function started")
    yield
    print("\nTest function finished")


@pytest.fixture()
def fixture_without():
    print("\nTest without started")
    yield
    print("\nTest without finished")
