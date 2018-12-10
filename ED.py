#The edit distance function takes two parameters
#word_one, and word_two. The function returns a
#2d array. 2d array returned also contains the number
#of operations necessary to change word_one to word_two.
def edit_distance(word_one, word_two):
    #Creates an empty matrix
    matrix = [[0 for i in range(1 + len(word_one))] for j in range(1 + len(word_two))]

    #Number of operations necessary to change word 1 to an empty string
    for i in range(len(matrix[0])):
        matrix[0][i] = i

    #Number of operations necessary to change word 2 to an empty string
    for i in range(len(matrix)):
        matrix[i][0] = i

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            #If current characters of both words don't match
            #set current cell to the closest cell containing
            #smallest value and add 1
            if word_two[i - 1] != word_one[j - 1]:
                minimum = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                matrix[i][j] = minimum + 1
            #Otherwise set current cell to top left diagnol cell
            else:
                matrix[i][j] = matrix[i - 1][j - 1]

    return matrix
