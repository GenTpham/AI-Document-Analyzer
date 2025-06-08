"""Module chứa các hàm tạo biểu đồ và visualization"""
"""Module cho hiển thị biểu đồ và trực quan hóa dữ liệu"""

import streamlit as st
import pandas as pd

def plot_word_frequency(text: str, top_n: int = 15):
    """Tạo biểu đồ tần suất từ sử dụng Streamlit

    Args:
        text: Văn bản cần phân tích
        top_n: Số lượng từ hiển thị
    """
    if not text or len(text) < 10:
        st.warning("Không đủ nội dung để phân tích tần suất từ.")
        return

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
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Tạo DataFrame
    df = pd.DataFrame(sorted_counts, columns=['Từ', 'Tần suất'])

    # Tạo biểu đồ sử dụng streamlit
    st.bar_chart(df.set_index('Từ'))

def plot_summary_comparison(original_text: str, summary: str):
    """Hiển thị so sánh độ dài giữa văn bản gốc và bản tóm tắt

    Args:
        original_text: Văn bản gốc
        summary: Bản tóm tắt
    """
    orig_words = len(original_text.split())
    summary_words = len(summary.split())

    # Tính tỷ lệ nén
    compression_ratio = 1 - (summary_words / orig_words)

    # Tạo dữ liệu cho biểu đồ
    data = {
        'Văn bản': ['Văn bản gốc', 'Bản tóm tắt'],
        'Số từ': [orig_words, summary_words]
    }

    df = pd.DataFrame(data)

    # Hiển thị biểu đồ
    st.bar_chart(df.set_index('Văn bản'))

    # Hiển thị thông tin
    st.markdown(f"**Tỷ lệ nén:** {compression_ratio:.1%}")
    st.markdown(f"**Số từ văn bản gốc:** {orig_words:,}")
    st.markdown(f"**Số từ bản tóm tắt:** {summary_words:,}")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from typing import List, Dict, Any, Optional

# Đặt style cho matplotlib
matplotlib.use("Agg")
plt.style.use('seaborn-v0_8-pastel')

def plot_word_frequency(text: str, top_n: int = 15):
    """Tạo biểu đồ tần suất từ

    Args:
        text: Văn bản cần phân tích
        top_n: Số lượng từ hiển thị
    """
    if not text or len(text) < 10:
        st.warning("Không đủ nội dung để phân tích tần suất từ.")
        return

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
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Tạo DataFrame
    df = pd.DataFrame(sorted_counts, columns=['Từ', 'Tần suất'])

    # Tạo biểu đồ
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(df['Từ'], df['Tần suất'], color='#2563eb')

    # Thêm số liệu trên mỗi cột
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{width}',
                ha='left', va='center', fontsize=10)

    # Thêm tiêu đề và nhãn
    ax.set_title('Top từ xuất hiện nhiều nhất', fontsize=15, pad=20)
    ax.set_xlabel('Tần suất', fontsize=12)
    ax.invert_yaxis()  # Đảo ngược trục y để từ nhiều nhất ở trên cùng

    # Tinh chỉnh
    fig.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Hiển thị trong Streamlit
    st.pyplot(fig)

