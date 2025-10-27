# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .external_url_object import ExternalURLObject

__all__ = ["SimplifiedArtistObject"]


class SimplifiedArtistObject(BaseModel):
    id: Optional[str] = None
    """
    The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the
    artist.
    """

    external_urls: Optional[ExternalURLObject] = None
    """Known external URLs for this artist."""

    href: Optional[str] = None
    """A link to the Web API endpoint providing full details of the artist."""

    name: Optional[str] = None
    """The name of the artist."""

    type: Optional[Literal["artist"]] = None
    """The object type."""

    uri: Optional[str] = None
    """
    The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the
    artist.
    """
