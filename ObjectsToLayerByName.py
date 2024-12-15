import rhinoscriptsyntax as rs


def ObjectsToLayerByName():
    
    ids = rs.NormalObjects()
    if not ids: return
    
    for id in ids:
        name = rs.ObjectName(id)
        if name is not None:
            if not rs.IsLayer(name):
                rs.AddLayer(name)
            rs.ObjectLayer(id, name)
        
if __name__ == '__main__': ObjectsToLayerByName()