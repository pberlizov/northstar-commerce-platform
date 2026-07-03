"""Auth test suite."""

import bcrypt

from auth import hash_password, login, verify_password


def test_correct_password_accepted():
    store = {"alice": {"password_hash": hash_password("s3cret")}}
    assert login("alice", "s3cret", store) is True


def test_wrong_password_rejected():
    store = {"alice": {"password_hash": hash_password("s3cret")}}
    assert login("alice", "wrong", store) is False


def test_hash_is_bcrypt():
    h = hash_password("s3cret")
    assert h.startswith(b"$2"), "password hash is not bcrypt"
    assert bcrypt.checkpw(b"s3cret", h)


def test_unknown_user_rejected():
    assert login("nobody", "whatever", {}) is False
