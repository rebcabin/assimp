from pyassimp import *
import os
cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
fname = '../../../../Ops-robotics-rsimcon/content/raw/mesh' \
        '/64907_Fanuc_430_Robot/j3-9-binary.fbx'
debug_me = os.path.isfile(fname)
assimp_scene = load (fname)
assimp_vertices = assimp_scene.meshes[0].vertices
print {"mesh_count": len(assimp_scene.meshes), "vertex_count_mesh_0": len(
    assimp_vertices)}