import rhinoscriptsyntax as rs
import scriptcontext as sc

strLayout = rs.CurrentView()
aDetails = sc.doc.Views.GetPageViews()[2].GetDetailViews()

for i in aDetails:
    rs.CurrentDetail("05047", detail=i.Id)

