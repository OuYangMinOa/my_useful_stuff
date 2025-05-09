from __future__ import annotations
from typing import Generic, Union, TypeVar, Callable

T = TypeVar('T')
E = TypeVar('E')

class Result(Generic[T, E]):
    def __init__(self, value : Union[T, E]) -> None:
        self.value = value

    def is_ok(self) -> bool:
        return isinstance(self, Ok)
    
    def is_err(self) -> bool:
        return isinstance(self, Err)
    
    def unwrap(self) -> T:
        if self.is_ok():
            return self.value
        raise ValueError("Called unwrap on an Err value")
    
    def unwrap_err(self) -> E:
        if self.is_err():
            return self.value
        raise ValueError("Called unwrap_err on an Ok value")
    
    def map(self, func: Callable[[T], T]) -> Result[T, E]:
        if self.is_ok():
            return Ok(func(self.value))
        return self  # Return the Err unchanged

    def map_err(self, func: Callable[[E], E]) -> Result[T, E]:
        if self.is_err():
            return Err(func(self.value))
        return self  # Return the Ok unchanged

    def and_then(self, func: Callable[[T], Result[T, E]]) -> Result[T, E]:
        if self.is_ok():
            return Ok(func(self.value))
        return self  # Return the Err unchanged

    def or_else(self, func: Callable[[E], Result[T, E]]) -> Result[T, E]:
        if self.is_err():
            return Err(func(self.value))
        return self  # Return the Ok unchanged

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"

class Ok(Result, Generic[T, E]):
    def __init__(self, value: T) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return f"Ok({self.value})"

class Err(Result, Generic[T, E]):
    def __init__(self, error: E) -> None:
        super().__init__(error)

    def __repr__(self) -> str:
        return f"Err({self.value})"