# =================================================== #
# @Author: Fantasy_Silence                            #
# @Time: 2024-05-28                                   #
# @IDE: Visual Studio Code & PyCharm                  #
# @Python: 3.9.7                                      #
# =================================================== #
# @Description: 分离自变量与目标值                      #
# =================================================== #
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TargetVaribleSplit(BaseEstimator, TransformerMixin):

    """
    用于分离自变量与目标值
    varibles：自变量标签
    """

    def __init__(self, varibles: list) -> None:
        
        self.variables = varibles

    def fit(self, X, y=None):
        return self
    
    def transform(self, X: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:

        x = X[self.variables]
        y = X.drop(columns=self.variables)
        return x, y