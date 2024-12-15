import rhinoscriptsyntax as rs
import scriptcontext as sc

page_width = sc.doc.Views.ActiveView.PageWidth
page_height = sc.doc.Views.ActiveView.PageHeight
page_name = sc.doc.Views.ActiveView.PageName

rs.ClipboardText("-_-_-".join([page_name, str(page_width), str(page_height)]))
