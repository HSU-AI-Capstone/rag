import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def create_slide_clip(image_path, audio_path):
    """이미지 + 오디오 → 단일 비디오 클립"""
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    img_clip = ImageClip(image_path).with_duration(duration).with_audio(audio)
    return img_clip

def create_full_lecture_video(slide_dir, audio_dir, output_path):
    """여러 슬라이드 + 오디오 → 하나의 통합 영상"""
    # 파일 정렬
    slide_files = sorted([f for f in os.listdir(slide_dir) if f.lower().endswith((".png", ".jpg"))])
    audio_files = sorted([f for f in os.listdir(audio_dir) if f.lower().endswith((".mp3", ".wav", ".m4a"))])

    if len(slide_files) != len(audio_files):
        raise ValueError("슬라이드 이미지 수와 오디오 파일 수가 일치하지 않습니다.")

    clips = []
    for slide, audio in zip(slide_files, audio_files):
        slide_path = os.path.join(slide_dir, slide)
        audio_path = os.path.join(audio_dir, audio)
        print(f"📌 슬라이드와 오디오 연결 중: {slide} + {audio}")
        clip = create_slide_clip(slide_path, audio_path)
        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
    )

    print(f"\n✅ 최종 영상 저장 완료: {output_path}")

# 실행
if __name__ == "__main__":
    slide_directory = "slides"
    audio_directory = "audios"
    output_video_path = "final_lecture_video.mp4"

    create_full_lecture_video(slide_directory, audio_directory, output_video_path)
