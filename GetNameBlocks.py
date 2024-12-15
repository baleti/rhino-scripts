import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def GetNameBlocks():
    block_ids = rs.GetObjects(filter=4096, preselect=True)
    
    if block_ids:
        block_names = list()
        for block_id in block_ids:
            block_name = rs.BlockInstanceName(block_id)
            block_names.append(block_name)
        Rhino.UI.Dialogs.ShowTextDialog("\n".join(sorted(block_names)), "Block Names")
#        rs.ComboListBox(block_names)

GetNameBlocks()