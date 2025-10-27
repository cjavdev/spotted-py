# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EpisodeSaveParams"]


class EpisodeSaveParams(TypedDict, total=False):
    query_ids: Required[Annotated[str, PropertyInfo(alias="ids")]]
    """
    A comma-separated list of the
    [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids). Maximum: 50
    IDs.
    """

    body_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="ids")]]
    """
    A JSON array of the
    [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids). <br/>A maximum
    of 50 items can be specified in one request. _**Note**: if the `ids` parameter
    is present in the query string, any IDs listed here in the body will be
    ignored._
    """
