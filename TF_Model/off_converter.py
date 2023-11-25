import os
from stl import mesh
import tripy
import numpy as np

def off_to_stl(input_path, output_path):

    with open(input_path, 'r') as off_file:
        lines = off_file.readlines()


    vertex_count, face_count, _ = map(int, lines[1].split())

    vertices = []
    for line in lines[2:2 + vertex_count]:
        vertices.append(list(map(float, line.split()[0:3])))

    faces = []
    for line in lines[2 + vertex_count:]:
        faces.append(list(map(int, line.split()[1:])))


    vertices = np.array(vertices)
    stl_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))

    for i, face in enumerate(faces):
        for j in range(3):
            stl_mesh.vectors[i][j] = vertices[face[j]]


    stl_mesh.save(output_path)

def convertir_carpeta(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for filename in os.listdir(input_folder):
        if filename.endswith(".off"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".stl")
            off_to_stl(input_path, output_path)

if __name__ == "__main__":
    input_folder = "train"
    output_folder = "train_stl"

    convertir_carpeta(input_folder, output_folder)