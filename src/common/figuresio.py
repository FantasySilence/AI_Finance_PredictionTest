# ================================================================== #
# @Author: Fantasy_Silence                                           #
# @Time: 2024-05-28                                                  #
# @IDE: Visual Studio Code & PyCharm                                 #
# @Python: 3.9.7                                                     #
# ================================================================== #
# @Description: 这是一个图片IO流类，用于图片读取与保存                  #
# ================================================================== #
import os
from typing import Optional


class FiguresIO:

    """
    图片IO流，便于图片读取或保存
    """

    @staticmethod
    def loadFigure(fig_name: Optional[str] = None) -> str:

        """
        fig_name: 图片名称
        """

        # ------ common路径 ------ #
        common_path = os.path.dirname(os.path.abspath(__file__))

        # ------ src路径 ------ #
        src_path = os.path.dirname(common_path)
        ROOTPATH = os.path.dirname(src_path)

        # ------ 检查是否存在数据文件夹，不存在就创建一个 ------ #
        if not os.path.exists(ROOTPATH + "/resources/row_pngs"):
            os.mkdir(ROOTPATH + "/resources/row_pngs")
            print("图片'%s'不存在，请重新保存..." % fig_name)
            return None
        
        # ------ 输出图片路径 ------ #
        if fig_name == None:
            return ROOTPATH + "/resources/row_pngs"
        else:
            return ROOTPATH + "/resources/row_pngs/" + fig_name
