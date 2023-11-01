# pre-process the sofas training set (SDF samples)
source ../prep_cuda.sh

export PANGOLIN_WINDOW_URI=headless://

SOURCE_PATH="/data/hdd1/storage/junpeng/data/ShapeNetCore.v2/"

CATEGORY="bottles"

conda activate deepsdf

python preprocess_data.py --data_dir data --source ${SOURCE_PATH} --name ShapeNetV2 --split examples/splits/sv2_${CATEGORY}_train.json --skip

# # train the model
# python train_deep_sdf.py -e examples/sofas


# pre-process the sofa test set (SDF samples)
python preprocess_data.py --data_dir data --source ${SOURCE_PATH} --name ShapeNetV2 --split examples/splits/sv2_${CATEGORY}_test.json --test --skip

# pre-process the sofa test set (surface samples)
python preprocess_data.py --data_dir data --source ${SOURCE_PATH} --name ShapeNetV2 --split examples/splits/sv2_${CATEGORY}_test.json --surface --skip

# # reconstruct meshes from the sofa test split (after 2000 epochs)
# python reconstruct.py -e examples/sofas -c 2000 --split examples/splits/sv2_sofas_test.json -d data --skip

# # evaluate the reconstructions
# python evaluate.py -e examples/sofas -c 2000 -d data -s examples/splits/sv2_sofas_test.json 