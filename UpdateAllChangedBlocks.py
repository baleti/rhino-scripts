import rhinoscriptsyntax as rs
import scriptcontext as sc

def UpdateAllChangedBlocks():
    block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
    block_definitions_list = list(block_definitions)
    linked_blocks=[i for i in block_definitions_list 
                    if rs.IsBlockEmbedded(i.Name)==False and
                    ">" not in i.Name]
    for linked_block in linked_blocks:
        if rs.BlockStatus(linked_block.Name) == 1:
            sc.doc.InstanceDefinitions.RefreshLinkedBlock(linked_block)

UpdateAllChangedBlocks()