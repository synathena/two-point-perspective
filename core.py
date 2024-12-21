import bpy
import math
import logging
import numpy as np

from mathutils import Vector


logger = logging.getLogger(__name__)


def nearest_quarter(ang):
    """Calculates the nearest quarter circle of an angle."""
    return (((round((ang / np.pi) / 0.5)) / 4) * (2 * np.pi)) % (2 * np.pi)


def add_two_point_perspective_camera(cam_obj, auto_direction=False, custom_direction_value=90):
    """Create a copy of a camera and turn the 3-point perspective
    to 2-point perspective."""
    # custom_direction_value = math.radians(custom_direction_value)
    scene = bpy.context.scene
    parent = cam_obj.parent
    cam_collections = cam_obj.users_collection

    matrix = cam_obj.matrix_world
    cam_obj.parent = None
    cam_obj.matrix_world = matrix

    cam_position = cam_obj.location
    cam_obj.rotation_mode = "XYZ"
    cam_rotation = cam_obj.rotation_euler
    sign = 1
    if cam_rotation[0] < 0:
        sign = -1
    cam = cam_obj.data
    camera_type = cam.type  
    cam.type = 'PERSP' 
    focal_length = cam.lens # set the camera to perspective in case it is not, temporarily
    ratio = scene.render.resolution_x / scene.render.resolution_y

    # if the camera is not already 2-point perspective
    if round(cam_rotation[0] % (math.pi / 2), 3) != 0:
        if cam.sensor_fit == "HORIZONTAL" or (cam.sensor_fit == "AUTO" and ratio >= 1):
            sensor_size = cam.sensor_width
        # elif cam.sensor_fit == "VERTICAL" or (cam.sensor_fit == "AUTO" and ratio < 1):
        # (this is equivalent to the "else" that follows)
        else:
            sensor_size = cam.sensor_height

        if auto_direction:
            # correct the distortion to the closest quarter
            corrected_rotation = nearest_quarter(cam_rotation[0])
        else:
            # correct the distortion to chosen direction
            corrected_rotation = sign * custom_direction_value

        # trigonometry calculations
        angle = corrected_rotation - cam_rotation[0]
        adjacent_side = focal_length / sensor_size
        opposite_side = -math.tan(angle) * adjacent_side
        offset = (adjacent_side / math.cos(angle)) - adjacent_side
        offset_vec = 0, 0, offset
        inv = cam_obj.matrix_world.copy()
        inv.invert()
        rotated_offset_vec = Vector(offset_vec) @ inv
        corrected_position = cam_position + rotated_offset_vec

  
        corrected_cam = cam.copy()
        corrected_cam.name = cam_obj.name + ".two_point_perspective"
        corrected_cam_obj = bpy.data.objects.new(corrected_cam.name, corrected_cam)
        active = corrected_cam_obj
        corrected_cam_obj.rotation_euler = cam_rotation

        for cam_collection in cam_collections:
            cam_collection.objects.link(corrected_cam_obj)


        corrected_cam_obj.location = corrected_position
        corrected_cam_obj.rotation_euler[0] = corrected_rotation
        corrected_cam.shift_y = opposite_side
        logger.debug("Corrected shift, position and rotation of the camera")
        if parent is not None:
            corrected_cam_obj.parent = parent
            logger.debug("Parent set to the corrected camera")
            corrected_cam_obj.matrix_parent_inverse = parent.matrix_world.inverted()
        logger.debug("Camera correction finished")

    else:
        logger.debug("This camera is already a two point perspective camera")
        active = cam_obj
    if parent is not None:
        cam_obj.parent = parent
        cam_obj.matrix_parent_inverse = parent.matrix_world.inverted()
    cam.type = camera_type
    return active
