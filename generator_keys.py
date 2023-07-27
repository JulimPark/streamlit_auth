import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ['박핑코','박토순','박흑코']
usernames = ['pinko','tosuni','hukko']
passwords = ['XXX','YYY','ZZZ']

hashed_passwords = stauth.Hasher(passwords).generate()


file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords,file)