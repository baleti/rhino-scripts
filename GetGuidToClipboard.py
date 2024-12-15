import rhinoscriptsyntax as rs

obj_guid = rs.GetObject(preselect=True)
obj = rs.coercerhinoobject(obj_guid)
rs.ClipboardText(obj.Id)