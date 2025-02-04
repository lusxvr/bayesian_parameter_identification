#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2023                                            ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import vtk

import dolfin_warp as dwarp

################################################################################

def generate_images(
        L,
        n_voxels,
        ref_image_model,
        working_folder,
        working_basename,
        upsampling_factor=1):

    ref_image = vtk.vtkImageData()
    n_voxels_upsampled = n_voxels * upsampling_factor
    dimensions           = [n_voxels          , n_voxels          , 1]
    dimensions_upsampled = [n_voxels_upsampled, n_voxels_upsampled, 1]
    ref_image.SetDimensions(dimensions_upsampled)
    delta           = L/n_voxels
    delta_upsampled = L/n_voxels_upsampled
    spacing           = [delta          , delta          , 1.]
    spacing_upsampled = [delta_upsampled, delta_upsampled, 1.]
    ref_image.SetSpacing(spacing_upsampled)
    origin           = [delta/2, delta/2, 0.]
    origin_upsampled = origin
    ref_image.SetOrigin(origin_upsampled)
    n_points_upsampled = ref_image.GetNumberOfPoints()
    ref_scalars = vtk.vtkDoubleArray()
    ref_scalars.SetName("ImageScalars")
    ref_scalars.SetNumberOfComponents(1)
    ref_scalars.SetNumberOfTuples(n_points_upsampled)
    ref_image.GetPointData().SetScalars(ref_scalars)

    dwarp.compute_warped_images(
        working_folder=working_folder,
        working_basename=working_basename,
        working_ext="vtu",
        working_displacement_field_name="U",
        ref_image=ref_image,
        ref_image_model=ref_image_model,
        ref_frame=0,
        suffix="",
        print_warped_mesh=0,
        verbose=0)
    dwarp.compute_downsampled_images(
        images_folder=working_folder,
        images_basename=working_basename,
        downsampling_factors=[upsampling_factor, upsampling_factor],
        images_ext="vti",
        keep_resolution=0,
        write_temp_images=0,
        suffix="",
        verbose=0)
