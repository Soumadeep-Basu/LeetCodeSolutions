class Solution {
    
    //Fill Elements that are connected to the border with arbitary value
    public char[][] change_border_connect(char[][] board, int i, int j){
        
        if(i < 0 || j < 0 || i > board.length - 1 || j > board[0].length -1){
            return board;
        }
        else if(board[i][j] == 'O'){
            board[i][j] = '1';
            board = change_border_connect(board, i+1, j);
            board = change_border_connect(board, i-1, j);
            board = change_border_connect(board, i, j-1);
            board = change_border_connect(board, i, j+1);
        }
        
        return board; 
        
        
    }
    
    
    //Convert Board to answer
    public char[][] convert(char[][] board){
        
        for (int i = 0; i< board.length; i++){
            for (int j =0; j < board[0].length ; j++){
                if(board[i][j]=='1') board[i][j] = 'O';
                else board[i][j] = 'X';
            
                
            }
        }
        
        return board;
    }
    
    
    
    public void solve(char[][] board) {
        
            for (int i = 0 ; i < board.length; i++){
            
            if(board[i][0] == 'O'){
            
            board = change_border_connect(board, i , 0 );

            }}
        
            for (int i = 0 ; i < board.length; i++){
            
            if(board[i][board[0].length-1] == 'O'){
            
            board = change_border_connect(board, i , board[0].length-1 );

            }}
        
            for (int j = 0 ; j < board[0].length; j++){
            
            if(board[0][j] == 'O'){
            
            board = change_border_connect(board, 0 , j );

            }}
        
        
            for (int j = 0 ; j < board[0].length; j++){
            
            if(board[board.length-1][j] == 'O'){
            
            board = change_border_connect(board, board.length-1 , j );

            }}
        
        
            board = convert(board);
        
        
        
    }
    
    
    
    
}
