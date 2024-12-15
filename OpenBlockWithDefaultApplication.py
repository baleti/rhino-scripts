import rhinoscriptsyntax as rs
import scriptcontext as sc
import os

def OpenBlockWithDefaultApplication():
    block_ids = rs.GetObjects(filter=4096, preselect=True)
    if block_ids:
        for block_id in block_ids:
            block_name = rs.BlockInstanceName(block_id)
            block_path = rs.BlockPath(block_name)
            os.startfile(block_path)

OpenBlockWithDefaultApplication()