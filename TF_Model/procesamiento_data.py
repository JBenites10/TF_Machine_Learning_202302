
import os
import numpy as np
import stltovoxel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image
from stl import mesh

def off_to_stl(input_path, output_path):
    with open(input_path, 'r') as off_file:
        lines = off_file.readlines()

    if len(lines) < 2:
        print(f"Error: Insufficient lines in {input_path}")
        return None

    counts = lines[1].split()

    if len(counts) != 3 or not all(c.isdigit() for c in counts):
        print(f"Error: Invalid counts format in {input_path}")
        return None

    vertex_count, face_count, _ = map(int, counts)

    if len(lines) < 2 + vertex_count:
        print(f"Error: Insufficient vertex lines in {input_path}")
        return None

    vertices = []
    for i, line in enumerate(lines[2:2 + vertex_count], start=2):
        values = line.split()[0:3]
        if len(values) != 3 or not all(v.replace('.', '', 1).replace('-', '', 1).isdigit() for v in values):
            print(f"Error: Invalid vertex format in {input_path}. Line {i}: {line}")
            return None
        vertices.append(list(map(float, values)))

    if len(lines) < 2 + vertex_count + face_count:
        print(f"Error: Insufficient face lines in {input_path}")
        return None

    faces = []
    for line in lines[2 + vertex_count:]:
        values = line.split()[1:]
        if len(values) < 3 or not all(v.lstrip('-').isdigit() for v in values):
            print(f"Error: Invalid face format in {input_path}. Problematic line: {line}")
            return None
        faces.append(list(map(int, values)))

    vertices = np.array(vertices)
    stl_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))

    for i, face in enumerate(faces):
        for j in range(3):
            stl_mesh.vectors[i][j] = vertices[face[j]]

    stl_mesh.save(output_path)
    return stl_mesh
    
def convertir_carpeta(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for filename in os.listdir(input_folder):
        if filename.endswith(".off"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".stl")
            off_to_stl(input_path, output_path)
def xyz_to_tensor(input, dim):
    with open(input, 'r') as xyz_file:
        coords = []
        min_x = float('inf')
        min_y = float('inf')
        min_z = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        max_z = float('-inf')
        lines = xyz_file.readlines()
        for line in lines:
            coord_tuple = line.split()
            x, y, z = float(coord_tuple[0]), float(coord_tuple[1]), float(coord_tuple[2])

            min_x = min(min_x, x)
            min_y = min(min_y, y)
            min_z = min(min_z, z)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)

            coords.append((x, y, z))

    range_x = max_x - min_x
    range_y = max_y - min_y
    range_z = max_z - min_z

    scale_x = dim / range_x
    scale_y = dim / range_y
    scale_z = dim / range_z

    # 3D tensor filled with zeros
    tensor = [[[0 for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]

    # Point mapping
    for x, y, z in coords:
        # Scaling
        scaled_x = int((x - min_x) * scale_x)
        scaled_y = int((y - min_y) * scale_y)
        scaled_z = int((z - min_z) * scale_z)
        # print(f"Scaled coordinates: ({scaled_x}, {scaled_y}, {scaled_z})")
        if 0 <= scaled_x < dim and 0 <= scaled_y < dim and 0 <= scaled_z < dim:
            # Setting to 1
            # TODO: change range to 31 instead of 32
            tensor[scaled_x][scaled_y][scaled_z] = 1

    return tensor

def readOff(filename):
    f = open(filename)
    f.readline()
    nvertices, nfaces, nedges = map(int, f.readline().split())
    vertices = []
    for _ in range(nvertices):
        vertices.append(list(map(float, f.readline().strip().split())))
    vertices = np.array(vertices)

    triangles = []
    for _ in range(nfaces):
        face = list(map(int, f.readline().strip().split()))
        ntriangles, verts = face[0] - 3 + 1, face[1:]
        for n in range(ntriangles):
            triangles.append([verts[0], verts[1 + n], verts[2 + n]])
    triangles = np.array(triangles)

    return vertices, triangles

def save_png(off_filename, png_filename):
    vertices, faces = readOff(off_filename)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection object with the faces and vertices
    mesh = Poly3DCollection(vertices[faces])
    mesh.set_edgecolor('k')
    ax.add_collection3d(mesh)

    ax.set_xlim([min(vertices[:, 0]), max(vertices[:, 0])])
    ax.set_ylim([min(vertices[:, 1]), max(vertices[:, 1])])
    ax.set_zlim([min(vertices[:, 2]), max(vertices[:, 2])])

    plt.axis('off')  # Turn off the axis
    plt.savefig(png_filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()


def process_directory(root_dir):
    X_train, y_train, X_test, y_test = [], [], [], []
    skip_count = 0
    for class_dir in os.listdir(root_dir):
        for dataset_type in ['train', 'test']:
            dataset_dir = os.path.join(root_dir, class_dir, dataset_type)
            for filename in os.listdir(dataset_dir):
                if filename.endswith(".off"):
                    input_path = os.path.join(dataset_dir, filename)
                    temp_stl_path = "./temporary.stl"
                    temp_xyz_path = "./temporary.xyz"
                    temp_png_path = "./temporary.png"

                    off_to_stl(input_path, temp_stl_path)
                    try:
                        stltovoxel.convert_file(temp_stl_path, temp_xyz_path, resolution)
                        voxel_tensor = xyz_to_tensor(temp_xyz_path, tensor_size)                    
                        save_png(input_path, temp_png_path)
                    except:
                        skip_count += 1
                        continue

                    image = Image.open(temp_png_path).convert('L').resize((128, 128))
                    image_tensor = np.array(image).reshape(128, 128, 1)

                    if dataset_type == 'train':
                        X_train.append(voxel_tensor)
                        y_train.append(image_tensor)
                    else:
                        X_test.append(voxel_tensor)
                        y_test.append(image_tensor)

    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)

resolution = 50
tensor_size = 32

npy_files = ['./X_train.npy', './y_train.npy', './X_test.npy', './y_test.npy']
if all(os.path.exists(npy_file) for npy_file in npy_files):
    # Load the arrays from the .npy files
    X_train = np.load(npy_files[0])
    y_train = np.load(npy_files[1])
    X_test = np.load(npy_files[2])
    y_test = np.load(npy_files[3])
else:
    X_train, y_train, X_test, y_test = process_directory("C:\\Users\\sebas\\Downloads\\3D GAN\\ModelNet40")
    np.save(npy_files[0], X_train)
    np.save(npy_files[1], y_train)
    np.save(npy_files[2], X_test)
    np.save(npy_files[3], y_test)


    