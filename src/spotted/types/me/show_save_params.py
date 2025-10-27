# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ShowSaveParams"]


class ShowSaveParams(TypedDict, total=False):
    query_ids: Required[Annotated[str, PropertyInfo(alias="ids")]]
    """
    A comma-separated list of the
    [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids) for the shows.
    Maximum: 50 IDs.
    """

    body_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="ids")]
    """
    A JSON array of the
    [Spotify IDs](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids).
    A maximum of 50 items can be specified in one request. _Note: if the `ids`
    parameter is present in the query string, any IDs listed here in the body will
    be ignored._
    """
