import rhinoscriptsyntax as rs
 
def DeleteBlock():
    block_names_all = rs.BlockNames()
    block_name = rs.ComboListBox(sorted(block_names_all))
    rs.DeleteBlock(block_name)

DeleteBlock()