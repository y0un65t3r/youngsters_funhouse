from typing import Tuple

import numpy as np # type: ignore???

# Tile graphics structured type compatible with Console.tiles_rgb
# dtype creates a data type which Numpy uses
graphic_dt = np.dtype(
    [
        # the character, in integer form
        ("ch", np.int32), # Unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes, for RGB colours, foreground colour
        ("bg", "3B"), # background colour
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool), # True if this tile can be walked over.
        ("transparent", np.bool), # True if this tile doesn't block FOV.
        ("dark", graphic_dt), #Graphics for when this tile is not in FOV.
        ("light", graphic_dt), # Graphics for when the tile is in FOV
    ]
)


def new_tile(
    *, # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (100, 100, 100), (0, 0, 0)),
    light=(ord("."), (200, 200, 200), (0, 0, 0)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (100, 100, 100), (0, 0, 0)),
    light=(ord("#"), (200, 200, 200), (0, 0, 0)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (100, 100, 100), (0, 0, 0)),
    light=(ord(">"), (200, 200, 200), (0, 0, 0)),
)
