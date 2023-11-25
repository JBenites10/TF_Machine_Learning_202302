import subprocess
import os

def convert_to_binvox(stl_file, voxel_size, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    binvox_file = os.path.join(output_folder, os.path.splitext(os.path.basename(stl_file))[0] + ".binvox")

    binvox_cmd = f".\\binvox -c -d {voxel_size} -t binvox -e {binvox_file} {stl_file}"
    subprocess.run(binvox_cmd, shell=True)

def main():
    stl_folder = "train_stl"
    output_folder = "train_voxels"
    voxel_size = 64

    for stl_file in os.listdir(stl_folder):
        if stl_file.endswith(".stl"):
            stl_path = os.path.join(stl_folder, stl_file)
            convert_to_binvox(stl_path, voxel_size, output_folder)

if __name__ == "__main__":
    main()