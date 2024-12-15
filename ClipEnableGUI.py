import rhinoscriptsyntax as rs
import scriptcontext as sc

def ClipEnable():
    selection_settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    selection_settings.ObjectTypeFilter = Rhino.DocObjects.ObjectType.ClipPlane
    clip_planes_iterator = sc.doc.Objects.GetObjectList(selection_settings)
    
    # getobjectlist methods yields an iterator that gets exhausted
    # line below converts it into an immutable list
    clip_planes = list(clip_planes_iterator)
    
    clip_plane_names = [clip_plane.Name for clip_plane in clip_planes
                            if clip_plane.Name is not None]
    
    selected_clip_planes = rs.MultiListBox(sorted(set(clip_plane_names)))
    
    if selected_clip_planes == None:
        return
    
    # new gui pop up that selects detail views by name
    # which means you'll have to name them
    # and addclipview
    
    selected_clip_planes_guids = [clip_plane.Id for clip_plane in clip_planes
                            if clip_plane.Name in selected_clip_planes]
    
    rs.SelectObjects(selected_clip_planes_guids)

ClipEnable()