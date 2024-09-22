"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


import math

def mul(x: float, y: float) -> float:
    """
    Multiplies two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y

def id(x: float) -> float:
    """
    Returns the input unchanged.

    Args:
        x (float): The input number.

    Returns:
        float: The same number x.
    """
    return x

def add(x: float, y: float) -> float:
    """
    Adds two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def neg(x: float) -> float:
    """
    Negates a number.

    Args:
        x (float): The input number.

    Returns:
        float: The negation of x.
    """
    return -x

def lt(x: float, y: float) -> bool:
    """
    Checks if one number is less than another.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        bool: True if x is less than y, False otherwise.
    """
    return x < y

def eq(x: float, y: float) -> bool:
    """
    Checks if two numbers are equal.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        bool: True if x is equal to y, False otherwise.
    """
    return x == y

def max(x: float, y: float) -> float:
    """
    Returns the larger of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The maximum of x and y.
    """
    return x if x > y else y

def is_close(x: float, y: float) -> bool:
    """
    Checks if two numbers are close in value.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        bool: True if the absolute difference between x and y is less than 1e-2, False otherwise.
    """
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    """
    Calculates the sigmoid function.

    Args:
        x (float): The input value.

    Returns:
        float: The sigmoid of x.
    """
    return 1 / (1 + math.exp(-x))

def relu(x: float) -> float:
    """
    Applies the ReLU activation function.

    Args:
        x (float): The input value.

    Returns:
        float: The ReLU of x (max(0, x)).
    """
    return max(0, x)

def log(x: float) -> float:
    """
    Calculates the natural logarithm.

    Args:
        x (float): The input value.

    Returns:
        float: The natural logarithm of x.
    """
    return math.log(x)

def exp(x: float) -> float:
    """
    Calculates the exponential function.

    Args:
        x (float): The input value.

    Returns:
        float: e raised to the power of x.
    """
    return math.exp(x)

def inv(x: float) -> float:
    """
    Calculates the reciprocal.

    Args:
        x (float): The input value.

    Returns:
        float: The reciprocal of x (1/x).
    """
    return 1 / x

def log_back(x: float, d: float) -> float:
    """
    Computes the derivative of log times a second arg.

    Args:
        x (float): The input value.
        d (float): The second argument.

    Returns:
        float: The derivative of log(x) multiplied by d.
    """
    return d / x

def inv_back(x: float, d: float) -> float:
    """
    Computes the derivative of reciprocal times a second arg.

    Args:
        x (float): The input value.
        d (float): The second argument.

    Returns:
        float: The derivative of 1/x multiplied by d.
    """
    return -d / (x * x)

def relu_back(x: float, d: float) -> float:
    """
    Computes the derivative of ReLU times a second arg.

    Args:
        x (float): The input value.
        d (float): The second argument.

    Returns:
        float: The derivative of ReLU(x) multiplied by d.
    """
    return d if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
