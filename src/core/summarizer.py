"""Module chức năng tóm tắt văn bản sử dụng mô hình AI"""
"""Module xử lý tóm tắt văn bản"""

import logging
import time
import re
from typing import Optional, Dict, Any, List

# Thiết lập logging
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Làm sạch văn bản trước khi tóm tắt

    Args:
        text: Văn bản cần xử lý

    Returns:
        Văn bản đã làm sạch
    """
    # Loại bỏ ký tự đặc biệt không cần thiết
    text = re.sub(r'[\r\t\n]+', ' ', text)
    # Loại bỏ khoảng trắng dư thừa
    text = re.sub(r'\s+', ' ', text)
    # Loại bỏ URL
    text = re.sub(r'https?://\S+|www\.\S+', '[LINK]', text)
    return text.strip()

def split_text(text: str, max_chunk_size: int = 1000) -> List[str]:
    """Chia văn bản thành các phần nhỏ hơn để xử lý

    Args:
        text: Văn bản cần chia
        max_chunk_size: Kích thước tối đa của mỗi phần (số từ)

    Returns:
        Danh sách các phần văn bản
    """
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0

    for word in words:
        current_chunk.append(word)
        current_size += 1

        if current_size >= max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0

    # Thêm phần còn lại nếu có
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def simulate_ai_summarization(text: str, config: Dict[str, Any]) -> str:
    """Giả lập quá trình tóm tắt bằng AI

    Args:
        text: Văn bản cần tóm tắt
        config: Cấu hình tóm tắt

    Returns:
        Bản tóm tắt
    """
    # Trong môi trường thực tế, đây là nơi kết nối với mô hình AI
    # Trong ví dụ này, chúng ta tạo một bản tóm tắt đơn giản

    words = text.split()
    word_count = len(words)

    if config["length"] == "short":
        ratio = 0.05  # Khoảng 5% của văn bản gốc
        target_length = min(50, max(20, int(word_count * ratio)))
    elif config["length"] == "medium":
        ratio = 0.1  # Khoảng 10% của văn bản gốc
        target_length = min(150, max(50, int(word_count * ratio)))
    else:  # long
        ratio = 0.2  # Khoảng 20% của văn bản gốc
        target_length = min(300, max(150, int(word_count * ratio)))

    # Tạo bản tóm tắt đơn giản bằng cách lấy phần đầu
    summary_words = words[:target_length]
    # Thêm dấu chấm cuối cùng nếu không có
    summary = ' '.join(summary_words)
    if not summary.endswith('.'):
        summary += '.'

    return summary

def summarize(text: str, length: str = "medium") -> str:
    """Tóm tắt văn bản

    Args:
        text: Văn bản cần tóm tắt
        length: Độ dài tóm tắt ("short", "medium", "long")

    Returns:
        Bản tóm tắt
    """
    try:
        # Thiết lập cấu hình
        config = {"length": length}

        # Làm sạch văn bản
        cleaned_text = clean_text(text)

        # Kiểm tra độ dài
        if len(cleaned_text.split()) <= 50:
            return cleaned_text  # Văn bản quá ngắn, không cần tóm tắt

        # Kiểm tra nếu văn bản dài, cần chia nhỏ
        if len(cleaned_text.split()) > 1000:
            logger.info("Văn bản dài, thực hiện chia nhỏ để tóm tắt")
            chunks = split_text(cleaned_text)

            # Tóm tắt từng phần
            summaries = []
            for i, chunk in enumerate(chunks):
                logger.info(f"Đang tóm tắt phần {i+1}/{len(chunks)}")
                chunk_summary = simulate_ai_summarization(chunk, config)
                summaries.append(chunk_summary)

            # Kết hợp các phần tóm tắt
            combined_summary = " ".join(summaries)

            # Nếu kết quả vẫn dài, tóm tắt lại một lần nữa
            if len(combined_summary.split()) > 500:
                logger.info("Đang tóm tắt lại tổng hợp các bản tóm tắt")
                final_summary = simulate_ai_summarization(combined_summary, config)
                return final_summary
            return combined_summary
        else:
            # Tóm tắt trực tiếp cho văn bản ngắn
            return simulate_ai_summarization(cleaned_text, config)

    except Exception as e:
        logger.error(f"Lỗi khi tóm tắt văn bản: {str(e)}")
        return f"Đã xảy ra lỗi khi tóm tắt: {str(e)}"
import logging
import time
import os
import textwrap
from typing import Dict, Any, Optional, List, Union

# Thiết lập logging
logger = logging.getLogger(__name__)

# Định nghĩa các cấp độ tóm tắt
LENGTH_CONFIG: Dict[str, Dict[str, Any]] = {
    "short": {
        "max_length": 100,
        "min_length": 30,
        "description": "ngắn gọn, tập trung vào điểm chính nhất"
    },
    "medium": {
        "max_length": 200,
        "min_length": 80,
        "description": "cân đối, bao gồm các điểm chính"
    },
    "long": {
        "max_length": 350,
        "min_length": 150,
        "description": "chi tiết, bao gồm hầu hết thông tin quan trọng"
    }
}

# Mô phỏng cho môi trường demo
def simulate_ai_summarization(text: str, config: Dict[str, Any]) -> str:
    """Mô phỏng chức năng tóm tắt AI trong môi trường demo

    Args:
        text: Văn bản cần tóm tắt
        config: Cấu hình tóm tắt

    Returns:
        Bản tóm tắt mô phỏng
    """
    logger.info(f"Mô phỏng tóm tắt với cấu hình: {config['description']}")

    # Đảm bảo có độ trễ tự nhiên để mô phỏng thực tế
    time.sleep(1.5)

    # Chiến lược tóm tắt đơn giản: lấy các câu đầu tiên dựa trên độ dài yêu cầu
    sentences = [s.strip() + "." for s in text.replace(".", ".<stop>").split("<stop>") if s.strip()]

    # Tính số câu dựa trên cấu hình độ dài
    if config["description"] == "ngắn gọn, tập trung vào điểm chính nhất":
        sentence_count = min(3, len(sentences))
    elif config["description"] == "cân đối, bao gồm các điểm chính":
        sentence_count = min(7, len(sentences))
    else:  # chi tiết
        sentence_count = min(12, len(sentences))

    # Lấy câu đầu tiên và một số câu quan trọng khác
    if len(sentences) <= sentence_count:
        summary = " ".join(sentences)
    else:
        # Lấy câu đầu tiên
        important_sentences = [sentences[0]]

        # Lấy một số câu ở giữa văn bản
        middle_start = max(1, len(sentences) // 3)
        middle_end = min(len(sentences) - 1, 2 * len(sentences) // 3)
        middle_sentences = sentences[middle_start:middle_end]
        step = max(1, len(middle_sentences) // (sentence_count - 2))
        important_sentences.extend(middle_sentences[::step][:sentence_count-2])

        # Lấy câu cuối cùng
        if len(sentences) > 1:
            important_sentences.append(sentences[-1])

        summary = " ".join(important_sentences[:sentence_count])

    # Cắt bớt nếu quá dài
    word_limit = config["max_length"]
    words = summary.split()
    if len(words) > word_limit:
        summary = " ".join(words[:word_limit]) + "..."

    return summary

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """Chia văn bản thành các đoạn nhỏ hơn để xử lý

    Args:
        text: Văn bản cần chia
        chunk_size: Kích thước mỗi đoạn (số từ)
        overlap: Số từ chồng lấp giữa các đoạn

    Returns:
        Danh sách các đoạn văn bản
    """
    words = text.split()
    chunks = []

    if len(words) <= chunk_size:
        return [text]

    i = 0
    while i < len(words):
        chunk_end = min(i + chunk_size, len(words))
        chunk = ' '.join(words[i:chunk_end])
        chunks.append(chunk)
        i += chunk_size - overlap

    return chunks

def clean_text_for_summary(text: str) -> str:
    """Làm sạch văn bản trước khi tóm tắt

    Args:
        text: Văn bản cần làm sạch

    Returns:
        Văn bản đã làm sạch
    """
    # Loại bỏ khoảng trắng thừa
    text = " ".join(text.split())

    # Chuẩn hóa dấu câu
    text = text.replace("..", ".")
    text = text.replace(".", ". ")
    text = text.replace("  ", " ")

    # Cắt bớt nếu quá dài
    if len(text) > 50000:
        logger.warning(f"Văn bản quá dài ({len(text)} ký tự), cắt bớt xuống 50000 ký tự")
        text = text[:50000] + "..."

    return text

def summarize(text: str, length: str = "medium") -> str:
    """Tóm tắt văn bản với độ dài đã chọn

    Args:
        text: Văn bản cần tóm tắt
        length: Độ dài tóm tắt ("short", "medium", "long")

    Returns:
        Bản tóm tắt của văn bản
    """
    if not text or not text.strip():
        return "Không có văn bản để tóm tắt."

    # Lấy cấu hình cho độ dài đã chọn
    config = LENGTH_CONFIG.get(length.lower(), LENGTH_CONFIG["medium"])

    try:
        # Làm sạch văn bản
        cleaned_text = clean_text_for_summary(text)

        # Xử lý văn bản dài
        if len(cleaned_text.split()) > 1000:
            logger.info(f"Văn bản dài ({len(cleaned_text.split())} từ), đang chia thành các đoạn")
            chunks = chunk_text(cleaned_text)

            # Tóm tắt từng đoạn
            summaries = []
            for i, chunk in enumerate(chunks):
                logger.info(f"Đang tóm tắt đoạn {i+1}/{len(chunks)}")
                result = simulate_ai_summarization(chunk, config)
                summaries.append(result)

            # Tóm tắt lại các bản tóm tắt nếu cần
            combined_summary = " ".join(summaries)
            if len(combined_summary.split()) > 500:
                logger.info("Đang tóm tắt lại tổng hợp các bản tóm tắt")
                final_summary = simulate_ai_summarization(combined_summary, config)
                return final_summary
            return combined_summary
        else:
            # Tóm tắt trực tiếp cho văn bản ngắn
            return simulate_ai_summarization(cleaned_text, config)

    except Exception as e:
        logger.error(f"Lỗi khi tóm tắt văn bản: {str(e)}")
        return f"Đã xảy ra lỗi khi tóm tắt: {str(e)}"