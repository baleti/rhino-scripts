import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

def HatchPlanarSrfs():

    srfs = rs.GetObjects("select planar surfaces to hatch", filter=8, preselect=True)
    if not srfs:
        return
    for srf in srfs:
        srf = rs.coercebrep(srf)
        face = srf.Faces[0]
        if not face.IsPlanar():
            continue
        edges = srf.Edges
        edges = [edge.DuplicateCurve() for edge in edges]
        edges = Rhino.Geometry.Curve.JoinCurves(edges)
        
	hatch_solid_idx = sc.doc.HatchPatterns.Find("Solid", True)
        hatch = Rhino.Geometry.Hatch.Create(edges, hatch_solid_idx, 0, 0)
        sc.doc.Objects.AddHatch(hatch[0])
    sc.doc.Views.Redraw()

if __name__ == "__main__":
    HatchPlanarSrfs()