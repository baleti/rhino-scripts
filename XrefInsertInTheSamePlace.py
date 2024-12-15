# takes into account blocks that have ModelBasePoint other than 0,0,0
# 22.11.22 updated to insert other formats than 3dm
# you forgot to restore the previous CPlane
import Rhino
import rhinoscriptsyntax as rs
import os

xref_file_names = rs.OpenFileNames()
for xref_file_name in xref_file_names:
    xref_file_basename, xref_file_ext = os.path.splitext(xref_file_name)
    if xref_file_ext == ".3dm":
        model_base_point = Rhino.FileIO.File3dm.Read(xref_file_name).Settings.ModelBasepoint
        rs.Command('-Cplane World Top -Insert LinkMode=Link LinkStyle=Reference "{}" Block {} 1 0'.format(xref_file_name, str(model_base_point)))
        rs.Command('SelLast')
    if xref_file_ext == ".dwg":
        rs.Command('-Cplane World Top -Insert LinkMode=Link LinkStyle=Reference "{}" Block _Enter 0,0,0 1 0'.format(xref_file_name))
        rs.Command('SelLast')
    # not tested yet - use with caution
    else:
        rs.Command('-Cplane World Top -Insert LinkMode=Link LinkStyle=Reference "{}" Block 0,0,0 1 0'.format(xref_file_name))
        rs.Command('SelLast')