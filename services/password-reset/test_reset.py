"""Password reset tests."""

from reset import generate_reset_token, validate_reset_token


def test_token_has_legacy_email_prefix():
    assert generate_reset_token("user-123").startswith("rst_user-123_")


def test_rejects_expired_token():
    assert validate_reset_token("x" * 40, issued_at=1000, now=2000) is False

