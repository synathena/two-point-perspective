import bpy
from bpy.types import Panel


class Camera_PT_Panel(Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    bl_label = "Two-Point Perspective Camera"
    bl_category = "Camera"

    def draw(self, context):
        layout = self.layout
        two_point_perspective = context.scene.two_point_perspective
        
        box = layout.box()

        row0 = box.row(align=True)
        col0_0 = row0.column()
        col0_0.prop(two_point_perspective, "custom_angle", text="Custom Angle")
        
        col0_1 = row0.column()
        col0_1.enabled = two_point_perspective.custom_angle
        col0_1.prop(context.scene.two_point_perspective,"custom_angle_value")
        
        layout.separator()
        layout.operator("scene.two_point_perspective", icon="CON_CAMERASOLVER")
