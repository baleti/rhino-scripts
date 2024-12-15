import Rhino.Geometry
from Rhino.DocObjects import ObjectType
from Rhino.Display import RhinoPageView
import scriptcontext as sc
import rhinoscriptsyntax as rs

def BatchMake2D():
    selected_page_names = rs.MultiListBox([i.PageName for i in sc.doc.Views.GetPageViews()])
    if selected_page_names == None:
        return
    selected_pages = [i for i in sc.doc.Views.GetPageViews() if i.PageName in selected_page_names]
    
    for selected_page in selected_pages:
        detail_views = RhinoPageView.GetDetailViews(selected_page)
        
        cgeo_views = [detail_view for detail_view in detail_views if detail_view.Name and "CGeo" in detail_view.Name]
        if len(cgeo_views) == 0:
            rs.MessageBox("No '-CGeo' viewports found.\nAdd corresponding named viewports.\nBatch Make2D will exit now.")
            return
        
        for detail_view in detail_views:
            if detail_view.Name == None:
                continue
            if "CGeo" in detail_view.Name:
                continue
            
            first_corner = Rhino.Geometry.Point2d(detail_view.Viewport.Bounds.Left, detail_view.Viewport.Bounds.Bottom)
            second_corner = Rhino.Geometry.Point2d(detail_view.Viewport.Bounds.Right, detail_view.Viewport.Bounds.Top)
            
            detail_view.IsActive = True
            
            rhino_objects = sc.doc.Objects.FindByCrossingWindowRegion(detail_view.Viewport, 
                                                                    first_corner, second_corner, 
                                                                    True, ObjectType.AnyObject)
            
            parameters = Rhino.Geometry.HiddenLineDrawingParameters()
            parameters.AbsoluteTolerance = sc.doc.ModelAbsoluteTolerance
            parameters.Flatten = True
            parameters.IncludeHiddenCurves = False
            parameters.IncludeTangentEdges = False
            parameters.IncludeTangentSeams = False
            parameters.SetViewport(detail_view.Viewport)
            for obj in rhino_objects:
                parameters.AddGeometry(obj.Geometry, obj.Id)
            
            for vp in detail_views:
                if vp.Name and detail_view.Name in vp.Name and "CGeo" in vp.Name:
                    cgeo_viewport = vp.Viewport
                    break
                else:
                    cgeo_viewport = None
            
            if cgeo_viewport == None:
                continue
            
            cgeo_viewport_plane = Rhino.Geometry.Plane(cgeo_viewport.CameraTarget, 
                                                cgeo_viewport.CameraX, 
                                                cgeo_viewport.CameraY)
            xform = Rhino.Geometry.Transform.PlaneToPlane(Rhino.Geometry.Plane.WorldXY, cgeo_viewport_plane)
            
            hld = Rhino.Geometry.HiddenLineDrawing.Compute(parameters, True)
            
            for hld_curve in hld.Segments:
                if not hld_curve: 
                    continue
                if not hld_curve.ParentCurve: 
                    continue
                if hld_curve.ParentCurve.SilhouetteType == Rhino.Geometry.SilhouetteType.None: 
                    continue
                if hld_curve.SegmentVisibility == Rhino.Geometry.HiddenLineDrawingSegment.Visibility.Visible:
                    source_obj_attribs = rs.coercerhinoobject(hld_curve.ParentCurve.SourceObject.Tag).Attributes
                    curve = hld_curve.CurveGeometry.DuplicateCurve()
                    curve.Transform(xform)
                    sc.doc.Objects.AddCurve(curve, source_obj_attribs)
            
            sc.doc.Views.Redraw()

BatchMake2D()