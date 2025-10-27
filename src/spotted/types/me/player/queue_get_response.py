# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from ...shared.track_object import TrackObject
from ...shared.episode_object import EpisodeObject

__all__ = ["QueueGetResponse", "CurrentlyPlaying", "Queue"]

CurrentlyPlaying: TypeAlias = Annotated[Union[TrackObject, EpisodeObject], PropertyInfo(discriminator="type")]

Queue: TypeAlias = Annotated[Union[TrackObject, EpisodeObject], PropertyInfo(discriminator="type")]


class QueueGetResponse(BaseModel):
    currently_playing: Optional[CurrentlyPlaying] = None
    """The currently playing track or episode. Can be `null`."""

    queue: Optional[List[Queue]] = None
    """The tracks or episodes in the queue. Can be empty."""
