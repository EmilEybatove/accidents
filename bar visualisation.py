import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("6 Аварии/transformation.csv")


def plotAndSaveBar(x, y, name, title):
    plt.title(title)
    sns.barplot(x=x, y=y, order=x)
    plt.savefig(f"images/{name}.png")
    plt.clf()


x = ["Светло", "Фонари"]
y = [df["isLight"].sum(), (1 - df["isLight"]).sum()]
plotAndSaveBar(x, y, "light", "Освещение")

x = ["Ясно", "Пасмурно", "Осадки"]
y = [df["isClear"].sum(), df["isCloudy"].sum(), (df["isClear"] + df["isCloudy"] == 0).sum()]
plotAndSaveBar(x, y, "weather", "Погода")

x = ["Передний", "Задний", "Полный", "Другой"]
y = [df["isFront"].sum(), df["isBack"].sum(), df["isAll"].sum(), (df["isFront"] + df["isBack"] + df["isAll"] == 0).sum()]
plotAndSaveBar(x, y, "privod", "Привод")

x = ["Сухое", "Мокрое"]
y = [df["isDry"].sum(), (1 - df["isDry"]).sum()]
plotAndSaveBar(x, y, "pokritie", "Покрытие")

x = ["Нет", "Есть"]
y = [df["isNotBroken"].sum(), (1 - df["isNotBroken"]).sum()]
plotAndSaveBar(x, y, "neispravnosti", "Неисправности")

x = ["Пострадал", "Не пострадал"]
y = [df["isInjured"].sum(), (1 - df["isInjured"]).sum()]
plotAndSaveBar(x, y, "injured", "результат")
