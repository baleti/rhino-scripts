import rhinoscriptsyntax as rs

obj_guid = rs.GetObject("Select Object to Measure its area", preselect=True)
obj = rs.coercerhinoobject(obj_guid)

text_guid = rs.GetObject("Select Text Object to report the area", preselect=True)

format_string = '%<format(floor(Area("' + str(obj.Id) + '","Millimeters")/100000)/10, "0.1f")>% sq m'

rs.TextObjectText(text_guid, format_string)