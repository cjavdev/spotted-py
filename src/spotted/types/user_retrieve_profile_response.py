# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.image_object import ImageObject
from .shared.followers_object import FollowersObject
from .shared.external_url_object import ExternalURLObject

__all__ = ["UserRetrieveProfileResponse"]


class UserRetrieveProfileResponse(BaseModel):
    id: Optional[str] = None
    """
    The [Spotify user ID](/documentation/web-api/concepts/spotify-uris-ids) for this
    user.
    """

    display_name: Optional[str] = None
    """The name displayed on the user's profile. `null` if not available."""

    external_urls: Optional[ExternalURLObject] = None
    """Known public external URLs for this user."""

    followers: Optional[FollowersObject] = None
    """Information about the followers of this user."""

    href: Optional[str] = None
    """A link to the Web API endpoint for this user."""

    images: Optional[List[ImageObject]] = None
    """The user's profile image."""

    type: Optional[Literal["user"]] = None
    """The object type."""

    uri: Optional[str] = None
    """
    The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for this
    user.
    """
