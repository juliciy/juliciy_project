import numpy as np
import librosa
from scipy.spatial import distance
from pydub import AudioSegment
from pydub.effects import compress_dynamic_range

def audio_segment_to_float_array(audio_segment):
    """
    将 AudioSegment 对象的音频数据转换为归一化的浮点数 NumPy 数组。

    参数
    ----------
    audio_segment : AudioSegment
        要转换的 AudioSegment 音频对象。

    返回值
    -------
    np.ndarray
        归一化的浮点数音频数据数组。
    """
    samples = audio_segment.get_array_of_samples()
    return np.array(samples).astype(np.float32) / 2**15  # assuming 16-bit audio

def load_and_compress_audio(file_path):
    """
    从文件路径加载音频，并应用动态范围压缩。

    参数
    ----------
    file_path : str
        音频文件的路径。

    返回值
    -------
    AudioSegment
        压缩后的 AudioSegment 音频对象。
    """
    audio = AudioSegment.from_file(file_path)
    compressed_audio = compress_dynamic_range(audio, threshold=-20.0, ratio=3.0)
    return compressed_audio

def load_and_extract_features(audio_data, sample_rate):
    """
    加载音频数据并提取压缩后的 MFCC 特征。

    参数
    ----------
    audio_data : np.ndarray
        原始音频数据数组。
    sample_rate : int
        音频的采样率。

    返回值
    -------
    np.ndarray
        压缩并提取的 MFCC 特征的均值向量。
    """
    audio_segment = AudioSegment(
        data=audio_data.tobytes(),
        sample_width=audio_data.dtype.itemsize,
        frame_rate=sample_rate,
        channels=1
    )
    compressed_audio = compress_dynamic_range(audio_segment)
    compressed_samples = np.array(compressed_audio.get_array_of_samples())
    audio_data_compressed = compressed_samples.astype(np.float32) / np.iinfo(np.int16).max
    print("Compressed data range:", np.min(audio_data_compressed), "to", np.max(audio_data_compressed))
    mfcc = librosa.feature.mfcc(y=audio_data_compressed, sr=sample_rate, n_mfcc=20, n_fft=2048, hop_length=512)
    mfcc_mean = np.mean(mfcc, axis=1)
    print("MFCC Mean:", mfcc_mean)
    return mfcc_mean

def euclidean_similarity(mfcc1, mfcc2):
    """
    计算两个 MFCC 特征向量之间的欧氏距离。

    参数
    ----------
    mfcc1 : np.ndarray
        第一个音频的 MFCC 特征向量。
    mfcc2 : np.ndarray
        第二个音频的 MFCC 特征向量。

    返回值
    -------
    float
        两个特征向量之间的欧氏距离。
    """
    dist = np.linalg.norm(mfcc1 - mfcc2)
    return np.exp(-dist / 10)

def compare_audio_similarity(audio_data1, audio_data2, sample_rate):
    """
    比较两段音频数据的相似度。

    参数
    ----------
    audio_data1 : np.ndarray
        第一段音频的数据。
    audio_data2 : np.ndarray
        第二段音频的数据。
    sample_rate : int
        音频的采样率。

    返回值
    -------
    float
        两段音频的相似度百分比。
    """
    mfcc1 = load_and_extract_features(audio_data1, sample_rate)
    mfcc2 = load_and_extract_features(audio_data2, sample_rate)
    similarity = euclidean_similarity(mfcc1, mfcc2)
    similarity_percentage = similarity * 100
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")
    return similarity_percentage

if __name__ == "__main__":
    # 主功能：比较两段音频文件的相似度
    # base_path = "../user_wake_words/user_1/zyh_wake_word_2024-04-15_15-19-01.wav"
    base_path_1 = "../user_wake_words/xiaomi/xiaomi_wake_word_2024-04-15_22-03-42.wav"
    base_path_2 = "../user_wake_words/xiaomi/xiaomi_wake_word_2024-04-15_22-40-59.wav"
    audio_data1, sr1 = librosa.load(base_path_2, sr=None)
    audio_data2, sr2 = librosa.load(base_path_1, sr=None)
    sample_rate = sr1
    similarity = compare_audio_similarity(audio_data1, audio_data2, sample_rate)
    print(f"The similarity between two audio samples is: {similarity:.2f}%")
