#!/usr/bin/env python3
"""Lesson 1 introduces the shapely module"""

from shapely.geometry import Point, LineString, Polygon

# Point() can take 2 or 3 coordinates
point_2d = Point(1.0, 2.0)
point_3d = Point(-1.5, 2.5, 5)

print(f"2d={point_2d}, 3d={point_3d}")

coords = point_2d.coords
xy = coords.xy
x = point_2d.x
y = point_2d.y

print(f"x={x}, y={y}, xy={xy}")
