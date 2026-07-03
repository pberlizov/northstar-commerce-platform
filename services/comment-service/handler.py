"""Comment-rendering handler."""


def render_comment(request: dict) -> str:
    body = request.get("body", "")
    return f"<div class='comment'>{body}</div>"
