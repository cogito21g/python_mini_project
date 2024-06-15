from gtts import gTTS
import os

# 변환할 텍스트 입력
text = "안녕하세요. 음성인식 테스트입니다."

# gTTS 객체 생성 (언어는 한국어로 설정)
tts = gTTS(text=text, lang='ko')

# 변환된 음성을 파일로 저장
tts.save("output.mp3")

# 저장된 파일을 재생 (선택사항, Windows에서만 동작)
# os.system("start output.mp3")

# 또는 MacOS에서 재생 (선택사항)
# os.system("afplay output.mp3")

# 또는 Linux에서 재생 (선택사항)
# os.system("mpg321 output.mp3")
