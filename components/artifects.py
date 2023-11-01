import os


def model_path():
    relative_path = "chatbot_model_m.h5"
    absolute_path = "D:\msn\pycharm_projects\chatbotcoustom\chatbot_model_m.h5"
    if os.path.exists(relative_path):
        return relative_path
    elif os.path.exists(absolute_path):
        return absolute_path
    else:
        raise FileNotFoundError("Neither relative nor absolute path exists.")


def classes_pickle_path():
    relative_path = "classes.pkl"
    absolute_path = "D:\msn\pycharm_projects\chatbotcoustom\classes.pkl"

    if os.path.exists(relative_path):
        return relative_path
    elif os.path.exists(absolute_path):
        return absolute_path
    else:
        raise FileNotFoundError("Neither relative nor absolute path exists.")


def words_pickle_path():
    relative_path = "words.pkl"
    absolute_path = "D:\msn\pycharm_projects\chatbotcoustom\words.pkl"

    if os.path.exists(relative_path):
        return relative_path
    elif os.path.exists(absolute_path):
        return absolute_path
    else:
        raise FileNotFoundError("Neither relative nor absolute path exists.")


def json_file_path():
    relative_path = "job_file.json"
    absolute_path = "D:\msn\pycharm_projects\chatbotcoustom\job_file.json"

    if os.path.exists(relative_path):
        return relative_path
    elif os.path.exists(absolute_path):
        return absolute_path
    else:
        raise FileNotFoundError("Neither relative nor absolute path exists.")
