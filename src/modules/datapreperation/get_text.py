# ====================================================== #
# @Author: Fantasy_Silence                               #
# @Time: 2024-05-28                                      #
# @IDE: Visual Studio Code & PyCharm                     #
# @Python: 3.9.7                                         #
# ====================================================== #
# @Description:从图片中提取文字生成数据集                  #
# ====================================================== #
import os
import pytesseract
import numpy as np
import pandas as pd
from PIL import Image
from typing import Optional
from src.common.filesio import FilesIO
from src.common.figuresio import FiguresIO


class GetTextFromPng:

    """
    从图片中获取文字并生成数据集
    """

    @staticmethod
    def saveTextIncsv(filename: Optional[str] = None) -> None:

        """
        filename: 保存的文件的名字
        """

        # ------ 获取图片名称 ------ #
        png_list = os.listdir(FiguresIO.loadFigure())

        # ------ 初始化一些矩阵用于存储 ------ #
        time_array = np.zeros(len(png_list), dtype=object)
        data_array = np.zeros((len(png_list), 10), dtype=object)

        # ------ 遍历所有的图片文件获取时间 ------ #
        for i in range(len(png_list)):
            # 从图片中提取文字
            strings_in_image: str = pytesseract.image_to_string(
                Image.open(
                    FiguresIO.loadFigure("%d.png" % (i + 1))
                ), lang='chi_sim'
            )
            # 获取时间
            time_array[i] = strings_in_image.split("\n")[0]
        data_array[:, 0] = time_array
        
        # ------ 遍历所有的图片文件获取其余数据 ------ #
        for i in range(len(png_list)):
            # 加载图片
            img = Image.open(
                FiguresIO.loadFigure("%d.png" % (i + 1))
            )
            # 获取图片大小，进行裁剪，对裁减后的图片的文字进行提取
            width, height = img.size
            cropped_img = img.crop((width * 0.7, 0, width, height))
            strings_in_image: str = pytesseract.image_to_string(
                cropped_img, lang='chi_sim'
            )
            # 将获取的数据存入备用
            num_list = []
            for j in strings_in_image.split("\n"):
                try:
                    num_list.append(float(j[:5]))
                except:
                    pass
            # 存入数据表
            data_array[i, 1:] = num_list
        
        df = pd.DataFrame(
            data_array, columns=[
                "time", "(720, +oo]", "(700, 720]", "(680, 700]", "(660, 680]", 
                "(640, 660]", "(620, 640]", "(600, 620]", "(580, 600]", "(0 580]"
            ]
        )
        df.to_csv(FilesIO.getDataset(filename), index=False)
        print("数据获取成功")
