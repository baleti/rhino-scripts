import rhinoscriptsyntax as rs

def SelTagObjects():

    file = rs.DocumentName()

    if not file:return

    tagString = file.split(".")[0]

    ids = rs.NormalObjects()

    if not ids: return
    rs.UnselectAllObjects()
    rs.EnableRedraw(False)

    for id in ids:
        if rs.SetUserText(id, 'FileTag', tagString):
            rs.SelectObject(id)
    rs.EnableRedraw(True)

SelTagObjects()