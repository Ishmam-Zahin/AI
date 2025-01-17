class TicTacToe:
    positiveInfinity = 10
    negativeInfinity = -10

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
    
    def getMoves(self):
        moves = []
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        
        return moves
    
    def maxPlayer(self):
        if self.isFinished():
            return self.getValue()
        
        value = TicTacToe.negativeInfinity
        for move in self.getMoves():
            i, j = move
            self.board[i][j] = 1
            tmp = self.minPlayer(initialCall = False)
            if tmp > value:
                value = tmp
                ti = i
                tj = j
            self.board[i][j] = 0

        return value
            
    
    def minPlayer(self, initialCall = True):
        if self.isFinished():
            return self.getValue()
        
        value = TicTacToe.positiveInfinity
        ti = -1
        tj = -1
        for move in self.getMoves():
            i, j = move
            self.board[i][j] = -1
            tmp = self.maxPlayer()
            if tmp < value:
                value = tmp
                ti = i
                tj = j
            self.board[i][j] = 0
        
        if initialCall:
            self.board[ti][tj] = -1

        return value
    
    def getValue(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0 :
            return self.board[0][2]
        for j in range(3):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[0][j] != 0:
                return self.board[0][j]
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                return self.board[i][0]
        
        return 0
    
    def isFinished(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            return True
        for j in range(3):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[0][j] != 0:
                return True
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                return True
        for row in self.board:
            if 0 in row:
                return False
        
        return True
        
    def print(self):
        counter = 1
        for i, row in enumerate(self.board):
            for j, ch in enumerate(row):
                if ch == 0:
                    print(counter, end = " ")
                    counter += 1
                elif ch == 1:
                    print("✖️ ", end = " ")
                elif ch == -1:
                    print("⭕", end = " ")
                else:
                    raise Exception("Unknown value encountered!")
                
                if j < 2:
                    print("|", end = " ")
            print()
            if i < 2:
                print("-"*10, sep = "")
    
    def start(self, player = 1):
        while not self.isFinished():
            self.print()
            if player == 1:
                x = int(input("YOUR TURN: "))
                x -= 1
                moves = self.getMoves()
                i, j = moves[x]
                self.board[i][j] = 1
            else:
                print("THINKING....")
                self.minPlayer()
            
            player = (player + 1) % 2
        
        self.print()
        print("GAME FINISHED.")
        if self.getValue() == 1:
            print("❌ WINS THE GAME 🤑🥇🏆🥇🤑")
        elif self.getValue():
            print("⭕ WINS THE GAME 🤑🥇🏆🥇🤑")
        else:
            print("IT'S A DRAW 😐0️⃣😐")




def main():
    obj = TicTacToe()
    obj.start()




if __name__ == "__main__":
    main()