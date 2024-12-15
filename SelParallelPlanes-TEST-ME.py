import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

def SelParallelPlanes():
    def filter_planar( rhino_object, geometry, component_index):
        
        if geometry.Faces[0].UnderlyingSurface().TryGetPlane()[0]:
            return True
        return False
        
    id = rs.GetObject('Select a planar surface', filter =8, preselect=True, custom_filter=filter_planar)
    if not id: return
    
    geo = rs.coercegeometry(id)
    rc, plane = geo.Faces[0].UnderlyingSurface().TryGetPlane()
    vecDir = plane.ZAxis
    
    ids = rs.ObjectsByType(8,state=1)
    if not ids or len(ids) == 1:
        print('No more planar surfaces found')
        return
        
    rs.EnableRedraw(False)
    count = 0
    for id in ids:
        geo = rs.coercegeometry(id)
        rc, plane = geo.Faces[0].UnderlyingSurface().TryGetPlane()
        
        if rc:
            if plane.ZAxis.IsParallelTo(vecDir) != 0:
                rs.SelectObject(id)
                count += 1
    print(str(count-1) + ' parallel planes selected.')
    rs.EnableRedraw(True)

if __name__ == '__main__':SelParallelPlanes()