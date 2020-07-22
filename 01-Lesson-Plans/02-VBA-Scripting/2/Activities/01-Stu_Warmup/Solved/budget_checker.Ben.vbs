Sub budgetChecker()
    'get values for budget, price, and fees
    Dim budget, price, fees, total As Double
    budget = Cells(3, 3)
    price = Range("F3")
    fees = Range("H3")
    'Calculate total after fees & enter the value in the "Total" cell.
   total = price + (price * fees)
   Range("L3").Value = total
    'Part 2: Create a Message Box for the user to designate whether the amount including fees is within or over budget.
    If total < budget Then
        MsgBox ("total w/ fees is less than budget")
    Else
        MsgBox ("total w/ fees is over budget")
           'adjust the price to fit the budget
            Dim adjustedPrice As Double
            adjustedPrice = price + (budget - total)
            Range("N3") = adjustedPrice
    End If
End Sub