import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

def SelHatchPattern():
    ids = rs.ObjectsByType(65536, state=1)
    if not ids:
        print "No hatches found"
        return
    
    h = sc.doc.HatchPatterns
    selIdx = None
    names = [item.Name for item in h]

    go = Rhino.Input.Custom.GetObject()
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Hatch
    go.SetCommandPrompt("Select hatch objects or type a hatch pattern name inside double quotes.")
    go.AddOption("ListPatterns")
    
    go.AcceptString(True)
    
    rc = go.GetMultiple(1,0)
    
    if go.CommandResult() != Rhino.Commands.Result.Success:
        return
    if rc == Rhino.Input.GetResult.Option:
        selNames = rs.CheckListBox([(name,False) for name in names])
        if not selNames: return
        selNames = [item[0].lower() for item in selNames if item[1]]
        
    elif rc == Rhino.Input.GetResult.String:
        nameString = go.StringResult()
        if not nameString: return
        nameList= nameString.Split(",")
        selNames= [name.lower() for name in nameList]
        
    elif rc == Rhino.Input.GetResult.Object:
        selIdx = [go.Object(n).Object().HatchGeometry.PatternIndex for n in range (go.ObjectCount)]
        
    if selIdx is None:
        selIdx = []
        for n in range(h.Count):
            if h[n].Name.lower() in selNames:
                selIdx.append(h[n].Index)
            
    indices = [rs.coercerhinoobject(id).HatchGeometry.PatternIndex for id in ids]
     
    rs.EnableRedraw(False)
    for n in range(len(indices)):
        if indices[n] in selIdx:
            rs.SelectObject(ids[n])
    rs.EnableRedraw(True)


if __name__ == '__main__':SelHatchPattern()