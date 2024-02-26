from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment
from pydub.silence import detect_silence

from functions.file_control import file_delete


def remove_silent_parts(video_path, output_path):
    # 비디오 클립 로드
    video_clip = VideoFileClip(video_path)

    # 오디오 파일 로드
    audio = video_clip.audio
    audio_path = video_path.replace(".mp4", ".mp3")
    audio.write_audiofile(audio_path)
    audio_segment = AudioSegment.from_file(audio_path, format="mp3")

    # 소리 안 나오는 부분 찾기
    silent_ranges = detect_silence(audio_segment, min_silence_len=500, silence_thresh=-40)

    # 새로운 비디오 클립 생성
    new_video_clip = VideoFileClip(video_path)

    # 소리가 없는 부분을 비디오에서 제거
    segments = []
    start = 0
    for s_start, s_end in silent_ranges:
        new_video_clip = video_clip.subclip(start, s_start / 1000)
        start = s_end / 1000
        segments.append(new_video_clip)

    # 새로운 비디오 파일로 저장
    final_clip = concatenate_videoclips(segments)
    final_clip.write_videofile(output_path)
    
    # 임시 오디오 파일 삭제
    file_delete(audio_path)
