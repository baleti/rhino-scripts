import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def GetBlocksOnLayers():
    layer_names = rs.GetLayers()
    blocks_using_layer = set()
    for layer_name in layer_names:
        layer_idx = sc.doc.Layers.FindByFullPath(layer_name, notFoundReturnValue=False)
        block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
        for block_definition in block_definitions:
            block_objects = block_definition.GetObjects()
            for block_object in block_objects:
                if block_object.Attributes.LayerIndex==layer_idx:
                    blocks_using_layer.add(block_definition.Name)
    selected_blocks = rs.MultiListBox(list(blocks_using_layer))
    return selected_blocks

def InsertSelectedBlocks(selected_blocks):
    for selected_block in selected_blocks:
        rs.InsertBlock(selected_block, "0,0,0")

#def InsertSelectedBlocksManually(selected_blocks):
#    for selected_block in selected_blocks:
#        rs.Command("-Insert _Enter " + chr(34) + selected_block + chr(34))

selected_blocks = GetBlocksOnLayers()
InsertSelectedBlocks(selected_blocks)