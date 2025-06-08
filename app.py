"""Ứng dụng AI Document Analyzer sử dụng Streamlit"""

import streamlit as st
import time
import logging
import re
import os
from datetime import datetime

from src.utils.file_loader import load_file
from src.utils.web_scraper import scrape_url
from src.core.summarizer import summarize
from src.core.qa import answer_question
from src.ui.layout import render_layout
from src.ui.components import (
    display_logo, info_card, success_box, info_box, error_box,
    file_stats_display, qa_result, progress_steps, enhanced_sidebar_info, custom_metric
)
from src.config import APP_CONFIG

# Thiết lập logging
logger = logging.getLogger(__name__)

# Cấu hình trang
st.set_page_config(
    page_title=APP_CONFIG["name"],
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Áp dụng CSS tùy chỉnh
render_layout()

# Khởi tạo session state
if 'text' not in st.session_state:
    st.session_state.text = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'file_name' not in st.session_state:
    st.session_state.file_name = ""
if 'processing_complete' not in st.session_state:
    st.session_state.processing_complete = False
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# Sidebar với logo và thông tin
with st.sidebar:
    display_logo(width=180)
    st.markdown("---")

    # Sử dụng component mới cho thông tin app
    enhanced_sidebar_info()

    # Input loại dữ liệu với styling mới
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
    ">
        <h3 style="color: white; margin-bottom: 1rem; text-align: center;">📌 Nguồn dữ liệu</h3>
    </div>
    """, unsafe_allow_html=True)
    
    input_type = st.radio(
        "Chọn nguồn dữ liệu",
        options=["Tải lên tài liệu", "Nhập URL Website", "Nhập văn bản trực tiếp"],
        index=0,
        key="input_type_radio",
        label_visibility="collapsed"
    )

    # Thông tin về dữ liệu hiện tại với styling mới
    if st.session_state.text:
        st.markdown("""
        <div style="
            background: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        ">
            <h3 style="color: white; margin-bottom: 1rem; text-align: center;">📊 Thông tin tài liệu</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Sử dụng custom metrics
        # Tính toán stats
        word_count = len(st.session_state.text.split())
        char_count = len(st.session_state.text)
        
        # Hiển thị metrics trong sidebar
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            color: white;
        ">
            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.5rem;">📄 Nguồn</div>
            <div style="font-weight: 600; word-break: break-word;">{st.session_state.file_name}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            color: white;
            text-align: center;
        ">
            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.5rem;">📝 Số từ</div>
            <div style="font-weight: 700; font-size: 1.5rem;">{word_count:,}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            color: white;
            text-align: center;
        ">
            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.5rem;">📊 Ký tự</div>
            <div style="font-weight: 700; font-size: 1.5rem;">{char_count:,}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.start_time:
            elapsed_time = time.time() - st.session_state.start_time
            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 1rem;
                margin-bottom: 1rem;
                color: white;
                text-align: center;
            ">
                <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.5rem;">⏱️ Thời gian</div>
                <div style="font-weight: 700; font-size: 1.5rem;">{elapsed_time:.1f}s</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Footer với styling mới
    st.markdown(f"""
    <div style="
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        color: white;
        margin-top: 2rem;
    ">
        <div style="font-size: 0.9rem; margin-bottom: 0.5rem;">
            <strong>Phiên bản:</strong> {APP_CONFIG['version']}
        </div>
        <div style="font-size: 0.8rem; opacity: 0.8;">
            © {datetime.now().year} {APP_CONFIG['name']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phần chính
st.markdown("<h1 class='main-title'>📄 AI Document Analyzer</h1>", unsafe_allow_html=True)

# Hiển thị các bước xử lý
process_steps = [
    {"name": "Nhập dữ liệu", "description": "Tải lên tài liệu hoặc nhập URL/văn bản"},
    {"name": "Tóm tắt", "description": "AI phân tích và tóm tắt nội dung"},
    {"name": "Hỏi đáp", "description": "Đặt câu hỏi về nội dung"}
]

progress_steps(process_steps, st.session_state.current_step)

# Container chính
main_container = st.container()
with main_container:
    # Tạo tabs
    input_tab, summary_tab, qa_tab = st.tabs(["📤 Nhập dữ liệu", "📝 Tóm tắt", "❓ Hỏi đáp"])

    # Tab nhập dữ liệu
    with input_tab:
        st.markdown("<h2>Nhập dữ liệu</h2>", unsafe_allow_html=True)

        col1, col2 = st.columns([3, 1])

        with col1:
            # Logic xử lý input dựa trên loại đã chọn
            if input_type == "Tải lên tài liệu":
                st.markdown("<h3>Tải lên tài liệu</h3>", unsafe_allow_html=True)
                info_box("Hỗ trợ file <strong>PDF</strong> và <strong>Word (.docx)</strong> với kích thước tối đa 50MB.")

                file = st.file_uploader("Chọn file", type=["pdf", "docx"], key="file_uploader")

                if file:
                    st.session_state.file_name = file.name

                    if st.button("Xử lý tài liệu", key="process_file", use_container_width=True):
                        st.session_state.start_time = time.time()
                        with st.spinner("Đang xử lý tài liệu..."):
                            # Hiển thị tiến trình xử lý
                            progress_bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.02)
                                progress_bar.progress(i + 1)

                            st.session_state.text = load_file(file)
                            if st.session_state.text and not st.session_state.text.startswith("Lỗi"):
                                st.session_state.current_step = 1  # Cập nhật bước
                                success_box(f"✅ Đã xử lý thành công: <strong>{file.name}</strong>")
                                st.balloons()
                            else:
                                error_box(f"❌ {st.session_state.text}")

            elif input_type == "Nhập URL Website":
                st.markdown("<h3>Phân tích Website</h3>", unsafe_allow_html=True)
                info_box("Nhập URL website để trích xuất và phân tích nội dung.")

                url = st.text_input("Nhập URL website", placeholder="https://example.com", key="url_input")

                if url:
                    if st.button("Trích xuất nội dung", key="extract_url", use_container_width=True):
                        st.session_state.start_time = time.time()
                        with st.spinner("Đang trích xuất nội dung từ website..."):
                            # Hiển thị tiến trình xử lý
                            progress_bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.01)
                                progress_bar.progress(i + 1)

                            st.session_state.text = scrape_url(url)
                            st.session_state.file_name = url

                            if st.session_state.text and not st.session_state.text.startswith("Lỗi"):
                                st.session_state.current_step = 1  # Cập nhật bước
                                success_box(f"✅ Đã trích xuất thành công từ: <strong>{url}</strong>")
                            else:
                                error_box(f"❌ {st.session_state.text}")

            elif input_type == "Nhập văn bản trực tiếp":
                st.markdown("<h3>Nhập văn bản</h3>", unsafe_allow_html=True)
                info_box("Nhập hoặc dán văn bản cần phân tích vào khung bên dưới.")

                text_input = st.text_area(
                    "Văn bản cần phân tích",
                    height=300,
                    placeholder="Dán nội dung văn bản vào đây...",
                    key="direct_text_input"
                )

                if text_input:
                    if st.button("Sử dụng văn bản này", key="use_text", use_container_width=True):
                        st.session_state.start_time = time.time()
                        st.session_state.text = text_input
                        st.session_state.file_name = "Văn bản nhập trực tiếp"
                        st.session_state.current_step = 1  # Cập nhật bước
                        success_box("✅ Đã nhận văn bản!")

        with col2:
            st.markdown("<h3>Xem trước</h3>", unsafe_allow_html=True)
            if st.session_state.text:
                # Hiển thị mẫu văn bản
                st.markdown("**Mẫu nội dung:**")
                st.markdown("""
                <div class="preview-container">
                {}
                </div>
                """.format(st.session_state.text[:1000] + "..." if len(st.session_state.text) > 1000 else st.session_state.text), 
                unsafe_allow_html=True)
            else:
                info_box("Chưa có nội dung. Vui lòng nhập dữ liệu từ một trong các nguồn bên trái.")

    # Tab tóm tắt
    with summary_tab:
        st.markdown("""
        <div class="fade-in-up">
            <h2 style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 1.5rem;
                text-align: center;
            ">📝 Tóm tắt nội dung</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.text:
            col1, col2 = st.columns([3, 1])

            with col1:
                # Enhanced styling cho cài đặt tóm tắt
                st.markdown("""
                <div class="card fade-in-up" style="
                    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                    border-radius: 20px;
                    padding: 2rem;
                    border: 1px solid #e3f2fd;
                    margin-bottom: 2rem;
                    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
                ">
                    <h3 style="
                        color: #1565c0;
                        font-weight: 700;
                        margin-bottom: 1.5rem;
                        display: flex;
                        align-items: center;
                    ">
                        <span style="margin-right: 0.75rem; font-size: 1.5rem;">⚙️</span>
                        Cài đặt tóm tắt
                    </h3>
                </div>
                """, unsafe_allow_html=True)

                length_options = {
                    "short": "Ngắn gọn (chỉ điểm chính)",
                    "medium": "Trung bình (cân đối)",
                    "long": "Chi tiết (đầy đủ thông tin)"
                }

                length = st.select_slider(
                    "Độ dài tóm tắt",
                    options=list(length_options.keys()),
                    value="medium",
                    format_func=lambda x: length_options[x]
                )

                info_card(
                    "Hướng dẫn chọn độ dài",
                    "✨ <strong>Ngắn gọn:</strong> ~50 từ - Chỉ ý chính<br>🎯 <strong>Trung bình:</strong> ~150 từ - Cân đối chi tiết<br>📖 <strong>Chi tiết:</strong> ~300 từ - Đầy đủ thông tin",
                    icon="📏"
                )

                if st.button("🚀 Tạo bản tóm tắt", key="generate_summary", use_container_width=True):
                    st.session_state.start_time = time.time()
                    with st.spinner("🤖 AI đang phân tích và tóm tắt nội dung..."):
                        # Enhanced progress bar
                        progress_container = st.container()
                        with progress_container:
                            progress_text = st.empty()
                            progress_bar = st.progress(0)
                            
                            steps = ["Phân tích văn bản...", "Trích xuất ý chính...", "Tạo bản tóm tắt...", "Hoàn thành!"]
                            
                            for i in range(100):
                                step_index = min(i // 25, len(steps) - 1)
                                progress_text.markdown(f"**{steps[step_index]}** ({i+1}%)")
                                time.sleep(0.03)
                                progress_bar.progress(i + 1)

                        st.session_state.summary = summarize(st.session_state.text, length)
                        st.session_state.summary_length = length
                        st.session_state.current_step = 2  # Cập nhật bước
                        st.success("🎉 Tóm tắt hoàn thành!")
                        st.balloons()

            with col2:
                # Enhanced info panel
                st.markdown("""
                <div class="card fade-in-up" style="
                    background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
                    border-radius: 20px;
                    padding: 2rem;
                    border: 1px solid #66bb6a;
                    margin-bottom: 2rem;
                    box-shadow: 0 12px 24px rgba(76, 175, 80, 0.2);
                ">
                    <h3 style="
                        color: #1b5e20;
                        font-weight: 700;
                        margin-bottom: 1.5rem;
                        display: flex;
                        align-items: center;
                    ">
                        <span style="margin-right: 0.75rem; font-size: 1.5rem;">📊</span>
                        Thông tin
                    </h3>
                </div>
                """, unsafe_allow_html=True)
                
                if 'summary_length' in st.session_state:
                    # Display current settings
                    st.markdown(f"""
                    <div style="
                        background: rgba(255, 255, 255, 0.8);
                        border-radius: 12px;
                        padding: 1rem;
                        margin-bottom: 1rem;
                        border: 1px solid #c8e6c9;
                    ">
                        <div style="font-size: 0.9rem; color: #2e7d32; margin-bottom: 0.5rem; font-weight: 600;">🎚️ Cấp độ</div>
                        <div style="color: #1b5e20; font-weight: 700;">{length_options[st.session_state.summary_length]}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.session_state.summary:
                        words_count = len(st.session_state.summary.split())
                        compression_ratio = 1 - (words_count / len(st.session_state.text.split()))
                        
                        st.markdown(f"""
                        <div style="
                            background: rgba(255, 255, 255, 0.8);
                            border-radius: 12px;
                            padding: 1rem;
                            margin-bottom: 1rem;
                            border: 1px solid #c8e6c9;
                        ">
                            <div style="font-size: 0.9rem; color: #2e7d32; margin-bottom: 0.5rem; font-weight: 600;">📝 Số từ</div>
                            <div style="color: #1b5e20; font-weight: 700; font-size: 1.3rem;">{words_count:,}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                        <div style="
                            background: rgba(255, 255, 255, 0.8);
                            border-radius: 12px;
                            padding: 1rem;
                            margin-bottom: 1rem;
                            border: 1px solid #c8e6c9;
                        ">
                            <div style="font-size: 0.9rem; color: #2e7d32; margin-bottom: 0.5rem; font-weight: 600;">🗜️ Tỷ lệ nén</div>
                            <div style="color: #1b5e20; font-weight: 700; font-size: 1.3rem;">{compression_ratio:.1%}</div>
                        </div>
                        """, unsafe_allow_html=True)

            # Hiển thị kết quả tóm tắt với enhanced styling
            if st.session_state.summary:
                st.markdown("""
                <div class="fade-in-up">
                    <h3 style="
                        color: #1565c0;
                        font-weight: 700;
                        margin: 2rem 0 1rem 0;
                        display: flex;
                        align-items: center;
                    ">
                        <span style="margin-right: 0.75rem; font-size: 1.5rem;">✨</span>
                        Kết quả tóm tắt
                    </h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Enhanced result display
                st.markdown(f"""
                <div class="fade-in-up" style="
                    background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
                    border-radius: 20px;
                    padding: 2rem;
                    border: 1px solid #66bb6a;
                    margin-bottom: 2rem;
                    box-shadow: 0 12px 24px rgba(76, 175, 80, 0.2);
                ">
                    <div style="
                        background: white;
                        border-radius: 15px;
                        padding: 1.5rem;
                        line-height: 1.8;
                        font-size: 1.1rem;
                        color: #2c3e50;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    ">
                        {st.session_state.summary}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Enhanced download section
                col1, col2, col3 = st.columns([1, 1, 2])
                with col1:
                    st.download_button(
                        label="📥 Tải TXT",
                        data=st.session_state.summary,
                        file_name=f"tomtat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                with col2:
                    # Option to copy to clipboard
                    if st.button("📋 Sao chép", use_container_width=True):
                        st.success("✅ Đã sao chép vào clipboard!")
        else:
            error_box("⚠️ Vui lòng nhập dữ liệu ở tab 'Nhập dữ liệu' trước khi tóm tắt.")

    # Tab hỏi đáp với enhanced styling
    with qa_tab:
        st.markdown("""
        <div class="fade-in-up">
            <h2 style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 1.5rem;
                text-align: center;
            ">❓ Hỏi đáp thông minh</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.summary:
            # Enhanced question input section
            st.markdown("""
            <div class="card fade-in-up" style="
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                border-radius: 20px;
                padding: 2rem;
                border: 1px solid #e3f2fd;
                margin-bottom: 2rem;
                box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
            ">
                <h3 style="
                    color: #1565c0;
                    font-weight: 700;
                    margin-bottom: 1.5rem;
                    display: flex;
                    align-items: center;
                ">
                    <span style="margin-right: 0.75rem; font-size: 1.5rem;">🗣️</span>
                    Đặt câu hỏi về nội dung
                </h3>
            </div>
            """, unsafe_allow_html=True)

            # Hiển thị nội dung tóm tắt với enhanced styling
            with st.expander("📖 Xem lại bản tóm tắt", expanded=False):
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                    border-radius: 15px;
                    padding: 1.5rem;
                    line-height: 1.7;
                    color: #2c3e50;
                ">
                    {st.session_state.summary}
                </div>
                """, unsafe_allow_html=True)

            # Enhanced suggestion buttons
            st.markdown("**💡 Câu hỏi gợi ý:**")
            suggestion_cols = st.columns(3)
            suggested_questions = [
                "Ý chính của bài viết là gì?",
                "Điểm quan trọng nhất được đề cập?",
                "Tác giả kết luận điều gì?"
            ]

            # Hiển thị các gợi ý câu hỏi với enhanced styling
            for i, (col, question) in enumerate(zip(suggestion_cols, suggested_questions)):
                with col:
                    if st.button(
                        question, 
                        key=f"suggested_q_{i}", 
                        help="Nhấn để sử dụng câu hỏi gợi ý này",
                        use_container_width=True
                    ):
                        st.session_state.question = question

            # Enhanced question input
            question = st.text_input(
                "💬 Nhập câu hỏi của bạn", 
                value=st.session_state.get("question", ""),
                placeholder="Ví dụ: Ý chính của bài viết là gì?",
                key="qa_input"
            )

            if question:
                if st.button("🔍 Tìm câu trả lời", key="answer_question", use_container_width=True):
                    with st.spinner("🤖 AI đang tìm câu trả lời..."):
                        # Enhanced progress with steps
                        progress_container = st.container()
                        with progress_container:
                            progress_text = st.empty()
                            progress_bar = st.progress(0)
                            
                            steps = ["Phân tích câu hỏi...", "Tìm kiếm thông tin...", "Tạo câu trả lời...", "Hoàn thành!"]
                            
                            for i in range(100):
                                step_index = min(i // 25, len(steps) - 1)
                                progress_text.markdown(f"**{steps[step_index]}** ({i+1}%)")
                                time.sleep(0.01)
                                progress_bar.progress(i + 1)

                        answer = answer_question(question, st.session_state.summary)

                        # Hiển thị câu trả lời với enhanced styling
                        st.markdown("""
                        <div class="fade-in-up">
                            <h3 style="
                                color: #1565c0;
                                font-weight: 700;
                                margin: 2rem 0 1rem 0;
                                display: flex;
                                align-items: center;
                            ">
                                <span style="margin-right: 0.75rem; font-size: 1.5rem;">💡</span>
                                Câu trả lời
                            </h3>
                        </div>
                        """, unsafe_allow_html=True)

                        if isinstance(answer, dict) and 'answer' in answer:
                            qa_result(
                                question=question,
                                answer=answer['answer'],
                                confidence=answer.get('score', None)
                            )
                            st.success("✅ Tìm thấy câu trả lời!")
                        else:
                            error_box(f"❌ Lỗi: {answer}" if isinstance(answer, str) else "Không thể xử lý câu hỏi.")
        else:
            error_box("⚠️ Vui lòng tạo bản tóm tắt trước khi sử dụng chức năng hỏi đáp.")

# Enhanced Footer
st.markdown("---")
st.markdown("""
<div class="fade-in-up" style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    color: white;
    box-shadow: 0 12px 24px rgba(102, 126, 234, 0.3);
">
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 1rem;">
        <span style="font-size: 2rem; margin-right: 1rem;">🚀</span>
        <h3 style="margin: 0; font-weight: 700;">AI Document Analyzer</h3>
    </div>
    <p style="
        margin-bottom: 1rem;
        font-size: 1.1rem;
        opacity: 0.9;
        line-height: 1.6;
    ">
        Phân tích tài liệu thông minh với công nghệ AI tiên tiến
    </p>
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 2rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        opacity: 0.8;
    ">
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 0.5rem;">🤖</span>
            <span>Powered by Transformers</span>
        </div>
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 0.5rem;">⚡</span>
            <span>Fast & Accurate</span>
        </div>
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 0.5rem;">🔐</span>
            <span>Secure & Private</span>
        </div>
    </div>
    <div style="
        font-size: 0.85rem;
        opacity: 0.7;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        padding-top: 1rem;
    ">
        © AI Document Analyzer Team | Sử dụng công nghệ Transformer & LangChain
    </div>
</div>
""", unsafe_allow_html=True)
