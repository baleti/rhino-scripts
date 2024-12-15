import rhinoscriptsyntax as rs

blocks = [rs.coercerhinoobject(block) for block in rs.GetObjects(message="Select blocks", preselect=True)]
surfaces = rs.GetObjects(message="Select Surfaces", filter=8)

for block in blocks:
    projected_point = rs.ProjectPointToSurface(block.InsertionPoint, surfaces, (0,0,-1))
    if projected_point:
        pull_vector = projected_point[0] - block.InsertionPoint
        rs.MoveObject(block, pull_vector)