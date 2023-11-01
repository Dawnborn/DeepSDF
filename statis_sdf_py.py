import numpy as np
from mesh_to_sdf import get_surface_point_cloud,scale_to_unit_cube, scale_to_unit_sphere, BadMeshException, sample_sdf_near_surface
import trimesh

import matplotlib.pyplot as plt

import pdb
import time

from vis_sdf import vis_sdf

deepsdf_sdf = "data/SdfSamples/ShapeNetV2/04256520/1a4a8592046253ab5ff61a3a2a0e2484.npz"
deepsdf_mesh = "data/ShapeNetCore.v2/04256520/1a4a8592046253ab5ff61a3a2a0e2484/models/model_normalized.obj"

samples = np.load(deepsdf_sdf)
neg_samples = samples["neg"]
pos_samples = samples["pos"]
points_dsdf = np.concatenate((neg_samples[:,:3], pos_samples[:,:3]), axis=0)
sdf_dsdf = np.concatenate((neg_samples[:,3], pos_samples[:,3]), axis=0)

mesh = trimesh.load(deepsdf_mesh)
points_py, sdf_py = sample_sdf_near_surface(mesh, number_of_points=500000, scale1=)

pdb.set_trace()

# plotting the SDF values
plt.hist(sdf_dsdf, bins=100, label="DeepSDF")
plt.hist(sdf_py, bins=100, label="mesh_to_sdf")
plt.legend()