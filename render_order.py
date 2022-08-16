from enum import auto, Enum

# Enum is a set of named functions that won't change
# auto assigns incrementing integer values autonatically
class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
