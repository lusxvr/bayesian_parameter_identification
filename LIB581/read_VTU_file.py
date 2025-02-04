#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2023                                            ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import os
import vtk

################################################################################

def read_VTU_file(
        filebasename):

    filename = filebasename+".vtu"

    assert (os.path.isfile(filename)), "Wrong filename (\""+filename+"\"). Aborting."

    ugrid_reader = vtk.vtkXMLUnstructuredGridReader()
    ugrid_reader.SetFileName(filename)
    ugrid_reader.Update()
    ugrid = ugrid_reader.GetOutput()

    return ugrid
