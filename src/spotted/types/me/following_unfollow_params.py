# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FollowingUnfollowParams"]


class FollowingUnfollowParams(TypedDict, total=False):
    query_ids: Required[Annotated[str, PropertyInfo(alias="ids")]]
    """
    A comma-separated list of the artist or the user
    [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids). For example:
    `ids=74ASZWbe4lXaubB36ztrGX,08td7MxkoHQkXnWAYD8d6Q`. A maximum of 50 IDs can be
    sent in one request.
    """

    type: Required[Literal["artist", "user"]]
    """The ID type: either `artist` or `user`."""

    body_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="ids")]
    """
    A JSON array of the artist or user
    [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids). For example:
    `{ids:["74ASZWbe4lXaubB36ztrGX", "08td7MxkoHQkXnWAYD8d6Q"]}`. A maximum of 50
    IDs can be sent in one request. _**Note**: if the `ids` parameter is present in
    the query string, any IDs listed here in the body will be ignored._
    """
