"""Các component UI tùy chỉnh cho ứng dụng"""

import streamlit as st
import base64
import re
from pathlib import Path
from typing import Optional, Union, Dict, List, Any

def display_logo(width: int = 200):
    """Hiển thị logo của ứng dụng với hiệu ứng gradient

    Args:
        width: Chiều rộng của logo
    """
    logo_html = f"""
    <div style="text-align: center; margin-bottom: 2rem;" class="fade-in-up">
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            text-shadow: 0 4px 8px rgba(0,0,0,0.1);
        ">
            🚀 AI Document Analyzer
        </div>
        <div style="
            color: #6c757d;
            font-size: 1rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 2px;
        ">
            Powered by AI
        </div>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

def info_card(title: str, content: str, icon: str = "💡"):
    """Hiển thị card thông tin với hiệu ứng hover

    Args:
        title: Tiêu đề của card
        content: Nội dung của card
        icon: Biểu tượng (emoji)
    """
    st.markdown(f"""
    <div class="card fade-in-up" style="
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid #e3f2fd;
        margin-bottom: 2rem;
        color: #424242;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    ">
        <div class="card-header" style="
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #e3f2fd;
        ">
            <div style="
                font-size: 2.5rem;
                margin-right: 1rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">{icon}</div>
            <div style="
                font-size: 1.4rem;
                font-weight: 700;
                color: #1565c0;
            ">{title}</div>
        </div>
        <div style="
            font-size: 1.1rem;
            color: #546e7a;
            line-height: 1.7;
        ">{content}</div>
    </div>
    """, unsafe_allow_html=True)

def success_box(content: str):
    """Hiển thị hộp thông báo thành công với animation

    Args:
        content: Nội dung thông báo
    """
    st.markdown(f"""
    <div class="success-box fade-in-up" style="
        background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #2e7d32;
        box-shadow: 0 8px 16px rgba(76, 175, 80, 0.2);
        border-left: 5px solid #4caf50;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        font-weight: 500;
    ">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 1.5rem; margin-right: 0.75rem;">✅</span>
            <div>{content}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def info_box(content: str):
    """Hiển thị hộp thông tin với style mới

    Args:
        content: Nội dung thông tin
    """
    st.markdown(f"""
    <div class="info-box fade-in-up" style="
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #1565c0;
        box-shadow: 0 8px 16px rgba(33, 150, 243, 0.2);
        border-left: 5px solid #2196f3;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        font-weight: 500;
    ">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 1.5rem; margin-right: 0.75rem;">💡</span>
            <div>{content}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def error_box(content: str):
    """Hiển thị hộp thông báo lỗi với animation

    Args:
        content: Nội dung lỗi
    """
    st.markdown(f"""
    <div class="error-box fade-in-up" style="
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #c62828;
        box-shadow: 0 8px 16px rgba(244, 67, 54, 0.2);
        border-left: 5px solid #f44336;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        font-weight: 500;
    ">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 1.5rem; margin-right: 0.75rem;">❌</span>
            <div>{content}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def file_stats_display(stats: Dict[str, Any]):
    """Hiển thị thống kê của file với design mới

    Args:
        stats: Dict chứa các thống kê
    """
    st.markdown(f"""
    <div class="file-stats fade-in-up" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 2rem;
    ">
        <div class="stat-item" style="
            background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
            border-radius: 15px;
            padding: 1.5rem;
            flex: 1;
            min-width: 120px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(255, 152, 0, 0.2);
            transition: all 0.3s ease;
            border: 1px solid #ffcc02;
        ">
            <div style="
                font-size: 0.9rem;
                color: #e65100;
                margin-bottom: 0.5rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            ">📝 Số từ</div>
            <div style="
                font-weight: 700;
                color: #bf360c;
                font-size: 2rem;
            ">{stats.get("word_count", 0):,}</div>
        </div>
        <div class="stat-item" style="
            background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
            border-radius: 15px;
            padding: 1.5rem;
            flex: 1;
            min-width: 120px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(156, 39, 176, 0.2);
            transition: all 0.3s ease;
            border: 1px solid #ab47bc;
        ">
            <div style="
                font-size: 0.9rem;
                color: #6a1b9a;
                margin-bottom: 0.5rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            ">📄 Số câu</div>
            <div style="
                font-weight: 700;
                color: #4a148c;
                font-size: 2rem;
            ">{stats.get("sentence_count", 0):,}</div>
        </div>
        <div class="stat-item" style="
            background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
            border-radius: 15px;
            padding: 1.5rem;
            flex: 1;
            min-width: 120px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(76, 175, 80, 0.2);
            transition: all 0.3s ease;
            border: 1px solid #66bb6a;
        ">
            <div style="
                font-size: 0.9rem;
                color: #2e7d32;
                margin-bottom: 0.5rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            ">📋 Số đoạn</div>
            <div style="
                font-weight: 700;
                color: #1b5e20;
                font-size: 2rem;
            ">{stats.get("paragraph_count", 0):,}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def qa_result(question: str, answer: str, confidence: Optional[float] = None):
    """Hiển thị kết quả hỏi đáp với design mới

    Args:
        question: Câu hỏi
        answer: Câu trả lời
        confidence: Điểm tin cậy (0-1)
    """
    # Main Q&A container
    st.markdown(f"""
    <div class="qa-container fade-in-up" style="
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid #e0e0e0;
        color: #424242;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    ">
        <div style="
            font-weight: 600;
            color: #1565c0;
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
        ">
            <span style="font-size: 1.5rem; margin-right: 0.75rem;">🙋‍♂️</span>
            {question}
        </div>
        <div style="
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 4px solid #667eea;
            color: #2c3e50;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            line-height: 1.7;
            font-size: 1.1rem;
            display: flex;
            align-items: flex-start;
        ">
            <span style="font-size: 1.5rem; margin-right: 0.75rem; margin-top: 0.1rem;">🤖</span>
            <div>{answer}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Separate confidence display if available
    if confidence is not None:
        confidence_percent = int(confidence * 100)
        confidence_color = "#4caf50" if confidence_percent >= 80 else "#ff9800" if confidence_percent >= 60 else "#f44336"
        
        st.markdown(f"""
        <div style="
            font-size: 0.95rem;
            color: {confidence_color};
            text-align: right;
            margin-top: -1rem;
            margin-bottom: 2rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: flex-end;
        ">
            <span style="margin-right: 0.5rem;">🎯</span>
            Độ tin cậy: {confidence_percent}%
        </div>
        """, unsafe_allow_html=True)

def progress_steps(steps: List[Dict[str, str]], current_step: int):
    """Hiển thị tiến trình xử lý theo bước với animation

    Args:
        steps: Danh sách các bước
        current_step: Bước hiện tại (0-based index)
    """
    # Simplified version to avoid HTML rendering issues
    cols = st.columns(len(steps))
    
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            is_active = i <= current_step
            is_complete = i < current_step
            
            # Icon selection
            if is_complete:
                icon = "✅"
                status_text = "Hoàn thành"
                color = "#4caf50"
            elif is_active:
                icon = "🚀"
                status_text = "Đang thực hiện"
                color = "#667eea"
            else:
                icon = "⏳"
                status_text = "Chờ xử lý"
                color = "#9e9e9e"
            
            # Display step
            st.markdown(f"""
            <div style="
                text-align: center;
                padding: 1rem;
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                border-radius: 15px;
                margin-bottom: 1rem;
                border: 2px solid {color};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="font-weight: 700; color: {color}; margin-bottom: 0.5rem;">{step['name']}</div>
                <div style="font-size: 0.8rem; color: #666; margin-bottom: 0.5rem;">{status_text}</div>
                <div style="font-size: 0.9rem; color: #777;">{step['description']}</div>
            </div>
            """, unsafe_allow_html=True)

def custom_metric(label: str, value: str, delta: Optional[str] = None, delta_color: str = "normal"):
    """Hiển thị metric tùy chỉnh

    Args:
        label: Nhãn của metric
        value: Giá trị
        delta: Thay đổi (optional)
        delta_color: Màu của delta
    """
    delta_html = ""
    if delta:
        color_map = {
            "normal": "#666",
            "inverse": "#666", 
            "off": "#666"
        }
        delta_html = f'<div style="color: {color_map.get(delta_color, "#666")}; font-size: 0.8rem;">{delta}</div>'
    
    st.markdown(f"""
    <div class="custom-metric fade-in-up" style="
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #e3f2fd;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    ">
        <div style="font-size: 0.9rem; color: #7b1fa2; font-weight: 600; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.5px;">{label}</div>
        <div style="font-size: 2rem; font-weight: 700; color: #1565c0; margin-bottom: 0.25rem;">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def enhanced_sidebar_info():
    """Hiển thị thông tin sidebar với design mới"""
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
    ">
        <div style="
            color: white;
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            line-height: 1.6;
        ">
            🚀 <strong>AI Document Analyzer</strong><br>
            <span style="font-size: 0.9rem; opacity: 0.9;">
            Phân tích tài liệu thông minh với AI
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
