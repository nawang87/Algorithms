#Keep Circles
# def rotate1(mat):

#Transpose and switch the columns - clockwise
#Transpose and swutch the rows - anticlockwise
def rotate2(mat):
    #anticlockwise
    mat = transpose(mat)
    return switchrows(mat)

    #clockwise
    mat = switchrows(mat)
    return transpose(mat)


def transpose(mat):
    for i in range(len(mat)):
        for j in range(i+1, len(mat[i])):
            temp = mat[i][j]
            mat[i][j]= mat[j][i]
            mat[j][i]= temp
    return mat

def switchrows(mat):
    for i in range(len(mat)//2):
        temp = mat[i]
        mat[i]= mat[-(i+1)]
        mat[-(i+1)]= temp
    return mat


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(rotate2(matrix))