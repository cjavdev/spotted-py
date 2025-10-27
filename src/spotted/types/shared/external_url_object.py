# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExternalURLObject"]


class ExternalURLObject(BaseModel):
    spotify: Optional[str] = None
    """
    The [Spotify URL](/documentation/web-api/concepts/spotify-uris-ids) for the
    object.
    """
