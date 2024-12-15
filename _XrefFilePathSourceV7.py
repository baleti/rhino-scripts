import os
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

block_defs = list(sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True))

for idx, block_def in enumerate(block_defs):
    if rs.IsBlockEmbedded(block_def.Name) == False and ".3dm" in block_def.SourceArchive:
        block_folder, block_file_name = os.path.split(block_def.SourceArchive)
        new_block_path = block_folder + "\\RhinoV7\\" + block_file_name
        sc.doc.InstanceDefinitions.ModifySourceArchive(block_def.Index,
                            new_block_path,
                            Rhino.DocObjects.InstanceDefinitionUpdateType.Linked,
                            0)