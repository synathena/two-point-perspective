import bpy

from .two_point_perspective_ot import Two_Point_Perspective_OT_Operator, Properties
from .two_point_perspective_pt import Camera_PT_Panel

bl_info = {
    "name": "2-Point Perspective Camera",
    "author": "Athina Syntychaki",
    "description": "Replaces the active camera with a copy of it that uses two point perspective",
    "blender": (4, 2, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Camera",
}
classes = (
    Camera_PT_Panel,
    Two_Point_Perspective_OT_Operator,
    Properties,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.two_point_perspective = bpy.props.PointerProperty(type=Properties)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()