#Бот для игры в шахматы на сайте immortals chess
#Работает в разрешении 1920x1080
#ActionChains с другим разрешением будет нажимать в другие позиции.


import asyncio
import random
import time
import chess
import chess.engine
import pgnToFen
import SearchPos
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import cv2
import numpy as np




#Мнемоническая фраза метамаска
mnemonic_phrase = ''

#Класс для работы с браузером
class Selenium():
    def __init__(self, mnemonic) -> None:
        self.mnemonicc = mnemonic
        pass

    #Запускает браузер и загружает метамаск, как расширение, из определённой папки
    def start_driver(self):
        options = uc.ChromeOptions()

        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun')
        options.add_argument('--password-store=basic')
        options.add_argument('--load-extension=C:\\Immortal\\MM')

        driver = uc.Chrome(
            options=options
        )
        driver.maximize_window()
        self.driver = driver
        return driver


    #нажимает на элемент на странице
    def take_element(self, path, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            time.sleep(delay)
            self.driver.find_element(By.XPATH, path).click()
        except Exception as e:
            print(f"No element after {timeout} seconds of waiting!!!\n{path}")
            return None

    #Передаёт текст в поле для ввода
    def send_text(self, path, text, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            time.sleep(delay)
            self.driver.find_element(By.XPATH, path).send_keys(text)

        except Exception as e:
            print(f"No input after {timeout} seconds of waiting!!!\n{path}")
            return None
        if element is not None:
            time.sleep(delay)
            return element
        else:
            print(f"NO SUCH ELEMENT!\n Path: {path}")
        self.driver.execute_script("""document.body.style.backgroundColor = 'green'""")
        input()

    #Открывает сайт по переданной ссылке
    def open_site(self, url):
        self.driver.get(url)

    #Меняет активное окно на последнее, для моментов, когда закрылось окно с расширением
    def lastWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    #Обновляет активную страницу
    def refresh(self):
        self.driver.refresh()

    #Делает клик мышью в указанную позицию
    def mouse_click(self, x, y):
        ac = ActionChains(self.driver)
        ac.reset_actions()
        ac.move_by_offset(x, y).click().perform()

    #Получает текст указанного элемента на странице
    def getText(self, path):
        text = self.driver.find_element(By.XPATH, path).text
        return text

#Класс для управления расширением метамаск, на входе наследуется от класса управления браузером
class Metamask(Selenium):
    def __init__(self, mnemonic, driver) -> None:
        self.mnemonic = mnemonic
        self.driver = driver
        pass

    #Ждёт открытия окна расширения
    def install_MM(self):
        while True:
            if len(self.driver.window_handles) > 1:
                time.sleep(1)
                self.driver.close()
                self.lastWindow()
                self.refresh()
                self.lastWindow()
                print('MM установлен')
                break
            else:
                time.sleep(1)

    #Ожидает появление кнопки расширения, а затем вставляет мнемоническую фразу и пароль(локальный, следовательно может быть простым)
    def create_wallet(self, mnemonic):
        while True:
            try:
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
                break
            except Exception as e:
                self.refresh()

        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
        self.send_text('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input', mnemonic)
        self.send_text('//*[@id="password"]', '12345678')
        self.send_text('//*[@id="confirm-password"]', '12345678')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/form/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/button')
        print('Кошелек импортирован')

#Класс для работы с сайтом шахмат
class Immortall(Selenium):
    def __init__(self, driver) -> None:
        self.driver = driver
        pass

    #Открывает ссылку ссайта и заходит, используя расширение метамаска.
    def login_to_site(self):
        self.open_site('https://immortal.game/login')
        time.sleep(3)
        self.take_element('/html/body/div[2]/div/div/div[2]/div[1]/div/button')
        while True:
            if len(self.driver.window_handles) > 1:
                self.lastWindow()
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]')
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
                time.sleep(3)
                self.lastWindow()
                self.take_element('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
                try:
                    time.sleep(3)
                    self.lastWindow()
                    self.take_element('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
                except:
                    pass
                time.sleep(1)
                self.lastWindow()
                print('Успешно авторизовались')
                break
            else:
                time.sleep(1)

    #Парсит расположение шахмат на доске и возвращает их
    def driver_locate_pieces(self):
        piece_locations = {
            'black_king': [],
            'black_queen': [],
            'black_rook': [],
            'black_bishop': [],
            'black_knight': [],
            'black_pawn': [],
            'white_knight': [],
            'white_pawn': [],
            'white_king': [],
            'white_queen': [],
            'white_rook': [],
            'white_bishop': []
        }


        for index in range(1, 33):
            try:
                piece = self.driver.find_element(By.XPATH,
                                            f'/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[{index}]')
                # get piece name in format 'white_pawn'
                piece_name = '_'.join(piece.get_attribute('class').split(' ')[2:4][::-1])
                # get piece_coords in format [0,0]
                piece_coords = [int(i) // 100 for i in
                                piece.get_attribute('style')[34:-2].replace('%', '', 2).split(',')]
                piece_locations[piece_name].append(piece_coords)
            except:
                pass

        get_square = [
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
        ];

        # map piece names to FEN chars
        piece_names = {
            'black_king': 'k',
            'black_queen': 'q',
            'black_rook': 'r',
            'black_bishop': 'b',
            'black_knight': 'n',
            'black_pawn': 'p',
            'white_knight': 'N',
            'white_pawn': 'P',
            'white_king': 'K',
            'white_queen': 'Q',
            'white_rook': 'R',
            'white_bishop': 'B'
        }

        return piece_locations, piece_names, get_square

    #Расположение шахмат переводится в универсальное расположение шахмат, для работы с движком нейросети
    def driver_locations_to_fen(self, piece_locations, piece_names, side_to_move):

        #Todo Если есть пустой ряд, то появляется ошибка
        # деление на ноль где-то
        fen = ''
        matrix = []
        key_value_change = {}
        for k, v in piece_locations.items():
            for coord in v:
                key_value_change[tuple(coord)] = k

        #создаёт матрицу из расположения шахмат
        for row in range(8):
            a = []
            for col in range(8):
                try:
                    a.append(piece_names[key_value_change[(row, col)]])
                except:
                    a.append(0)
            matrix.append(a)

        trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        #Конвертирует матрицу из положений шахмат в fen
        for row in trans_matrix:
            empty = 0
            for col in row:
                if isinstance(col, str):
                    if empty: fen += str(empty)
                    fen += col
                    empty = 0
                elif isinstance(col, int):
                    empty += 1
            if empty: fen += str(empty)
            if trans_matrix.index(row) < 7: fen += '/'

        if fen[0] == '/':
            fen = fen[1:]
        if fen[-1] == '/':
            fen = fen[:-1]
        fen += ' ' + side_to_move

        # add placeholders (NO EN PASSANT AND CASTLING are static placeholders)
        fen += ' KQkq - 0 1'
        time.sleep(1.5)
        return fen

    #Запускает поиск противника
    def start_game(self):
        self.open_site('https://immortal.game/play')
        self.take_element('/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div/div[1]/div/label')

        time.sleep(2)
        self.take_element('/html/body/div[2]/div/div[4]/div[2]/button')

    #Делает ход по заданным координатам для белых
    def make_move_w(self, x1, y1, x2, y2):
        self.mouse_click(276 + x1, 913 - y1)
        time.sleep(0.5)
        self.mouse_click(276 + x2, 913 - y2)

    # Делает ход по заданным координатам для чёрных
    def make_move_b(self, x1, y1, x2, y2):
        self.mouse_click(1132 - x1, 57 + y1)
        self.mouse_click(1132 - x2, 57 + y2)

    # Ожидает первый ход чёрных и получает ход чёрных
    def get_first_move_b(self):
        myMove = None
        while True:
            try:
                if len(self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]')) > 0:
                    enemy_move = 'gg'
                    break
                else:
                    enemy_move = self.getText('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/button[2]')
                    break
            except:
                pass
        return enemy_move

    #Ожидает и получает ход чёрных
    def get_move_b(self, id_):
        myMove = None
        while True:
            try:
                if len(self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]')) > 0:
                    enemy_move = 'gg'
                    break
                else:
                    enemy_move = self.getText(f'/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[{id_}]/div/button[2]')
                    break
            except:
                pass
        return enemy_move

    # Ожидает первый ход белых и получает ход белых
    def get_first_move_w(self):
        myMove = None
        while True:
            try:
                if len(self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]')) > 0:
                    myMove = 'gg'
                    break
                else:
                    myMove = self.getText('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/button[1]')
                    break
            except:
                pass
        return myMove

    # Ожидает и получает ход белых
    def get_move_w(self, id_):
        myMove = None
        while True:
            try:
                if len(self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]')) > 0:
                    myMove = 'gg'
                    break
                else:
                    myMove = self.getText(f'/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[{id_}]/div/button[1]')
                    break
            except:
                pass
        return myMove

    #Получает свой цвет шахмат за счёт положения белого короля на доске
    def driver_color_identifier(self):
        start_time = time.time()
        while True:
            try:
                element = WebDriverWait(self.driver, 90).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[17]'))
                )
                piece = self.driver.find_element(By.XPATH,
                                                 f'/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[17]')
                # get piece name in format 'white_pawn'
                piece_name = '_'.join(piece.get_attribute('class').split(' ')[2:4][::-1])
                # get piece_coords in format [0,0]
                piece_coords = [int(i) // 100 for i in
                                piece.get_attribute('style')[34:-2].replace('%', '', 2).split(',')]
                if piece_coords == [4, 7]:
                    print('white')
                    return 'w'
                else:
                    print('black')
                    return 'b'

                if (time.time() - start_time) > 90:
                    return None
            except:
                return None

    # Получает свой цвет шахмат за использования OpenCV
    def color(self):
        while True:
            self.driver.get_screenshot_as_file('Immortal.png')
            x = 276
            y = 698
            w = x + 108
            h = y + 108
            fullImg = Image.open("Immortal.png")
            cropImg = fullImg.crop((x, y, w, h))
            cropImg.save('cropImage.png')

            img = cv2.imread('cropImage.png')

            white_min = np.array((0, 0, 255), np.uint8)
            white_max = np.array((255, 255, 255), np.uint8)
            black_min = np.array((0, 0, 0), np.uint8)
            black_max = np.array((0, 0, 0), np.uint8)

            white_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            white_thresh = cv2.inRange(white_hsv, white_min, white_max)
            white_moments = cv2.moments(white_thresh, 1)
            white_dArea = white_moments['m00']
            black_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            black_thresh = cv2.inRange(black_hsv, black_min, black_max)
            black_moments = cv2.moments(black_thresh, 1)
            black_dArea = black_moments['m00']

            if white_dArea == 1879:
                print('white')
                return 'w'
            elif black_dArea == 2675:
                print('black')
                return 'b'

#Ассинхронная функция требуется для работы нейросети
async def main() -> None:
    mnemonic = mnemonic_phrase


    pgnConverter = pgnToFen.PgnToFen()
    player = None
    start_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    searchPos = SearchPos.SearchPos()
    fen = None
    gg = 0

    print('Запуск браузера...')

    driver = ''
    driver_session = Selenium(mnemonic)
    driver = driver_session.start_driver()
    metamask = Metamask(mnemonic, driver)
    immortall = Immortall(driver)
    print('Браузер запущен')

    log_url = driver.command_executor._url
    log_session_id = driver.session_id
    log_txt = f'{log_url=}\n{log_session_id=}'
    with open('log.txt','w') as file:
        file.write(log_txt)
    metamask.install_MM()
    metamask.create_wallet(mnemonic)

    immortall.login_to_site()
    print('Запуск нейросети...')
    transport, engine = await chess.engine.popen_uci(r"engine/lc0.exe")
    board = chess.Board(start_fen)
    info = await engine.analyse(board, chess.engine.Limit(depth=2))
    print('Нейросеть запущена')
    while True:
        time.sleep(5)
        while True:
            immortall.start_game()
            player = immortall.driver_color_identifier()
            if player is not None:
                break
        gg = 0
        id_ = 2


        if player == 'w':
            board = chess.Board(start_fen)
            print("Start")
            info = await engine.analyse(board, chess.engine.Limit(depth=2))
            print('Board analised')
            move = info["pv"]
            move_ = str(move).split("'")[1]
            print(move_)
            x1 = searchPos.GetX1(move_)
            y1 = searchPos.GetY1(move_)
            x2 = searchPos.GetX2(move_)
            y2 = searchPos.GetY2(move_)
            immortall.make_move_w(x1, y1, x2, y2)
            time.sleep(0.5)
            my_move = immortall.get_first_move_w()
            pgnConverter.move(my_move)
            en_move = immortall.get_first_move_b()
            pgnConverter.move(en_move)
            if en_move == 'gg':
                gg = 1
            else:
                fen_ = str(pgnConverter.getFullFen())
                fen = f"{fen_.split(' ')[0]} {fen_.split(' ')[1]}"

            while True:

                if gg == 1:
                    pgnConverter.resetBoard()
                    break

                piece_locations, piece_names, get_square = immortall.driver_locate_pieces()
                fen = immortall.driver_locations_to_fen(piece_locations, piece_names, 'w')

                if fen[0] == '/':
                    fen = fen[1:]
                try:
                    play_again = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]').click
                    if play_again:
                        pgnConverter.resetBoard()
                        break
                except:
                    pass
                board = chess.Board(fen)

                info = await engine.analyse(board, chess.engine.Limit(depth=2))
                move = info["pv"]
                move_ = str(move).split("'")[1]
                print(move_)
                x1 = searchPos.GetX1(move_)
                y1 = searchPos.GetY1(move_)
                x2 = searchPos.GetX2(move_)
                y2 = searchPos.GetY2(move_)
                immortall.make_move_w(x1, y1, x2, y2)
                time.sleep(0.5)
                if len(list(move_)) == 4:
                    my_move = immortall.get_move_w(id_)
                else:
                    my_move = move_

                try:
                    play_again = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[3]/button[2]').click
                    if play_again:
                        pgnConverter.resetBoard()
                        break
                except:
                    pass
                # if my_move == 'gg':
                #     pgnConverter.resetBoard()
                #     break
                pgnConverter.move(my_move)
                en_move = immortall.get_move_b(id_)
                try:
                    time.sleep(0.5)
                    driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[1]').click()
                except ValueError:
                    print('Ошибка значения ValueError успешно послана НАХУЙ!')
                except:
                    pass
                # if en_move == 'gg':
                #     pgnConverter.resetBoard()
                #     break
                pgnConverter.move(en_move)
                print(en_move)
                fen_ = str(pgnConverter.getFullFen())
                print(fen)
                # fen = f"{fen_.split(' ')[0]} {fen_.split(' ')[1]}"
                id_ += 1


        elif player == 'b':
            print("Start")
            en_move = immortall.get_first_move_w()
            pgnConverter.move(en_move)
            if en_move == 'gg':
                gg = 1
            else:
                fen_ = str(pgnConverter.getFullFen())
                fen = f"{fen_.split(' ')[0]} {fen_.split(' ')[1]}"

                board = chess.Board(fen)
                info = await engine.analyse(board, chess.engine.Limit(depth=2))
                print('Analysed')
                move = info["pv"]
                move_ = str(move).split("'")[1]
                print(move_)
                x1 = searchPos.GetX1(move_)
                y1 = searchPos.GetY1(move_)
                x2 = searchPos.GetX2(move_)
                y2 = searchPos.GetY2(move_)
                immortall.make_move_b(x1, y1, x2, y2)
                time.sleep(0.5)
                my_move = immortall.get_first_move_b()
                pgnConverter.move(my_move)


            while True:

                en_move = immortall.get_move_w(id_)
                if en_move == 'gg':
                    pgnConverter.resetBoard()
                    break
                pgnConverter.move(en_move)
                print(en_move)
                fen_ = str(pgnConverter.getFullFen())
                print(fen_)

                piece_locations, piece_names, get_square = immortall.driver_locate_pieces()
                fen = immortall.driver_locations_to_fen(piece_locations, piece_names, 'b')

                new_fen = fen[::-1][13:] + fen[-13:]
                if new_fen[0] == '/':
                    new_fen = new_fen[1:]
                try:
                    play_again = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]').click
                    if play_again:
                        pgnConverter.resetBoard()
                        break
                except:
                    pass
                board = chess.Board(new_fen)
                info = await engine.analyse(board, chess.engine.Limit(depth=2))
                move = info["pv"]
                move_ = str(move).split("'")[1]
                print(move_)
                x1 = searchPos.GetX1(move_)
                y1 = searchPos.GetY1(move_)
                x2 = searchPos.GetX2(move_)
                y2 = searchPos.GetY2(move_)
                immortall.make_move_b(x1, y1, x2, y2)
                time.sleep(0.5)
                if len(list(move_)) == 4:
                    my_move = immortall.get_move_b(id_)
                else:
                    my_move = move_
                try:
                    play_again = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]/button[2]').click
                    if play_again:
                        pgnConverter.resetBoard()
                        break
                except:
                    pass
                # if my_move == 'gg':
                #     pgnConverter.resetBoard()
                #     break
                pgnConverter.move(my_move)
                try:
                    time.sleep(0.5)
                    driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[1]').click()
                except:
                    pass
                id_ += 1

    await engine.quit()

if __name__ == '__main__':
    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    asyncio.run(main())


