#!/usr/local/bin/python3


import numpy as np
import struct
import sys
from plyfile import PlyData, PlyElement


def bin_to_pcd(binFileName):
  size_float = 4
  list_pcd = []
  with open(binFileName, "rb") as f:
    byte = f.read(size_float * 4)
    while byte:
      x, y, z, intensity = struct.unpack("ffff", byte)
      list_pcd.append((x, y, z, intensity))
      byte = f.read(size_float * 4)
  vertex = np.array(
    list_pcd,
    dtype=[
      ('x', 'f4'),
      ('y', 'f4'),
      ('z', 'f4'),
      ('intensity', 'f4')
    ]
  )
  ply_element = PlyElement.describe(vertex, 'vertex')
  ply_data = PlyData([ply_element], text=False)
  return ply_data


def main(binFileName, pcdFileName):
  ply_data = bin_to_pcd(binFileName)
  ply_data.write(pcdFileName)



if __name__ == "__main__":
  a = sys.argv[1]
  b = sys.argv[2]
  main(a, b)
