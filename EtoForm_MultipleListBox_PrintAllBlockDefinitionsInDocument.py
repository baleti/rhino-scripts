"""
    Show a dialog window with all document layers
    Allow searching through the list 
    
    print selected layer name(s)
    
    
"""
import System

import Rhino
import Rhino.UI
import rhinoscriptsyntax as rs

import Eto
import Eto.Drawing as drawing
import Eto.Forms as forms

import scriptcontext as sc

import os
import fnmatch

import itertools
flatten = itertools.chain.from_iterable
graft = itertools.combinations

# make modal dialog
class DocLayerSelectionDialog(Eto.Forms.Dialog[bool]):  
    # Initializer
    def __init__(self):
        # Eto initials
        self.Title = "All Layers"
        self.Padding = Eto.Drawing.Padding(5)
        self.Spacing = Eto.Drawing.Size(5, 5)
        
        
        # fields
        self.ScriptList = self.InitializeScriptList()
        self.SearchedScriptList = self.ScriptList[::]
        
        
        # initialize layout
        layout = Eto.Forms.DynamicLayout()
        layout.Padding = Eto.Drawing.Padding(5)
        layout.Spacing = Eto.Drawing.Size(5, 5)
        
        
        # add search
        layout.BeginVertical()
        layout.AddRow(*self.CreateSearchBar())
        layout.EndVertical()
        
        # add listBox
        layout.BeginVertical()
        layout.AddRow(self.CreateScriptListBox())
        layout.EndVertical()
        
        # add buttons
        layout.BeginVertical()
        layout.AddRow(*self.CreateButtons())
        layout.EndVertical()
        
        # set content
        self.Content = layout
        
        
        
    # collect data for list
    def InitializeScriptList(self):
        return allDocLayers
        #return sorted(allDocLayers)
        
        
    # create search bar function
    def CreateSearchBar(self):
        """
        Creates two controls for the search bar
        self.lbl_Search as a simple label
        self.tB_Search as a textBox to input search strings to
        """
        self.lbl_Search = Eto.Forms.Label()
        self.lbl_Search.Text = "Search: "
        self.lbl_Search.VerticalAlignment = Eto.Forms.VerticalAlignment.Center
        
        self.tB_Search = Eto.Forms.TextBox()
        self.tB_Search.TextChanged += self.tB_Search_TextChanged
        
        return [self.lbl_Search, self.tB_Search]
        
        
        
    def CreateScriptListBox(self):
        # Create a multi selection box with grid view - this is similar to Rhino MultipleListBox
        self.lb = forms.GridView()
        self.lb.ShowHeader = False
        self.lb.AllowMultipleSelection = True
        self.lb.Height = 200
        self.lb.AllowColumnReordering = True
        
        self.lb.DataStore = sorted(allDocLayers)
        
        self.lb.SelectedRowsChanged += self.RowsChanged
        
        
        # Create Gridview Column
        column1 = forms.GridColumn()
        column1.Editable = False
        column1.Width = 350
        column1.DataCell = forms.TextBoxCell(0)
        self.lb.Columns.Add(column1)        
        
        self.lb.DataStore = self.SearchedScriptList
        
        return self.lb
        
        
        
    def CreateButtons(self):
        """
        Creates buttons for either print the selection result
        or exiting the dialog
        """
        self.btn_Run = Eto.Forms.Button()
        self.btn_Run.Text = "Run"
        self.btn_Run.Click += self.btn_Run_Clicked
        
        self.btn_Cancel = Eto.Forms.Button()
        self.btn_Cancel.Text = "Cancel"
        self.btn_Cancel.Click += self.btn_Cancel_Clicked
        
        return [self.btn_Run, None, self.btn_Cancel]
        
        
        
    # create a search function    
    def Search(self, text):
        """
        Searches self.ScriptList with a given string
        Supports wildCards
        """
        if text == "":
            self.lb.DataStore = self.ScriptList
        else:
            self.SearchedScriptList = list(graft(fnmatch.filter(flatten(self.ScriptList), "*" + text + "*"), 1))
            self.lb.DataStore = self.SearchedScriptList
            
            
    # Gridview SelectedRows Changed Event
    def RowsChanged (self,sender,e):
        return self.lb.SelectedRows
        
        
        
    # function to run when call at button click
    def RunScript(self):
        # return selected layer names
        return self.lb.SelectedValue
        
        
        
    # event handler handling text input in ther search bar
    def tB_Search_TextChanged(self, sender, e):
        self.Search(self.tB_Search.Text)
        
        
        
    # event handler handling clicking on the 'run' button    
    def btn_Run_Clicked(self, sender, e):
        # close window after double click action. Otherwise, run with error
        self.Close(True)
        self.RunScript()
        
        
    # event handler handling clicking on the 'cancel' button    
    def btn_Cancel_Clicked(self, sender, e):
        self.Close(False)
        
        

def ShowDocLayerSelectionDialog():
    
    dlg = DocLayerSelectionDialog()
    rc = Rhino.UI.EtoExtensions.ShowSemiModal(dlg, Rhino.RhinoDoc.ActiveDoc, Rhino.UI.RhinoEtoApp.MainWindow)
    
    if (rc):
        pickedLayers = []
        pickedLayers.append(dlg.RunScript())
        
        print pickedLayers
        
    else:
        print "Dialog did not run"


if __name__ == "__main__":
    docBlocks = rs.BlockNames()
    
    allDocLayers = []
    i = 0
    while i < len(docBlocks):
        allDocLayers.append(docBlocks[i:i+1])
        i += 1
    ShowDocLayerSelectionDialog()