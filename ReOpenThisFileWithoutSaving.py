import rhinoscriptsyntax as rs
import os
import scriptcontext as sc

this_location = rs.DocumentPath() + os.path.sep + rs.DocumentName()

if sc.doc.Modified:
    rs.Command("-Open No " + chr(34) + this_location + chr(34) + " _Enter _Enter _Enter")
else:
    rs.Command("-Open " + chr(34) + this_location + chr(34) + " _Enter _Enter _Enter")