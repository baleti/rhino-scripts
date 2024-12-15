import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

rhino_file = rs.OpenFileName()
rhino_file_layers = Rhino.FileIO.File3dm.Read(rhino_file).Layers
selected_layers = rs.ComboListBox(sorted(list(rhino_file_layers)))
a

for rhino_file_layer in rhino_file_layers:
    print(rhino_file_layer)
#    sc.doc.Layers.Add()