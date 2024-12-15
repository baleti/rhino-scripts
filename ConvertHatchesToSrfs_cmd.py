import rhinoscriptsyntax as rs

def RunCommand( is_interactive ):

    #get current color
    hatchId = rs.GetObject(
        "Pick one hatch", filter=65536, preselect=True, select=True, 
        subobjects=False)
    color = rs.ObjectColor(hatchId)

    #run macro
    macro = """
    selcolor invert hide selprev dupborder invert
    delete selall planarsrf delete selall join dupborder
    invert delete selall planarsrf delete selall group show
    """
    rs.Command(macro, echo=False)

    #set previous color as a new material
    new_objects = rs.SelectedObjects()
    for i in new_objects:
        material_idx = rs.AddMaterialToObject(i)
        rs.MaterialColor(material_idx, color)