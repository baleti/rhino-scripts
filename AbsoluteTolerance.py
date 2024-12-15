from rhinoscriptsyntax import UnitAbsoluteTolerance, ComboListBox

def AbsoluteTolerance():
    selected_tolerance = ComboListBox([100,10,1,0.1,0.01,0.001,0.0001], 
                message="Choose Absolute Tolerace",
                title="Absolute Tolerace")
    if selected_tolerance == None:
        return
    UnitAbsoluteTolerance(float(selected_tolerance))

AbsoluteTolerance()