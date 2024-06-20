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




