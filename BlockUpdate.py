import rhinoscriptsyntax as rs
import scriptcontext as sc

def BlockUpdate():
    object_ids = rs.GetObjects(preselect=True)
    for id in object_ids:
        block_instance = sc.doc.Objects.Find(id)
        block_definition = block_instance.InstanceDefinition
        sc.doc.InstanceDefinitions.RefreshLinkedBlock(block_definition)

BlockUpdate()