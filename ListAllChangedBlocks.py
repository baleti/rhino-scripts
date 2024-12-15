import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
block_definitions_list = list(block_definitions)
linked_blocks=[i for i in block_definitions_list 
                if rs.IsBlockEmbedded(i.Name)==False and
                ">" not in i.Name]

changed_blocks = list()
for linked_block in linked_blocks:
    if rs.BlockStatus(linked_block.Name) == 1:
        changed_blocks.append((linked_block.Name, linked_block.SourceArchive))

# might use better string formatting, but will do for now
Rhino.UI.Dialogs.ShowTextDialog("\n".join(sorted([i for sub in changed_blocks for i in sub])),
                                 "Changed Blocks")