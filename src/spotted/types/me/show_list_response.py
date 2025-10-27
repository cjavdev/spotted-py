# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..shared.show_base import ShowBase

__all__ = ["ShowListResponse"]


class ShowListResponse(BaseModel):
    added_at: Optional[datetime] = None
    """
    The date and time the show was saved. Timestamps are returned in ISO 8601 format
    as Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If
    the time is imprecise (for example, the date/time of an album release), an
    additional field indicates the precision; see for example, release_date in an
    album object.
    """

    show: Optional[ShowBase] = None
    """Information about the show."""
