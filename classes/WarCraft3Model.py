from typing import List

from .WarCraft3GeosetAnimation import WarCraft3GeosetAnimation
from .WarCraft3Material import WarCraft3Material
from .WarCraft3Geoset import WarCraft3Geoset
from .WarCraft3Node import WarCraft3Node
from .WarCraft3Sequence import WarCraft3Sequence
from .WarCraft3Texture import WarCraft3Texture


class WarCraft3Model:
    def __init__(self):
        self.file = ''
        self.version = 800
        self.name = ''
        self.geosets: List[WarCraft3Geoset] = []
        self.materials: List[WarCraft3Material] = []
        self.textures: List[WarCraft3Texture] = []
        # self.nodes: List[]  = []
        self.nodes: List[WarCraft3Node] = []
        self.sequences: List[WarCraft3Sequence] = []
        self.geoset_animations: List[WarCraft3GeosetAnimation] = []
        self.pivot_points: List[List[float]] = []

    def normalize_meshes_names(self):
        for mesh in self.geosets:
            mesh.name = self.name
