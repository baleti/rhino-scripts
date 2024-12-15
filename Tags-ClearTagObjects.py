import rhinoscriptsyntax as rs

def ClearTagObjects():

    ids = rs.AllObjects()

    if not ids: return

    for id in ids:
        rs.SetUserText(id, 'FileTag', "")

ClearTagObjects()