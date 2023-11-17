#!/bin/bash

# pre-process the sofas training set (SDF samples)

# source ../prep_cuda.sh

# 激活Anaconda环境
conda activate hjp_deepsdf
which python
PYTHON="/usr/wiss/lhao/anaconda3/envs/hjp_deepsdf/bin/"

export PANGOLIN_WINDOW_URI=headless://
export MESA_GL_VERSION_OVERRIDE=3.3

# SOURCE_PATH="/data/hdd1/storage/junpeng/data/ShapeNetCore.v2/"
# SOURCE_PATH="/storage/group/dataset_mirrors/ShapeNetV2/ShapeNetCore.v2"
SOURCE_PATH="DATA/ScanARCW/canonical_mesh_manifoldplus"
# SOURCE_PATH="DATA/ShapeNetV2"

SOURCE_NAME=""
# SOURCE_NAME="--name ShapeNetV2"

SPLIT="examples/splits/sv2_sofas_all_manifoldplus_scanarcw.json"
# SPLIT="examples/splits/sv2_chairs_train.json"

python preprocess_data.py --data_dir data --source ${SOURCE_PATH} ${SOURCE_NAME} --split ${SPLIT} --skip

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