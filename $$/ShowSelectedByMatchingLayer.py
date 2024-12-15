import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
import System

def ShowSelectedByMatchingLayers():
    
    hIds = rs.HiddenObjects()
    if not hIds:
        print "No objects are hidden."
        return

    selIds = rs.SelectedObjects()
          
    if not selIds:
        selIds = rs.GetObjects("Select objects on the layers to match.")
        if not selIds:return
    
    allIds = rs.AllObjects()
    if not allIds: return
    
    offLayers = []
    lockedLayers = []
    selLayers = list(set([System.Guid((rs.LayerId(rs.ObjectLayer(id)))) for id in selIds]))
    
    rs.EnableRedraw(False)
    for id in allIds:
        obj = sc.doc.Objects.Find(id)
        if obj.IsHidden:
            idx = obj.Attributes.LayerIndex
            layerId = sc.doc.Layers.FindIndex(idx).Id
            if layerId in selLayers:
                rs.ShowObject(id)
                
    rs.EnableRedraw(True)
    
if __name__ == "__main__": ShowSelectedByMatchingLayers()