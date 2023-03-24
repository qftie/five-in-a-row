import pygame

# 初始化 Pygame
pygame.init()
FONT = pygame.font.Font('./simhei.ttf')
# 设置游戏窗口的尺寸
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# 设置游戏棋盘的尺寸
BOARD_WIDTH = 500
BOARD_HEIGHT = 500

# 设置游戏棋盘上每个格子的尺寸
CELL_SIZE = 30

# 设置游戏棋盘的行数和列数
ROWS = BOARD_HEIGHT // CELL_SIZE
COLUMNS = BOARD_WIDTH // CELL_SIZE

# 设置游戏棋盘和棋子的颜色
BLACK = (50, 50, 50)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 128)

# 设置显示获胜者的字体
# FONT = pygame.font.SysFont('Arial', 50)

# 设置起始玩家
current_player = 1

# 设置游戏棋盘
board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

# 设置游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('五子棋')

# 绘制游戏棋盘
def draw_board():
    # 将游戏棋盘的背景颜色设置为白色
    window.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLUMNS):
            # 将游戏棋盘的分隔线颜色设置为黑色
            pygame.draw.rect(window, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

# 落子提示
def draw_turn():
    # 清空上一次的显示内容
    pygame.draw.rect(window, WHITE, (0, WINDOW_HEIGHT - 70, WINDOW_WIDTH, 70))

    # 渲染文本
    text = FONT.render('轮到玩家 ' + str(current_player) + ' 落子', True, BLACK)

    # 计算文本的位置
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)

    # 绘制文本
    window.blit(text, text_rect)



def draw_pieces():
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == 1:
                # Set the color of the red pieces to black
                pygame.draw.circle(window, BLACK, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            elif board[i][j] == 2:
                # Set the color of the blue pieces to gray
                pygame.draw.circle(window, (128, 128, 128), (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

# 检查是否有玩家获胜
def check_win(player):
    # 检查行
    for i in range(ROWS):
        for j in range(COLUMNS - 4):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player and board[i][j+4] == player:
                return True

    # 检查列
    for i in range(ROWS - 4):
        for j in range(COLUMNS):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player and board[i+4][j] == player:
                return True

    # 检查对角线
    for i in range(ROWS - 4):
        for j in range(COLUMNS - 4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player and board[i+4][j+4] == player:
                return True
            if board[i][j+4] == player and board[i+1][j+3] == player and board[i+2][j+2] == player and board[i+3][j+1] == player and board[i+4][j] == player:
                return True

    return False

# 主游戏循环
def main():
    global current_player
    global board
    global FONT

    # 绘制游戏棋盘
    draw_board()

    # 游戏循环
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标点击的位置
                x, y = pygame.mouse.get_pos()

                # 计算被点击的格子的行和列
                row = y // CELL_SIZE
                column = x // CELL_SIZE

                # 检查格子是否为空
                if board[row][column] == 0:
                    # 在棋盘上放置棋子
                    board[row][column] = current_player

                    # 在棋盘上绘制棋子
                    draw_pieces()
                    
                    # 在游戏棋盘外显示哪个玩家落子
                    draw_turn()

                    # 检查当前玩家是否获胜
                    if check_win(current_player):
                        # 显示获胜者
                        text = FONT.render('玩家 ' + str(current_player) + ' 获胜！', True, WHITE, BLACK)
                        text_rect = text.get_rect()
                        text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                        window.blit(text, text_rect)
                        pygame.display.update()

                        # 等待 3 秒
                        pygame.time.wait(3000)

                        # 重置游戏棋盘
                        board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
                        draw_board()

                        # 切换起始玩家
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                    else:
                        # 切换当前玩家
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1

        # 更新显示
        pygame.display.update()

# 开始游戏
if __name__ == '__main__':
    main()
