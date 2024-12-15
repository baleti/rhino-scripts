import rhinoscriptsyntax as rs
#import os
import subprocess

def OpenBlockWithRhino8WIP():
    block_ids = rs.GetObjects(filter=4096, preselect=True)
    if block_ids:
        for block_id in block_ids:
            block_name = rs.BlockInstanceName(block_id)
            block_path = rs.BlockPath(block_name)
#            os.system("C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" + " " + block_path)
            subprocess.Popen(["C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe", block_path], close_fds=True)

OpenBlockWithRhino8WIP()