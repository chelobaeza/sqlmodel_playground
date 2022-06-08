import os
import random
import string
import pytest
from sqlmodel import SQLModel, Session, create_engine




@pytest.fixture(scope="session")
def file_path():
    filename = "".join(random.choices(string.ascii_uppercase, k=10))
    filepath = "./" + filename + ".db"
    yield filepath
    os.remove(filepath)


@pytest.fixture(scope="session")
def test_engine(file_path):
    sqlite_url = f"sqlite:///{file_path}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def test_session(test_engine):
    with Session(test_engine) as session:
        session.begin()
        yield session
        session.rollback()