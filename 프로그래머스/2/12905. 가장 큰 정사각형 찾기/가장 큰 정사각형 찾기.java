class Solution
{
    public int solution(int [][]board)
    {
        int answer = 0;
       	int n = board.length;
        int m = board[0].length;
        
        for (int i = 0; i < n; i++) {
            answer = Math.max(board[i][0], answer);
        }
        
        for (int j = 0; j < m; j++) {
            answer = Math.max(board[0][j], answer);
        }
		
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (board[i][j] == 0) continue;
                int min = Math.min(Math.min(board[i-1][j], board[i][j-1]), board[i-1][j-1]) + 1;
                board[i][j] = min;
                answer = Math.max(min, answer);
            }
        }
	
        return (int) Math.pow(answer, 2);
    }
}