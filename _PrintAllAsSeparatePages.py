import Rhino
import scriptcontext as sc
import System.Drawing
import rhinoscriptsyntax as rs
import os

folder = os.getcwd()
titleblock = dict()

def createSinglePDF(view, titleblock):
    pdf = Rhino.FileIO.FilePdf.Create()
    dpi = 300
    settings = Rhino.Display.ViewCaptureSettings(view, dpi)
    settings.OutputColor = Rhino.Display.ViewCaptureSettings.ColorMode.DisplayColor
    settings.DefaultPrintWidthMillimeters = 0.18
    pdf.AddPage(settings)
    filename = folder + os.path.sep + titleblock.get("project_number","0000") + "-" + \
                titleblock.get("originator", "00") + "-" + \
                titleblock.get("zone", "00") + "-" + \
                titleblock.get("level", "00") + "-" + \
                titleblock.get("drawing_type", "00") + "-" + \
                titleblock.get("role", "0") + "-" + \
                titleblock.get("drawing_number", "00000") + "_" + \
                titleblock.get("latest_revision", "00") + " " + \
                titleblock.get("drawing_title_1", "000000000") + " " + \
                titleblock.get("drawing_title_2", "") + " " + \
                titleblock.get("drawing_title_3", "") + ".pdf"
    pdf.Write(filename)

for view in sc.doc.Views.GetPageViews():
    for object in sc.doc.Objects.FindByLayer("titleblock index-AR002"):
        if type(object) == Rhino.DocObjects.TextObject and \
            view.ActiveViewportID == object.Attributes.ViewportId:
            if object.Name == "Project Number":
                titleblock["project_number"] = object.DisplayText
            if object.Name == "Originator":
                titleblock["originator"] = object.DisplayText
            if object.Name == "Zone":
                titleblock["zone"] = object.DisplayText
            if object.Name == "Level":
                titleblock["level"] = object.DisplayText
            if object.Name == "Drawing Type":
                titleblock["drawing_type"] = object.DisplayText
            if object.Name == "Role":
                titleblock["role"] = object.DisplayText
            if object.Name == "Drawing Number":
                titleblock["drawing_number"] = object.DisplayText
            if object.Name == "Latest Revision":
                titleblock["latest_revision"] = object.DisplayText
            if object.Name == "Drawing Title 1":
                titleblock["drawing_title_1"] = object.DisplayText
            if object.Name == "Drawing Title 2":
                titleblock["drawing_title_2"] = object.DisplayText
            if object.Name == "Drawing Title 3":
                titleblock["drawing_title_3"] = object.DisplayText
    createSinglePDF(view, titleblock)