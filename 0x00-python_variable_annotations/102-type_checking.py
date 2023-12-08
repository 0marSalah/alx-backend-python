#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import List


def zoom_array(lst: List, factor: float = 2.0) -> List:
    """ Return a tuple """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
