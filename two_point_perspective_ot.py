import bpy
from bpy.types import Operator
from bpy.types import PropertyGroup

from .core import *


class Two_Point_Perspective_Properties(PropertyGroup):
    custom_angle: bpy.props.BoolProperty(
        name="Custom target angle",
        default=False,
        description="Set the target angle manually",
    )
    custom_angle_value: bpy.props.FloatProperty(
        name="",
        default=0,
        min=0.0,
        max=360.0,
        subtype="ANGLE",
        description="Set the target angle manually",
    )


class Two_Point_Perspective_OT_Operator(Operator):
    bl_idname = "scene.two_point_perspective"
    bl_label = "Create Two-Point Perspective Camera"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = (
        "Make the active camera two-point perspective"
    )

    def execute(self, context):
        if context.scene.camera is None:
            self.report(
                {"WARNING"},
                "No camera was assigned to the scene, the first camera in the hierarchy will be used",
            )
            for obj in context.scene.objects:
                if obj.type == "CAMERA":
                    context.scene.camera = obj
                    break
            else:
                self.report({"ERROR"}, "There is no camera in the scene")
                return

        active_cam = add_two_point_perspective_camera(
            context.scene.camera,
            auto_direction=not context.scene.two_point_perspective.custom_angle,
            custom_direction_value=context.scene.two_point_perspective.custom_angle_value,
        )
        context.scene.camera = active_cam
        return {"FINISHED"}
