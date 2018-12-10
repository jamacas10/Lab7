from ED import edit_distance

#Used to test the edit distace function
def main():
    list_words = ["apples", "apply", "sams", "", "peel", "pens", "fragment", "frack", "crack", "juice", "juice"]
    for i in range(len(list_words)-1):
        matrix = edit_distance(list_words[i], list_words[i+1])
        print("Two words being used: " + "[" +  list_words[i]+ "] [" + list_words[i+1] + "]")
        print("Number of operations: " + str(matrix[len(matrix)-1][len(matrix[0])-1]))
        print()

main()
