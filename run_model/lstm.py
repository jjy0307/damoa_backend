import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf



loaded_model = tf.keras.models.load_model('C:/Users/USER/Desktop/최종 프로젝트/NBLastProjectBackend/model/lstm_model.h5')

okt = Okt()
okt.morphs('역시 한국인은 남 잘되는 꼴을 못 봐', stem=True)
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
tokenizer = Tokenizer()
max_len = 30

import pickle

with open('C:/Users/USER/Desktop/최종 프로젝트/NBLastProjectBackend/model/tokenizer_lstm.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def sentiment_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)

    new_sentence = okt.morphs(new_sentence, stem=True)  

    new_sentence = [word for word in new_sentence if not word in stopwords]  

    encoded = tokenizer.texts_to_sequences([new_sentence])  

    pad_new = pad_sequences(encoded, maxlen=max_len) 
    score = float(loaded_model.predict(pad_new))  
    return score