#!/usr/bin/python3

"""
  This function determines if all the boxes can be opened.

  Args:
      boxes: A list of lists, where each inner list
      represents the keys a box contains.

  Returns:
      True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    opened = [False] * len(boxes)
    opened[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                queue.append(key)
    return all(opened)
