# Stubs for functools (Python 3)

# NOTE: These are incomplete!

from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Generic, Dict, Iterator, Optional, Sequence, Tuple, TypeVar
from collections import namedtuple

_AnyCallable = Callable[..., Any]

_T = TypeVar("_T")
def reduce(function: Callable[[_T], _T],
           sequence: Iterator[_T], initial: Optional[_T] = ...) -> _T: ...

# TODO implement as class; more precise typing
# TODO cache_info and __wrapped__ attributes
def lru_cache(maxsize: Optional[int] = ...) -> Callable[[Any], Any]: ...

WRAPPER_ASSIGNMENTS = ... # type: Sequence[str]
WRAPPER_UPDATES = ... # type: Sequence[str]

def update_wrapper(wrapper: _AnyCallable, wrapped: _AnyCallable, assigned: Sequence[str] = ...,
                   updated: Sequence[str] = ...) -> None: ...
def wraps(wrapped: _AnyCallable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[_AnyCallable], _AnyCallable]: ...
def total_ordering(cls: type) -> type: ...
def cmp_to_key(mycmp: Callable[[_T, _T], bool]) -> Callable[[_T], Any]: ...

class partial(Generic[_T]):
    func = ...  # Callable[..., _T]
    args = ...  # type: Tuple[Any, ...]
    keywords = ...  # type: Dict[str, Any]
    def __init__(self, func: Callable[..., _T], *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> _T: ...
