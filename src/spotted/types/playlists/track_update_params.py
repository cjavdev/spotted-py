# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TrackUpdateParams"]


class TrackUpdateParams(TypedDict, total=False):
    query_uris: Annotated[str, PropertyInfo(alias="uris")]
    """
    A comma-separated list of
    [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) to set, can be
    track or episode URIs. For example:
    `uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M,spotify:episode:512ojhOuo1ktJprKbVcKyQ`<br/>A
    maximum of 100 items can be set in one request.
    """

    insert_before: int
    """
    The position where the items should be inserted.<br/>To reorder the items to the
    end of the playlist, simply set _insert_before_ to the position after the last
    item.<br/>Examples:<br/>To reorder the first item to the last position in a
    playlist with 10 items, set _range_start_ to 0, and _insert_before_
    to 10.<br/>To reorder the last item in a playlist with 10 items to the start of
    the playlist, set _range_start_ to 9, and _insert_before_ to 0.
    """

    range_length: int
    """The amount of items to be reordered.

    Defaults to 1 if not set.<br/>The range of items to be reordered begins from the
    _range_start_ position, and includes the _range_length_ subsequent
    items.<br/>Example:<br/>To move the items at index 9-10 to the start of the
    playlist, _range_start_ is set to 9, and _range_length_ is set to 2.
    """

    range_start: int
    """The position of the first item to be reordered."""

    snapshot_id: str
    """The playlist's snapshot ID against which you want to make the changes."""

    body_uris: Annotated[SequenceNotStr[str], PropertyInfo(alias="uris")]
