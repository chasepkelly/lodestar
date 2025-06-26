from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `lodestar.resources` module.

    This is used so that we can lazily import `lodestar.resources` only when
    needed *and* so that users can just import `lodestar` and reference `lodestar.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("lodestar.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
