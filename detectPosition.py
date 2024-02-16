cols = ("A" , "B", "C", "D", "E", "F", "G", "H")
rows = ("8" , "7", "6", "5", "4", "3", "2", "1")

while True:

    print("Enter square position: ", end="")

    square_col, square_row = input().split("-")
    if (square_col in cols) and (square_row in rows):
        break
    else:
        print("Invalid position")

col_idx = cols.index(square_col)
row_idx = rows.index(square_row)
print("Coordinates : ", (row_idx, col_idx))