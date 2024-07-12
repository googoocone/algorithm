def solution(maps):
    # 이동 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    rows = len(maps)
    cols = len(maps[0])
    answer = float('inf')
    
    visited = [[False] * cols for _ in range(rows)]
    
    def go(row, col, num):
        nonlocal answer
        print('실행됩니다', num, '번째', row, col)
        
        if row == rows - 1 and col == cols - 1:
            answer = min(answer, num)
            print(answer)
            return
        
        for i in range(4):
            new_row, new_col = row + dx[i], col + dy[i]
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and maps[new_row][new_col] == 1:
                visited[new_row][new_col] = True
                go(new_row, new_col, num + 1)
                visited[new_row][new_col] = False 
                
    visited[0][0] = True
    go(0, 0, 1)

    return answer if answer != float('inf') else -1

result = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(result)
