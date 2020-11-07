def check_rows(row, s):
    r = row
    if row == -1:
        r = s - 1
    if row == s:
        r = 0
    return r

def check_cols(col, s):
    c = col
    if col == -1:
        c = s - 1
    if col == s:
        c = 0
    return c
