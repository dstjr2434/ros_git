# ros_git

4월 19일부터 6월 24일까지 연희직업전문학교에서 진행된 프로젝트를 보여주는 git입니다.

---


>## 프로젝트 배경


박물관 관람객들이 전시품을 관람할 때 전시품의 위치와 배경내용을 잘 알지 못하는 경우가 많습니다. 이를 위해 큐레이터가 존재하나 시간과 비용의 제약이 발생한다 판단.
이런 제약조건을 해결하기위해 실제 존재하는 박물관 큐레이터봇과 인천공항의 안내로봇(에어스타)를 벤치마킹하였습니다.



>## 프로젝트 필수 기능
1. 저희팀은 박물관의 구조가 변경되었을 시 실시간으로 수정 및 저장이 가능하도록 기능
2. 박물관 내 전시품을 CAMERA로 인식 후 인공지능 Deep-learning을 활용하여 인식의 정확도 향상
3. 관람객이 원하는 전시품으로 찾아가는 서비스
4. 관리자 및 사용자들이 사용할 gui

>## 필수기능 구현을 위한 기술스택
1. AI
2. ROS SLAM, Navigation
3. GUI
4. MediaPipe,Opencv


>## 프로젝트 관리도구
1. git, github
  * repository 생성
  * 프로젝트, 코드 관리
  * ~~버전관리, 협업~~ (Slack, Notion으로 대체됨)
    * 버전관리 및 협업 Slack, Notion 환경에서 실시

