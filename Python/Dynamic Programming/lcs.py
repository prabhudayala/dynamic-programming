# Longest common subsequences recursive solution
def lcs(X, Y):
    if not X or not Y:
        return ""
    x, xs, y, ys = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(X, ys), lcs(xs, Y), key=len)
print(lcs('thisisatest', 'testing123testing'))	

# DP solution
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    print(lengths)
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
        print(lengths)
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result
print(lcs('testgf', 'taest'))	