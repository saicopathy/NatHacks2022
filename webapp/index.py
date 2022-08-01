import streamlit as st
import pandas as pd
import numpy as np
##import sentiment_analysis
##from sentiment_analysis import *

app_mode = st.sidebar.selectbox("Navigate to",['Home','About us'])
stress_score = 0
sentences = ""

sounds_of_nature_playlist = ['https://www.youtube.com/watch?v=eKFTSSKCzWA&ab_channel=johnnielawson',
                             'https://www.youtube.com/watch?v=ipf7ifVSeDU&ab_channel=CalmedByNature',
                             'https://www.youtube.com/watch?v=q76bMs-NwRk&ab_channel=TheRelaxedGuy']
classical_music_playlist = ['https://www.youtube.com/watch?v=pxEj6m_7Qfk&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=yH3_tTPv2bo&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=uk-DSogtQRo']
lofi_music_playlist = ['https://www.youtube.com/watch?v=81WBzpwK1Rk&ab_channel=Mr_MoMoMusic',
                       'https://www.youtube.com/watch?v=0xs-oaSZdqE&ab_channel=LittleSoul',
                       'https://www.youtube.com/watch?v=W6YI3ZFOL0A&ab_channel=Ambition']

def parse_youtube_link(col1,col2,col3,linkArray):
    col1.video(linkArray[0])
    col2.video(linkArray[1])
    col3.video(linkArray[2])

def predict_stress_score(sentences):
    stress_count = 0
    ##prediction_array = predict(sentences)
    ##for prediction in prediction_array:
        ##if(prediction == 'stress'):
            ##stress_count += 1
    return stress_count

st.image("/Users/mac/Documents/GitHub/NatHacks2022/webapp/pictures/braincore_icons-02-e1495563799323.png")
st.title("Neuro Journal")
if app_mode == 'Home':
    journal = st.text_area("Journal your feelings",placeholder="natHacks2022 is closing in 12 hours, but I haven't finished my code yet!")
    clicked = st.button("Close journal")
    if (clicked == True):
        sentences = journal.split(".")
        stress_score = 1
        if (stress_score < 3):
            st.markdown("It seems like you are stressed right now. We think these music playlists will help you de-stress.")
            tab1, tab2, tab3 = st.tabs(['Nature','Classical','lofi'])
            col1_1,col2_1,col3_1 = tab1.columns(3)
            parse_youtube_link(col1_1,col2_1,col3_1,sounds_of_nature_playlist)
            col1_2,col2_2,col3_2 = tab2.columns(3)
            parse_youtube_link(col1_2,col2_2,col3_2,classical_music_playlist)
            col1_3,col2_3,col3_3 = tab3.columns(3)
            parse_youtube_link(col1_3,col2_3,col3_3,lofi_music_playlist)
        else:
            st.markdown("It seems like you are distressed right now. We recommend you contacting the nearest therapist in your area.")
