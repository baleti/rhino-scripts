import rhinoscriptsyntax as rs
import scriptcontext as sc
def RunCommand( is_interactive ):
    if sc.escape_test(False):
        print "script cancelled" #do something
    print "Resetting..."
    objectIds = rs.GetObjects("Pick some blocks", 4096, preselect=True)
    if not objectIds:
        print "No objects"
        return False
    rs.EnableRedraw(False)
    for id in objectIds:
        blockXForm = rs.BlockInstanceXform(id)
        inverseBlockXForm = blockXForm.TryGetInverse()[1]
        rs.TransformObject(id, inverseBlockXForm)
    rs.SelectObjects(objectIds)
    rs.EnableRedraw(True)
    print "...aaand its done."
    return 0
RunCommand(True)