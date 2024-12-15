import Rhino.PlugIns as rp
import rhinoscriptsyntax as rs

pl_cmd = dict()
query_string = rs.GetString(message="name of the command")

for plkv in rp.PlugIn.GetInstalledPlugIns():
    guid = plkv.Key
    name = plkv.Value
    pl_info = rp.PlugIn.GetPlugInInfo(guid)
    pl_cmd[name] = [cmd for cmd in pl_info.CommandNames]

for pl in pl_cmd:
    for pl_com
    if query_string in pl:
        print pl
        print "\t" + str(pl_cmd[pl])
