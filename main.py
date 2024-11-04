import re
from youtube_transcript_api import YouTubeTranscriptApi
import os


def extract_video_id(url):
    """YouTube URL에서 비디오 ID를 추출합니다."""
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    print (f"{video_id_match}")
    if video_id_match:
        return video_id_match.group(1)
    return None

def get_transcript(video_id):
    """YouTube 비디오의 트랜스크립트를 가져옵니다."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"트랜스크립트를 가져오는 데 실패했습니다: {e}")
        return None


def main():
    # YouTube URL 입력 받기
    url = input("YouTube 동영상 URL을 입력하세요: ")
    
    # 비디오 ID 추출
    video_id = extract_video_id(url)
    if not video_id:
        print("올바른 YouTube URL이 아닙니다.")
        return
    
    # 트랜스크립트 가져오기
    transcript = get_transcript(video_id)
    print (f"{transcript}")
    if not transcript:
        return

if __name__ == "__main__":
    main()