def plot_summary_comparison(original_text: str, summary_text: str):
    """Tạo biểu đồ so sánh giữa văn bản gốc và bản tóm tắt

    Args:
        original_text: Văn bản gốc
        summary_text: Văn bản tóm tắt
    """
    if not original_text or not summary_text:
        st.warning("Không đủ dữ liệu để tạo biểu đồ so sánh.")
        return

    # Phân tích thống kê
    original_words = len(original_text.split())
    summary_words = len(summary_text.split())
    compression_ratio = 1 - (summary_words / original_words)

    original_sentences = len([s for s in original_text.split(".") if s.strip()])
    summary_sentences = len([s for s in summary_text.split(".") if s.strip()])

    # Tạo dữ liệu so sánh
    metrics = ['Số từ', 'Số câu']
    original_values = [original_words, original_sentences]
    summary_values = [summary_words, summary_sentences]

    # Tạo biểu đồ
    fig, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax.bar(x - width/2, original_values, width, label='Văn bản gốc', color='#3b82f6')
    bars2 = ax.bar(x + width/2, summary_values, width, label='Bản tóm tắt', color='#10b981')

    # Thêm số liệu trên mỗi cột
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:,}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10)

    # Thêm tiêu đề và nhãn
    ax.set_title('So sánh văn bản gốc và bản tóm tắt', fontsize=15, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()

    # Thêm thông tin tỷ lệ nén
    plt.figtext(0.5, 0.01, f'Tỷ lệ nén: {compression_ratio:.1%}', ha='center', fontsize=12, 
                bbox={"facecolor":"#eff6ff", "alpha":0.5, "pad":5, "boxstyle":"round"})

    # Tinh chỉnh
    fig.tight_layout(pad=3)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Hiển thị trong Streamlit
    st.pyplot(fig)

def plot_readability_radar(text_stats: Dict[str, Any]):
    """Tạo biểu đồ radar thể hiện các chỉ số về độ dễ đọc

    Args:
        text_stats: Từ điển chứa các thống kê văn bản
    """
    if not text_stats or 'readability' not in text_stats:
        st.warning("Không đủ dữ liệu để phân tích độ dễ đọc.")
        return

    # Chuẩn bị dữ liệu
    metrics = [
        'Độ dài câu',
        'Độ phức tạp',
        'Độ dài từ',
        'Số đoạn',
        'Số câu'
    ]

    # Chuẩn hóa các chỉ số
    values = [
        min(1.0, text_stats['avg_sentence_length'] / 30),  # Chuẩn hóa độ dài câu
        min(1.0, text_stats['readability']['complexity_score'] / 50),  # Chuẩn hóa độ phức tạp
        min(1.0, text_stats['avg_word_length'] / 8),  # Chuẩn hóa độ dài từ
        min(1.0, text_stats['paragraph_count'] / 50),  # Chuẩn hóa số đoạn
        min(1.0, text_stats['sentence_count'] / 200)  # Chuẩn hóa số câu
    ]

    # Tạo biểu đồ radar
    angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
    values += values[:1]  # Đóng polygon
    angles += angles[:1]  # Đóng polygon
    metrics += metrics[:1]  # Đóng polygon

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Tạo radar
    ax.plot(angles, values, 'o-', linewidth=2, color='#2563eb')
    ax.fill(angles, values, color='#2563eb', alpha=0.25)

    # Thêm nhãn
    ax.set_thetagrids(np.degrees(angles[:-1]), metrics[:-1])

    # Thêm tiêu đề
    ax.set_title('Phân tích độ dễ đọc', fontsize=15, pad=20)

    # Tinh chỉnh
    ax.grid(True)

    # Hiển thị trong Streamlit
    st.pyplot(fig)

def display_keyword_cloud(keywords: List[str]):
    """Hiển thị đám mây từ khóa

    Args:
        keywords: Danh sách các từ khóa
    """
    if not keywords or len(keywords) < 3:
        st.warning("Không đủ từ khóa để hiển thị.")
        return

    # Tạo HTML cho đám mây từ khóa
    keyword_html = """
    <div style="background-color:#f8fafc;padding:15px;border-radius:10px;text-align:center;">
    """

    colors = ['#2563eb', '#1d4ed8', '#1e40af', '#3b82f6', '#60a5fa']
    sizes = [1.8, 1.6, 1.4, 1.2, 1.0] * 10  # Để đảm bảo đủ cho tất cả từ khóa

    for i, keyword in enumerate(keywords):
        color = colors[i % len(colors)]
        size = sizes[i % len(sizes)]
        keyword_html += f'<span style="display:inline-block;margin:6px;font-size:{size}rem;color:{color};">{keyword}</span>'

    keyword_html += "</div>"

    # Hiển thị trong Streamlit
    st.markdown(keyword_html, unsafe_allow_html=True)
