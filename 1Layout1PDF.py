import Rhino
import scriptcontext as sc
import System.Drawing
import rhinoscriptsyntax as rs

def createSinglePDF(view):
    folder = rs.BrowseForFolder()
    prefix = "PREFIX"
    folder += "\\" + prefix
    pdf = Rhino.FileIO.FilePdf.Create()
    dpi = 300
#    size = System.Drawing.Size(8.5*dpi,11*dpi)
    settings = Rhino.Display.ViewCaptureSettings(view, dpi)
    pdf.AddPage(settings)
    filename = folder+view.PageName+'.pdf'
    pdf.Write(filename)


for i in sc.doc.Views:
    if type(i) is Rhino.Display.RhinoPageView:
        createSinglePDF(i)
