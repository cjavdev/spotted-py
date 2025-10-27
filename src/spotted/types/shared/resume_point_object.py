# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResumePointObject"]


class ResumePointObject(BaseModel):
    fully_played: Optional[bool] = None
    """Whether or not the episode has been fully played by the user."""

    resume_position_ms: Optional[int] = None
    """The user's most recent position in the episode in milliseconds."""
