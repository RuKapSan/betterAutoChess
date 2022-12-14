#Модуль для быстрого тестирования fen на валидность

import asyncio
import time
import chess
import chess.engine
import pgnToFen
import SearchPos
# import undetected_chromedriver.v2 as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import cv2
import numpy as np


async def main(fen) -> None:
    transport, engine = await chess.engine.popen_uci(
        r"engine/lc0.exe")
    board = chess.Board(fen)
    info = await engine.analyse(board, chess.engine.Limit(depth=1))
    print(info)
    move = info["pv"]
    move_ = str(move).split("'")[1]
    print(move_)
    await engine.quit()

def exec(fen):
    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    asyncio.run(main(fen))