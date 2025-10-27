# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    body: Required[str]
    """Base64 encoded JPEG image data, maximum payload size is 256 KB."""
