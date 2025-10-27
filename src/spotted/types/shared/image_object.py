# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ImageObject"]


class ImageObject(BaseModel):
    height: Optional[int] = None
    """The image height in pixels."""

    url: str
    """The source URL of the image."""

    width: Optional[int] = None
    """The image width in pixels."""
