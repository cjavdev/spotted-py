# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.episode_object import EpisodeObject

__all__ = ["EpisodeListResponse"]


class EpisodeListResponse(BaseModel):
    episodes: List[EpisodeObject]
