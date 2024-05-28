# =================================================== #
# @Author: Fantasy_Silence                            #
# @Time: 2024-05-28                                   #
# @IDE: Visual Studio Code & PyCharm                  #
# @Python: 3.9.7                                      #
# =================================================== #
# @Description: 一个自动截图工具用于获取历史走势         #
# =================================================== #
import time
import pyautogui
import numpy as np
from src.common.figuresio import FiguresIO


class GetScreenshot:

    """
    截取历史走势，用于分析数据
    """
    
    @staticmethod
    def save(is_save: bool = True) -> None:

        # ------ 睡5秒，便于将待截取的网页打开 ------ #
        time.sleep(5)

        # ------ 定位鼠标的位置 ------ #
        x, y = np.arange(245, 1644, 4), 817

        # ------ 截取的图片的尺寸 ------ #
        width, height = 195, 300

        # ------ 遍历所有鼠标位置进行截图 ------ #
        for i in range(len(x)):
            pyautogui.moveTo(x[i], y)
            time.sleep(1)
            # 如果生成的图在鼠标的左边
            if i <= 303:

                # 截图操作
                sub_x = x[i] + 29
                screenshot = pyautogui.screenshot(
                region=(int(sub_x), 520, int(width), int(height))
                )
                if is_save:
                    screenshot.save(FiguresIO.loadFigure("%d.png" % (i + 1)))

            # 如果生成的图在鼠标的右边
            else:

                # 截图操作
                sub_x = x[i] - 29 - width
                screenshot = pyautogui.screenshot(
                    region=(int(sub_x), 520, int(width), int(height))
                )
                if is_save:
                    screenshot.save(FiguresIO.loadFigure("%d.png" % (i + 1)))
