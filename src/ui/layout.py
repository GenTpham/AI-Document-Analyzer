"""Module cho layout và styling của giao diện Streamlit"""

import streamlit as st

def render_layout():
    """Áp dụng CSS tùy chỉnh cho ứng dụng"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
    }
    
    .css-1d391kg .sidebar-content {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }

    /* Title Styling */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Enhanced Box Styles */
    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #1565c0;
        box-shadow: 0 8px 16px rgba(33, 150, 243, 0.2);
        border-left: 5px solid #2196f3;
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(33, 150, 243, 0.3);
    }

    .success-box {
        background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #2e7d32;
        box-shadow: 0 8px 16px rgba(76, 175, 80, 0.2);
        border-left: 5px solid #4caf50;
        transition: all 0.3s ease;
    }
    
    .success-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(76, 175, 80, 0.3);
    }

    .error-box {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: none;
        margin-bottom: 1.5rem;
        color: #c62828;
        box-shadow: 0 8px 16px rgba(244, 67, 54, 0.2);
        border-left: 5px solid #f44336;
        transition: all 0.3s ease;
    }
    
    .error-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(244, 67, 54, 0.3);
    }

    /* Q&A Container */
    .qa-container {
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid #e0e0e0;
        color: #424242;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .qa-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 16px 32px rgba(0, 0, 0, 0.15);
    }

    .qa-question {
        font-weight: 600;
        color: #1565c0;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }

    .qa-answer {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #667eea;
        color: #2c3e50;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        line-height: 1.6;
    }

    .qa-confidence {
        font-size: 0.9rem;
        color: #7b1fa2;
        text-align: right;
        margin-top: 1rem;
        font-weight: 500;
    }

    /* Enhanced Progress Steps */
    .step-container {
        display: flex;
        margin-bottom: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    .step {
        flex: 1;
        text-align: center;
        padding: 1rem 0.5rem;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .step:hover {
        transform: translateY(-2px);
    }

    .step-active {
        font-weight: 600;
        color: #667eea;
    }

    .step-inactive {
        color: #9e9e9e;
    }

    .step-number {
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        background: linear-gradient(135deg, #e0e0e0 0%, #bdbdbd 100%);
        color: #757575;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem auto;
        font-weight: 700;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .step-active .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: scale(1.1);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }

    .step-description {
        font-size: 0.9rem;
        margin-top: 0.5rem;
        line-height: 1.4;
    }

    /* Enhanced File Stats */
    .file-stats {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .stat-item {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 1.5rem;
        flex: 1;
        min-width: 120px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid #e3f2fd;
    }
    
    .stat-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }

    .stat-label {
        font-size: 0.8rem;
        color: #7b1fa2;
        margin-bottom: 0.5rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stat-value {
        font-weight: 700;
        color: #1565c0;
        font-size: 1.8rem;
    }

    /* Enhanced Card Styling */
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid #e3f2fd;
        margin-bottom: 2rem;
        color: #424242;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }

    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #e3f2fd;
    }

    .card-icon {
        font-size: 2rem;
        margin-right: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1565c0;
    }

    .card-content {
        font-size: 1rem;
        color: #546e7a;
        line-height: 1.6;
    }

    /* Enhanced Preview Container */
    .preview-container {
        height: 400px;
        overflow-y: auto;
        padding: 1.5rem;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        font-size: 0.95rem;
        border: 2px solid #e3f2fd;
        color: #37474f;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        line-height: 1.6;
    }

    /* Enhanced Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
    
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 0.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        color: #6c757d;
        font-weight: 500;
        padding: 1rem 1.5rem;
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }

    /* Animation Classes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .step-container {
            flex-direction: column;
            gap: 1rem;
        }
        
        .file-stats {
            flex-direction: column;
        }
        
        .card {
            padding: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)