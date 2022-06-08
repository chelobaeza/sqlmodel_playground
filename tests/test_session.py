import pytest
from sqlmodel import Session, select

from app.models.user import User


@pytest.fixture
def user():
    return User(
        display_name="display name",
    )


def test_get_id_after_add(test_session: Session, user: User):
    test_session.add(user)
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id


def test_get_id_after_flush(test_session: Session, user: User):
    test_session.add(user)
    assert user.id is None
    test_session.flush()
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id


def test_get_id_after_refresh(test_session: Session, user: User):
    test_session.add(user)
    test_session.refresh(user)
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id


def test_get_id_after_flush_refresh(test_session: Session, user: User):
    test_session.add(user)
    test_session.flush()
    test_session.refresh(user)
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id


def test_get_id_after_commit(test_session: Session, user: User):
    test_session.add(user)
    test_session.commit()
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id


def test_get_id_after_commit_refresh(test_session: Session, user: User):
    test_session.add(user)
    test_session.commit()
    test_session.refresh(user)
    test_session.rollback()
    saved_user = test_session.exec(select(User)).first()
    assert user.id is not None
    assert saved_user.id == user.id
