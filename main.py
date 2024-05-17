#Data approximation and neville's method
import streamlit as st
import tool as tl
st.title('Data Approximation and Neville\'s Method')
st.write('This is a simple example of data approximation using Neville\'s Method')
exercise = st.selectbox('Select the exercise', ['Exercise 1', 'Exercise 2'])
data_x = st.text_input('Enter the data x separated by commas')
data_y = st.text_input('Enter the data y separated by commas')
x0 = st.text_input('Enter the x0 value')
data_x = list(map(float, data_x.split(',')))
data_y = list(map(float, data_y.split(',')))
x0 = float(x0)
result = tl.neville_method(data_x, data_y, x0)
st.write(f'The result of the approximation is {result}')

if exercise == 'Exercise 1':
    data_x = [8.1, 8.3, 8.6, 8.7]
    data_y = [16.94410,17.56492,18.50515,18.82091]
    x0 = 8.4