#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2023                                            ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import dolfin

################################################################################

def write_XML_file(
        filebasename,
        function):

    dolfin.File(filebasename+".xml") << function
