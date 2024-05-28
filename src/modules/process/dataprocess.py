# ======================================================= #
# @Author: Fantasy_Silence                                #
# @Time: 2024-05-28                                       #
# @IDE: Visual Studio Code & PyCharm                      #
# @Python: 3.9.7                                          #
# ======================================================= #
# @Description: 数据处理模块，对数据进行特征工程             #
# ======================================================= #
import pandas as pd
from src.common.filesio import FilesIO
from sklearn.base import BaseEstimator, TransformerMixin


class PipeLineForDataProcess(BaseEstimator, TransformerMixin):

    """
    设计实现数据处理的特征工程
    is_save：是否存储处理后的数据
    """

    def __init__(self, is_save: bool = False) -> None:
        
        self.is_save = is_save
    
    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:

        # ------ 转换时间格式 ------ #
        X["time"] = pd.to_datetime(X["time"], errors="coerce")

        # ------ 检查并去除无效的时间数据 ------ #
        X = X.dropna(subset=["time"])

        # ------ 提取时间特征 ------ #
        X['year'] = X['time'].dt.year
        X['month'] = X['time'].dt.month
        X['day'] = X['time'].dt.day
        X['hour'] = X['time'].dt.hour
        X['minute'] = X['time'].dt.minute
        X['day_of_week'] = X['time'].dt.dayofweek
        X['is_weekend'] = X['day_of_week'].apply(
            lambda x: 1 if x >= 5 else 0
        )
        X = X.drop(columns=["time"])

        # ------ 持久化存储 ------ #
        if self.is_save:
            X.to_csv(
                FilesIO.getDataset(
                    "data_processed.csv"
                ), index=False, encoding="utf-8-sig"
            )

        return X
