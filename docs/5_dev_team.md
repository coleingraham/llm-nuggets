# Simple Software Development Team

This simplistic example uses the concepts of prompt chaining (the output from
one prompt addressing a subtask is fed to the next) and
[Multi-Agent Debate](https://arxiv.org/abs/2305.19118) in order to simulate
how a theoretical software development team works. This consists of three
personas:

* **developer**: writes code
* **qa**: critiques code and suggests improvements
* **release manager**: considers the current code and feedback to decide whether
to release it or not

These three "mini agents" perform their tasks one after another, giving their
output to the next, and repeat until either the release manager decides to stop,
or until a maximum number of iterations is reached.

## Considerations

Here are some assumptions that were made and things to think about if you plan
to do something similar:

* This example intentionally only passes the most recent version of the code and
feedback to the next step. You may decide that keeping a history of iterations
is valuable.
* Using a reasoning model may improve performance, but will also be much slower
and more expensive.
* It is very possible that more powerful coding models outperform this approach
in a single shot, depending on which models you use.

# Example Usage

Task: write a function to calculate the fibonacci sequence

```
$ cd src
$ python dev_team.py --provider ollama --model qwen3:8b --temperature 0.3

Iteration: 0

def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the sequence.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence 

- Consider adding input validation to ensure `n` is a positive integer.
- The function could be made more efficient using memoization or iterative methods for larger values of `n`.
- Add docstring examples to clarify how the function behaves for different inputs.
- Consider handling edge cases more explicitly, such as when `n` is greater than 2.
- The function could be refactored to allow for generating the sequence starting from 0 or 1 based on user preference. 

UPDATE

Iteration: 1

def fibonacci(n, start_from_0=True):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the sequence. Must be a positive integer.
    start_from_0 (bool): If True, the sequence starts with 0, 1, ...; if False, starts with 1, 1, ...

    Returns:
    list: A list containing the first n Fibonacci numbers.

    Examples:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(5, start_from_0=False)
    [1, 1, 2, 3, 5]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    if start_from_0:
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        fib_sequence = [0, 1]
    else:
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        fib_sequence = [1, 1]

    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

- **Parameter Validation:** Add more detailed validation for the `start_from_0` parameter to ensure it is a boolean.
- **Edge Case Handling:** Ensure the function handles cases where `n` is 0 or 1 properly, even when `start_from_0` is False.
- **Docstring Improvements:** Clarify the behavior of the function in the docstring, especially the difference between starting from 0 or 1.
- **Performance Consideration:** For very large `n`, this implementation is acceptable, but consider an iterative approach for better performance and memory efficiency.
- **Consistency in Examples:** Ensure the examples in the docstring match the actual behavior of the function.
- **Error Message Clarity:** Improve the error message for non-integer `n` to be more informative. 

UPDATE

Iteration: 2

def fibonacci(n, start_from_0=True):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the sequence. Must be a positive integer.
    start_from_0 (bool): If True, the sequence starts with 0, 1, ...; if False, starts with 1, 1, ...

    Returns:
    list: A list containing the first n Fibonacci numbers.

    Examples:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(5, start_from_0=False)
    [1, 1, 2, 3, 5]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    if not isinstance(start_from_0, bool):
        raise ValueError("start_from_0 must be a boolean (True or False).")

    if n == 0:
        return []
    elif n == 1:
        return [0] if start_from_0 else [1]
    elif n == 2:
        return [0, 1] if start_from_0 else [1, 1]

    fib_sequence = [0, 1] if start_from_0 else [1, 1]

    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

- **Consider adding input validation for edge cases**: For example, ensure `n` is not greater than a reasonable limit to prevent excessive memory usage or infinite loops.

- **Improve error handling for invalid inputs**: For example, if `n` is not a positive integer, raise a more descriptive error message.

- **Handle the case where `n` is 0 or 1 more gracefully**: The current implementation returns empty lists or single-element lists, but it might be clearer to raise an error or return an empty list with a message.

- **Add more test cases in the docstring**: Include examples for edge cases like `n=0`, `n=1`, and `n=2` to clarify expected behavior.

- **Consider using a more efficient algorithm for large `n`**: The current implementation is O(n) and is acceptable for most use cases, but for very large `n`, a generator or iterative approach could be more memory-efficient.

- **Add type hints**: Improve readability and maintainability by adding type hints for function parameters and return types.

- **Consider making the function more flexible**: For example, allow the user to specify the starting values instead of just `start_from_0`.

- **Document the behavior for `n=0` more clearly**: The current code returns an empty list, but it might be better to raise an error or explicitly document this behavior. 

UPDATE

Iteration: 3

from typing import List

def fibonacci(n: int, start_from_0: bool = True) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the sequence. Must be a positive integer.
    start_from_0 (bool): If True, the sequence starts with 0, 1, ...; if False, starts with 1, 1, ...

    Returns:
    List[int]: A list containing the first n Fibonacci numbers.

    Raises:
    ValueError: If n is not a positive integer or if start_from_0 is not a boolean.

    Examples:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(5, start_from_0=False)
    [1, 1, 2, 3, 5]
    >>> fibonacci(0)
    []
    >>> fibonacci(1)
    [0]
    >>> fibonacci(1, start_from_0=False)
    [1]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    if not isinstance(start_from_0, bool):
        raise ValueError("start_from_0 must be a boolean (True or False).")

    if n == 0:
        return []
    elif n == 1:
        return [0] if start_from_0 else [1]
    elif n == 2:
        return [0, 1] if start_from_0 else [1, 1]

    fib_sequence = [0, 1] if start_from_0 else [1, 1]

    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

- **Handle edge cases for n = 0 and n = 1 more clearly** in the docstring and examples to ensure clarity.
- **Consider adding a check for n being a positive integer** in the function, as the current check allows n = 0, which is already handled.
- **Improve the docstring** to clarify that `n` must be a positive integer (even though it's already checked).
- **Add more test cases** in the docstring for different values of `n` and `start_from_0` to ensure comprehensive coverage.
- **Consider adding a parameter** to control whether the sequence should be printed or returned, though this is not required for the current task.
- **Ensure the function is efficient** for large values of `n`, but the current implementation is already O(n), which is optimal for generating the Fibonacci sequence.
- **Clarify the behavior** when `n` is less than 2 in the docstring to avoid confusion. 

UPDATE


      developer token usage: {'qwen3:8b': {'output_tokens': 1191, 'input_tokens': 1633, 'total_tokens': 2824}}
             qa token usage: {'qwen3:8b': {'output_tokens': 750, 'input_tokens': 1499, 'total_tokens': 2249}}
release manager token usage: {'qwen3:8b': {'output_tokens': 8, 'input_tokens': 2357, 'total_tokens': 2365}}

=== Final Code ===
from typing import List

def fibonacci(n: int, start_from_0: bool = True) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the sequence. Must be a positive integer.
    start_from_0 (bool): If True, the sequence starts with 0, 1, ...; if False, starts with 1, 1, ...

    Returns:
    List[int]: A list containing the first n Fibonacci numbers.

    Raises:
    ValueError: If n is not a positive integer or if start_from_0 is not a boolean.

    Examples:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(5, start_from_0=False)
    [1, 1, 2, 3, 5]
    >>> fibonacci(0)
    []
    >>> fibonacci(1)
    [0]
    >>> fibonacci(1, start_from_0=False)
    [1]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    if not isinstance(start_from_0, bool):
        raise ValueError("start_from_0 must be a boolean (True or False).")

    if n == 0:
        return []
    elif n == 1:
        return [0] if start_from_0 else [1]
    elif n == 2:
        return [0, 1] if start_from_0 else [1, 1]

    fib_sequence = [0, 1] if start_from_0 else [1, 1]

    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

total token usage: {'qwen3:8b': {'output_tokens': 1949, 'input_tokens': 5489, 'total_tokens': 7438}}
```
