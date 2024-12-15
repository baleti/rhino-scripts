import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


a=sc.doc.Objects.GetObjectList(Rhino.DocObjects.ObjectType.InstanceReference)

a[0].SourceArchive

#temp= []
#for i in a:
#    if i.SourceArchive