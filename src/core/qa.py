"""Module xử lý hỏi đáp dựa trên nội dung văn bản"""

import logging
import time
import random
import re
from typing import Dict, Union, Any, Optional, List

# Thiết lập logging
logger = logging.getLogger(__name__)

def preprocess_text(text: str) -> str:
    """Tiền xử lý văn bản để cải thiện chất lượng trả lời

    Args:
        text: Văn bản cần xử lý

    Returns:
        Văn bản đã được xử lý
    """
    # Loại bỏ khoảng trắng thừa
    text = " ".join(text.split())
    # Chuẩn hóa dấu câu
    text = text.replace("..", ".")
    text = text.replace(".", ". ")
    text = text.replace("  ", " ")
    return text

def find_relevant_context(question: str, full_context: str, max_length: int = 512) -> str:
    """Tìm phần context liên quan nhất với câu hỏi

    Args:
        question: Câu hỏi cần trả lời
        full_context: Toàn bộ văn bản
        max_length: Độ dài tối đa của context (số từ)

    Returns:
        Phần văn bản liên quan nhất đến câu hỏi
    """
    # Nếu context đủ ngắn, sử dụng toàn bộ
    if len(full_context.split()) <= max_length:
        return full_context

    # Chia context thành các đoạn với overlap
    words = full_context.split()
    chunk_size = max_length
    overlap = 100
    chunks = []

    i = 0
    while i < len(words):
        chunk_end = min(i + chunk_size, len(words))
        chunk = ' '.join(words[i:chunk_end])
        chunks.append(chunk)
        i += chunk_size - overlap

    # Tìm điểm số cho mỗi đoạn (số từ chung giữa câu hỏi và đoạn văn)
    question_words = set(question.lower().split())
    scores = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        common_words = question_words.intersection(chunk_words)
        scores.append(len(common_words))
"""Module xử lý hỏi đáp (Question-Answering)"""

import logging
import re
import time
from typing import Dict, Any, Union, List

# Thiết lập logging
logger = logging.getLogger(__name__)

def preprocess_question(question: str) -> str:
    """Tiền xử lý câu hỏi

    Args:
        question: Câu hỏi gốc

    Returns:
        Câu hỏi đã được xử lý
    """
    # Loại bỏ ký tự đặc biệt và khoảng trắng không cần thiết
    question = re.sub(r'[\r\n\t]+', ' ', question)
    question = re.sub(r'\s+', ' ', question)

    # Đảm bảo câu hỏi kết thúc bằng dấu hỏi
    if not question.endswith('?'):
        question += '?'

    return question.strip()

def simulate_qa_model(question: str, context: str) -> Dict[str, Any]:
    """Giả lập mô hình hỏi đáp

    Args:
        question: Câu hỏi đã tiền xử lý
        context: Ngữ cảnh để tìm câu trả lời

    Returns:
        Dict chứa câu trả lời và điểm tin cậy
    """
    # Trong môi trường thực tế, đây là nơi kết nối với mô hình AI
    # Trong ví dụ này, chúng ta trả về câu trả lời đơn giản

    # Tạo phản hồi giả lập
    question_lower = question.lower()

    # Mẫu câu trả lời tùy thuộc vào loại câu hỏi
    if "gì" in question_lower or "là gì" in question_lower:
        answer = "Dựa trên văn bản, đây là khái niệm hoặc định nghĩa liên quan đến chủ đề trong tài liệu."
        score = 0.85
    elif "tại sao" in question_lower or "vì sao" in question_lower:
        answer = "Theo thông tin trong tài liệu, nguyên nhân chính là do các yếu tố được đề cập trong phần tóm tắt."
        score = 0.78
    elif "bao nhiêu" in question_lower or "mấy" in question_lower:
        answer = "Dựa trên dữ liệu trong tài liệu, con số chính xác không được nêu rõ, nhưng có thể ước tính từ ngữ cảnh."
        score = 0.65
    elif "làm thế nào" in question_lower or "làm sao" in question_lower or "cách" in question_lower:
        answer = "Văn bản đề xuất phương pháp giải quyết thông qua các bước được mô tả trong phần tóm tắt."
        score = 0.82
    elif "ai" in question_lower or "người nào" in question_lower:
        answer = "Theo thông tin trong tài liệu, đây liên quan đến các cá nhân hoặc nhóm người được đề cập."
        score = 0.75
    elif "ở đâu" in question_lower or "nơi nào" in question_lower or "đâu" in question_lower:
        answer = "Dựa trên ngữ cảnh, địa điểm được đề cập trong văn bản là khu vực liên quan đến chủ đề chính."
        score = 0.73
    elif "khi nào" in question_lower or "thời gian" in question_lower:
        answer = "Thời gian cụ thể không được nêu rõ, nhưng có thể suy luận từ các sự kiện được đề cập trong tài liệu."
        score = 0.68
    elif "chính" in question_lower or "ý chính" in question_lower:
        answer = "Ý chính của văn bản là về chủ đề trung tâm được phân tích và tóm tắt, thể hiện quan điểm và luận điểm chính."
        score = 0.92
    else:
        answer = "Dựa trên thông tin trong tài liệu, câu trả lời có thể tìm thấy trong ngữ cảnh của vấn đề được đề cập."
        score = 0.7

    return {
        "answer": answer,
        "score": score
    }

