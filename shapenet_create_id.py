#%%
import os
import json
import pdb
import random
import json

shapenet_root="/data/hdd1/storage/junpeng/ws_dditplus/DeepSDF/data/ShapeNetCore.v2"
category_name2id = {}
category_name2id['bottle']='02876657'
category_name2id['cup']=''
#%%
pdb.set_trace()
list_path = os.listdir(os.path.join(shapenet_root,category_name2id['bottle']))
#%%
seed=2254

def split_list(input_list, seed=None,ratio=0.8):
    """
    Split a list into two parts: 20% and 80% based on a given seed.
    
    Parameters:
    - input_list: The list to be split.
    - seed: Random seed for reproducibility.
    
    Returns:
    - tuple containing two lists: the first one with 20% of the elements and the second one with 80% of the elements.
    """
    random.seed(seed)  # Set the seed for reproducibility
    shuffled_list = random.sample(input_list, len(input_list))  # This shuffles the list without replacement
    
    split_index = int(len(input_list) * ratio)  # Calculate index for 20% split
    
    return shuffled_list[:split_index], shuffled_list[split_index:]  # Return the two parts

train_list, test_list = split_list(list_path,seed=seed,ratio=0.8) 

train_data = {
    "ShapeNetV2": {
        category_name2id['bottle']: train_list
    }
}

test_data = {
    "ShapeNetV2":{
        category_name2id['bottle']: test_list
    }
}

output_root = "/data/hdd1/storage/junpeng/ws_dditplus/DeepSDF/examples/splits/"
train_data_path = os.path.join(output_root,"sv2_bottles_train.json")
test_data_path = os.path.join(output_root,"sv2_bottles_test.json")

with open(train_data_path,'w') as file:
    json.dump(train_data, file, indent=4)

with open(test_data_path,'w') as file:
    json.dump(test_data, file, indent=4)

pdb.set_trace()