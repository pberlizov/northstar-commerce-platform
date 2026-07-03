"""Auth test suite."""

import hashlib

from auth import hash_password, login, verify_password


def test_correct_password_accepted():
    store = {"alice": {"password_hash": hash_password("s3cret")}}
    assert login("alice", "s3cret", store) is True


def test_wrong_password_rejected():
    store = {"alice": {"password_hash": hash_password("s3cret")}}
    assert login("alice", "wrong", store) is False


def test_hash_is_sha256():
    h = hash_password("s3cret")
    expected = hashlib.sha256(b"s3cret").hexdigest().encode("utf-8")
    assert h == expected, "password hash is not sha256"


def test_unknown_user_rejected():
    assert login("nobody", "whatever", {}) is False
