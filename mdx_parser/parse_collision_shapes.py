from typing import List

from ..classes.WarCraft3CollisionShape import WarCraft3CollisionShape
from . import binary_reader
from .parse_node import parse_node
from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Node import WarCraft3Node


def parse_collision_shapes(data: bytes):
    data_size = len(data)
    r = binary_reader.Reader(data)

    nodes: List[WarCraft3Node] = []
    while r.offset < data_size:

        collision_shape = WarCraft3CollisionShape()
        parse_node(r, collision_shape)
        collision_type = r.getf('<I')[0]

        if collision_type == 0:
            vertices_count = 2
        elif collision_type == 2:
            vertices_count = 1
        else:
            raise Exception('UNSUPPORTED COLLISION SHAPE TYPE:', collision_type)

        for _ in range(vertices_count):
            position = r.getf('<3f')

        if collision_type == 2:
            bounds_radius = r.getf('<f')[0]

        nodes.append(collision_shape)
    return nodes
