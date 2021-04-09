import pandas as pd
import plotly.express as px
import plotly
import plotly.graph_objs as go


df = pd.read_csv('nedvizh.csv')
df = df.dropna().reset_index(drop=True)
df = df.loc[df['rooms'] != 'Студия'].reset_index(drop=True)

df['year'] = df['year'].astype(int)
df['price'] = df['price'].astype(int)
df['floors'] = df['floors'].astype(int)
df['rooms'] = df['rooms'].astype(int)
df['m2'] = df['m2'].astype(int)
df = df.loc[df['year'] != 2104].reset_index(drop=True)
df = df.loc[df['year'] != 1860].reset_index(drop=True)
df = df.loc[df['year'] != 1894].reset_index(drop=True)
df = df.loc[df['year'] != 1917].reset_index(drop=True)
df = df.loc[df['year'] != 1918].reset_index(drop=True)
df = df.loc[df['year'] != 1938].reset_index(drop=True)
df = df.loc[df['year'] != 1951].reset_index(drop=True)
df = df.loc[df['year'] != 1954].reset_index(drop=True)
df = df.loc[df['year'] != 1955].reset_index(drop=True)
df = df.loc[df['floors'] != 99].reset_index(drop=True)

df1 = df['year'].value_counts()
df1 = pd.DataFrame(df1)
df1 = df1.rename(columns={'year': 'count_house'})
df1['year'] = df1.index
df1 = df1.sort_values(by=['year'])

large_rockwell_template = dict(
layout = go.Layout(
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
        title='Количество объявлений об аренде квартиры',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )

    )
)
)
# Формируем гистограмму
fig = px.bar(df1, x="year", y='count_house',
                   color_discrete_sequence=['rgb(226,83,221)'],
                   title='<b>Количество объявлений по году постройки дома</b>',
                   template=large_rockwell_template)

fig.update_xaxes(showgrid=False)  # Убираем отображение линий по оси X
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(153,153,255, 0.7)')  # Оставляем только отображение по оси Y
fig.update_layout(hovermode="x", xaxis=dict(title='Год постройки дома'), yaxis=dict(title='Количество объявлений об аренде квартиры'))  # Тип отображения данных при наведении мышки, заголовок и название оси
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)
fig.update(layout=dict(title=dict(x=0.5)))  # Располагаем заголовок по центру
fig.show()
