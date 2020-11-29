# Tic-tacc(Opp).py , Lập trình hướng đối tượng
ALL_SPACE = list('123456789') # các phím để chơi tic=tac 3x3
X,O, BLANK ='X','O',' ' # hăng số cho giá trị chuối
def main():
        "" "Chạy trò chơi tic-tac-toe." ""
        print('Chào mừng bạn đến với tic-tac-toe!')
        gameBoard = TTTBoard ()#tạo đối tượng bảng TTT.
        currentPlayer, nextPlayer = X, O  # X đi trước, O tiếp theo.

        while True:
            print(gameBoard.getBoardstr())
            # Hiển thị bảng trên màn hình.
            '''Tiếp tục hỏi người chơi cho đến khi 
            họ nhập từ (1-9)'''
            move = None
            while not gameBoard.isvalidspace(move):
                print(f'what is {currentPlayer}\'s move  (1-9)')
                move = input()
            gameBoard.updateBoard(move,currentPlayer) # di chuyển

            # Kiểm tra xem trò chơi đã kết thúc chưa
            if gameBoard.isWinner(currentPlayer):
                #  đầu tiên dành chiến thắng
                print(gameBoard.getBoardstr())
                print(currentPlayer+'Đã dành chiến thắng')
                break
            elif gameBoard.isBoardFull():
                # TRường hợp hòa nhau
                print(gameBoard.getBoardstr())
                print('game hoa!')
                break
            currentPlayer,nextPlayer = nextPlayer,currentPlayer
            # Đảo lộn vị trí thăng thua
            print('Cảm ơn bạn đã chơi game!')
class TTTBoard ():
    def __init__(self,userPrettyBoard=False,userLogggin=False):
          '''Tạo một bảng tic tac toe mới, trống'''
          self.space = {}
          for i in ALL_SPACE:
              self.space[i] = BLANK #
    def getBoardstr(self):
        "" "Trả về biểu diễn văn bản của bảng." ""
        return f'''
        {self.space['1']}|{self.space['2']}|{self.space['3']}  1 2 3
        -+-+-
        {self.space['4']}|{self.space['5']}|{self.space['6']}  4 5 6
        -+-+-
        {self.space['7']}|{self.space['8']}|{self.space['9']}  7 8 9 '''
    def isvalidspace(self,i):
        ''' Trả về True nếu khoảng trắng trên bảng là một số hợp lệ '''
        return i in ALL_SPACE and self.space[i] == BLANK
    def isWinner(self,player):
        ''' Trả về True nếu người chơi này là người chiến thắng
        trên TTTBoard này
        '''
        s,p = self.space,player # Tên ngắn hơn là "đường cú pháp".
        # Kiểm tra 3 dấu trên 3 hàng, 3 cột và 2 đường chéo.
        return ((s['1'] == s['2'] == s['3'] == p) or  # Thắng trên đầu
         (s['4'] == s['5'] == s['6'] == p) or # Thắng dòng hai
         (s['7'] == s['8'] == s['9'] == p) or # Thắng dòng 3
         (s['1'] == s['4'] == s['7'] == p) or # Thăng cột đầu
         (s['2'] == s['5'] == s['8'] == p) or # Thắng cột hai
         (s['3'] == s['6'] == s['9'] == p) or # Thắng cột cuối
         (s['3'] == s['5'] == s['7'] == p) or # Thắng chéo trái
         (s['1'] == s['5'] == s['9'] == p))   # Chéo sang phải
    def isBoardFull(self):
        "" "Trả về True nếu mọi khoảng trắng trên bảng đã được sử dụng." ""
        for i in ALL_SPACE:
            if self.space[i] == BLANK:
                return False # Nếu space là trong thi sai
        return True # khong co khoang trong nao tra ve True
    def updateBoard(self,i,player):
        '''Đặt không gian trên board thành player.'''
        self.space[i] = player
if __name__ == '__main__':
    main()








