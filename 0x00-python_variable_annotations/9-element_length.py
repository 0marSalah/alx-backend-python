#!/usr/bin/env python3
""" Basic annotations - to string """
from typing import Tuple, List


def element_length(lst: list) -> List[Tuple[str, int]]:
    """ Return list of tuples, first element is the string, second element is the length of the string """
    return [(i, len(i)) for i in lst]
