import streamlit as st
import pandas as pd

sample = pd.read_excel("teste.xlsx")
sample2 = pd.read_excel("teste2.xlsx")
st.title("ola testando")
st.subheader("ola")
st.write(sample)

st.subheader("ola2")
st.write(sample2)

