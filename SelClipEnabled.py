# not finished - can't seem to find a way to get ViewIds
# on the clipping planes
# https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_Render_ChangeQueue_ClippingPlane_ViewIds.htm

import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

def SelClipEnabled():
    selection_settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    selection_settings.ObjectTypeFilter = Rhino.DocObjects.ObjectType.ClipPlane
    clip_planes_iterator = sc.doc.Objects.GetObjectList(selection_settings)
    
    # getobjectlist methods yields an iterator that gets exhausted
    # line below converts it into an immutable list
    clip_planes = list(clip_planes_iterator)
    
    clip_planes_enabled = [clip_plane.Name for clip_plane in clip_planes
                            if clip_plane.Name is not None]
    
    selected_clip_planes_guids = [clip_plane.Id for clip_plane in clip_planes
                            if clip_plane.Name in selected_clip_planes]
    
    rs.SelectObjects(selected_clip_planes_guids)

SelClipEnabled()