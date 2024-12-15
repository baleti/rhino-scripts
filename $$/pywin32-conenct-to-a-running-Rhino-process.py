import win32com.client as win32

a = win32.Dispatch("Rhino.Interface")
b=a.IsInitialized
c=a.BringToTop()
d=a.Visible