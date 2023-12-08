#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: float = 2) -> List:
    """ Return a tuple """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
