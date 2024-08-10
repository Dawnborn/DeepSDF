#!/bin/bash

# pre-process the sofas training set (SDF samples)

export CUDA_VISIBLE_DEVICES=5

export LD_LIBRARY_PATH=/home/wiss/lhao/storage/user/hjp/ws_dditnach/third-party/myopenexr/lib:$LD_LIBRARY_PATH
export PATH=/home/wiss/lhao/storage/user/hjp/ws_dditnach/third-party/myopenexr/bin:$PATH
export LD_LIBRARY_PATH=/home/wiss/lhao/storage/user/hjp/ws_dditnach/third-party/myglew/lib64:$LD_LIBRARY_PATH
export PATH=/home/wiss/lhao/storage/user/hjp/ws_dditnach/third-party/myglew/bin:$PATH

# 激活Anaconda环境
conda activate hjp_deepsdf
which python
PYTHON="/usr/wiss/lhao/anaconda3/envs/hjp_deepsdf/bin/"

export PANGOLIN_WINDOW_URI=headless:// # 避免弹窗
export MESA_GL_VERSION_OVERRIDE=3.3 # 避免GL版本报错

# SOURCE_PATH="/data/hdd1/storage/junpeng/data/ShapeNetCore.v2/"
# SOURCE_PATH="/storage/group/dataset_mirrors/ShapeNetV2/ShapeNetCore.v2"
# SOURCE_PATH="DATA/ScanARCW/canonical_mesh_manifoldplus"
# SOURCE_PATH="DATA/ShapeNetV2"
SOURCE_PATH="/storage/user/huju/transferred/ws_dditnach/DATA/ShapeNet_manifoldplus"
# SOURCE_PATH="/storage/group/dataset_mirrors/ShapeNetV2/ShapeNetCore.v2"

# SOURCE_NAME=""
# SOURCE_NAME="--name ShapeNetV2"

SPLIT="examples/splits/sv2_sofas_all_manifoldplus_scanarcw.json"
SPLIT="examples/splits/scanarcw_chairs_all_manifoldplus.json"
SPLIT="examples/splits/scanarcw_bathtubs_all_manifoldplus.json"
SPLIT="examples/splits/scanarcw_beds_all_manifoldplus.json"
SPLIT="examples/splits/scanarcw_bookshelfs_all_manifoldplus.json"
SPLIT="examples/splits/scanarcw_cabinets_all_manifoldplus.json"
# SPLIT="examples/splits/scanarcw_tables_all_manifoldplus.json"
# SPLIT="examples/splits/sv2_chairs_train.json"
# SPLIT="examples/splits/sv2_tables_train.json"
# SPLIT="examples/splits/sv2_sofas_train.json"
# SPLIT="examples/splits/sv2_sofas_all_manifoldplus_shapenet.json"
# SPLIT="examples/splits/sv2_sofas_all.json"

SPLIT="examples/splits/shapenet2_manifold_bathtubs_all.json"
SPLIT="examples/splits/shapenet2_manifold_tables_all.json"
SPLIT="examples/splits/shapenet2_manifold_chairs_all.json"

SKIP="--skip"
# SKIP=""

SURFACE="--surface"
SURFACE=""

NUM_THREADS="28"

/usr/wiss/lhao/anaconda3/envs/hjp_deepsdf/bin/python preprocess_data.py --data_dir data --source ${SOURCE_PATH} ${SOURCE_NAME} --split ${SPLIT} ${SKIP} ${SURFACE} --threads ${NUM_THREADS}

# # train the model
# python train_deep_sdf.py -e examples/sofas

# pre-process the sofa test set (SDF samples)
# python preprocess_data.py --data_dir data --source ${SOURCE_PATH} --name ShapeNetV2 --split ${SPLIT} --test --skip

# pre-process the sofa test set (surface samples)
# python preprocess_data.py --data_dir data --source ${SOURCE_PATH} --name ShapeNetV2 --split ${SPLIT} --surface --skip

# # reconstruct meshes from the sofa test split (after 2000 epochs)
# python reconstruct.py -e examples/sofas -c 2000 --split examples/splits/sv2_sofas_test.json -d data --skip

# # evaluate the reconstructions
# python evaluate.py -e examples/sofas -c 2000 -d data -s examples/splits/sv2_sofas_test.json 