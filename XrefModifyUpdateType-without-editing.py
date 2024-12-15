import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import time

block_id = rs.GetObject(filter=4096, preselect=True)
block_definition = rs.coercerhinoobject(block_id).InstanceDefinition

update_type = rs.ComboListBox(["Embedded", "Linked"], "Change Block Update Type to:")
if update_type == "Embedded" and \
block_definition.UpdateType == Rhino.DocObjects.InstanceDefinitionUpdateType.Linked:
    if rs.SetUserText(block_id, key="SourceArchive", 
                    value=block_definition.SourceArchive):
        sc.doc.InstanceDefinitions.ModifySourceArchive(block_definition.Index,
                                         block_definition.SourceArchive,
                                         Rhino.DocObjects.InstanceDefinitionUpdateType.Static,
                                         quiet=1)
        rs.SelectObject(block_id)
        rs.Command("BlockEdit")

# use Static instead of Embedded
# Rhino will default to Static even if Embedded was set in ModifySourceArchive function
# https://github.com/mcneel/rhinocommon/blob/master/dotnet/rhino/rhinosdkinstance.cs#L23
if update_type == "Linked" and \
block_definition.UpdateType == Rhino.DocObjects.InstanceDefinitionUpdateType.Static:
    # you can't store user text on block definition 
    # and I'd rather not use the description field
    # so store it on the first block instance user clicked and
    # iterate through all of them (hoping that wasn't deleted)
    # don't want to store it in document, because the block may be renamed/reinserted
    # https://discourse.mcneel.com/t/can-you-add-user-text-to-block-definition/150530
    for block_instance_id in rs.BlockInstances(block_definition.Name):
        block_instance_source_archive = rs.GetUserText(block_instance_id, key="SourceArchive")
        if block_instance_source_archive:
            model_base_point = Rhino.FileIO.File3dm.Read(block_instance_source_archive).Settings.ModelBasepoint
            sc.doc.ModelBasepoint = model_base_point
            rs.Command("-Cplane World Top")
            rs.Command("-Insert File=No " + chr(34) + block_definition.Name + chr(34) + " Block " + str(model_base_point) + " 1 0")
            rs.Command("SelLast")
            rs.Command("Explode")
            rs.Command("-Export " + chr(34) + block_instance_source_archive + chr(34))
            rs.Command("Delete")
            sc.doc.ModelBasepoint = Rhino.Geometry.Point3d(0,0,0)
            
            sc.doc.InstanceDefinitions.ModifySourceArchive(block_definition.Index,
                                         block_instance_source_archive,
                                         Rhino.DocObjects.InstanceDefinitionUpdateType.Linked,
                                         quiet=1)
            
            rs.SelectObject(block_id)
            
            # use the first one found - problably should 
            # add extra checks in case there are multiple paths
            break