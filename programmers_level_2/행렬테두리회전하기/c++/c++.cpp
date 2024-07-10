#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// std::vector를 출력하는 함수
void print2DVector(const vector<vector<int>>& matrix) {
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> matrix(rows, vector<int>(columns));
    vector<vector<int>> new_matrix(rows, vector<int>(columns));
    vector<int> min_matrix;
    
    
    // 행렬을 초기화합니다.
    for (int row = 0; row < rows; row++) {
        for (int column = 0; column < columns; column++) {
            matrix[row][column] = row * columns + (column + 1);
        }
    }

    // 2차원 벡터를 출력합니다.
    // print2DVector(queries);
    
    new_matrix = matrix;
    for(int num = 0 ; num < queries.size(); num ++ ) {
        int a1 = queries[num][0]-1;
        int a2 = queries[num][1]-1;
        int b1 = queries[num][2]-1;
        int b2 = queries[num][3]-1;

        vector<int> matrix_top;
        vector<int> matrix_right;
        vector<int> matrix_bottom;
        vector<int> matrix_left;

        // 매트릭스의 top 부분 부터 가져오자
        for(int row = a2 ; row < b2; row ++){
            matrix_top.push_back(matrix[a1][row]);
        }

        // 매트릭스의 right 부분 가져오자
        for(int column = a1; column < b1 ; column ++ ){
            
            matrix_right.push_back(matrix[column][b2]);
        }
        
        // 매트릭스의 bottom 부분 가져오자
        for(int row = a2 +1; row < b2+1; row ++){
            matrix_bottom.push_back(matrix[b1][row]);
        }

        // 매트릭스의 left 부분 가져오자
        for(int column = a1 + 1; column < b1+1; column ++ ){
            matrix_left.push_back(matrix[column][a2]);
        }
        

        // 뽑은 행렬을 새 매트릭스에 넣어봅시다....
        // 매트릭스의 top 부분 부터...

        for(int num = 0; num < b2 - a2; num ++ ){
            new_matrix[a1][a2+1+num] = matrix_top[num];
        }

        // 매트릭스의 right 부분에 넣어봅시다...
        for(int num = 0; num < b1-a1; num ++) {
            new_matrix[a1+num+1][b2] = matrix_right[num];
        }

        // 매트릭스의 bottom 부분에 넣어봅시다.
        for(int num = 0; num < b2-a2; num ++) {
            new_matrix[b1][a2+num] = matrix_bottom[num];
        }

        // 매트릭스의 left 부분
        for(int num = 0; num < b1-a1; num ++ ) {
            new_matrix[a1+num][a2] = matrix_left[num];
        }

        vector<int> mergedArray;
        mergedArray.insert(mergedArray.end(), matrix_top.begin(), matrix_top.end());
        mergedArray.insert(mergedArray.end(), matrix_right.begin(), matrix_right.end());
        mergedArray.insert(mergedArray.end(), matrix_bottom.begin(), matrix_bottom.end());
        mergedArray.insert(mergedArray.end(), matrix_left.begin(), matrix_left.end());
        auto minElementIt = min_element(mergedArray.begin(), mergedArray.end());
        
        min_matrix.push_back(*minElementIt);

        matrix = new_matrix;
    }
    

    cout << min_matrix[0];
    cout << min_matrix[1];
    cout << min_matrix[2];

    return answer;
}

int main() {
    // 테스트를 위해 행렬 크기와 쿼리를 설정합니다.
    int rows = 6;
    int columns = 6;
    vector<vector<int>> queries ={{2, 2, 5, 4},{3,3,6,6},{5,1,6,3}}; // 쿼리는 현재 사용되지 않음

    // solution 함수를 호출합니다.
    solution(rows, columns, queries);

    return 0;
}
