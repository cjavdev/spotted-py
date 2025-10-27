# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TrackAddParams"]


class TrackAddParams(TypedDict, total=False):
    query_position: Annotated[int, PropertyInfo(alias="position")]
    """The position to insert the items, a zero-based index.

    For example, to insert the items in the first position: `position=0`; to insert
    the items in the third position: `position=2`. If omitted, the items will be
    appended to the playlist. Items are added in the order they are listed in the
    query string or request body.
    """

    query_uris: Annotated[str, PropertyInfo(alias="uris")]
    """
    A comma-separated list of
    [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) to add, can be
    track or episode URIs. For
    example:<br/>`uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh, spotify:track:1301WleyT98MSxVHPZCA6M, spotify:episode:512ojhOuo1ktJprKbVcKyQ`<br/>A
    maximum of 100 items can be added in one request. <br/> _**Note**: it is likely
    that passing a large number of item URIs as a query parameter will exceed the
    maximum length of the request URI. When adding a large number of items, it is
    recommended to pass them in the request body, see below._
    """

    body_position: Annotated[int, PropertyInfo(alias="position")]
    """The position to insert the items, a zero-based index.

    For example, to insert the items in the first position: `position=0` ; to insert
    the items in the third position: `position=2`. If omitted, the items will be
    appended to the playlist. Items are added in the order they appear in the uris
    array. For example:
    `{"uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M"], "position": 3}`
    """

    body_uris: Annotated[SequenceNotStr[str], PropertyInfo(alias="uris")]
    """
    A JSON array of the
    [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) to add. For
    example:
    `{"uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M", "spotify:episode:512ojhOuo1ktJprKbVcKyQ"]}`<br/>A
    maximum of 100 items can be added in one request. _**Note**: if the `uris`
    parameter is present in the query string, any URIs listed here in the body will
    be ignored._
    """
