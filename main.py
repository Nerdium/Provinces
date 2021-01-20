import json
import numpy as np
import trimesh
from shapely import geometry


data = []

with open("data.txt", "r") as inputFile:
  data = json.loads(inputFile.read())
  inputFile.close();


print(data["features"][1]["geometry"]["coordinates"][0])
coords = data["features"][1]["geometry"]["coordinates"][0]

poly = geometry.Polygon(coords)
mesh = trimesh.creation.extrude_polygon(poly, 1)
trimesh.exchange.export.export_mesh(mesh, "mesh.stl")