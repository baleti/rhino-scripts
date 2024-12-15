import rhinoscriptsyntax as rs
import scriptcontext as sc

def XrefHideBlocks():
    block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
    block_definitions_list = list(block_definitions)
    linked_blocks=[i.Name for i in block_definitions_list 
                    if rs.IsBlockEmbedded(i.Name)==False and
                    ">" not in i.Name]
    selection_names = rs.MultiListBox(sorted(linked_blocks))
    selection_instances = list()
    for selection_name in selection_names:
        selection_instances.append(rs.BlockInstances(selection_name))
    rs.HideObjects(selection_instances)

XrefHideBlocks()