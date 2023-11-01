from components.artifects import *
import spacy
nlp = spacy.load('en_core_web_sm')  # Load the language model (English in this case)
import tensorflow as tf
import json
import pickle
import numpy as np

from tensorflow.keras.models import load_model


class prediction_line:
    def __init__(self):
        self.model = model_path()

    @staticmethod
    def classes_pickle_file():
        classes_ = classes_pickle_path()
        try:
            # Assuming 'file_path.pkl' is the path to your .pkl file
            with open(classes_, 'rb') as file:
                class_file = pickle.load(file)
            return class_file

        except Exception as e:
            raise f"pickle file not called {e}"

    @staticmethod
    def word_pickle_file():
        word_ = words_pickle_path()
        try:
            # Assuming 'file_path.pkl' is the path to your .pkl file
            with open(word_, 'rb') as file:
                word_file = pickle.load(file)
            return word_file

        except Exception as e:
            raise f"word file not called {e}"

    @staticmethod
    def json_file():
        json_ = json_file_path()
        try:
            data_file = open(json_, encoding='utf-8').read()
            json_file = json.loads(data_file)
            return json_file

        except Exception as e:
            raise f"json file not called {e}"

    def input_text(self, text):
        classes = self.classes_pickle_file()
        unique_vocab = self.word_pickle_file()
        try:
            pattern_words = []
            bag = []
            doc = nlp(text)
            for i in doc:
                word = ''.join(i.lemma_.lower())
                pattern_words.append(word)

            for w in unique_vocab:
                if w in pattern_words:
                    bag.append(1)
                else:
                    bag.append(0)

            input_data = [bag]
            model = load_model(self.model)
            preds = model.predict(input_data)
            class_tag = classes[np.argmax(preds)]
            return class_tag

        except Exception as e:
            raise f"input file error {e}"


def pipeline(text):
    function_class = prediction_line()
    return function_class.input_text(text), function_class.json_file()


# print(pipeline("hi"))


print(spacy.__version__)