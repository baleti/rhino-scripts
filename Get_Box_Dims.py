from __future__ import print_function
import Rhino.Geometry.Box as Box

x,y,z=[],[],[]

for i in range(len(breps)):
    x1,x2 = Box.X.GetValue(breps[i])
    y1,y2 = Box.Y.GetValue(breps[i])
    z1,z2 = Box.Z.GetValue(breps[i])
    
    x.append(round(abs(x1-x2)*2)/2)
    y.append(round(abs(y1-y2)*2)/2)
    z.append(round(abs(z1-z2)*2)/2)

[print(i,j,k) for i,j,k in zip(x,y,z)]
