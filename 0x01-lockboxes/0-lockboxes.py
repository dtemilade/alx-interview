#!/usr/bin/python3
"""
Lockboxes
This script determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """

    if not boxes:
        return False

    from collections import deque

    queue = deque([0])
    open_boxes = set(queue)

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key not in open_boxes:
                queue.append(key)
                open_boxes.add(key)

    return len(open_boxes) == len(boxes)
