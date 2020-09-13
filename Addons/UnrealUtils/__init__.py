# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Bryan Unreal Utils",
    "author" : "Bryan Robertson",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . unrealtools_panel import UnrealTools_PT_Panel
from . unrealtools_panel import BL_OT_RenameBones
from . unrealtools_panel import BL_OT_CreateFirstPersonArms
from . unrealtools_panel import BL_OT_CreateFirstPersonLegs

classes = { UnrealTools_PT_Panel, BL_OT_RenameBones, BL_OT_CreateFirstPersonArms, BL_OT_CreateFirstPersonLegs }

def register():
    for entry in classes:
        bpy.utils.register_class(entry)

def unregister():
    for entry in reversed(classes):
        bpy.utils.unregister_class(entry)

if __name__ == "__main__":
    register()