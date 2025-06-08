<div align="center">

# 🚀 AI Document Analyzer

*Ứng dụng phân tích tài liệu thông minh với công nghệ AI tiên tiến*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[📖 Demo](#-demo) • [✨ Tính năng](#-tính-năng-chính) • [🚀 Cài đặt](#-cài-đặt-nhanh) • [📱 Sử dụng](#-hướng-dẫn-sử-dụng) • [🤝 Đóng góp](#-đóng-góp)

---

</div>

## 📖 Giới thiệu

**AI Document Analyzer** là một ứng dụng web hiện đại được xây dựng để giúp bạn phân tích, tóm tắt và tương tác với các tài liệu một cách thông minh. Sử dụng các mô hình AI tiên tiến, ứng dụng có thể xử lý nhiều loại định dạng tài liệu và cung cấp thông tin chính xác, hữu ích.

### 🎯 Tại sao chọn AI Document Analyzer?

- ⚡ **Xử lý nhanh**: Phân tích tài liệu lớn trong vài giây
- 🎨 **Giao diện hiện đại**: Thiết kế đẹp mắt, dễ sử dụng
- 🤖 **AI thông minh**: Sử dụng mô hình ngôn ngữ tiên tiến
- 📱 **Responsive**: Hoạt động tốt trên mọi thiết bị
- 🔒 **Bảo mật**: Xử lý tài liệu cục bộ, không lưu trữ

## ✨ Tính năng chính

<table>
<tr>
<td width="50%">

### 📝 Tóm tắt thông minh
- **3 mức độ tóm tắt**: Ngắn gọn, Cân đối, Chi tiết
- **Xử lý văn bản lớn**: Tự động chia nhỏ và tổng hợp
- **Tải xuống kết quả**: Định dạng TXT
- **Thống kê chi tiết**: Số từ, tỷ lệ nén

</td>
<td width="50%">

### ❓ Hỏi đáp thông minh
- **Gợi ý câu hỏi**: Câu hỏi mẫu để bắt đầu
- **Độ tin cậy**: Hiển thị mức độ chính xác
- **Phản hồi nhanh**: Trả lời trong vài giây
- **Ngữ cảnh**: Hiểu rõ nội dung tài liệu

</td>
</tr>
<tr>
<td width="50%">

### 📄 Hỗ trợ đa định dạng
- **PDF Files**: Trích xuất text từ PDF
- **Word Documents**: Đọc file .docx
- **Website URLs**: Crawl nội dung web
- **Text Input**: Nhập trực tiếp văn bản

</td>
<td width="50%">

### 🎨 Giao diện hiện đại
- **Gradient Design**: Màu sắc chuyên nghiệp
- **Animations**: Hiệu ứng mượt mà
- **Progress Tracking**: Theo dõi tiến trình
- **Mobile Friendly**: Responsive design

</td>
</tr>
</table>

## 🚀 Cài đặt nhanh

### 📋 Yêu cầu hệ thống

- **Python**: 3.8 hoặc cao hơn
- **RAM**: Tối thiểu 4GB (khuyến nghị 8GB)
- **Disk**: 500MB trống

### ⚡ Cài đặt một lệnh

```bash
# Clone repository
git clone https://github.com/yourusername/ai-document-analyzer.git
cd ai-document-analyzer

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py
```

### 🐳 Docker (Tùy chọn)

```bash
# Build image
docker build -t ai-document-analyzer .

# Run container
docker run -p 8501:8501 ai-document-analyzer
```

## 📱 Hướng dẫn sử dụng

### 1️⃣ Nhập dữ liệu

<table>
<tr>
<td width="33%">
<h4>📄 Upload File</h4>
<ul>
<li>Chọn file PDF/Word</li>
<li>Tối đa 50MB</li>
<li>Drag & drop hỗ trợ</li>
</ul>
</td>
<td width="33%">
<h4>🌐 Website URL</h4>
<ul>
<li>Nhập URL hợp lệ</li>
<li>Tự động crawl content</li>
<li>Hỗ trợ các trang tin tức</li>
</ul>
</td>
<td width="33%">
<h4>✏️ Text Input</h4>
<ul>
<li>Dán văn bản trực tiếp</li>
<li>Không giới hạn độ dài</li>
<li>Copy từ clipboard</li>
</ul>
</td>
</tr>
</table>

### 2️⃣ Tóm tắt văn bản

1. **Chọn độ dài**: Ngắn gọn (~50 từ) | Cân đối (~150 từ) | Chi tiết (~300 từ)
2. **Nhấn "Tạo bản tóm tắt"** 
3. **Xem kết quả** với thống kê chi tiết
4. **Tải xuống** file TXT nếu cần

### 3️⃣ Hỏi đáp

1. **Sử dụng câu hỏi gợi ý** hoặc nhập câu hỏi tùy chỉnh
2. **Nhấn "Tìm câu trả lời"**
3. **Xem kết quả** với độ tin cậy được hiển thị

## 🏗️ Cấu trúc dự án

```
ai-document-analyzer/
├── 📱 app.py                    # Ứng dụng chính Streamlit
├── 📦 requirements.txt          # Dependencies Python
├── 📁 src/                      # Source code chính
│   ├── 🧠 core/                 # Logic xử lý AI
│   │   ├── summarizer.py        # Module tóm tắt
│   │   └── qa.py                # Module hỏi đáp
│   ├── 🎨 ui/                   # Giao diện người dùng
│   │   ├── layout.py            # CSS và styling
│   │   ├── components.py        # UI components
│   │   └── visualization.py     # Charts và graphs
│   ├── 🛠️ utils/                # Tiện ích hỗ trợ
│   │   ├── file_loader.py       # Đọc file PDF/Word
│   │   └── web_scraper.py       # Crawl web content
│   └── ⚙️ config.py             # Cấu hình ứng dụng
├── 📊 data/                     # Thư mục dữ liệu (tùy chọn)
├── 📝 docs/                     # Tài liệu hướng dẫn
└── 🧪 tests/                    # Unit tests
```

## 🛠️ Công nghệ sử dụng

<div align="center">

### Frontend & UI
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

### Backend & AI
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Transformers](https://img.shields.io/badge/🤗_Transformers-FFCA28?style=for-the-badge)](https://huggingface.co/transformers/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-121212?style=for-the-badge)](https://langchain.com/)

### Data Processing
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful_Soup-59666C?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)

