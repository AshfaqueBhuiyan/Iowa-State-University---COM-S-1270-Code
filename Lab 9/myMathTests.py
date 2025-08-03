# Ash Bhuiyan                                    07-22-2025
# Lab #9 - Unit tests for myMath.py functions using pytest to identify and validate behavior of mathematical operations.

from myMath import add, subtract, multiply, divide, power, factorial, is_prime, sum_of_digits, gcd, fib, lcm, square_root, abs_diff, log, mod, mean, median, mode, celsius_to_fahrenheit, fahrenheit_to_celsius, inverse, triangular_number
import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0  # Should catch error in original implementation
    assert add(0, 0) == 0
    assert add(-5, -3) == -8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, -1) == 1/3

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(17) == True
    assert is_prime(4) == False

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(999) == 27

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8

def test_lcm():
    assert lcm(6, 8) == 24
    assert lcm(3, 5) == 15
    assert lcm(7, 7) == 7

def test_square_root():
    assert square_root(16) == 4
    assert square_root(2) == pytest.approx(1.4142135623730951)
    assert square_root(0) == 0

def test_abs_diff():
    assert abs_diff(5, 3) == 2
    assert abs_diff(3, 5) == 2
    assert abs_diff(-1, 1) == 2

def test_log():
    assert log(100, 10) == 2
    assert log(2.718281828459045, 2.718281828459045) == pytest.approx(1)
    with pytest.raises(ValueError):
        log(0)

def test_mod():
    assert mod(10, 3) == 1
    assert mod(7, 7) == 0
    assert mod(-10, 3) == 2

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([10]) == 10
    assert mean([-1, 0, 1]) == 0

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5]) == 5

def test_mode():
    assert mode([1, 2, 2, 3, 4]) == 2
    assert mode([1, 1, 1, 2, 2]) == 1
    assert mode([5]) == 5

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212  # Should catch error in original implementation
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100  # Should catch error in original implementation
    assert fahrenheit_to_celsius(-40) == -40

def test_inverse():
    assert inverse(2) == 0.5
    assert inverse(-1) == -1
    with pytest.raises(ZeroDivisionError):
        inverse(0)

def test_triangular_number():
    assert triangular_number(1) == 1
    assert triangular_number(3) == 6
    assert triangular_number(0) == 0