__author__ = "Alasdair Mott"
__version__ = "2018.03.15"
# modified 24.11.22 to replace CheckListBox with MultiListBox

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def hideLayerInLayouts(page):
    details = Rhino.Display.RhinoPageView.GetDetailViews(page)
    
    for i, detail in enumerate(details):
    
        #rs.CurrentDetail(pageName, detail)
        detailId = detail.Id
    
        for layerString in layers:
    
            layer_idx = sc.doc.Layers.FindByFullPath(layerString, True)
            layer = sc.doc.Layers.FindIndex(layer_idx)
            Rhino.DocObjects.Layer.SetPerViewportVisible(layer, detailId, False)

pageName = rs.CurrentView()
pageNames = rs.ViewNames(True, 1)
pages = sc.doc.Views.GetPageViews()

""" User Input """
layers = rs.GetLayers()

if pageNames and layers:
    pageNamesHide  = rs.MultiListBox(pageNames, "Layouts to turn off Layer In", "Hide Layer In Layout")

""" Iterate Pages """
rs.EnableRedraw(False)
if layers:
    if pageNamesHide:
        for page in pages:
            hideLayerInLayouts(page)
rs.EnableRedraw(True)
rs.Redraw()
