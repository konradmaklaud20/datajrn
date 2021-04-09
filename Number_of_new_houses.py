import plotly.express as px
import plotly
import plotly.graph_objs as go

df = pd.read_csv('houses.csv')

y = pd.DataFrame(df.groupby(["year"]).agg('count'))
y['ind'] = y.index

y['ind'] = y['ind'].apply(lambda x: int(x))
y['link'] = y['link'].apply(lambda x: int(x))
y = y.loc[y['ind'] != 1917].reset_index(drop=True)
y = y.loc[y['ind'] != 1918].reset_index(drop=True)
y = y.loc[y['ind'] != 1818].reset_index(drop=True)
y = y.loc[y['ind'] != 2018].reset_index(drop=True)
y = y.loc[y['ind'] != 1830].reset_index(drop=True)
y = y.loc[y['ind'] != 1860].reset_index(drop=True)
y = y.loc[y['ind'] != 1880].reset_index(drop=True)
y = y.loc[y['ind'] != 1876].reset_index(drop=True)
y = y.loc[y['ind'] != 1895].reset_index(drop=True)
y = y.loc[y['ind'] != 1900].reset_index(drop=True)

trace = go.Scatter(
    x=y['ind'],
    y=y['link'],
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
    title='<b>Количество новых домов,<br>построенных за год в Рязани</b>',
    titlefont=dict(
        size=20,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title='Год',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Количество домов',
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
