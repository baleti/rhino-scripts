import scriptcontext as sc
import rhinoscriptsyntax as rs
import collections

def ConsolidateLayers():
    
    layers = rs.LayerNames()
    
    stripped = []
    top = []
    crnt = False
    for layer in layers:
        if not rs.LayerChildren(layer) and not crnt:
            rs.CurrentLayer(layer)
            crnt=True
        idx = layer.find("::",1)
        if idx>-1:
          stripped.append(layer[idx+1:])
        else:
            top.append(layer)
        pass
    dups = [item for item, count in collections.Counter(stripped).items() if count > 1]
    

    
    
    rs.EnableRedraw(False)
    for item in dups:
        targLayer = None
        for tLayer in top:
            tempLayer = tLayer+":"+item
            if rs.IsLayer(tempLayer):
                if not targLayer:
                    targLayer = tempLayer
                ids = rs.ObjectsByLayer(tempLayer)
                rs.ObjectLayer(ids, targLayer)
                if tempLayer != targLayer:
                    rs.DeleteLayer(tempLayer)

        if targLayer:pass
            
    for layer in layers:
        if rs.IsLayer(layer):
            if rs.IsLayerEmpty(layer):
                rs.DeleteLayer(layer)
                
    #    for layer in top:
    #        if rs.IsLayer(layer):
    #            print layer
    #            print rs.PurgeLayer(layer)
                
    rs.EnableRedraw(True)
    
if __name__== '__main__': ConsolidateLayers()