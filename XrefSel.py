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
                    if i.SourceArchive and
                    rs.BlockContainerCount(i.Name) == 0
                    and ">" not in i.Name]
    
    selected_xref = rs.ComboListBox(sorted(xrefs))
    xref_instances = rs.BlockInstances(selected_xref)
    rs.SelectObjects(xref_instances)

XrefSel()