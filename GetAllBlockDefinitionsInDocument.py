import rhinoscriptsyntax as rs
import scriptcontext as sc

def GetAllBlockDefinitionsInDocument():
    all_block_definitions = rs.BlockNames()
    rs.ComboListBox(all_block_definitions)

GetAllBlockDefinitionsInDocument()