import streamlit as st
import pandas as pd

sample = pd.read_csv("teste.csv")
sample2 = pd.read_csv("teste2.csv")
st.title("ola testando")
st.subheader("ola")
st.write(sample)

st.subheader("ola2")
st.write(sample2)

