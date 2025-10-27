# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TimeIntervalObject"]


class TimeIntervalObject(BaseModel):
    confidence: Optional[float] = None
    """The confidence, from 0.0 to 1.0, of the reliability of the interval."""

    duration: Optional[float] = None
    """The duration (in seconds) of the time interval."""

    start: Optional[float] = None
    """The starting point (in seconds) of the time interval."""
