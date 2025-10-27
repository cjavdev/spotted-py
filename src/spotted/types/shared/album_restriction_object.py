# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AlbumRestrictionObject"]


class AlbumRestrictionObject(BaseModel):
    reason: Optional[Literal["market", "product", "explicit"]] = None
    """The reason for the restriction.

    Albums may be restricted if the content is not available in a given market, to
    the user's subscription type, or when the user's account is set to not play
    explicit content. Additional reasons may be added in the future.
    """
