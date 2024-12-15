import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs
import os
import subprocess
import System.Drawing

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
    # FIX ME - special formatting variables aka <%%> don't seem to work
    # https://discourse.mcneel.com/t/displaytext-property-of-text-objects-returns-text-field-aka/150514
    pdf.Write(filename)

def print_views():
    print_chunk_pages_str = rs.GetDocumentUserText("Print_Chunk_Pages").split("--||--")
    # cast to integer in case 'if in' below didn't work for strings  
    print_chunk_pages = [int(i) for i in print_chunk_pages_str]
    for view in sc.doc.Views.GetPageViews():
        if int(view.PageNumber) in print_chunk_pages:
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
                        titleblock["drawing_number"] = "{0}".format(object.DisplayText)
                    if object.Name == "Latest Revision":
                        titleblock["latest_revision"] = object.DisplayText
                    if object.Name == "Drawing Title 1":
                        titleblock["drawing_title_1"] = object.DisplayText
                    if object.Name == "Drawing Title 2":
                        titleblock["drawing_title_2"] = object.DisplayText
                    if object.Name == "Drawing Title 3":
                        titleblock["drawing_title_3"] = object.DisplayText
            createSinglePDF(view, titleblock)

# get folder
folder = rs.GetDocumentData("Print", "Folder")
if folder is None:
    folder = rs.BrowseForFolder(message="choose location for PDFs - " + \
                                        "once chosen won't prompt for it again, " + \
                                        "can be changed in Rhino - Options " + \
                                        "- Document User Text")
    rs.SetDocumentData("Print", "Folder", folder)
    
    # prompt to save the file with the above variable in DocumentUserData 
    # so subprocesses can use it
    answer = rs.ComboListBox(["yes", "no"], message="Need to save the file first, proceed?")
    if answer == "yes":
        rs.Command("-Save _Enter")
    else:
        raise Exception('User chose not to save the file - exiting...')

if rs.GetDocumentUserText("Child") is None:
    # number of child processes
    n = 3
    for i in xrange(n):
        print_chunk_pages = [view.PageNumber for view in sc.doc.Views.GetPageViews()[i::n]]
        print_chunk_pages_str = [str(i) for i in print_chunk_pages]
        print_chunk_pages_str_joined = "--||--".join(print_chunk_pages_str)
        subprocess.Popen('start "" /min "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-SetDocumentUserText Child Child -SetDocumentUserText Print_Chunk_Pages ' + print_chunk_pages_str_joined + ' -RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\PrintAllAsSeparatePagesMultiprocess.py) -Exit No" ' + chr(34) + rs.DocumentPath() + "\\" + rs.DocumentName() + chr(34), shell=True)
else:
    titleblock = dict()
    print_views()