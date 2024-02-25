from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment

from functions.file_control import file_delete


def remove_silent_parts(video_path, output_path):
    # 비디오 클립 로드
    video_clip = VideoFileClip(video_path)

    # 오디오 파일 로드
    audio = AudioSegment.from_file(video_path)

    # 소리 안 나오는 부분 찾기
    silent_ranges = audio.detect_silence(min_silence_len=500, silence_tresh=-40)

    # 찾은 구간 제거하기
    segments = []
    start = 0
    for r in silent_ranges:
        # 비디오 자르기
        trimmed_clip = video_clip.subclip(start, r[0])

        # 새 파일로 저장
        segments.append(trimmed_clip)

        # 메모리에서 비디오 클립 삭제
        video_clip.close()
        start = r[1]

    # 클립들을 이어 붙여 새로운 비디오 생성
    final_clip = concatenate_videoclips(segments)
    final_clip.write_videofile(output_path)

    # 메모리에서 클립들 삭제
    for segment in segments:
        segment.close()

    file_delete(video_path)