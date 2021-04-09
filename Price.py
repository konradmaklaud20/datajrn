df = pd.read_csv('nedvizh.csv')
df = df.dropna().reset_index(drop=True)

df['year'] = df['year'].apply(lambda x: int(x))
df['m2'] = df['m2'].apply(lambda x: int(x))

df = df.loc[df['year'] != 2104].reset_index(drop=True)
df = df.loc[df['year'] != 1860].reset_index(drop=True)
df = df.loc[df['year'] != 1894].reset_index(drop=True)
df = df.loc[df['year'] != 1917].reset_index(drop=True)
df = df.loc[df['year'] != 1918].reset_index(drop=True)
df = df.loc[df['year'] != 1938].reset_index(drop=True)
df = df.loc[df['year'] != 1951].reset_index(drop=True)
df = df.loc[df['year'] != 1954].reset_index(drop=True)
df = df.loc[df['year'] != 1955].reset_index(drop=True)
df = df.loc[df['year'] != 2000].reset_index(drop=True)
df = df.loc[df['year'] != 2019].reset_index(drop=True)
b = {'year': 2000, 'm2': 290}
df = df.append(b, ignore_index=True)
df1 = df['year'].value_counts(sort=True)
d = pd.DataFrame(df.groupby(["year"])['m2'].agg('sum'))
d['year'] = d.index
d['ind'] = range(len(d))
d.index = d['ind']

f = pd.DataFrame(df.groupby(["year"])['m2'].agg('count'))
f['year'] = f.index
f['ind'] = range(len(f))
f.index = f['ind']

sl = {}
for g in range(len(f)):
    h = d['m2'][g] // f['m2'][g]
    sl[d['year'][g]] = h


df_g = pd.DataFrame(sl.items(), columns=['year', 'm2'])[5:]

large_rockwell_template = dict(layout=go.Layout(titlefont=dict(size=20,), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(title='Год постройки дома', titlefont=dict(size=18, color='#7f7f7f')), yaxis=dict(title='Количество объявлений об аренде квартиры', titlefont=dict(size=18, color='#7f7f7f'))))
# Формируем гистограмму
fig4 = px.bar(df_g, x="year", y='m2', color_discrete_sequence=['rgba(153,153,255, 1)'], title='<b>Средняя цена за кв. метр<br>в зависимости от года постройки дома</b>', template=large_rockwell_template)
fig4.update_xaxes(showgrid=False)  # Убираем отображение линий по оси X
fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(226,83,221, 0.7)')  # Оставляем только отображение по оси Y
fig4.update_layout(hovermode="x", xaxis=dict(title='Год постройки дома'), yaxis=dict(title='Средняя цена за кв. метр'))  # Тип отображения данных при наведении мышки, заголовок и название оси
fig4.update_layout(hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"))
fig4.update(layout=dict(title=dict(x=0.5)))  # Располагаем заголовок по центру
fig.show()
