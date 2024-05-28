# =========================================================== #
# @Author: Fantasy_Silence                                    #
# @Time: 2024-05-28                                           #
# @IDE: Visual Studio Code & PyCharm                          #
# @Python: 3.9.7                                              #
# =========================================================== #
# @Description: 这是一个文件IO流类，用于文件读取与保存           #
# =========================================================== #
import os
from typing import Optional


class FilesIO:

    """
    文件IO流，便于文件读取或保存时自动获取文件路径
    """

    @staticmethod
    def getDataset(filename: Optional[str] = None) -> str:

        """
        filename：文件名
        """

        # ------ common路径 ------ #
        common_path = os.path.dirname(os.path.abspath(__file__))

        # ------ src路径 ------ #
        src_path = os.path.dirname(common_path)
        ROOTPATH = os.path.dirname(src_path)

        # ------ 检查是否存在数据文件夹，不存在就创建一个 ------ #
        if not os.path.exists(ROOTPATH + "/resources/data"):
            os.mkdir(ROOTPATH + "/resources/data")
            print("'%s'数据集不存在，请重新保存..." % filename)
        
        # ------ 获取文件路径 ------ #
        if filename == None:
            return ROOTPATH + "/resources/data"
        else:
            return ROOTPATH + "/resources/data/" + filename
