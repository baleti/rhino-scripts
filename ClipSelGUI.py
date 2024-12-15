import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def ClipSel():
    selection_settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    selection_settings.ObjectTypeFilter = Rhino.DocObjects.ObjectType.ClipPlane
    clip_planes_iterator = sc.doc.Objects.GetObjectList(selection_settings)
    
    # getobjectlist methods yields an iterator that gets exhausted
    # line below converts it into an immutable list
    clip_planes = list(clip_planes_iterator)
    
    clip_plane_names = [clip_plane.Name for clip_plane in clip_planes
                            if clip_plane.Name is not None]
    
    selected_clip_planes = rs.ComboListBox(sorted(set(clip_plane_names)))
    
    if selected_clip_planes == None:
        return
    
    # may be a problem if there is only one clipping plane with that name?
    
    selected_clip_planes_guids = [clip_plane.Id for clip_plane in clip_planes
                            if clip_plane.Name == selected_clip_planes]
    
    rs.SelectObjects(selected_clip_planes_guids)

ClipSel()