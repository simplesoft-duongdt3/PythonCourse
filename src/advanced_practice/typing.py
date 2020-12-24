import typing

def main():
    # For simple built-in types, just use the name of the type
    x: int = 1
    x: float = 1.0
    x: bool = True
    x: str = "test"
    x: typing.Any = 1
    x: typing.Any = ""

    # Use Optional[] for values that could be None
    x: typing.Optional[str] = None
    x: typing.Optional[str] = "Text is so long!"

    if x is not None:
    print(x.upper())

    # For collections, the name of the type is capitalized, and the
    # name of the type inside the collection is in brackets
    x: typing.List[int] = [1]
    x: typing.Set[int] = {6, 7}

    # For mappings, we need the types of both keys and values
    x: typing.Dict[str, float] = {'field': 2.0}

    # For tuples of fixed size, we specify the types of all the elements
    x: typing.Tuple[int, str, float] = (3, "yes", 7.5)

    # For tuples of variable size, we use one type and ellipsis
    x: typing.Tuple[int, ...] = (1, 2, 3)

    # This is how you annotate a function definition
    def stringify(num: int) -> str:
        return str(num)

    # And here's how you specify multiple arguments
    def plus(num1: int, num2: int) -> int:
        return num1 + num2

    # Add default value for an argument after the type annotation
    def f(num1: int, my_float: float = 3.5) -> float:
        return num1 + my_float

    def f(value: typing.Union[int, str, None]) -> str:
        if isinstance(value, str):
            return "string"
        elif isinstance(value, int):
            return "int"
        else:
            return "None"

    # This is how you annotate a callable (function) value
    x: typing.Callable[[int, float], float] = f


if __name__ == "__main__": 
    main()
else: 
    print ("typing.py imported")