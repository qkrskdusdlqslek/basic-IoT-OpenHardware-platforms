# basic-IoT-OpenHardware-platforms
IoT 개발자과정 라즈베리파이 리포지토리

## 1일차
- 기본 이론 정리
    - 전류 : 전하의 흐름, 단위 시간동안에 흐른 전하의 양으로 정의됨
    - 전압 : 전기장 안에서 전하가 갖는 전위의 차이 // 전압의 차이가 있어야 전류가 흐름
    - 저항 : 전기의 흐름을 방해하는 부품

    - 옴의법칙 : V=IR 
        - 두 지점 간의 전압차, 두 지점 간에 흐르는 전류, 전류 경로의 저항은 모두 비례함
        - 전압, 전류, 저항 간의 관계를 컨덕터의 두 지점 간에 흐르는 전류가 두 지점의 전위차에 비례하는 것

    - 키르히호프 법칙: 전압법칙/ 전류법칙
        - 전류가 흐르는 즉 전기가 통과하는 분기점(선의 연결지점, 만나는 지점)에서, 전류의 합 즉 들어온 전류의 양과 나간 전류의 양의 합은 같다. 즉 0이다. 
        - 도선망(회로)안에서 전류의 대수적 합은 0이다.

    - VCC : 5v/ High/ 1 <-> Ground : 0v/Low/ 0

- GPIO
    - Python
    - GPIO 설정함수
	    - GPIO.setmode(GPIO.BOARD) -wPi (별도의 핀을 사용하겠다)
	    - GPIO.setmode(GPIO.BCM) - BCM (초록색으로 표시되어 있는 핀을 기준으로 사용하겠다)
	    - GPIO.setup(channel, GPIO.mode) 
	    - channel: 핀번호, mode: IN/OUT
	    - GPIO.cleanup() - 초기화

    - GPIO 출력함수
	    - GPIO.output(channel, state)
	    - channel: 핀번호, state: 상태(HIGH/LOW or 1/0 or True/False)

    - GPIO 입력함수
	    - GPIO.input(channel)
	    - channel: 핀번호, 반환값: HIGH/LOW or 1/0 or True/Flase

    - 시간지연 함수
	    - time.sleep(secs)

    - 실행: python 파일명.py
    - 한 줄 삭제 : Ctrl + k
    - 줄 복붙 : Ctrl + u

- 실습
    - LED 
    - SWITCH 활용해서 LED 색깔 제어
    - 디지털 음계
    - 키보드로 LED ON/OFF   
        - input으로만 받아야한다. ->GPIO.input() : x // input() : o
        - python에서는 if 뒤에 괄호 없음 
    - 디지털 음계 키보드로 제어
        ```
         try:
          while True:
            Buzz.start(30)
            user_input = input('숫자입력')
                if user_input == '1':
                    Buzz.ChangeFrequency(melody[0])
                elif user_input == '2':
                    Buzz.ChangeFrequency(melody[1])
        ```

## 2일차
- 실습
    - 손 동작 센서(pir01.py)
    - 가상환경
        - python -m venv 파일명 (가상환경 생성)
        - source ./파일명/bin/activate (가상환경 들어가는 법)
        - deactivate(가상환경 나오는 법)
        - pip install RPi.GPIO
    
    - 손 동작 센서 응용
        - 손이 감지되면 LED 불 켜기(pri02.py)

    - 초음파 센서
        - 초음파 센서 동작(ultra01.py)
        - 초음파 센서 제어 (차량 후방감지센서)(ultra02.py)

## 3일차 
- 전자석 
    - 전자들의 흐름을 '전류'라고 하는데 전류 주변에는 자동으로 **자기장**이 형성됨
    -  전류가 흐를 때만 자석이 되고, 전류를 끊으면 자석의 성질을 잃고 원래의 상태로 되돌아가는 자석

- 릴레이(자동 스위치)
    - 검출된 정보를 갖고 있는 제어 전류의 유무 또는 방향에 따라 다른 회로를 여닫는 장치
    - 입력이 어떤 값에 도달하였을 때 작동하여 다른 회로를 개폐하는 장치 

- 스텝모터
    -  DC 브러시리스 모터의 일종
    - 고정자와 회전자가 기어 모양의 돌기(작은 톱니)로 맞물려 있어, 고정자 코일에 흐르는 전류를 일정한 각도로 서서히 회전하는 모터

- 웹서버 
    - 간단한 웹서버(flask01.py)
    - URL 접속을 /led/on, /led/off로 접속하면 led를 on,off 하는 웹페이지 : 방법1(flask03.py)
    - URL 접속을 /led/on, /led/off로 접속하면 led를 on,off 하는 웹페이지 : 방법2(flask04.py)
    - get() : http://192.168.5.3:10011/?이름=000&주소=00 형태로 주소창에 적음(flask05.py)

## 4일차
- 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html파일을 저장함
    - 버튼을 만들어 LED ON/OFF 실행(flask06.py)

- 사진 찍고 저장(camera.py)
    - 클릭 버튼으로 사진 찍고 저장(camera01.py)

- FND 세그먼트
    - 양극(COM1 - 3v3 / dp - GND)
    - 1초마다 타이머 (FND01.py,)

## 5일차
- FND 세그먼트  
    - 스위치 누를 때마다 1씩 증가(FND04.py)
        - list 함수 사용(대괄호 사용)
        ```
         digit_patterns = [
            [False, False, False, False, False, False, True],
            [True, False, False, True, True, True, True],
            ...
         ]
            try:
                while True:
                    if GPIO.input(Button) == True:
                        GPIO.output(segments[0], digit_patterns[count][0])
                        GPIO.output(segments[1], digit_patterns[count][1])
                        ...
        ``` 

## 6일차
- FND 세그먼트
    - 4자리 숫자 돌아가게(FND09.py)
    - 타이머 형식(FND11.py)

- QuTy5
    - 기본 틀
        ```
        import sys
        from PyQt5.QtWidgets import *
        from PyQt5 import uic

        form_class = uic.loadUiType("./test01.ui")[0]

        class WindowClass(QMainWindow, form_class):
            def __init__(self):        # 생성자
            super().__init__()
            self.setupUi(self)


        ```

    - 이벤트 함수 등록
        - Putty에서 
            ```
                self.버튼이름.버튼작용.connect(self.버튼함수이름)
                -> self.btn_1.clicked.connect(self.btn1Function)
            ```

## 7일차
- 평가
    - QtDesigner로 브레드보드에 연결시킨 장치들 작동시키기 (final01-02.py)

    ![평가 이미지](https://raw.githubusercontent.com/qkrskdusdlqslek/basic-IoT-OpenHardware-platforms/main/day07/final03.png)

## 8일차
- 평가
- 팀프로젝트