"""Comment-rendering handler."""

import html

MAX_COMMENT_LEN = 2000


def render_comment(request: dict) -> str:
    body = request.get("body", "")

    if len(body) > MAX_COMMENT_LEN:
        raise ValueError("comment too long")
    safe = html.escape(body)

    return f"<div class='comment'>{safe}</div>"
