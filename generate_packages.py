import os
import subprocess

# 目录到debs、rootfull、roothide和rootless
debs_dir = "./debs"
rootfull_dir = os.path.join(debs_dir, "rootfull")
roothide_dir = os.path.join(debs_dir, "roothide")
rootless_dir = os.path.join(debs_dir, "rootless")
repo2_dir = "./repo2"
packages_file = os.path.join(repo2_dir, "Packages")

# 删除旧的 Packages 文件
if os.path.exists(packages_file):
    os.remove(packages_file)

# 函数来遍历目录并生成 Packages 文件
def generate_packages(directory):
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".deb"):
                    deb_path = os.path.join(root, filename)
                    # 使用dpkg-deb获取包信息
                    output = subprocess.check_output(["dpkg-deb", "-I", deb_path])
                    # 将包信息写入Packages文件
                    with open(packages_file, "a") as f:
                        f.write(output.decode("utf-8"))
                        f.write("\n\n")
    else:
        print(f"Directory {directory} does not exist.")

# 遍历debs目录下的所有deb文件夹
generate_packages(debs_dir)

# 遍历rootfull目录下的所有deb文件夹
generate_packages(rootfull_dir)

# 遍历roothide目录下的所有deb文件夹
generate_packages(roothide_dir)

# 遍历rootless目录下的所有deb文件夹
generate_packages(rootless_dir)

print("Packages file generated successfully.")
