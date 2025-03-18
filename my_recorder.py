import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import messagebox

blur_enabled = False  # 배경 블러 활성화 여부
cnt = 0  # 녹화 파일 번호
isRecording = False  # 녹화 상태
save = None  # 비디오 저장 객체

fourcc = cv.VideoWriter_fourcc(*'XVID')  # 비디오 코덱 설정
fps = 30.0  # 프레임 속도
frame_size = (640, 480)  # 비디오 프레임 크기
red_dot_position = (590, 240)  # 녹화 표시 점 위치
REC_position = (575, 260)  # 'REC' 텍스트 위치

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')  # 얼굴 검출기
video_file = 0  # 카메라 입력 (0 = 기본 웹캠)
video = cv.VideoCapture(video_file)  # 비디오 캡처 객체 생성
assert video.isOpened(), 'Cannot open camera!!!'  # 카메라가 열렸는지 확인

# Tkinter 팝업
root = tk.Tk()
root.withdraw()
messagebox.showinfo("안내", "ESC를 눌러 창을 종료하세요\n스페이스를 눌러 녹화를 시작하거나 종료하세요\n'B'를 눌러 얼굴 제외 블러를 켜거나 끌 수 있습니다.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    original_frame = frame.copy()  # 녹화용 (REC 표시 제외 및 블러 포함)
    display_frame = frame.copy()   # 화면 출력용 (블러와 REC 표시 포함)

    # 얼굴 제외 블러 처리 (화면 & 녹화 모두 적용)
    if blur_enabled:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # gray scale에서 속도가 더 빠름름
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) # gray scale에서 얼굴 검출

        blurred_frame = cv.GaussianBlur(frame, (35, 35), 30)  # 전체 배경 블러 적용

        for (x, y, w, h) in faces:
            blurred_frame[y:y+h, x:x+w] = frame[y:y+h, x:x+w]  # 얼굴 부분만 원본 유지

        original_frame = blurred_frame.copy()  # 녹화용 블러 프레임 저장
        display_frame = blurred_frame.copy()  # 화면 출력도 블러 적용

    # 화면 표시용: REC 표시 추가 (녹화에는 들어가지 않음)
    if isRecording:
        cv.circle(display_frame, red_dot_position, 5, color=(0, 0, 255), thickness=-1)
        cv.putText(display_frame, 'REC', REC_position, cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

    # 화면 출력
    cv.imshow('Video Recording', display_frame)

    key = cv.waitKey(1)
    
    # 스페이스바: 녹화 시작/중지
    if key == ord(' '):
        if not isRecording:
            print("Recording started...")
            filename = f'output{cnt}.avi'
            save = cv.VideoWriter(filename, fourcc, fps, frame_size)
            isRecording = True
        else:
            print(f"Recording stopped and saved as output{cnt}.avi")
            save.release()
            isRecording = False
            cnt += 1
            
    # 'B' 키: 블러 토글
    if key == ord('b') or key == ord('B'):
        blur_enabled = not blur_enabled
        print("Background blur enabled" if blur_enabled else "Background blur disabled")

    # 녹화 중이면 블러 적용된 원본 저장 (REC는 제외외)
    if isRecording and save is not None:
        save.write(original_frame)

    # ESC 키: 종료
    if key == 27:
        print("exit")
        break

video.release()
if save is not None:
    save.release()
cv.destroyAllWindows()