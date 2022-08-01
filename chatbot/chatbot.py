# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import streamlit as st
import webbrowser
# from nltk.tokenize import word_tokenize

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Buddy',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

conversation_starter0 = ['Hi', 'Hello!']
conversation_starter1 = ['Hello', 'Hello!']
info = ['What services are available?',
        'We offer games and music to help you relax']  # NEEDS EDIT

trainer = ListTrainer(bot)

for item in (conversation_starter0, conversation_starter1, info):
    trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')


class personal_info:
    def __init__(phone, prefered_music_type):
        personal_info.therpist_info = phone
        personal_info.music_pref = prefered_music_type


class EEG_info:
    def __init__(EEG_therapist_threshold, EEG_relax_threshold, EEG_value):
        EEG_info.therapist_threshold = EEG_therapist_threshold
        EEG_info.need_relax_threshold = EEG_relax_threshold
        EEG_info.value = EEG_value


games_list = ['https://app.brainsatplay.com/#BreathGarden',
              'https://unboundcreations.itch.io/rain-on-your-parade-prologue',
              'https://dr-d-king.itch.io/tiny-islands',
              'https://bearmaskstudios.itch.io/lofi-room',
              'https://picogram.itch.io/pe-noire']
sounds_of_nature_playlist = ['https://www.youtube.com/watch?v=eKFTSSKCzWA&ab_channel=johnnielawson',
                             'https://www.youtube.com/watch?v=ipf7ifVSeDU&ab_channel=CalmedByNature',
                             'https://www.youtube.com/watch?v=q76bMs-NwRk&ab_channel=TheRelaxedGuy']
classical_music_playlist = ['https://www.youtube.com/watch?v=pxEj6m_7Qfk&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=yH3_tTPv2bo&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=uk-DSogtQRo']
lofi_music_playlist = ['https://www.youtube.com/watch?v=81WBzpwK1Rk&ab_channel=Mr_MoMoMusic',
                       'https://www.youtube.com/watch?v=0xs-oaSZdqE&ab_channel=LittleSoul',
                       'https://www.youtube.com/watch?v=W6YI3ZFOL0A&ab_channel=Ambition']

# games and music suggestions
def activities():
    reponse = input(
        'Bot: Would you like to play games or listen to some music?').lower()
    if any(word in inputTokenized for word in ['games', 'game']):
        map(lambda game: print(webbrowser.open(game)), games_list)
    elif any(word in inputTokenized for word in ['listen', 'music', 'musics']):
        music_style_input = input(
            'Bot: What genre of music would you like to listen to? Sounds of Nature, LoFi, Classical, or Other?').lower()
        if any(word in inputTokenized for word in ['nature', 'sounds', 'sound']):
            map(lambda playlist: print(webbrowser.open(
                playlist)), sounds_of_nature_playlist)
        elif any(word in inputTokenized for word in ['classical', 'classic', 'instrumental']):
            map(lambda playlist: print(webbrowser.open(
                playlist)), classical_music_playlist)
        elif any(word in inputTokenized for word in ['lofi']):
            map(lambda playlist: print(
                webbrowser.open(playlist)), lofi_music_playlist)
        else:
            print('Bot: You can search for some songs on Youtube ' + webbrowser.open('https://www.youtube.com/') +
                  ' or Spodify ' + webbrowser.open('https://open.spotify.com') + ' !')
    else:
        activities()


EEG_wave = input('plz input eeg wave value')

# when EEG wave values are abnormal
if EEG_wave >= EEG_info.therapist_threshold:
    print('Our system detects that you are currently really stressed and would recommend you speak to a therapist.')
    if personal_info.therpist_info == None:
        print('We recommend consulting a specalist using one of these sites:')
        # provide cloest therpists/websites
    else:
        print(personal_info.therpist_info)

elif EEG_wave >= EEG_info.need_relax_threshold:
    inputTokenized = input(
        'Bot: Our system detects that you are feeling a bit stressed right now, would you like to play a game or listen to some music to de-stress?').lower()
    activities()

# Chatbot testing
while True:
    request = input('Bot: Hello! ')
    if request.lower() == 'bye':
        print('Bot: See you next time!')
        break
    else:
        activities()
