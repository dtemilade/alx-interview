#!/usr/bin/python3
"""
Lockboxes

This script determines if all the boxes can be opened.

Args:
    boxes (list): lists representing the lockboxes and their keys.

Returns:
    bool: True if all boxes can be opened, False otherwise.
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): lists representing the lockboxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if len(boxes[0]) == 0:
        return False

    keys = {0}
    open_boxes = {0}
    total_boxes = len(boxes)
    keys = keys.union(boxes[0])

    while total_boxes > 0:
        for idx in keys:
            if idx in open_boxes:
                continue
            keys = keys.union(boxes[idx])
            open_boxes.add(idx)
        total_boxes -= 1

    return len(keys) == len(boxes)