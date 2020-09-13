import bpy

def separate_submesh(mesh, vertex_group_names, new_mesh_name=None):
    # Select the mesh
    mesh.select_set(True)

    # Duplicate the original mesh
    bpy.ops.object.duplicate()
    mesh = bpy.context.object

    if new_mesh_name:
        mesh.name = new_mesh_name

    # Separate out all the specified vertex groups from a mesh into a separate mesh, and return the new mesh object
    if mesh.type != 'MESH':
        return None
    
    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    
     # Deselect any parts of the mesh that might be selected
    bpy.ops.mesh.select_all( action = 'DESELECT' )

    # Select specified groups
    for group_to_select in vertex_group_names:
        if not group_to_select in mesh.vertex_groups:
            print('No vertex group for ' + group_to_select)
            continue
        print("Select " +  group_to_select)
        bpy.ops.object.vertex_group_set_active(group=group_to_select)
        bpy.ops.object.vertex_group_select()
    
    # Select everything except the mesh groups we want to keep
    bpy.ops.mesh.select_all(action='INVERT')

    # Delete everything except the groups we want to keep
    bpy.ops.mesh.delete(type='VERT')
    
    return bpy.context.object

# Starting from a root bone, return a set containing name of root bone and all children
# Bones in the exclude set, and all of their children will be ignored
def get_bone_names_recursive(skeleton, root_bone_name, exclude={}):
    bones = skeleton.data.bones
    openset = [root_bone_name]
    output = set()

    while len(openset) > 0:
        current_bone = openset.pop()
        output.add(current_bone)
        for child in bones[current_bone].children:
            if not child.name in exclude:
                openset.append(child.name)
    
    return output

# Get list of bones that should go into the first-person arms mesh
def get_arm_mesh_bones_list(inputmesh):
    if inputmesh.parent is None:
        return None
    if inputmesh.parent.type != 'ARMATURE':
        return None
    skeleton = inputmesh.parent
    left_bones = get_bone_names_recursive(skeleton, 'upperarm_l')
    right_bones = get_bone_names_recursive(skeleton, 'upperarm_r', {'weapon_r'})
    # Append left bone set to right
    arm_bones = left_bones | right_bones
    return arm_bones

# Create first person arms mesh
def create_first_person_arms(inputmesh, vertex_group_names=None):
    print('-------------------------------------------------')
    print('Creating first person arms from ' + inputmesh.name)
    print('-------------------------------------------------')

    if (inputmesh.type != 'MESH'):
        print('Error: {name} is not a mesh, it is a {type}!'.format(name=inputmesh.name, type=inputmesh.type))
        return

    if vertex_group_names is None:
        vertex_group_names = get_arm_mesh_bones_list(inputmesh)
    
    if len(vertex_group_names) > 0:
        separate_submesh(inputmesh, vertex_group_names, 'FP_Arms')

# Get list of bones that should go into the third-person legs mesh
def get_leg_mesh_bones_list(inputmesh):
    if inputmesh.parent is None:
        return None
    if inputmesh.parent.type != 'ARMATURE':
        return None
    skeleton = inputmesh.parent
    leg_bones = get_bone_names_recursive(skeleton, 'pelvis', {'spine_01'})
    return leg_bones

# Create first person legs mesh
def create_first_person_legs(inputmesh, vertex_group_names=None):
    print('-------------------------------------------------')
    print('Creating first person legs from ' + inputmesh.name)
    print('-------------------------------------------------')

    if (inputmesh.type != 'MESH'):
        print('Error: {name} is not a mesh, it is a {type}!'.format(name=inputmesh.name, type=inputmesh.type))
        return
    
    if vertex_group_names is None:
        vertex_group_names = get_leg_mesh_bones_list(inputmesh)
    
    if len(vertex_group_names) > 0:
        separate_submesh(inputmesh, vertex_group_names, 'FP_Legs')

