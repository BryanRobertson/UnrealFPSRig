import bpy
import sys
from . import mesh_utils

class BL_OT_RenameBones(bpy.types.Operator):
    bl_idname = "unrealtools.renamebones"
    bl_label = "Rename Bones To Epic Skeleton"
    bl_description = "Rename Bones to Epic Skeleton"
    
    def execute(self, context):
        return {'FINISHED'}

class BL_OT_CreateFirstPersonArms(bpy.types.Operator):
    bl_idname = "unrealtools.createfirstpersonarms"
    bl_label = "Create First Person Arms"
    bl_description = "Create first person arm mesh from input mesh"

    def execute(self, context):
        source = bpy.context.object
        mesh_utils.create_first_person_arms(source)
        return {'FINISHED'}

class BL_OT_CreateFirstPersonLegs(bpy.types.Operator):
    bl_idname = "unrealtools.createfirstpersonlegs"
    bl_label = "Create First Person Legs"
    bl_description = "Create first person leg mesh from input mesh"

    def execute(self, context):
        source = bpy.context.object
        mesh_utils.create_first_person_legs(source)
        return {'FINISHED'}


class UnrealTools_PT_Panel(bpy.types.Panel):
    bl_idname = "UnrealTools_PT_Panel"
    bl_label = "Bryan Unreal Tools"
    bl_category = "Bryan Unreal Utils"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = 'Shootergame Tools')
        row = layout.row()
        row.operator('unrealtools.renamebones', icon='PASTEDOWN', text='Rename Bones')
        row = layout.row()
        row.operator('unrealtools.createfirstpersonarms', icon='PASTEDOWN', text='Create First Person Arm Mesh')
        row = layout.row()
        row.operator('unrealtools.createfirstpersonlegs', icon='PASTEDOWN', text='Create First Person Legs Mesh')



