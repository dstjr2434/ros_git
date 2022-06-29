# ros_git

4월 19일부터 6월 24일까지 연희직업전문학교에서 진행된 프로젝트를 보여주는 폴더입니다.

---


>프로젝트의 배경

박물관 관람객들이 전시품을 관람할 때 전시품의 위치와 배경내용을 잘 알지 못하는 경우가 많습니다. 이를 위해 큐레이터가 존재하나 시간과 비용의 제약이 발생한다 판단.
이런 제약조건을 해결하기위해 실제 존재하는 박물관 큐레이터봇과 인천공항의 안내로봇(에어스타)를 벤치마킹하였습니다.

>프로젝트의 필수 기능
1. 저희팀은 박물관의 구조가 변경되었을 시 실시간으로 수정 및 저장이 가능하도록 기능
2. 박물관 내 전시품을 CAMERA로 인식 후 인공지능 Deep-learning을 활용하여 인식의 정확도 향상
3. 관람객이 원하는 전시품으로 찾아가는 서비스
4. 관리자 및 사용자들이 사용할 gui

>기능구현을 위한 기술스택
1. 인공지능
2. ROS SLAM, Navigation
3. GUI
4. MediaPipe,Opencv

위의 4가지 기술을 사용한 큐레이터봇을 만들었으며 제가 구현한 파트는 2번과 3번입니다

> 내가 맡은 기능에 대한 기술스택

Ros1
linux-ubuntu 18.04
python 3.6.9버전
pyqt5


> 요구명서세
-기능 요구사항(목적,요구,세부사항)

-설계 제약사항(pyqt5 이상,

- 소프트웨어 시스템 속성

> 트러블슈팅

> 의존성파일

구글 catographer
stella n2

>실행

>참고자료
https://github.com/ntrexlab/STELLA_ODROID_C4
https://github.com/ntrexlab/STELLA_REMOTE_PC_N2
https://makingrobot.tistory.com/134
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/








git에 저장되어있는 파일들은 프로젝트의 전체소스코드가 아닌 git opensource를 활용한 예시들 제가 추가적으로 구현한 것들입니다.

필요하신분들은 참고하시고 편하게 재사용해주시면 됩니다.

