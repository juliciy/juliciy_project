import numpy as np
import librosa
from sklearn.metrics.pairwise import cosine_similarity

def load_and_extract_features(audio_data, sample_rate):
    print("Original data range:", np.min(audio_data), "to", np.max(audio_data))
    audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max
    print("Normalized data range:", np.min(audio_data), "to", np.max(audio_data))

    mfcc = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)
    print("MFCC Mean:", mfcc_mean)
    return mfcc_mean

def compare_audio_similarity(audio_data1, audio_data2, sample_rate):
    mfcc1 = load_and_extract_features(audio_data1, sample_rate)
    print("\n")
    mfcc2 = load_and_extract_features(audio_data2, sample_rate)

    similarity = cosine_similarity([mfcc1], [mfcc2])[0][0]
    print("Similarity:", similarity)
    return similarity


# 示例使用
if __name__ == "__main__":
    # 假设 audio_data1 和 audio_data2 已经是加载和转换为 np.ndarray 的音频数据
    # 以下为示例代码，您需要替换为实际的音频数据加载代码
    # base_path = "../user_wake_words/user_1/zyh_wake_word_2024-04-15_15-19-01.wav"
    base_path = "../user_wake_words/baidu/baidu_wake_word_2024-04-15_16-16-53.wav"
    audio_data1, sr1 = librosa.load("../user_wake_words/zyh/zyh_wake_word_2024-04-15_15-19-01.wav", sr=None)
    audio_data2, sr2 = librosa.load(base_path, sr=None)

    # 确保两个音频数据的采样率相同
    sample_rate = sr1  # 假设两个音频文件采样率相同

    similarity = compare_audio_similarity(audio_data1, audio_data2, sample_rate)
    print(f"The similarity between two audio samples is: {similarity:.3f}")
