import rhinoscriptsyntax as rs
import scriptcontext as sc

named_views = rs.NamedViews()
if not named_views:
    raise Exception("No Named Views")
else:
    selected_view = rs.ComboListBox(sorted(named_views), "Named Views")
    rs.RestoreNamedView(selected_view)