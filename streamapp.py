import streamlit as st
import numpy as np
import pandas as pd
st.title('MY first streamlit app')
st.text_input('Enter text')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)

df = pd.DataFrame({
'first column': [' ',1, 2, 3, 4],
'second column': [0, 10, 20, 30, 40]
})
option = st.sidebar.selectbox(
'Which number do you like best?',
df['first column']

)
st.sidebar.button('Click here')
'You selected:', option