</div>

## 🎯 Roadmap

- [ ] 🌍 **Đa ngôn ngữ**: Hỗ trợ tiếng Anh, Trung, Nhật
- [ ] 📊 **Export formats**: PDF, Word, Excel
- [ ] 🔍 **Advanced search**: Tìm kiếm trong tài liệu
- [ ] 📈 **Analytics**: Dashboard thống kê sử dụng
- [ ] 🤖 **Custom models**: Tích hợp mô hình riêng
- [ ] 🔄 **Batch processing**: Xử lý nhiều file cùng lúc

## 🤝 Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp! 

### 🔥 Cách đóng góp

1. **Fork** repo này
2. **Create** feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** Pull Request

### 🐛 Báo lỗi

Nếu bạn tìm thấy bug, vui lòng [tạo issue](https://github.com/yourusername/ai-document-analyzer/issues) với:
- Mô tả chi tiết lỗi
- Các bước tái hiện
- Screenshot (nếu có)
- Thông tin môi trường

## 📄 License

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 👨‍💻 Tác giả

<div align="center">

**Phạm Trúc**

[![Email](https://img.shields.io/badge/Email-phamtruc120604@gmail.com-red?style=for-the-badge&logo=gmail)](mailto:phamtruc120604@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)

</div>

---

<div align="center">

### ⭐ Nếu bạn thấy dự án hữu ích, hãy cho chúng tôi một star!

**[⬆ Về đầu trang](#-ai-document-analyzer)**

</div>