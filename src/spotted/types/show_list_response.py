# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.show_base import ShowBase

__all__ = ["ShowListResponse"]


class ShowListResponse(BaseModel):
    shows: List[ShowBase]
