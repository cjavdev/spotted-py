# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.image_object import ImageObject

__all__ = ["CategoryRetrieveResponse"]


class CategoryRetrieveResponse(BaseModel):
    id: str
    """
    The [Spotify category ID](/documentation/web-api/concepts/spotify-uris-ids) of
    the category.
    """

    href: str
    """A link to the Web API endpoint returning full details of the category."""

    icons: List[ImageObject]
    """The category icon, in various sizes."""

    name: str
    """The name of the category."""
