# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CopyrightObject"]


class CopyrightObject(BaseModel):
    text: Optional[str] = None
    """The copyright text for this content."""

    type: Optional[str] = None
    """
    The type of copyright: `C` = the copyright, `P` = the sound recording
    (performance) copyright.
    """
