def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """

    if not boxes:
        return False

    keys = {0}
    open_boxes = {0}
    total_boxes = len(boxes)

    while total_boxes > 0:
        new_keys = set()
        for idx in keys:
            if idx >= total_boxes:
                continue
            if idx in open_boxes:
                continue
            new_keys = new_keys.union(boxes[idx])
            open_boxes.add(idx)
        keys = keys.union(new_keys)
        total_boxes -= 1

    return len(open_boxes) == len(boxes)
