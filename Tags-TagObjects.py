import rhinoscriptsyntax as rs

def TagObjects():

    file = rs.DocumentName()

    if not file:return

    tagString = file.split(".")[0]

    ids = rs.AllObjects()

    if not ids: return

    for id in ids:
        rs.SetUserText(id, 'FileTag', tagString)

TagObjects()