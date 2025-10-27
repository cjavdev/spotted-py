# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FollowersObject"]


class FollowersObject(BaseModel):
    href: Optional[str] = None
    """
    This will always be set to null, as the Web API does not support it at the
    moment.
    """

    total: Optional[int] = None
    """The total number of followers."""
