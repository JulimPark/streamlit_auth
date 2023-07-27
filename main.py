import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title='Test',page_icon=':bar_chart:',layout='wide')


names = ['박핑코','박토순','박흑코']
usernames = ['pinko','tosuni','hukko']


file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('rb') as file:
    hashed_passwords = pickle.load(file)
    

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
                                    'Test1','abcdef',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('로그인','main')

if authentication_status == False:
    st.error('아이디/비밀번호가 일치하지 않습니다.')
    
if authentication_status == None:
    st.warning('아이디와 비밀번호를 입력하세요')
    
if authentication_status:
    st.title('OKOKOK')