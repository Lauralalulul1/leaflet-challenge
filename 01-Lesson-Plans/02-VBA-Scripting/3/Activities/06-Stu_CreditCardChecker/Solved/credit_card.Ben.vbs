Sub main()
'Create a VBA script that will process the credit card purchases,
'identifying each of the unique brands listed.
Dim brandColumn  As Integer
brandColumn = 1
Dim brandName As String
Dim brandTotal As Double
Dim summaryRow As Integer
summaryRow = 2
'For the Basic assignment, create a single pop-up message
'for each of the Credit Card brands listed by looping through the list.
For i = 2 To 101
    'if the next brand is different
    If Cells(i + 1, brandColumn).Value <> Cells(i, brandColumn).Value Then
    'store the brand
     brandName = Cells(i, brandColumn).Value
     'store the total, one last time since the next row is a new brand
     brandTotal = brandTotal + Cells(i, 3).Value
     'write the brand and summary row
     Range("G" & summaryRow).Value = brandName
     Range("H" & summaryRow).Value = brandTotal
     'because we are seeing the nextbrand is changed, reset the total
     brandTotal = 0
     'set summary to the next row
     summaryRow = summaryRow + 1
    Else
        'we are in the same brand, so add the value
        brandTotal = brandTotal + Cells(i, 3).Value
    End If
Next i
'For the Advanced assignment, tally the total credit card purchases for each Credit Card brand and add it to the summary table.
End Sub