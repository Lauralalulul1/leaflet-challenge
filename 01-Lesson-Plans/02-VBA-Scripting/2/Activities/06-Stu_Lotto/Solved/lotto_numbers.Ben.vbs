Sub main()
    'Create variables
    Dim firstName, lastName As String
    Dim winnersNumber As Long
    Dim numberOfRows As Integer
    Dim First, Second, Third As Long
    Dim powerBalls(3) As Long
    'set constants
    numberOfRows = 1001
    First = 3957481
    Second = 5865187
    Third = 2817729
    powerBalls(1) = 2275339
    powerBalls(2) = 5868182
    powerBalls(3) = 1841402
    'start the loop
    For i = 2 To numberOfRows
        firstName = Cells(i, 1).Value
        lastName = Cells(i, 2).Value
        currentNumber = Cells(i, 3).Value
        If currentNumber = First Then
            Range("F2").Value = firstName
            Range("G2").Value = lastName
            Range("H2").Value = currentNumber
            ElseIf currentNumber = Second Then
                 Range("F3").Value = firstName
                 Range("G3").Value = lastName
                 Range("H3").Value = currentNumber
           ElseIf currentNumber = Third Then
                 Range("F4").Value = firstName
                 Range("G4").Value = lastName
                 Range("H4").Value = currentNumber
            Else
                For pbNumber = 1 To 3
                    If powerBalls(pbNumber) = currentNumber Then
                        Range("F5").Value = firstName
                        Range("G5").Value = lastName
                        Range("H5").Value = currentNumber
                    End If
                Next pbNumber
        End If
    Next i
End Sub