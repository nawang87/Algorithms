def setZeroes(mat):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    col1flag = 0
    row1flag = 0

    for i in range(len(mat)):
        if mat[i][0] == 0:
            print(i)
            col1flag = 1

        for j in range(1, len(mat[0])):
            if mat[i][j] == 0:
                if i == 0:
                    row1flag = 1
                    continue
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat[0]) - 1, -1, -1):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
            if j == 0 and col1flag == 1:
                mat[i][j] = 0
            if i == 0 and row1flag == 1:
                mat[i][j] = 0

    print(mat)

mat = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
setZeroes(mat)