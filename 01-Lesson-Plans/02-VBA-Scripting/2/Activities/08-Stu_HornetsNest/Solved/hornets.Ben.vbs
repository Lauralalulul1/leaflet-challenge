Sub main()
Dim col As Integer
col = 7
Dim row As Integer
row = 6
Dim bugs As Integer
bugs = Range("L2").Value
Dim hornetsFound As Integer
hornetsFound = 0
For i = 1 To row
    For j = 1 To col
    currentValue = Cells(i, j).Value
    If currentValue = "Hornets" Then
        hornetsFound = hornetsFound + 1
        If (hornetsFound <= bugs) Then
            Cells(i, j).Value = "bugs"
            Else
               MsgBox ("all out of bugs")
        End If
    End If
    Next j
Next i
MsgBox (Str(hornetsFound))
End Sub