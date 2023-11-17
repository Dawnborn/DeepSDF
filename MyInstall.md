# Myinstall

## Preprocessing

### C++
```
cd third-party
mkdir dependency
git clone --recursive git@github.com:CLIUtils/CLI11.git
```
Pangolin
```
git clone --recursive -b v0.6 https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=third-party/dependency
make
make install
```

### Python environment
check cuda version
```
conda create -n hjp_dit37 python=3.7
conda install pytorch==1.12.1 torchvision==0.13.1 cudatoolkit=11.3 -c pytorch
conda install plyfile scikit-image trimesh

```

run the preprocessing script, take lamp as example
```
python preprocess_data.py .--data_dir data --source /storage/group/dataset_mirrors/ShapeNetV2/ShapeNetCore.v2 --name ShapeNetV2 --split examples/splits/sv2_lamps_test.json --skip
```

## ShapeNetV2
```
/storage/group/dataset_mirrors/ShapeNetV2/ShapeNetCore.v2
```