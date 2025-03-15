# my_video_recorder
my personal video recorder using OpenCV

**기본 설명**
1. 기본적인 동영상 녹화 기능이 탑재되어 있습니다. 여러분의 랩탑이나 데스크탑 등의 웹캠을 통해 녹화할 수 있습니다.
2. 스페이스(space)를 눌러 녹화를 시작하거나 중단할 수 있습니다.
3. 'B' 또는 'b'를 눌러 얼굴을 제외한 배경을 블러 처리할 수 있습니다.

**사용 방법**
1. 파이썬 코드를 실행합니다. 그러면 다음과 같이 알림창이 나옵니다.
![screenshot1](/imgs/screenshot1.png)

2. 알림창을 닫으면 다음과 같이 카메라 녹화를 할 수 있는 창이 나옵니다.
![screenshot2](/imgs/screenshot2.png)

3. 'B' 또는 'b'를 누르면 얼굴을 제외한 나머지 부분을 다음과 같이 블러 처리할 수 있습니다.
![screenshot3](/imgs/screenshot3.png)

4. 스페이스(space)를 누르면 녹화를 시작하거나 중단할 수 있습니다. 녹화 중일 때는 다음과 같이 <span style="color:red">REC</span>와 <span style="color:red">붉은 점</span>이 화면에 나타납니다. 이 부분은 녹화된 파일에 저장되지 않습니다.
![screenshot4](/imgs/screenshot4.png)

5. 저장된 파일은 다음과 같이 저장소에 output(숫자).avi로 저장되며 한 번에 여러 번의 녹화를 진행할 수 있습니다.
![screenshot5](/imgs/screenshot5.png)

6. 창을 닫으려면 esc를 눌러 프로그램을 종료할 수 있습니다. 종료 이후 재시작하여 녹화를 진행할 시 원래 있던 파일을 덮어쓰기 하므로 주의하시기 바랍니다.

**예시**
![output0](/imgs/output0.gif)
예시로 녹화된 파일입니다.

*본 설명에서 쓰인 사람의 이미지는 Grok3를 이용해 만들어진 이미지입니다.*