import rhinoscriptsyntax as rs

def SelectAllObjsOnObjLayers():
    objs=rs.GetObjects("Select objects",preselect=True)
    if not objs: return
    rs.EnableRedraw(False)
    layers=[rs.ObjectLayer(obj) for obj in objs]
    for layer in layers: rs.ObjectsByLayer(layer,True)
SelectAllObjsOnObjLayers()