""" Game tháp hà Nội , ò nickname:Quyetsk
gmail: quyetzz12d@gmail.com """
import copy
import sys
number_disk = 5
# số đĩa mà bạn muốn chơi với chúng
#  Chúng tôi tạo ra một danh sách để giải quyết
SOLVED_TOWER = list(range(number_disk,0,-1))

def main():
    """ Chạy trò chơi tháp Hà Nội """
    print("""Luật chơi :
    Di chuyển các đĩa tháp , từng đĩa một sang tháp khác.
    Lưu ý đĩa lơn hơn không thể nào nằm trên đĩa nhỏ . Xem thông tin chi tiết về trò chơi tại
    https://vi.wikipedia.org/wiki/Th%C3%A1p_H%C3%A0_N%E1%BB%99i""")

    """Từ điển của tháp có các khóa là 'A','B','C' và các giá trị đó là danh sách
    đại diện cho một tháp . Danh sách bao gồm số nguyên đại diện cho cc đĩa có kích thước khác
    nhau .......vv"""

    Hanoi={'A':copy.copy(SOLVED_TOWER),'B':[],'C':[]}
    while True:
        displayTowers(Hanoi)

        '''Yêu cầu người dùng di chuyển'''
        fromTower,toTower = getplayerMove(Hanoi)

        # Di chuyển đĩa trên cùng của tháp này sang tháp khác
        disk = Hanoi[fromTower].pop()
        Hanoi[toTower].append(disk)

        # kiểm tra xem người dùng đã giải quyết được câu đố hay chưa
        if SOLVED_TOWER == Hanoi['B'] or SOLVED_TOWER == Hanoi['C']:
            displayTowers(Hanoi)
            print("CHÚC MỪNG BẠN ĐÃ THẮNG TRÒ CHƠI CỦA CHÚNG TÔI ")
            sys.exit()
def getplayerMove(Hanoi):
    # Yêu cầu người chơi di chuyển . Quay lại (from tower, to tower)
    while True: # Tiếp tục hỏi người chơi cho đên khi họ chơi một nước đi hợp lệ
        print("Nhập các chữ cái của tháp 'from' và 'to' hoặc 'QUIT',")
        print("(ex: AB để di chuyển từ A >> B)")
        print()
        respone = input("nhap>>").upper().strip()

        if respone == "QUIT":
            print('Cảm ơn bạn đã chơi:')
            sys.exit()
        # Đảm bảo rằng người dùng đã nhập các chữ cái hợp lệ
        if respone not in ("AB","AC","BA","BC","CA","CB"):
            print('Nhập các kỹ tự AB,AC,BA,BC,CA,CB')
            continue
        # tiếp tục hỏi lại người chơi nước đi của họ

        ''' sử dụng nhiều tên biến để mô tả '''
        fromTower, toTower = respone[0], respone[1]
        if len(Hanoi[fromTower])== 0:
        # thap 0 la thap trong
            print('Bạn đã chọn một tháp không có đĩa ')
            continue # HỎi lại về người chơi nước đi của họ
        elif len(Hanoi[toTower])==0:
            return fromTower,toTower
        elif Hanoi[toTower][-1]< Hanoi[fromTower][-1]:
            print('Không thể đặt đĩa lớn lên trên đĩa nhỏ')
            continue
        else:
            '''# Đây là một nước đi hợp lệ,
             vì vậy hãy trả lại các tháp đã chọn:'''
            return fromTower, toTower

def displayTowers(Hanoi):
    """ Hien thi 3 giai phap cua chung"""
    for level in range(number_disk,-1,-1):
        for tower in (Hanoi['A'], Hanoi['B'], Hanoi['C']):
            if level >= len(tower):
                displayDisk(0) # hien thi cot ko co dia
            else:
                displayDisk(tower[level])
        print()
    ''' Hieen thi thap A,B,C'''
    emptyspace =" "*(number_disk)
    print(f"{emptyspace} A{emptyspace}{emptyspace} B{emptyspace}{emptyspace} C\n")
def displayDisk(width):
    """"""
    emptyspace = " " * (number_disk - width)
    ''' Hien thi dia da co chieu rong da cho'''
    if width == 0:
        print(f"{emptyspace}||{emptyspace}", end="")
    else:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptyspace}{disk}{numLabel}{disk}{emptyspace}", end="")
# Một câu lệnh phổ biến trong python
if __name__ == "__main__":
    main()
