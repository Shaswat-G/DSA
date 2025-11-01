"""
Flood Fill Algorithm

Problem Statement:
You are given a 2D array representing an image where each element represents a pixel value.
You are also given a starting pixel (sr, sc) and a new color. Write a function to perform a flood fill on the image starting from the given pixel.

Flood fill changes the color of the starting pixel and all connected pixels with the same color to the new color. Two pixels are considered connected if they are adjacent horizontally or vertically.

Input:
- image: List[List[int]] - A 2D array representing the image.
- sr: int - Row index of the starting pixel.
- sc: int - Column index of the starting pixel.
- newColor: int - The new color to apply.

Output:
- List[List[int]] - The modified image after performing the flood fill.

Example:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Constraints:
- The number of rows and columns in the image is in the range [1, 50].
- The pixel values and newColor are integers in the range [0, 65535].
"""

from typing import List
from collections import deque


def flood_fill(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    """
    Perform a flood fill on the given image starting from the pixel (sr, sc).

    :param image: List[List[int]] - The 2D array representing the image.
    :param sr: int - Row index of the starting pixel.
    :param sc: int - Column index of the starting pixel.
    :param newColor: int - The new color to apply.
    :return: List[List[int]] - The modified image after performing the flood fill.
    """

    if not image or not image[0]:
        raise ValueError("Empty Image")

    if not is_valid_pixel(sr, sc, image, 0, 65535):
        raise ValueError("Invalid Pixel")

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cur_color = image[sr][sc]
    q = deque([(sr, sc)])
    image[sr][sc] = newColor

    while q:
        cr, cc = q.popleft()
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if is_valid_pixel(nr, nc, image, 0, 65535):
                if image[nr][nc] == cur_color:
                    q.append((nr, nc))
                    image[nr][nc] = newColor

    return image


def is_valid_pixel(r, c, image, range_min, range_max):
    is_valid = (
        (0 <= r < len(image))
        and (0 <= c < len(image[0]))
        and (range_min <= image[r][c] <= range_max)
    )
    return is_valid


# Example usage
if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc = 1, 1
    newColor = 2
    result = flood_fill(image, sr, sc, newColor)
    print("Modified Image:", result)
