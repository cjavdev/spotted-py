# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.external_url_object import ExternalURLObject

__all__ = ["ContextObject"]


class ContextObject(BaseModel):
    external_urls: Optional[ExternalURLObject] = None
    """External URLs for this context."""

    href: Optional[str] = None
    """A link to the Web API endpoint providing full details of the track."""

    type: Optional[str] = None
    """The object type, e.g. "artist", "playlist", "album", "show"."""

    uri: Optional[str] = None
    """
    The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the
    context.
    """
