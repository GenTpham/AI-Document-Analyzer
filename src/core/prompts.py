from langchain_core.prompts import PromptTemplate
"""Module chứa các prompt template cho các chức năng AI"""

from langchain_core.prompts import PromptTemplate

# Prompt cho chức năng tóm tắt
SUMMARIZATION_PROMPT = PromptTemplate.from_template("""
Hãy tóm tắt văn bản sau một cách {length}. 
Tóm tắt cần nắm bắt được ý chính, thông tin quan trọng và cấu trúc của văn bản gốc.
Đảm bảo tóm tắt có tính liên kết, mạch lạc và dễ hiểu.

Văn bản:
{text}

Tóm tắt:
""")

# Prompt cho chức năng hỏi đáp nâng cao
QA_PROMPT = PromptTemplate.from_template("""
Dựa vào đoạn văn bản dưới đây, hãy trả lời câu hỏi một cách chính xác và đầy đủ.
Nếu không thể trả lời được từ thông tin trong văn bản, hãy nói rõ rằng không có đủ thông tin.

Văn bản:
{context}

Câu hỏi: {question}

Trả lời:
""")

# Prompt cho phân tích tài liệu
DOCUMENT_ANALYSIS_PROMPT = PromptTemplate.from_template("""
Hãy phân tích tài liệu sau và cung cấp thông tin chi tiết về:
1. Chủ đề chính
2. Các ý chính được trình bày
3. Thông tin quan trọng và dữ liệu
4. Kết luận hoặc đề xuất (nếu có)

Tài liệu:
{document}

Phân tích:
""")

# Prompt cho việc trích xuất từ khóa
KEYWORDS_EXTRACTION_PROMPT = PromptTemplate.from_template("""
Hãy trích xuất 5-10 từ khóa hoặc cụm từ quan trọng nhất từ văn bản sau.
Sắp xếp các từ khóa theo thứ tự quan trọng giảm dần.

Văn bản:
{text}

Từ khóa:
""")
# Prompt cho tóm tắt văn bản
summary_prompt = PromptTemplate.from_template(
    "Summarize the following text in a {length} way:\n\n{text}"
)

# Prompt cho hỏi đáp nếu bạn muốn tùy biến thêm trong tương lai
qa_prompt = PromptTemplate.from_template(
    "Given the context below, answer the question as accurately as possible.\n\nContext:\n{context}\n\nQuestion:\n{question}"
)
