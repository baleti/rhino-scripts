# should check first which object is higher - at the moment meshes are always first then srfs then polysrfs

import rhinoscriptsyntax as rs
import Rhino

blocks = [rs.coercerhinoobject(block) for block in rs.GetObjects(message="Select blocks", preselect=True)]
targets = rs.GetObjects(message="Select Meshes, Surfaces or Polysurfaces", filter=56)

mesh_ids = [target for target in targets if rs.IsMesh(target)]
surface_ids = [target for target in targets if rs.IsSurface(target)]
poly_surface_ids = [target for target in targets if rs.IsPolysurface(target)]

def move_object(projected_point):
    pull_vector = projected_point[0] - block.InsertionPoint
    rs.MoveObject(block, pull_vector)

for block in blocks:
    if mesh_ids:
        projected_point = rs.ProjectPointToMesh(block.InsertionPoint, mesh_ids, (0,0,-1))
        if projected_point:
            move_object(projected_point)
    if surface_ids:
        projected_point = rs.ProjectPointToSurface(block.InsertionPoint, surface_ids, (0,0,-1))
        if projected_point:
            move_object(projected_point)
    if poly_surface_ids:
        poly_surfaces = [rs.coercebrep(poly_surface_id) for poly_surface_id in poly_surface_ids]
        
        vector = Rhino.Geometry.Vector3d.ZAxis * -1
        ray = Rhino.Geometry.Ray3d(block.InsertionPoint, vector)
        
        projected_point = Rhino.Geometry.Intersect.Intersection.RayShoot(ray, poly_surfaces, 1)
        if projected_point:
            move_object(projected_point)