l= [[0,0,1,1],[1,1,0,0],[1,1,1,0],[0,0,0,0]]
max_row = 0
max_col = 0
row_no = 0
col_no = 0
for i in range(4):
    row = 0
    col = 0
    for j in range(4):
        if l[i][j] == 1:
            row += 1
        if l[j][i] == 1:
            col += 1
    if row > max_row:
        max_row = row
        row_no = i
    if col > max_col:
        max_col = col
        col_no = i
print("Row with most number of 1s is row", row_no, "with", max_row, "1s")
print("Column with most number of 1s is column", col_no, "with", max_col, "1s")