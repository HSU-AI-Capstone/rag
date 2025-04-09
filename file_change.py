import os
import subprocess
from pdf2image import convert_from_path

def convert_ppt_to_images(pptx_file, pdf_file, output_dir):
    """PPTX 파일을 PDF로 변환한 후 슬라이드별 이미지를 저장하는 함수"""

    # 출력 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)

    # 1. PPTX → PDF 변환 (LibreOffice CLI 사용)
    cmd = f'soffice --headless --invisible --convert-to pdf --outdir "{os.path.dirname(pdf_file)}" "{pptx_file}"'
    subprocess.run(cmd, shell=True)

    # 2. PDF → 이미지 변환
    images = convert_from_path(pdf_file)

    # 3. 이미지 저장
    image_paths = []
    for i, image in enumerate(images):
        img_path = os.path.join(output_dir, f'slide_{i+1:03d}.png')
        image.save(img_path, 'PNG')
        image_paths.append(img_path)

    return image_paths


# === 사용 예시 ===
pptx_file = os.path.abspath("presentation.pptx")
pdf_file = os.path.abspath("presentation.pdf")
output_dir = os.path.abspath("slides")

convert_ppt_to_images(pptx_file, pdf_file, output_dir)