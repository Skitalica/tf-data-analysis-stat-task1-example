import pandas as pd
import numpy as np


chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Преобразуем данные о сумме чеков в значения дохода
    income = 327 + np.log(x)
    
    # Создаем датафрейм с данными дохода
    df = pd.DataFrame({'income': income})
    
    # Оцениваем параметры распределения LogN и получаем оценку параметра alpha
    mu = df['income'].mean()
    sigma_sq = ((df['income'] - mu)**2).mean()
    alpha = np.exp(mu - sigma_sq/2)
    
    return alpha
