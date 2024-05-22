import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from woralysis import trt
import difflib
from difflib import get_close_matches

st.title("English - Farsi Dictionary")

dic={}

trans=trt()
dic=trans.dictionary
    
word = st.selectbox("Enter your word",['']+ list(dic.keys()))
print(word)
if word: 
    trans=trt(word.lower())

    st.markdown(f"<h4 style='color:#FFFFA0'>{trans}</h4> ",unsafe_allow_html=True)
    #st.write(get_close_matches(word, list(dic.keys()), n=1, cutoff = 0.2))
input=st.text_input("Enter your word") 
st.write(st.write(get_close_matches(input, list(dic.keys()), n=4, cutoff = 0.5)))