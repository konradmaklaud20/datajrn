import pandas as pd
import plotly.express as px
import plotly
import plotly.graph_objs as go

df2 = pd.DataFrame(
    {"Процент опрошенных": [27, 67, 6], "Тип дома": ['Многоквартиный дом', 'Частный дом', 'Затрудняюсь ответить']})

fig2 = px.pie(df2, values='Процент опрошенных', names='Тип дома', title='<b>В каком доме Вы хотели бы жить?<b>',
              color_discrete_sequence=px.colors.sequential.Agsunset)
fig2.update_traces(textposition='inside', textinfo='percent+label', textfont_size=17)
fig2.update(layout=dict(title=dict(x=0.5), titlefont=dict(size=20)))
div2 = plotly.io.to_html(fig2, full_html=False, config=dict(displayModeBar=False))
