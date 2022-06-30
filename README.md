# ros_git

4월 19일부터 6월 24일까지 연희직업전문학교에서 진행된 프로젝트를 보여주는 폴더입니다.

---


>프로젝트 배경

박물관 관람객들이 전시품을 관람할 때 전시품의 위치와 배경내용을 잘 알지 못하는 경우가 많습니다. 이를 위해 큐레이터가 존재하나 시간과 비용의 제약이 발생한다 판단.
이런 제약조건을 해결하기위해 실제 존재하는 박물관 큐레이터봇과 인천공항의 안내로봇(에어스타)를 벤치마킹하였습니다.

>프로젝트 필수 기능
1. 저희팀은 박물관의 구조가 변경되었을 시 실시간으로 수정 및 저장이 가능하도록 기능
2. 박물관 내 전시품을 CAMERA로 인식 후 인공지능 Deep-learning을 활용하여 인식의 정확도 향상
3. 관람객이 원하는 전시품으로 찾아가는 서비스
4. 관리자 및 사용자들이 사용할 gui

>필수기능 구현을 위한 기술스택
1. AI
2. ROS SLAM, Navigation
3. GUI
4. MediaPipe,Opencv

->이중 제가 맡은 기술은 2번과 3번입니다.

> 요구명서세


기능적 요구사항(목적)


  1.관리자가 사용할 수 있는 관리자용 gui를 구성
  
    1-1.무인 이동체-관리자용 실시간 cam 구성
    
    1-2.수동, 자동모드를 통해 맵을 그려주고 저장하여 관리자의 편의성 향상을 위한 목적
    
    1-3.박물관에 어떤 전시품이 진열되어 있는지 확인
    
    1-4.관람객이 관람하고싶은 전시품으로 안내할 수 있는 선택지 설정

  2.주행개선 알고리즘
  
    2-1.이동체가 최단경로로 이동
    
    2-2.목표설정지로 오차없이 이동
    
    2-3.자동으로 지도를 만들어주는 알고리즘


기능 요구사항(세부사항)

  1. pyqt5를 통해 무인이동체 정면을 사용자 pc로 내보내주는 구성
  
  2. 키보드를 이용하여 이동체를 제어, 버튼을 클릭하여 스스로 벽을 따라 다니며 주행후 map 생성
  
  3. 인식된 전시품을 저장하고 이를 관리자 화면에 송출해 주는 화면
  
  4. 관람객이 자신이 원하는 전시품을 추가 삭제할 수 있는 화면
  
  5. 벽을 스스로 따라 다니면서 맵을 생성할수 있는 알고리즘 구성

> 요구사항에 대한 기술스택

Ros1

linux-ubuntu 18.04

python 3.6.9버전

pyqt5

opencv-python==4.2.0.32


> 의존성파일
*구글 catographer
*stella n2

>실행예시


<img src = "https://github.com/dstjr2434/ros_git/blob/master/wallFollow.gif" width="200" height ="400"/>
<img src = "https://github.com/dstjr2434/ros_git/blob/master/SLAM.gif" width="200" height ="400"/>
<img src = "https://github.com/dstjr2434/ros_git/blob/master/gui1.gif" width="200" height ="400"/>
<img src = "https://github.com/dstjr2434/ros_git/blob/master/gui2.gif" width="200" height ="400"/>
<img src = "https://github.com/dstjr2434/ros_git/blob/master/wallFollow.gif" width="200" height ="400"/>


>참고자료
https://github.com/ntrexlab/STELLA_ODROID_C4
https://github.com/ntrexlab/STELLA_REMOTE_PC_N2
https://makingrobot.tistory.com/134
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/








git에 저장되어있는 파일들은 프로젝트의 전체소스코드가 아닌 git opensource를 활용한 예시들 제가 추가적으로 구현한 것들입니다.

필요하신분들은 참고하시고 편하게 재사용해주시면 됩니다.
