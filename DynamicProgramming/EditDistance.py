def findeditdistance(word1,word2):
    m = len(word1)
    n = len(word2)
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        matrix[i][0] = i
    for j in range(n+1):
        matrix[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                k= min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1]+1)
                matrix[i][j] = k
    # print(matrix[m][n])

    #Find Alignment
    aword1 = ''
    aword2 = ''
    while m!=0 and n !=0:
        if word1[m-1] == word2[n-1]:
            aword1 += word1[m-1]
            aword2 += word2[n-1]
            m-=1
            n-=1

        elif matrix[m][n] ==  matrix[m][n-1]+1:
            aword1 += '-'
            aword2 += word2[n-1]
            n -= 1

        elif matrix[m][n] ==  matrix[m-1][n]+1:
            aword1 += word1[m - 1]
            aword2 += '-'
            m -= 1

        elif matrix[m][n] == matrix[m - 1][n - 1] + 1:
            aword1 += word1[m - 1]
            aword2 += word2[n - 1]
            m -= 1
            n -= 1

    print(aword1[::-1])
    print(aword2[::-1])

    return (matrix[-1][-1]) #Edit Distance

x = 'ACTTWO'
y = 'ACTTOOL'
findeditdistance(x,y)