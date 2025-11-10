# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.audiobook_base import AudiobookBase
from .simplified_chapter_object import SimplifiedChapterObject

__all__ = ["AudiobookBulkRetrieveResponse", "Audiobook", "AudiobookChapters"]


class AudiobookChapters(BaseModel):
    href: str
    """A link to the Web API endpoint returning the full result of the request"""

    items: List[SimplifiedChapterObject]

    limit: int
    """
    The maximum number of items in the response (as set in the query or by default).
    """

    next: Optional[str] = None
    """URL to the next page of items. ( `null` if none)"""

    offset: int
    """The offset of the items returned (as set in the query or by default)"""

    previous: Optional[str] = None
    """URL to the previous page of items. ( `null` if none)"""

    total: int
    """The total number of items available to return."""


class Audiobook(AudiobookBase):
    chapters: AudiobookChapters
    """The chapters of the audiobook."""


class AudiobookBulkRetrieveResponse(BaseModel):
    audiobooks: List[Audiobook]
