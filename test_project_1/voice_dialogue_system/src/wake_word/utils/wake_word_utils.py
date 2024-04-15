import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from test_project_1.voice_dialogue_system.src.wake_word.utils.audio_similarity_analysis import compare_audio_similarity
from test_project_1.voice_dialogue_system.src.wake_word.utils.functions import generate_wake_words_dict
import librosa


def load_and_extract_features(audio_data, sample_rate):
    # 将音频数据转换为浮点型，并规范化到[-1, 1]
    audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max

    # 计算 MFCC
    mfcc = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    # 对 MFCC 取均值，简化为单个向量
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean


def is_wake_word_2(audio_data_np, sample_rate, users_wake_words_dict):
    print("\n")
    # 先转换输入音频数据
    input_mfcc = load_and_extract_features(audio_data_np, sample_rate)

    # 准备存放结果的字典
    similarity_results = {}

    # 遍历提供的用户唤醒词路径
    for filepath, username in users_wake_words_dict.items():
        # 加载文件并提取MFCC特征
        y, sr = librosa.load(filepath, sr=sample_rate)
        mfcc_saved = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_saved_mean = np.mean(mfcc_saved, axis=1)

        # 计算与输入音频的相似度
        similarity = compare_audio_similarity(input_mfcc, mfcc_saved_mean, sample_rate)
        # similarity = cosine_similarity([input_mfcc], [mfcc_saved_mean])[0][0]

        # 将结果存入字典
        similarity_results[filepath] = {
            "user": username,
            "similarity": similarity
        }
        print("similarity_results : ", filepath, similarity, username)

    print("\n")
    return similarity_results

def is_wake_word(audio_data_np, sample_rate, users_wake_words_dict):
    print("\n")
    # 先转换输入音频数据
    input_mfcc = load_and_extract_features(audio_data_np, sample_rate)

    # 准备存放结果的字典
    similarity_results = {}

    # 遍历提供的用户唤醒词路径
    for filepath, username in users_wake_words_dict.items():
        # 加载文件并提取MFCC特征
        y, sr = librosa.load(filepath, sr=sample_rate)
        mfcc_saved = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_saved_mean = np.mean(mfcc_saved, axis=1)

        # 计算与输入音频的相似度
        similarity = compare_audio_similarity(input_mfcc, mfcc_saved_mean, sample_rate)
        # similarity = cosine_similarity([input_mfcc], [mfcc_saved_mean])[0][0]

        # 将结果存入字典
        similarity_results[filepath] = {
            "user": username,
            "similarity": similarity
        }
        print("similarity_results : ", filepath, similarity, username)

    print("\n")
    return similarity_results

if __name__ == '__main__':
    # 测试代码...
    # 加载用户的唤醒词特征并计算相似度

    base_path = "../user_wake_words/"
    users_wake_words = generate_wake_words_dict(base_path)

    print(users_wake_words)
    # 注意，您不需要传递文件路径，而应该是音频数据的字节流。
    pass
