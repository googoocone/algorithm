def solution(rows, columns, queries):
    answer = []
    matrix = []
    matrix_row = []
    matrix_min = []
    c = 0
    
    # 행렬 초기화
    for a in range(rows):
        for b in range(columns):
            matrix_row.append(1 + b + c)
            if b == columns - 1:
                c += columns
                matrix.append(matrix_row)
                matrix_row = []
    
    new_matrix = matrix
    
    for i in range(len(queries)):
        a1 = queries[i][0] - 1
        a2 = queries[i][1] - 1
        b1 = queries[i][2] - 1
        b2 = queries[i][3] - 1

        matrix_top = []
        matrix_right = []
        matrix_bottom = []
        matrix_left = []

        # 옮겨야될 행렬을 뽑아보자
        # 매트릭스의 top 부분부터..
        for row in range(a2, b2):
            matrix_top.append(matrix[a1][row])

        # 매트릭스의 right 부분
        for column in range(a1, b1):
            matrix_right.append(matrix[column][b2])

        # 매트릭스의 bottom 부분
        for row in range(a2, b2):
            matrix_bottom.append(matrix[b1][row + 1])

        # 매트릭스의 left 부분
        for column in range(a1, b1):
            matrix_left.append(matrix[column + 1][a2])

        # 뽑은 행렬을 새 매트릭스에 넣어보자...
        # 매트릭스의 top 부분부터...

        for num in range(b2 - a2):
            new_matrix[a1][a2 + num + 1] = matrix_top[num]

        # 매트릭스의 right 부분을 옮기자
        for num in range(b1 - a1):
            new_matrix[a1 + num + 1][b2] = matrix_right[num]

        # 매트릭스의 bottom 부분을 옮기자
        for num in range(b2 - a2):
            new_matrix[b1][a2 + num] = matrix_bottom[num]

        # 매트릭스의 left 부분을 옮기자
        for num in range(b1 - a1):
            new_matrix[a1 + num][a2] = matrix_left[num]

        # 옮긴 매트릭스를 기존의 매트릭스 위에 덮어씌웁니다.
        matrix = new_matrix

        min_top = min(matrix_top)
        min_right = min(matrix_right)
        min_bottom = min(matrix_bottom)
        min_left = min(matrix_left)

        # 전체 리스트에서 최소값을 구하기
        overall_min = min(min_top, min_right, min_bottom, min_left)
        matrix_min.append(overall_min)

    print(matrix_min)
    return matrix_min
