import rhinoscriptsyntax as rs


def ChangeLayerInBlockRecursively():
    
    ids = rs.GetObjects("Select block instances", 4096, preselect=True)
    if not ids:return
    
    targ = rs.GetLayer()
    if not targ:return
    
    names = list(set([rs.BlockInstanceName(id) for id in ids]))
    done = []
    
    def BlockDrill(names):
        while True:
            if len (names) > 0 :
                name = names.pop()
            else: break
            
            done.append(name)
            temp = rs.BlockObjects(name)
            rs.ObjectLayer(temp, targ)
            
            for tempId in temp:
                if rs.IsBlockInstance(tempId):
                    tempName = rs.BlockInstanceName(tempId)
                    if tempName not in names and tempName not in done:
                        names.append(tempName)
                        BlockDrill(names)
            
    BlockDrill(names)
    
if __name__ == "__main__": ChangeLayerInBlockRecursively()