2. Notion (https://funny-tracker-34e.notion.site/HOME-b09bad420f4242c2bd7d9d953949108f)
  * Meeting Log
  * Issue 관리
  * Task 관리

3. Slack
  * 커뮤니케이션
  * daily dev journal
  * data, code 공유


>## 요구명서세


### 기능 요구사항(목적)


  1.관리자가 사용할 수 있는 관리자용 gui를 구성
  
    1-1.무인 이동체-관리자용 실시간 cam 구성
    
    1-2.수동, 자동모드를 통해 맵을 그려주고 저장하여 관리자의 편의성 향상을 위한 목적
    
    1-3.박물관에 어떤 전시품이 진열되어 있는지 확인
    
    1-4.관람객이 관람하고싶은 전시품으로 안내할 수 있는 선택지 설정

  2.주행개선 알고리즘
  
    2-1.이동체가 최단경로로 이동
    
    2-2.목표설정지로 오차없이 이동
    
    2-3.자동으로 지도를 만들어주는 알고리즘


### 기능 요구사항(세부사항)

  1. pyqt5를 통해 무인이동체 정면을 사용자 pc로 내보내주는 구성
  
  2. 키보드를 이용하여 이동체를 제어, 버튼을 클릭하여 스스로 벽을 따라 다니며 주행후 map 생성
  
  3. 인식된 전시품을 저장하고 이를 관리자 화면에 송출해 주는 화면
  
  4. 관람객이 자신이 원하는 전시품을 추가 삭제할 수 있는 화면
  
  5. 벽을 스스로 따라 다니면서 맵을 생성할수 있는 알고리즘 구성

  6. 동적 장애물 회피를 위한 D* 

>## 요구사항에 대한 기술스택

ROS (ROS1_melodic)

linux-ubuntu 18.04

python 3.6.9버전

pyqt5

opencv-python==4.2.0.32


>## 실행예시

<p align="center">
 turtlebot3 시뮬레이션
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/simul.gif" width="400" height ="400"/>
</p>

<p align="center">
 slam-pc 구현화면
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/SLAM.gif" width="400" height ="400"/>
</p>

<p align="center">
 wall-follower 실제구현영상
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/wallFollow.gif" width="400" height ="400"/>
</p>

<p align="center">
move 2 destination구현영상
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/godestination.gif" width="400" height ="400"/>
</p>

<p align="center">
gui 구현화면1
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/gui1.gif" width="400" height ="400"/>
</p>

<p align="center">
gui 구현화면2
</p>

<p align="center">
<img src = "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/gui2.gif" width="400" height ="400"/>
</p>


>## 프로젝트 관리
* Simulator (https://github.com/ROBOTIS-GIT/turtlebot3_simulations)
  * 코드 테스트 및 변수 관리
* Notion
* Slack - 커뮤니케이션


### 이슈 관리 (Notion)

<p align="center">
  <img src= "https://github.com/dstjr2434/ros_git/blob/master/photo-doc/issues.png" width="400" height ="400"/>
</p>
<p align="center">
  Issue Log
</p>

* Notion
  * https://funny-tracker-34e.notion.site/924096c581d643c78881fb4c7dbbb3f5?v=d9bff0f0c53d44f2a83fa9b8618f0c5f
  


### 테스크 관리 (Notion)

<p align="center">
  <img src="https://github.com/dstjr2434/ros_git/blob/master/photo-doc/tasks.png"/>
</p>
<p align="center">
  Task Log
</p>

* Notion
  * https://funny-tracker-34e.notion.site/574ceb7ae62143b3847b295002abf0e2?v=8f01e42b95b64fbf84bf2470895841e6



### 커뮤니케이션 관리 (Slack)
* 커뮤니케이션
* daily_dev_journal - 일일 개발 일지 관리
* data, code 공유 및 버전 관리

<p align="center">
  <img src="https://github.com/dstjr2434/ros_git/blob/master/photo-doc/slack.png/">
</p>


>## 미구현 및 개선사항

## 저장된 맵 정보를 불러온 뒤 정상적으로 작동하는 기능 구현 미완성
  * 미완성 사유
    * Navigation Pose Estimation Issue
      * 2D맵 저장, 불러오기 기능 구현은 완성
      * Navigation을 위한 2D맵 불러오기 이후, 이동체 위치 calibration이 정상적으로 작동하지 않아 위치 오차가 지속적으로 누적
  * Try&Error
    * SLAM 환경에서 정상적으로 Calibration이 작동하는 점에서 착안, SLAM 환경에서의 calibration method를 Navigation 환경에 적용 시도
      * lidar depth 기반 위치 추정하는 정확한 알고리즘 분석 미흡
      * SLAM method 강제 적용시 2D맵 정보가 override되는 현상 발생
  * 기능 대체 구현
    * 실시간 작동
      * 작동 종료시 맵, 좌표, 객체 위치 데이터 휘발
        * 초기화 및 2D맵 스캔 등 초기화 후 기능 동작
  * 향후 개선 방법
    * Navigation Pose Estimation Issue는 AMR 구현의 고질적인 이슈
    * SLAM에서 위치를 추정하기 위해 사용하는 알고리즘 대략적인 위치 추정, (Grid map 분할), 범위 내 depth 정보 비교



## Full Autonomous Drive 미완성
  * 미완성 사유
    * Wall_follower Node 기반의 완전 자동화를 구현하려고 하였으나, GUI, Remote_PC 등 분산되어 있는 처리를 통합하는 과정에서 잦은 에러 발생, 초기 계획보다 소요 시간이 길어져서 완성 시간 부족
  * How to solve
    * 이동체 초기화 위치 원점(0, 0, 0, 0)을 기반으로 4사분면으로 분할, 4분면 모두 방문한 이후 원점과 근접할 시 (tolerance 70% 이상) 원점으로 강제 이동 및 대기모드 전환 (미구현)
    * 2D맵 폐쇄성 검사(벽면으로 모든 공간이 막혀 있는지 여부 확인), 스캔 완성도 검사(벽면 외에 스캔되지 않은 영역 존재 여부 확인) 실시 후 통과할 시 원점으로 강제 이동 및 대기모드 전환 (미구현)
  * 향후 개선 방법
    * 주간 단위 프로젝트 통합을 실시하여 최종 기능 통합 시 소요시간 단축
  
  * wall-follower 완전자동화
  * 제어 완전 자동화



## 객체 인지 모델 정확도 부족
  * 부족 사유
    * 학습 데이터 부족
      * 이미지는 충분히 확보하였으나 데이터 전처리 및 라벨링 작업에 예상되는 소요 시간이 길어 부득이하게 최소한의 데이터만으로 모델 학습 실시
  * 향후 개선 방법
    * Auto labeling 기능 활용
    * 유사 프로젝트 진행시, 모델 학습을 위한 데이터에 대한 검토를 프로젝트 초반부터 실시하여 데이터 확보 및 전처리에 충분한 시간 할당


## git, github 기반 프로젝트 진행을 위한 개선점
  * 모듈, 패키지화
    * 프로젝트 repository 내부에 각 파트별, 기능별로 코드를 모듈, 패키지화하여 독립적으로 관리
    * 반복적으로 pull, push, merge를 해야 하는 상황에서 작업 전 pull&merge 습관화
  * 코드리뷰 기반 커뮤니케이션 실시
    * github 내부의 comment 기능을 활용하여 Slack, github 이원화 관리에서 github 단일 소스 기반 관리
  * 주석, 코드 리뷰 코드 중심 일원화 관리
    * 추가, 수정되는 내용이 적은 상황에서도 주석, 리뷰 중심의 변동 사항을 남기는 방식으로 관리










>## References

https://github.com/ntrexlab/STELLA_REMOTE_PC_N2
  * 실습용 이동체 Stella N2 제공 모듈
    * Cartographer (SLAM, Navigation) 패키지 포함
    * Hardware (Lidar, IMU, Motordriver, Camera) 패키지 포함
    
https://github.com/ROBOTIS-GIT/turtlebot3_simulations
  * 터틀봇 시뮬레이터 패키지 - 터틀심
    * 실제 기능 적용 이전 시뮬레이션 테스트
    * Node, topic, service 구조 파악

https://github.com/tensorflow/examples
  * Tensorflow를 활용하는 다양한 기능이 포함된 패키지
    * Object Detection 모듈 사용

https://colab.research.google.com/github/khanhlvg/tflite_raspberry_pi/blob/main/object_detection/Train_custom_model_tutorial.ipynb
  * Model-Maker
    * 자체 데이터(img + xml)를 활용한 tflite 분류 모델 학습

----------

*참고 Reference*

https://github.com/cartographer-project/cartographer
  * 카토그래퍼 repository
    * SLAM Calibration과 Navigation Pose Estimation 기능 분석을 위해 활용

https://github.com/cartographer-project/cartographer_ros
  * ROS 환경에서 작동하는 카토그래퍼 repository
    * ROS 환경에서 SLAM, Navigation 노드 구조 분석을 위해 활용

https://github.com/ros-perception/slam_gmapping
  * SLAM gammping 패키지
    * 맵 생성과 좌표계 시스템 분석을 위해 활용

https://github.com/ntrexlab/MW_MotorControllers_Manual
  * 모터 드라이버 (Stella_N2 의존성 패키지)
    * 주행성 개선, 위치 정확도 개선을 위해 slip현상 억제를 위해 encode 분석 목적으로 활용
    
https://github.com/EAIBOT/ydlidar
  * 라이다 센서 패키지 (Stella_N2 의존성 패키지)
    * 라이다 센서 raw data 분석을 위해 활용
      * 라이다 raw data 중에서 관심 영역의 depth를 추출하기 위해 활용
      * 라이다 raw data와 map depth 비교를 통한 위치 보정 정보 분석을 위해 활용

https://github.com/ntrexlab/ahrs_v2_ROS1
  * IMU 센서 패키지  (Stella_N2 의존성 패키지)
    * pose estimation 오차 분석을 위해 활용

https://github.com/tensorflow/tensorflow
  * Tensorflow repository
    * Tensorflow 환경설정, 구조, 예시 분석을 위해 활용
    
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi
  * TensorFlow-Object-Detection-on-the-Raspberry-Pi
    * 라즈베리파이 환경에서 원활하게 작동하는 객체 인식을 위해 참조
    * tflite로 기능 구현 이후에는 참조용으로 활용

https://teachablemachine.withgoogle.com/
  * Classification Model 학습을 Local 환경설정 없이 구현하기 위해 참조
  * tflite Model-Maker로 모델 학습 이후에는 참조용으로 활용

https://github.com/nimbekarnd/Wall-follower-in-ROS-using-Python
  * Wall-Follower opensource
    * Wall-Follower 알고리즘 개선을 위해 참조

https://github.com/ssscassio/ros-wall-follower-2-wheeled-robot
  * Wall-Follower opensource
    * Wall-Follower 알고리즘 개선을 위해 참조





---

git에 저장되어있는 파일들은 프로젝트의 전체소스코드가 아닌 git opensource를 활용한 예시들 제가 추가적으로 구현한 것들입니다.

필요하신분들은 참고하시고 편하게 재사용해주시면 됩니다.
