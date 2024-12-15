import rhinoscriptsyntax as rs
import scriptcontext as sc
import System
import Rhino
import os

block_guids = rs.GetObjects(preselect=True)

block_names = list()
for block_guid in block_guids:
    block_names.append(rs.BlockInstanceName(block_guid))

dlg = System.Windows.Forms.OpenFileDialog()
dlg.Title = " and ".join(block_names)
if dlg.ShowDialog()==System.Windows.Forms.DialogResult.OK:
    file_location = dlg.FileName

for block_guid in block_guids:
    block_obj = rs.coercerhinoobject(block_guid)
    block_idx = block_obj.InstanceDefinition.Index
    
    sc.doc.InstanceDefinitions.ModifySourceArchive(block_idx,
                            file_location,
                            Rhino.DocObjects.InstanceDefinitionUpdateType.Linked,
                            1)