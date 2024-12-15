import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import os

# get folder
xref_export_stash = rs.GetDocumentData("Xrefs", "Folder")
if xref_export_stash is None:
    xref_export_stash = rs.BrowseForFolder(message="choose location to stash xrefs - once chosen won't prompt for it again")
    rs.SetDocumentData("Xrefs", "Folder", xref_export_stash)

# get doc name but check if it's an "Untitled" aka not yet saved document
rhino_doc_name = rs.DocumentName()
if rhino_doc_name:
    rhino_doc_name = os.path.splitext(rhino_doc_name)[0]

# get prefix
xref_prefix_set_str = rs.GetDocumentData("Xrefs", "Prefix")

if xref_prefix_set_str:
    xref_prefix_set = set(xref_prefix_set_str.split("--||--"))
else:
    xref_prefix_set = set()
    xref_prefix_set.add("0")

selected_xref_prefix = rs.ComboListBox(sorted(xref_prefix_set), message="Choose Xref Prefix")
xref_prefix_set.add(selected_xref_prefix)
rs.SetDocumentData("Xrefs", "Prefix", "--||--".join(xref_prefix_set))

# get Cplane
named_cplanes = sc.doc.NamedConstructionPlanes
selected_cplane = rs.ComboListBox([i.Name for i in named_cplanes], "Named CPlanes")

xref_file_name = xref_export_stash + os.path.sep + rhino_doc_name + " - " + selected_xref_prefix + " - " + selected_cplane

for named_cplane in named_cplanes:
    if named_cplane.Name == selected_cplane:
        sc.doc.ModelBasepoint = named_cplane.Plane.Origin

rs.Command("-Export " + chr(34) + xref_file_name + chr(34))

sc.doc.ModelBasepoint = Rhino.Geometry.Point3d(0,0,0)