import bpy
from bpy.types import Panel


class Camera_PT_Panel(Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    bl_label = "2-Point Perspective Camera"
    bl_category = "Camera"

    def draw(self, context):
        layout = self.layout
        row0 = layout.row()
        col0_0 = row0.column()
        col0_0.prop(context.scene.two_point_perspective, "custom_angle")
        col0_1 = row0.column()
        col0_1.prop(context.scene.two_point_perspective, "custom_angle_value")
        row1 = layout.row()
        col1_0 = row1.column()
        col1_0.operator("scene.two_point_perspective", icon="CON_CAMERASOLVER")
