import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


st.set_page_config(page_title = "Dasboard")
                   #layout='')

xls = pd.ExcelFile('gdval4.xlsx')
sheet_name = xls.sheet_names

st.sidebar.header('Sélectionnez les sous-jacents de la note res')

selected_sjcts = st.sidebar.selectbox("Selectionnez le sous-jacent:", sheet_name)

df = pd.read_excel(xls, sheet_name=selected_sjcts)

st.sidebar.header('Sélectionnez la région')

zone = ['AFOR', 'AFOC', 'AFCENT', 'AFAUS']

selected_region = st.sidebar.selectbox("Selectionnez une Region:", zone)

df = df[df['zone']== selected_region]

#df = df[['pays', 'daoi_eco', 'res_eco']]

#plt.figure(figsize=(10,10))
#plt.axline((0,0), slope=+1, linestyle='--', color='red')
#jitter= 0.5

#df['daoi_def'] += np.random.uniform(-jitter, jitter, size=len(df))
#df['res_def'] += np.random.uniform(-jitter, jitter, size=len(df))

#label = df['pays']

#sns.scatterplot(data=df, x='daoi_def', y='res_def', hue='pays', s=300)

liste_criter = ['économie','défense','affinitaires','liens culture','consulaire','soutien']
liste_criter2 = [['daoi_eco','res_eco'], ['daoi_def','res_def'],['daoi_affin','res_affin'],
                 ['daoi_link','res_link'],['daoi_fae','res_fae'],['daoi_supp','res_supp']]

criter = st.selectbox('Critère de notation:', liste_criter2)

x_axis = criter[0]
y_axis = criter[1]

fig =px.scatter(df, x=x_axis, y=y_axis, color='pays', hover_data='pays', size_max=1000)

fig.add_shape(type='line', 
    x0= 0,
    y0= 0,
    x1= 5,
    y1= 5, line=dict(color='red', width=3, dash='dash'))

fig.update_layout(template='plotly_dark', width=600, height=600)

fig.update_traces(marker=dict(size=12))
 
st.plotly_chart(fig)

