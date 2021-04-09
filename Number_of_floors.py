import plotly.express as px
import plotly
import plotly.graph_objs as go

df = pd.read_csv('houses.csv')

df['year'] = df['year'].apply(lambda x: int(x))
df['floors'] = df['floors'].apply(lambda x: int(x))
df = df.loc[df['year'] != 1926].reset_index(drop=True)
df = df.loc[df['year'] != 1928].reset_index(drop=True)

df1 = df['year'].value_counts(sort=True)
d = pd.DataFrame(df.groupby(["year"])['floors'].agg('sum'))
d['year'] = d.index
d['ind'] = range(len(d))
d.index = d['ind']

f = pd.DataFrame(df.groupby(["year"])['floors'].agg('count'))
f['year'] = f.index
f['ind'] = range(len(f))
f.index = f['ind']

sl = {}
for g in range(len(f)):
    h = d['floors'][g] // f['floors'][g]
    sl[d['year'][g]] = h


df_g = pd.DataFrame(sl.items(), columns=['year', 'floors'])[5:]

trace = go.Scatter(
    x=df_g['year'],
    y=df_g['floors'],
    mode='lines',
    line=dict(width=5, shape='spline', smoothing=0.5),
    fillcolor='rgba(0,100,80,0.2)',
    marker=dict(
        color='rgb(226,83,221)',
        size=202,
        line=dict(
            color='MediumPurple',
            width=2,
            colorscale="Cividis",
        )
    ),
)

# Добавляем слой с указанием заголовка, названиями осей
layout = go.Layout(
    title='<b>Среднее количество этажей<br>в домах Рязани (по годам)</b>'.format('П'),
    titlefont=dict(
        size=20,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title='Год постройки дома',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Среднее количество этажей',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )

    )
)

fig = go.Figure(data=[trace], layout=layout)  # Собираем всё в один график
fig.update_xaxes(showgrid=False)  # Убираем отображение линий по оси X
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(153,153,255, 0.7)')  # Оставляем только отображение по оси Y
fig.update_layout(hovermode="x")  # Тип отображения данных при наведении мышки
# Указываем, как именно будут отображаться данные при наведении
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)
fig.update(layout=dict(title=dict(x=0.5)))  # Располагаем заголовок по центру
fig.show()