def answer_question(question: str, context: str) -> Union[Dict[str, Any], str]:
    """Xử lý câu hỏi và trả về câu trả lời

    Args:
        question: Câu hỏi từ người dùng
        context: Ngữ cảnh để tìm câu trả lời (thường là tóm tắt hoặc văn bản gốc)

    Returns:
        Dict chứa câu trả lời và thông tin bổ sung hoặc thông báo lỗi
    """
    try:
        # Tiền xử lý câu hỏi
        processed_question = preprocess_question(question)

        # Kiểm tra câu hỏi
        if len(processed_question) < 5:
            return "Câu hỏi quá ngắn. Vui lòng cung cấp câu hỏi chi tiết hơn."

        # Kiểm tra ngữ cảnh
        if not context or len(context) < 20:
            return "Không đủ thông tin để trả lời câu hỏi này."

        # Xử lý hỏi đáp (trong thực tế, đây là nơi gọi mô hình AI)
        logger.info(f"Đang xử lý câu hỏi: {processed_question}")
        result = simulate_qa_model(processed_question, context)

        return result

    except Exception as e:
        logger.error(f"Lỗi khi xử lý câu hỏi: {str(e)}")
        return f"Đã xảy ra lỗi khi xử lý câu hỏi: {str(e)}"
    # Lấy đoạn có điểm cao nhất
    if max(scores) > 0:
        best_chunk_index = scores.index(max(scores))
        return chunks[best_chunk_index]
    else:
        # Nếu không tìm thấy đoạn nào có từ chung, lấy đoạn đầu tiên
        return chunks[0]

def simulate_qa_response(question: str, context: str) -> Dict[str, Any]:
    """Mô phỏng phản hồi hỏi đáp trong môi trường demo

    Args:
        question: Câu hỏi cần trả lời
        context: Văn bản chứa thông tin

    Returns:
        Kết quả trả lời và điểm tin cậy
    """
    logger.info(f"Mô phỏng trả lời cho câu hỏi: {question}")

    # Đảm bảo có độ trễ tự nhiên để mô phỏng thực tế
    time.sleep(1.0)

    # Tách thành câu
    sentences = [s.strip() for s in context.replace(".", ".<stop>").split("<stop>") if s.strip()]

    # Tìm câu liên quan nhất
    question_words = set(question.lower().split())
    sentence_scores = []

    for sentence in sentences:
        sentence_words = set(sentence.lower().split())
        common_words = len(question_words.intersection(sentence_words))
        sentence_scores.append((sentence, common_words))

    # Sắp xếp câu theo điểm số
    sentence_scores.sort(key=lambda x: x[1], reverse=True)

    # Lấy câu có điểm cao nhất
    if sentence_scores and sentence_scores[0][1] > 0:
        best_sentence = sentence_scores[0][0]
        # Thêm câu tiếp theo để có context
        for i, (sent, _) in enumerate(sentence_scores):
            if sent == best_sentence and i < len(sentence_scores) - 1:
                best_sentence += " " + sentence_scores[i+1][0]
                break

        # Điểm tin cậy dựa trên số từ chung
        confidence = min(0.9, max(0.5, sentence_scores[0][1] / max(1, len(question_words))))

        return {
            "answer": best_sentence,
            "score": confidence
        }
    else:
        # Không tìm thấy câu liên quan
        return {
            "answer": "Tôi không tìm thấy thông tin để trả lời câu hỏi này trong văn bản.",
            "score": 0.1
        }

def answer_question(question: str, context: str) -> Union[Dict[str, Any], str]:
    """Trả lời câu hỏi dựa trên văn bản

    Args:
        question: Câu hỏi cần trả lời
        context: Văn bản chứa thông tin để trả lời

    Returns:
        Kết quả trả lời kèm điểm tin cậy, hoặc thông báo lỗi
    """
    # Kiểm tra đầu vào
    if not question or not question.strip():
        return "Câu hỏi không hợp lệ. Vui lòng nhập câu hỏi."

    if not context or not context.strip():
        return "Không có nội dung để trả lời câu hỏi."

    try:
        # Tiền xử lý
        preprocessed_question = preprocess_text(question)
        preprocessed_context = preprocess_text(context)

        # Tìm context liên quan
        relevant_context = find_relevant_context(preprocessed_question, preprocessed_context)

        # Kiểm tra nếu câu hỏi thuộc dạng đặc biệt
        result = None

        # Câu hỏi về chủ đề/tiêu đề
        if re.search(r'(chủ đề|tiêu đề|nói về gì|về gì|chủ yếu|ý chính)', preprocessed_question.lower()):
            # Lấy câu đầu tiên làm ý chính
            sentences = [s.strip() for s in relevant_context.replace(".", ".<stop>").split("<stop>") if s.strip()]
            if sentences:
                result = {
                    "answer": f"Văn bản chủ yếu nói về {sentences[0]}",
                    "score": 0.85
                }

        # Câu hỏi về điểm quan trọng nhất
        elif re.search(r'(quan trọng nhất|điểm chính|đáng chú ý nhất)', preprocessed_question.lower()):
            sentences = [s.strip() for s in relevant_context.replace(".", ".<stop>").split("<stop>") if s.strip()]
            if len(sentences) > 1:
                result = {
                    "answer": f"Điểm quan trọng nhất là {sentences[1]}",
                    "score": 0.8
                }

        # Câu hỏi về kết luận
        elif re.search(r'(kết luận|kết quả|cuối cùng)', preprocessed_question.lower()):
            sentences = [s.strip() for s in relevant_context.replace(".", ".<stop>").split("<stop>") if s.strip()]
            if sentences:
                result = {
                    "answer": f"Kết luận của văn bản là {sentences[-1]}",
                    "score": 0.82
                }

        # Các câu hỏi khác, sử dụng mô phỏng QA
        if result is None:
            result = simulate_qa_response(preprocessed_question, relevant_context)

        return result

    except Exception as e:
        logger.error(f"Lỗi khi trả lời câu hỏi: {str(e)}")
        return f"Đã xảy ra lỗi khi xử lý câu hỏi: {str(e)}"