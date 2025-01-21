"""
 Author: Aidan Kiser
 Version: 11 September 2024
"""

import pytest
from source import *


# Unit Test Cases
def test_returns1With1PassedIn():
    checkFizzBuzz(1, '1')


def test_returns2With2PassedIn():
    checkFizzBuzz(2, '2')


def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, 'Fizz')


def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, 'Buzz')


def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, 'Fizz')


def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, 'Buzz')


def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, 'Fizz')