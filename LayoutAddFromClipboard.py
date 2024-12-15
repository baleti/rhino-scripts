import rhinoscriptsyntax as rs

message = rs.ClipboardText().split("-_-_-")

page_name = message[0]
page_width = message[1]
page_height = message[2]

rs.AddLayout(page_name, [float(page_width), float(page_height)])