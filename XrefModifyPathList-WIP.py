import rhinoscriptsyntax as rs
import scriptcontext as sc

def XrefChangePath():
    block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
    block_definitions_list = list(block_definitions)
    linked_blocks=[i.Name for i in block_definitions_list 
                    if rs.IsBlockEmbedded(i.Name)==False and
                    ">" not in i.Name]
    selected_blocks = rs.MultiListBox(linked_blocks)
    for linked_block in selected_blocks:
        test=rs.OpenFileName("test")
#        sc.doc.InstanceDefinitions.ModifySourceArchive(

XrefChangePath()