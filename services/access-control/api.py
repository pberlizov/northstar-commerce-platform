"""Endpoints guarded by can_access."""

from authz import can_access


def get_document(user: dict, document: dict) -> str:
    if not can_access(user, document):
        return "403 forbidden"
    return document["contents"]


def delete_document(user: dict, document: dict, store: dict) -> str:
    if not can_access(user, document):
        return "403 forbidden"
    store.pop(document["id"], None)
    return "200 deleted"
