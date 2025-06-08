"""Cấu hình cho ứng dụng AI Document Analyzer"""
"""Cấu hình ứng dụng"""

APP_CONFIG = {
    "name": "AI Document Analyzer",
    "version": "1.0.0",
    "description": "Ứng dụng tóm tắt và phân tích tài liệu sử dụng AI",
    "max_file_size_mb": 50,
    "supported_file_types": ["pdf", "docx"],
    "summary_levels": {
        "short": "Ngắn gọn (~50 từ)",
        "medium": "Trung bình (~150 từ)",
        "long": "Chi tiết (~300 từ)"
    }
}
import os
import logging
from typing import Dict, Any
from pathlib import Path

# Thiết lập logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", mode='a')
    ]
)
"""Cấu hình toàn cục cho ứng dụng"""

# Cấu hình chung của ứng dụng
APP_CONFIG = {
    "name": "AI Document Analyzer",
    "version": "1.0.0",
    "description": "Ứng dụng AI phân tích, tóm tắt và trả lời câu hỏi từ tài liệu",
    "max_file_size_mb": 50,
    "supported_file_types": ["pdf", "docx"],
    "default_summary_length": "medium",
    "log_level": "INFO"
}

# Cấu hình cho web scraper
SCRAPER_CONFIG = {
    "timeout": 15,  # Thời gian timeout cho request (giây)
    "max_retries": 3,  # Số lần thử lại tối đa
    "user_agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    ],
    "blocked_content_types": ["application/pdf", "image/", "video/", "audio/"],
    "max_content_size": 10 * 1024 * 1024  # Kích thước tối đa có thể download (10MB)
}

# Cấu hình cho AI model
MODEL_CONFIG = {
    "summarization": {
        "short": {
            "max_tokens": 150,
            "temperature": 0.3
        },
        "medium": {
            "max_tokens": 300,
            "temperature": 0.4
        },
        "long": {
            "max_tokens": 500,
            "temperature": 0.5
        }
    },
    "qa": {
        "max_tokens": 200,
        "temperature": 0.2
    }
}
# Đường dẫn cơ sở
BASE_DIR = Path(__file__).resolve().parent.parent

# Thư mục dữ liệu
DATA_DIR = BASE_DIR / "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Cấu hình ứng dụng
APP_CONFIG = {
    "name": "AI Document Analyzer",
    "version": "1.0.0",
    "description": "Ứng dụng AI tóm tắt và hỏi đáp về tài liệu",
    "max_file_size_mb": 50,
    "max_text_length": 100000,
}

# Cấu hình mô hình AI
MODEL_CONFIG = {
    "summarization": {
        "model_name": "facebook/bart-large-cnn",
        "max_length": 1024,
        "use_gpu": True,
    },
    "qa": {
        "model_name": "deepset/roberta-base-squad2",
        "max_length": 512,
        "use_gpu": True,
    }
}

# Cấu hình xử lý file
FILE_CONFIG = {
    "allowed_extensions": ["pdf", "docx"],
    "max_pages": 100,
}

# Cấu hình scraper
SCRAPER_CONFIG = {
    "timeout": 15,
    "max_retries": 3,
    "user_agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    ]
}