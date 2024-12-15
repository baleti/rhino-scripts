import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

a = [view.GetDetailViews() for view in sc.doc.Views.GetPageViews()]
b = [view.PageName for view in sc.doc.Views.GetPageViews()]
c

if rs.GetDocumentUserText("Child") is None:
#    dwg_folder_path = rs.BrowseForFolder("Choose folder to save DWGs into")
    a = [view for view in sc.doc.Views.GetPageViews()]
    
    selected_views = rs.MultiListBox(sorted())
    files = rs.OpenFileNames("Choose files to save as DWG")
    for file in files: 
        subprocess.Popen('start "" /min "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" ' + \
                        '/nosplash /runscript="-SetDocumentUserText Child Child ' + \
                        '-SetDocumentUserText Export_DWG_folder_path ' + \
                        chr(34) + chr(34) + dwg_folder_path + chr(34) + chr(34) + ' ' + \
                        '-RunPythonScript (' + __file__ + ') -Exit No" ' + \
                        chr(34) + file + chr(34), shell=True)
else:
    dwg_folder_path_child = rs.GetDocumentUserText("Export_DWG_folder_path")
    rs.Command("-SaveAs " + chr(34) + dwg_folder_path_child + "\\" + \
                os.path.splitext(rs.DocumentName())[0] + ".dwg" + chr(34))
    rs.Command("-Exit No")


rs.Command("-Make2D Layout=CPlane Properties=MaintainSourceLayers "
        +"CreateHiddenLines=No ShowTangents=No CreateSceneSilhouette=Yes "
        +"CreateClippingPlaneIntersections=Yes ShowViewRectangle=Yes "
        +"GroupOutput=No " 
        +"LayerName test2 "
        +"_Enter",
        echo=True)

#for reference - methods in RhinoCommon:
#https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_HiddenLineDrawingParameters.htm
#make2d_options = Rhino.Geometry.HiddenLineDrawingParameters()
#Rhino.Geometry.HiddenLineDrawing.Compute()