# can't get it to work when file isn't saved, below commands return None
import rhinoscriptsyntax as rs

document_location = rs.DocumentPath() + rs.DocumentName()
rs.Command("Open No " + chr(34) + document_location + chr(34))