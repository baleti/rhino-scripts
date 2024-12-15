import scriptcontext as sc

for i in sc.doc.InstanceDefinitions:
    if i.SourceArchive and ".dwg" in i.SourceArchive:
        sc.doc.InstanceDefinitions.Purge(i.Index)