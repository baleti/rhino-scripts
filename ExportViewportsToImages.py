import rhinoscriptsyntax as rs
import Rhino
import os
import scriptcontext as sc
import System.Drawing.Size

def ExportViewportsToImages():
    
    details = Rhino.Display.RhinoPageView.GetDetailViews(sc.doc.Views.ActiveView)
    names = [detail.Attributes.Name for detail in details if detail.Attributes.Name != None]
    
    if len(names) == 0:
        rs.MessageBox("No named Viewports found on this page.\n\n" +
                    "Please give viewports a name that will be used to name output images.\n\n" +
                    "To do this select each viewport on the sheet and in the properties panel fill in the 'Name' field.", title="Error")
        return
    
    folder = rs.BrowseForFolder()
    
    for detail in details:
        if detail.Attributes.Name:
            bbox = rs.BoundingBox(detail.Id)
            width = abs(bbox[0].X - bbox[1].X)
            length = abs(bbox[1].Y - bbox[2].Y)
            size = System.Drawing.Size(width*12, length*12)
            
            viewcap = Rhino.Display.ViewCapture()
            viewcap.TransparentBackground = False
            
            settings = Rhino.Display.ViewCaptureSettings(sc.doc.Views.ActiveView, size, 300)
            settings.SetWindowRect(bbox[0], bbox[2])
            settings.RasterMode = True
            settings.DrawGrid = False
            settings.DrawAxis = False
            settings.DrawWallpaper = False
            settings.OutputColor = Rhino.Display.ViewCaptureSettings.ColorMode.DisplayColor
            
            capture = Rhino.Display.ViewCapture.CaptureToBitmap(settings)
            capture.Save(folder + os.path.sep + detail.Attributes.Name + ".jpg")

ExportViewportsToImages()