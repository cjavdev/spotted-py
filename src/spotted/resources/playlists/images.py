# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.playlists.image_list_response import ImageListResponse

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/spotted-py#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/spotted-py#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def list(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageListResponse:
        """
        Get the current image associated with a specific playlist.

        Args:
          playlist_id: The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) of the
              playlist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playlist_id:
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._get(
            f"/playlists/{playlist_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageListResponse,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/spotted-py#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/spotted-py#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def list(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageListResponse:
        """
        Get the current image associated with a specific playlist.

        Args:
          playlist_id: The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) of the
              playlist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playlist_id:
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._get(
            f"/playlists/{playlist_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageListResponse,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_raw_response_wrapper(
            images.list,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_raw_response_wrapper(
            images.list,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_streamed_response_wrapper(
            images.list,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
