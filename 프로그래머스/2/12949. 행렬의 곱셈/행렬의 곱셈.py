def solution(arr1, arr2):
    answer = [[]]
    arr1r = len(arr1)
    arr1c = len(arr1[0])
    arr2c = len(arr2[0])
    answer = [[0]*arr2c for _ in range(arr1r)]
    
    for i in range(arr1r):
        for j in range(arr2c):
            for k in range(arr1c):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer