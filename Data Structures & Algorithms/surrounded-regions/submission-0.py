class Solution:
    def dfs(self,i,j,visited,board):
        m = len(board)
        n =  len(board[0])
        if 0<= i <m and 0<= j < n and visited[i][j]== -1 and board[i][j]=='O':
            visited[i][j]= 1
            self.dfs(i+1,j,visited,board)
            self.dfs(i,j+1,visited,board)
            self.dfs(i-1,j,visited,board)
            self.dfs(i,j-1,visited,board)

    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n =  len(board[0])
        visited = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j==0 or j==n-1:
                    if board[i][j] == 'O':
                        self.dfs(i,j,visited,board)
        for i in range(m):
            for j in range(n):
                if visited[i][j]== -1 and board[i][j]== 'O':
                    board[i][j]= 'X'

        


        