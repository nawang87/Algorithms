def findeditdistance(word1,word2):
    m = len(word1)
    n = len(word2)
    maxi = 0
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        matrix[i][0] = 0
    for j in range(n+1):
        matrix[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] +1
                if matrix[i][j]>maxi:
                    maxi = matrix[i][j]
                    x = i
                    y = j
            else:
                matrix[i][j] = 0
    print ("Length of the substring", maxi)
    # Find substring
    substring = ''
    while matrix[x][y]!=0:
        substring += word2[y-1]
        x-=1
        y-=1
    return substring[::-1]

word1 = 'tutorialhorizon'
word2 = 'dynamictutorialProgramming'
print(findeditdistance(word1,word2))