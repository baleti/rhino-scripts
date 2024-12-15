import rhinoscriptsyntax as rs
import os

file_name = rs.OpenFileName()
# in case user added extension 
file_name_without_ext, file_name_with_ext = os.path.splitext(file_name)
file_name = file_name_without_ext + ".dwg"

rs.Command('-Export "C:\\Users\\user\\Desktop\\test" Scheme "Default-Copy" _Enter')
