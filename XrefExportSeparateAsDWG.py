import rhinoscriptsyntax as rs
import scriptcontext as sc
import itertools
import os

folder = rs.BrowseForFolder("Select Folder to export xref instances")

# allow for custom prefix in file name
# if doesn't exist in the list append it and save it in the Document's User Text
file_name_prefix_list_str = rs.GetDocumentUserText("File-Name-Prefix-List")
if file_name_prefix_list_str is None:
    file_name_prefix_list_str = rs.ComboListBox(["None"], message="Add File Name Prefix")
    rs.SetDocumentUserText("File-Name-Prefix-List", file_name_prefix_list_str)
    selected_prefix = ""
else:
    file_name_prefix_list = file_name_prefix_list_str.split(",")
    selected_prefix = rs.ComboListBox(file_name_prefix_list)
    file_name_prefix_list_new = list(set(file_name_prefix_list.append(selected_prefix)))
    file_name_prefix_list_new_str = ",".join(file_name_prefix_list_new)
    rs.SetDocumentUserText("File-Name-Prefix-List", file_name_prefix_list_str)

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
for xref_instance in xref_instances_unpacked:
    rs.Command("SelNone")
    rs.SelectObject(xref_instance)
    block_name = rs.coercerhinoobject(xref_instance).InstanceDefinition.Name
#        document_name = "Untitled"
#        if rs.DocumentName():
#            document_name, document_ext = os.path.splitext(rs.DocumentName())
    rs.Command("-Export " + chr(34) + folder + os.path.sep + selected_prefix + block_name + ".dwg" + chr(34))
    rs.Command("SelNone")