#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2023                                            ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import dolfin
import os
import shutil

################################################################################

def write_VTU_file(
        filebasename,
        function):

    file_pvd = dolfin.File(filebasename+"_.pvd")
    file_pvd << (function, 0.)
    os.remove(
        filebasename+"_.pvd")
    shutil.move(
        filebasename+"_"+"".zfill(6)+".vtu",
        filebasename+".vtu")
