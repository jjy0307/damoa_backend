import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf



loaded_model = tf.keras.models.load_model('C:/Users/user/Documents/damoa_backend/model/lstm_model.h5')

okt = Okt()
okt.morphs('역시 한국인은 남 잘되는 꼴을 못 봐', stem=True)
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
tokenizer = Tokenizer()
max_len = 30

import pickle

with open('/model/tokenizer_lstm.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def sentiment_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)
    # print("new_sentence_1 = ", end=""), print(new_sentence)

    new_sentence = okt.morphs(new_sentence, stem=True)  # 토큰화
    # print("new_sentence_2 = ", end=""), print(new_sentence)

    new_sentence = [word for word in new_sentence if not word in stopwords]  # 불용어 제거
    # print("new_sentence_3 = ", end=""), print(new_sentence)

    encoded = tokenizer.texts_to_sequences([new_sentence])  # 정수 인코딩
    # print("encoded = ", end=""), print(encoded)

    pad_new = pad_sequences(encoded, maxlen=max_len)  # 패딩
    score = float(loaded_model.predict(pad_new))  # 예측
    # return score

    if (score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))

sentiment_predict('이직에 하려는 회사에 오퍼를 받고나니 몸이 부르르떨립니다')

sentiment_predict('한 두개 대답 못한 정도로 불합격되진 않아요. 기술 면접은 기술적인 것도 보지만, 태도도 많이 보거든요')

sentiment_predict('그렇게 일 할거면 접어라')