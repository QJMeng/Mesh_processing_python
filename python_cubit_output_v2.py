#!python 
#This mesh processing python script is used only for split fault model (and slave and master node location shift by a small value)
from __future__ import print_function
import math
import os
import sys 
try:
    #cubit.init([""])
    cubit.init(["-noecho","-nojournal"])
except:
    pass
# gets version string
cubit_version = cubit.get_version()
print("version: ",cubit_version)
#                                                                                                     
# GEOCUBIT
#
# adds path to geocubit (if not setup yet)
sys.path.append('./')
import geocubitlib
sys.path.append(geocubitlib.__path__[0])

print("path: ")
print(sys.path)
print("")

from geocubitlib import save_fault_nodes_elements_EQdyna
from geocubitlib import save_mesh_nodes_elements_EQdyna
os.system('mkdir -p MESH')
#no input; output is mesh_file and node_file in MESH folder
save_mesh_nodes_elements_EQdyna.mesh_input()        
#input fault id, fault surface list for slave fault; output file is fault_file_id.dat in MESH folder
save_fault_nodes_elements_EQdyna.fault_input(1,[20])
