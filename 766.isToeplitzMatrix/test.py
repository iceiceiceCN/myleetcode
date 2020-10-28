matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
list(r for r, row in enumerate(matrix))
list(row for r, row in enumerate(matrix))
list(c for c, val in enumerate([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
list(val for c, val in enumerate([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))