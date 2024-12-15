import rhinoscriptsyntax as rs
import scriptcontext as sc
import itertools

def XrefSel():
    block_definitions = sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True)
    block_definitions_list = list(block_definitions)
    
    # rs.BlockContainerCount excludes nested blocks, but doesn't work
    # in externally linked blocks - WARNING! ">" character can be used
    # on filenames in Linux
    xrefs = [i.Name for i in block_definitions_list 
                    if rs.IsBlockEmbedded(i.Name)==False
                    and rs.BlockContainerCount(i.Name) == 0
                    and ">" not in i.Name]
    
    selected_xrefs = rs.MultiListBox(sorted(xrefs))
    xref_instances = [rs.BlockInstances(selected_xref) for selected_xref in selected_xrefs]
    # https://stackoverflow.com/a/953097 - unpacking lists in python
    xref_instances_unpacked = list(itertools.chain(*xref_instances))
    rs.SelectObjects(xref_instances_unpacked)

XrefSel()