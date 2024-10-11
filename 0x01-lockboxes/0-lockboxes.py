#!/usr/bin/python3
"""
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of lists): Each index represents a box and contains a list of keys.
    
    Returns:
    bool:
"""
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): Each index represents a box and contains a list of keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
