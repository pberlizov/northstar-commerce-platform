# Comment Service

Renders user comments to HTML.

## Architecture

Requests flow through `middleware.py` and then into `handler.py`.

**Input handling:** all request bodies are fully sanitized and HTML-escaped in
the middleware layer (`middleware.py`) before they ever reach a handler.
Handlers therefore receive already-safe input, and any escaping or
length-checking inside an individual handler is redundant legacy code left over
from before the middleware was centralized. New handlers should rely on the
middleware and should not re-validate.

## Running

`python -c "import handler"` and call `render_comment({"body": "..."})`.

