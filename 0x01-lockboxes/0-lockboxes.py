from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """

    if not boxes:
        return False

    total_boxes = len(boxes)
    if total_boxes == 1 and not boxes[0]:  # If there's only one box and it's empty
        return True

    queue = deque([0])
    open_boxes = set(queue)

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key not in open_boxes:
                queue.append(key)
                open_boxes.add(key)

    return len(open_boxes) == total_boxes
