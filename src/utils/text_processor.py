"""Module xử lý và phân tích văn bản nâng cao"""

import re
import string
import logging
from typing import List, Dict, Tuple, Set, Optional
from collections import Counter

# Thiết lập logging
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Làm sạch văn bản

    Args:
        text: Văn bản cần làm sạch

    Returns:
        Văn bản đã được làm sạch
    """
    # Loại bỏ ký tự đặc biệt và định dạng
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text)
    # Thay thế nhiều dấu cách bằng một dấu cách
    text = re.sub(r'\s+', ' ', text)
    # Loại bỏ dấu cách ở đầu và cuối chuỗi
    text = text.strip()
    return text

def split_into_sentences(text: str) -> List[str]:
    """Chia văn bản thành các câu

    Args:
        text: Văn bản cần chia

    Returns:
        Danh sách các câu
    """
    # Mẫu regex cơ bản để tách câu
    sentence_endings = r'(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_endings, text)
    return [s.strip() for s in sentences if s.strip()]

def extract_keywords(text: str, num_keywords: int = 10) -> List[str]:
    """Trích xuất từ khóa từ văn bản

    Args:
        text: Văn bản cần trích xuất từ khóa
        num_keywords: Số lượng từ khóa trả về

    Returns:
        Danh sách các từ khóa
    """
    # Chuyển thành chữ thường
    text = text.lower()

    # Loại bỏ dấu câu
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tách từ
    words = text.split()

    # Loại bỏ stopwords (từ phổ biến không mang nhiều ý nghĩa)
    stopwords = {'và', 'là', 'của', 'có', 'trong', 'cho', 'không', 'được', 'các', 'với',
                'những', 'để', 'này', 'một', 'về', 'đã', 'như', 'khi', 'từ', 'tới',
                'theo', 'trên', 'tại', 'đến', 'bởi', 'cũng', 'vì', 'đây', 'còn', 'nên'}

    # Lọc từ
    filtered_words = [word for word in words if word not in stopwords and len(word) > 1]

    # Đếm tần suất
    word_counts = Counter(filtered_words)

    # Lấy top N từ khóa
    keywords = [word for word, count in word_counts.most_common(num_keywords)]

    return keywords

def calculate_readability(text: str) -> Dict[str, float]:
    """Tính toán độ dễ đọc của văn bản

    Args:
        text: Văn bản cần đánh giá

    Returns:
        Từ điển chứa các chỉ số đánh giá
    """
    # Tách câu và từ
    sentences = split_into_sentences(text)
    words = text.split()

    # Đếm số câu, từ, ký tự
    num_sentences = len(sentences)
    num_words = len(words)
    num_chars = len(text)

    if num_sentences == 0 or num_words == 0:
        return {
            "avg_words_per_sentence": 0,
            "avg_chars_per_word": 0,
            "complexity_score": 0
        }

    # Tính toán các chỉ số
    avg_words_per_sentence = num_words / num_sentences
    avg_chars_per_word = num_chars / num_words

    # Điểm phức tạp (càng cao càng khó đọc)
    complexity_score = (avg_words_per_sentence * 0.39) + (avg_chars_per_word * 11.8) - 15.59

    return {
        "avg_words_per_sentence": avg_words_per_sentence,
        "avg_chars_per_word": avg_chars_per_word,
        "complexity_score": complexity_score
    }

def find_similar_sentences(text: str, query: str, top_n: int = 3) -> List[str]:
    """Tìm các câu tương tự với câu truy vấn

    Args:
        text: Văn bản chứa các câu cần so sánh
        query: Câu truy vấn
        top_n: Số lượng câu trả về

    Returns:
        Danh sách các câu tương tự nhất
    """
    # Tách văn bản thành các câu
    sentences = split_into_sentences(text)
"""Module xử lý và phân tích văn bản"""

import re
import logging
from typing import Dict, Any, List, Tuple

# Thiết lập logging
logger = logging.getLogger(__name__)

def analyze_text_stats(text: str) -> Dict[str, Any]:
    """Phân tích thống kê cơ bản của văn bản

    Args:
        text: Văn bản cần phân tích

    Returns:
        Dict chứa các thống kê cơ bản
    """
    if not text or not text.strip():
        return {
            "word_count": 0,
            "char_count": 0,
            "sentence_count": 0,
            "paragraph_count": 0,
            "avg_word_length": 0,
            "avg_sentence_length": 0
        }

    # Tính số ký tự (không bao gồm khoảng trắng)
    char_count = len(text.replace(" ", ""))

    # Tính số từ
    words = text.split()
    word_count = len(words)

    # Tính số câu
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)

    # Tính số đoạn
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)

    # Tính độ dài trung bình của từ
    avg_word_length = sum(len(word) for word in words) / max(1, word_count)

    # Tính độ dài trung bình của câu (theo số từ)
    avg_sentence_length = word_count / max(1, sentence_count)

    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "avg_word_length": round(avg_word_length, 1),
        "avg_sentence_length": round(avg_sentence_length, 1)
    }

def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
    """Trích xuất từ khóa từ văn bản

    Args:
        text: Văn bản cần trích xuất
        max_keywords: Số lượng từ khóa tối đa

    Returns:
        Danh sách các từ khóa
    """
    # Xử lý văn bản
    words = text.lower().split()

    # Loại bỏ stopwords
    stopwords = {'và', 'là', 'của', 'có', 'trong', 'cho', 'không', 'được', 'các', 'với',
                'những', 'để', 'này', 'một', 'về', 'đã', 'như', 'khi', 'từ', 'tới',
                'theo', 'trên', 'tại', 'đến', 'bởi', 'cũng', 'vì', 'đây', 'còn', 'nên'}

    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]

    # Đếm tần suất
    word_counts = {}
    for word in filtered_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sắp xếp và lấy top N
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    keywords = [word for word, count in sorted_words[:max_keywords]]

    return keywords

def get_readability_score(text: str) -> Tuple[float, str]:
    """Tính điểm dễ đọc của văn bản (đơn giản hóa)

    Args:
        text: Văn bản cần đánh giá

    Returns:
        Tuple gồm điểm số và mô tả
    """
    # Tính số từ
    words = text.split()
    word_count = len(words)

    # Tính số câu
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = max(1, len(sentences))

    # Tính số từ phức tạp (giả sử từ > 7 ký tự là phức tạp)
    complex_words = [word for word in words if len(word) > 7]
    complex_word_count = len(complex_words)

    # Tỷ lệ từ phức tạp
    complex_ratio = complex_word_count / max(1, word_count)

    # Độ dài trung bình của câu
    avg_sentence_length = word_count / sentence_count

    # Tính điểm dễ đọc (công thức đơn giản hóa)
    score = 100 - (avg_sentence_length * 0.6 + complex_ratio * 30)
    score = max(0, min(100, score))  # Giới hạn trong khoảng 0-100

    # Xác định mức độ
    if score >= 80:
        level = "Rất dễ đọc"
    elif score >= 60:
        level = "Dễ đọc"
    elif score >= 40:
        level = "Trung bình"
    elif score >= 20:
        level = "Khó đọc"
    else:
        level = "Rất khó đọc"

    return score, level
    if not sentences:
        return []

    # Tách query thành từ và loại bỏ stopwords
    query_words = set(query.lower().split())
    stopwords = {'và', 'là', 'của', 'có', 'trong', 'cho', 'không', 'được', 'các'}
    query_words = {w for w in query_words if w not in stopwords and len(w) > 1}

    # Tính điểm tương đồng cho mỗi câu
    scores = []
    for sentence in sentences:
        sentence_words = set(sentence.lower().split())
        # Số từ chung
        common_words = query_words.intersection(sentence_words)
        # Điểm = số từ chung / độ dài query
        score = len(common_words) / max(1, len(query_words))
        scores.append((sentence, score))

    # Sắp xếp theo điểm giảm dần và lấy top N
    scores.sort(key=lambda x: x[1], reverse=True)
    similar_sentences = [s[0] for s in scores[:top_n]]

    return similar_sentences

def analyze_text_stats(text: str) -> Dict[str, any]:
    """Phân tích thống kê văn bản

    Args:
        text: Văn bản cần phân tích

    Returns:
        Từ điển chứa các thống kê
    """
    if not text or not text.strip():
        return {
            "char_count": 0,
            "word_count": 0,
            "sentence_count": 0,
            "paragraph_count": 0,
            "avg_word_length": 0,
            "avg_sentence_length": 0,
            "readability": {"complexity_score": 0}
        }

    # Tách văn bản
    paragraphs = [p for p in text.split('\n') if p.strip()]
    sentences = split_into_sentences(text)
    words = text.split()
    characters = len(text)

    # Tính toán
    word_count = len(words)
    sentence_count = len(sentences)
    paragraph_count = len(paragraphs)

    # Độ dài trung bình
    avg_word_length = sum(len(word) for word in words) / max(1, word_count)
    avg_sentence_length = word_count / max(1, sentence_count)

    # Độ dễ đọc
    readability = calculate_readability(text)

    # Từ khóa
    keywords = extract_keywords(text, num_keywords=10)

    return {
        "char_count": characters,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
        "readability": readability,
        "keywords": keywords
    }
