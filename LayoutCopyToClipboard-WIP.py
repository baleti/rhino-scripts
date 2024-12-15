import rhinoscriptsyntax as rs
import scriptcontext as sc
import pickle

#page_width = sc.doc.Views.ActiveView.PageWidth
#page_height = sc.doc.Views.ActiveView.PageHeight
#page_name = sc.doc.Views.ActiveView.PageName
#
#rs.ClipboardText("-_-_-".join([page_name, str(page_width), str(page_height)]))

page_obj_ids = list()
for obj in sc.doc.Objects:
    if obj.Attributes.ViewportId == sc.doc.Views.ActiveView.ActiveViewportID:
        page_obj_ids.append(obj.Id)

#rs.SelectObjects(page_obj_ids)

