import os
import json
import random

num2cat = {
    "02808440": "bathtub",
    "02818832": "bed",
    "02871439": "bookshelf",
    "02933112": "cabinet",
    "03001627": "chair",
    "04256520": "sofa",
    "04379243": "table"
}

cat2num = dict()
for key in num2cat.keys():
    cat2num[num2cat[key]] = key

# 设置随机种子，确保每次运行得到相同的随机结果
random_seed = 42
random.seed(random_seed)

cat = "table"
num = cat2num[cat]

# 假设你有一个文件列表
# file_list = os.listdir("/home/wiss/lhao/storage/user/hjp/ws_dditnach/Diffusion-SDF/data/canonical_manifoldplus/02808440")
# file_list = os.listdir("/home/wiss/lhao/storage/user/hjp/ws_dditnach/DeepImplicitTemplates/data/ScanARCW/sdf_samples_canonical_manifoldplus/04256520")
file_list = os.listdir("/storage/user/huju/transferred/ws_dditnach/DATA/ShapeNet_manifoldplus/02808440")
file_list = os.listdir("/storage/user/huju/transferred/ws_dditnach/DATA/ShapeNet_manifoldplus/04379243")

file_list = [file.split(".")[0] for file in file_list]

# 随机打乱文件列表
random.shuffle(file_list)

# 计算80%的索引位置
split_index = int(0.8 * len(file_list))

# 分割成80%和20%两份
train_files = file_list[:split_index]
test_files = file_list[split_index:]

# test_json_file_path = "/home/wiss/lhao/storage/user/hjp/ws_dditnach/DeepImplicitTemplates/examples/splits/sv2_sofas_test_manifoldplus_scanarcw.json"
# train_json_file_path = "/home/wiss/lhao/storage/user/hjp/ws_dditnach/DeepImplicitTemplates/examples/splits/sv2_sofas_train_manifoldplus_scanarcw.json"
# all_json_file_path = "/home/wiss/lhao/storage/user/hjp/ws_dditnach/DeepImplicitTemplates/examples/splits/sv2_sofas_all_manifoldplus_scanarcw.json"

sdf_dataset = "ShapeNet_manifoldplus"

train_json_file_path = "/storage/user/huju/transferred/ws_dditnach/DeepSDF/examples/splits/shapenet2_manifold_{}s_train.json".format(cat)
test_json_file_path = "/storage/user/huju/transferred/ws_dditnach/DeepSDF/examples/splits/shapenet2_manifold_{}s_test.json".format(cat)
all_json_file_path = "/storage/user/huju/transferred/ws_dditnach/DeepSDF/examples/splits/shapenet2_manifold_{}s_all.json".format(cat)

with open(train_json_file_path, "w") as json_file:
    data = dict()
    idata = dict()
    idata[num] = train_files
    data[sdf_dataset] = idata
    json.dump(data, json_file, indent=4)

with open(train_json_file_path, "w") as json_file:
    data = dict()
    idata = dict()
    idata[num] = train_files
    data[sdf_dataset] = idata
    json.dump(data, json_file, indent=4)

with open(all_json_file_path, "w") as json_file:
    data = dict()
    idata = dict()
    idata[num] = file_list
    data[sdf_dataset] = idata
    json.dump(data, json_file, indent=4)