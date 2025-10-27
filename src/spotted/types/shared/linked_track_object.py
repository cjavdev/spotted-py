# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .external_url_object import ExternalURLObject

__all__ = ["LinkedTrackObject"]


class LinkedTrackObject(BaseModel):
    id: Optional[str] = None
    """
    The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the
    track.
    """

    external_urls: Optional[ExternalURLObject] = None
    """Known external URLs for this track."""

    href: Optional[str] = None
    """A link to the Web API endpoint providing full details of the track."""

    type: Optional[str] = None
    """The object type: "track"."""

    uri: Optional[str] = None
    """
    The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the
    track.
    """
