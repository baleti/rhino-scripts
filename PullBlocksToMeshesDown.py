import rhinoscriptsyntax as rs

blocks = [rs.coercerhinoobject(block) for block in rs.GetObjects(message="Select blocks", preselect=True)]
meshes = rs.GetObjects(message="Select Meshes", filter=32)

for block in blocks:
    projected_point = rs.ProjectPointToMesh(block.InsertionPoint, meshes, (0,0,-1))
    if projected_point:
        pull_vector = projected_point[0] - block.InsertionPoint
        rs.MoveObject(block, pull_vector)