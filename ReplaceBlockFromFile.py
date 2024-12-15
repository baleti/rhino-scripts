import rhinoscriptsyntax as rs
import scriptcontext as sc

def ReplaceBlockFromFile():
    new_block_file_path = rs.OpenFileName()
    
    sc.doc.ActiveDoc.InstanceDefinitions.ModifySourceArchive(
    
    block_ids = rs.GetObjects(filter=4096, preselect=True)
    
    if block_ids:
        block_paths = list()
        for block_id in block_ids:
            block_name = rs.BlockInstanceName(block_id)
            block_path = rs.BlockPath(block_name)
            block_paths.append(block_path)
        rs.ComboListBox(block_paths)

ReplaceBlockFromFile()