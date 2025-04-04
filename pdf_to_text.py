import os
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def remove_specific_lines(text, filename):
    # 필요에 따라 특정 줄 제거 (예시: 파일명 포함된 줄 삭제)
    lines = text.splitlines()
    filtered_lines = [line for line in lines if filename not in line]
    return "\n".join(filtered_lines)

def remove_patterns(text):
    # 정규표현식 기반으로 패턴 제거 (예: 날짜, 페이지 번호 등)
    import re
    text = re.sub(r"Page \d+", "", text)  # 예시: "Page 1", "Page 2" 제거
    return text

def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def convert_local_pdfs_to_txt():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for file in os.listdir(current_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(current_dir, file)
            filename = os.path.splitext(file)[0]

            # 텍스트 추출 및 전처리
            text = extract_text_from_pdf(pdf_path)
            text = remove_specific_lines(text, filename)
            text = remove_patterns(text)

            # txt 파일로 저장
            txt_path = os.path.join(current_dir, filename + ".txt")
            save_text_to_file(text, txt_path)

            print(f"Converted {file} → {filename}.txt")

convert_local_pdfs_to_txt()
