import pandas as pd

# обработка файла с сериями типовых домов

df = pd.read_csv('series.csv')
df = df.loc[df['link'] != 'кирпичный'].reset_index(drop=True)
df = df.loc[df['link'] != 'Кирпичный'].reset_index(drop=True)
df = df.loc[df['link'] != 'монолитный'].reset_index(drop=True)
df = df.loc[df['link'] != 'нет данных'].reset_index(drop=True)
df = df.loc[df['link'] != 'Сведения отсутствуют'].reset_index(drop=True)
df = df.loc[df['link'] != 'Без особенностей'].reset_index(drop=True)
df = df.loc[df['link'] != 'блочный'].reset_index(drop=True)
df = df.loc[df['link'] != 'многоквартирный жилой дом'].reset_index(drop=True)
df = df.loc[df['link'] != 'Панельный'].reset_index(drop=True)
df = df.loc[df['link'] != 'панельный'].reset_index(drop=True)
df = df.loc[df['link'] != 'бревенчатый'].reset_index(drop=True)
df = df.loc[df['link'] != 'деревянный'].reset_index(drop=True)
df = df.loc[df['link'] != 'керамзитобетонный'].reset_index(drop=True)
df = df.loc[df['link'] != '-'].reset_index(drop=True)
df = df.loc[df['link'] != 'кирпич'].reset_index(drop=True)
df = df.loc[df['link'] != 'кирпичные'].reset_index(drop=True)
df = df.loc[df['link'] != 'Сведению отсутствуют'].reset_index(drop=True)
df = df.loc[df['link'] != 'вновь выстроенное здание'].reset_index(drop=True)
df = df.loc[df['link'] != 'Не обозначены в тех. паспорте'].reset_index(drop=True)
df = df.loc[df['year'] != 'вновь выстроенное здание'].reset_index(drop=True)

