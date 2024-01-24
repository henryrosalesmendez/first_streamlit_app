import streamlit
import pandas
streamlit.title('Title example 1')
streamlit.header('header example 2')
streamlit.text('text example 3')
streamlit.text('text example 4')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

