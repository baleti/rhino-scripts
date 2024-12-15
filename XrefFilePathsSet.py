import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def GetPathSetBlocks():
    block_ids = rs.GetObjects(filter=4096, preselect=True)
    
    if block_ids:
        block_paths = list()
        for block_id in block_ids:
            block_name = rs.BlockInstanceName(block_id)
            block_path = rs.BlockPath(block_name)
            block_paths.append(block_path)
        Rhino.UI.Dialogs.ShowTextDialog("\n".join(sorted(set(list(block_paths)))), "Selected Block Paths")
#        rs.ComboListBox(sorted(set(list(block_paths))))

GetPathSetBlocks()