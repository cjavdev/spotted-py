# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FollowerFollowParams"]


class FollowerFollowParams(TypedDict, total=False):
    components_schemas_properties_published: Annotated[
        bool, PropertyInfo(alias="$.components.schemas.*.properties.published")
    ]
    """Defaults to `true`.

    If `true` the playlist will be included in user's public playlists (added to
    profile), if `false` it will remain private. For more about public/private
    status, see [Working with Playlists](/documentation/web-api/concepts/playlists)
    """
