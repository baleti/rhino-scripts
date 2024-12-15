import scriptcontext as sc
from Rhino.UI.Dialogs import ShowTextDialog

active_viewport = sc.doc.Views.ActiveView.ActiveViewport

string = str(active_viewport.CameraLocation[0]) + ";" + \
         str(active_viewport.CameraLocation[1]) + ";" + \
         str(active_viewport.CameraLocation[2]) + ";" + \
         str(active_viewport.CameraTarget[0]) + ";" + \
         str(active_viewport.CameraTarget[1]) + ";" + \
         str(active_viewport.CameraTarget[2]) + ";" + \
         str(active_viewport.CameraUp[0]) + ";" + \
         str(active_viewport.CameraUp[1]) + ";" + \
         str(active_viewport.CameraUp[2]) + ";" + \
         "0.0" + ";" + \
         "true" + ";" + \
         str(active_viewport.Camera35mmLensLength) + ";"

ShowTextDialog(string, "Active Viewport Parameters")