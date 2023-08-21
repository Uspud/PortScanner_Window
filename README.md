# PortScanner_Window
using Pyqt6 UI PortScanner that Service detection logic using double service detection was used. (service list matching, banner grabbing, Response Message-Based Identification)

portdetail 파일은 응답 값을 확인 해 볼 수 있는 개별 작동하는 코드 입니다.
port_scanner_7.2.py 파일을 동작 시키면, 사용할 수 있는 PyQt6를 사용하여 UI를 구성하여였기에 Window에서만 작동하는 포트 스캐너 입니다.(맥북에서도 작동은 되는 것으로 확인하였습니다.)

기능 사용 방법 : 
![Untitled](https://github.com/LikeyUserspray/PortScanner_Window/assets/98539049/fff7d520-8b4a-46d1-b639-0b61add98519)
1. Scan type에서 TCP Scan(TCP FULL Connect), Stealth Scan 기능 중 선택한다.
2. Host 부분에 ip주속 혹은 domain주소를 입력한다. (도메인 주소는 https://www.은 제외하고 입력한다.) 예시: naver.com
3. PortRange 부분에 원하는 포트 대역을 입력한다. (1-65535 처럼 입력 양식에 맞추어 사용한다.)
4. Start Scanning 버튼을 눌러 포트 스캔을 시작한다. (도메인에 두개의 ip가 달려있을 경우 추가 선택 창이 나온다.)
5. 포트 스캔이 완료되면, Service Scan 버튼을 눌러 열려있는 포트에 대한 서비스 판별을 시작한다.
6. 저장하기 위해서는 Folder 부분에 저장할 경로 + 파일 명을 입력하고, Export를 누르면 파일의 형태로 저장된다.
7. Reset 버튼을 눌러 스캔 결과를 초기화 할 수 있다. 

구현 기능으로는
1. TCP FULL Connect 를 통한 포트 스캔
2. SYN Scan 을 통한 포트 스캔

이 포트 스캐너의 특징으로는 서비스 탐지의 신뢰성에 대해 높이고자 했습니다.
이를 위해 여러가지 방법을 사용하였습니다.
1. 포트 번호를 통한 서비스 매치(service_list.txt)
2. 서비스 별 웰컴 메세지와 배너 그래빙을 통한 서비스 식별
3. 서비스 별 서버의 응답을 수신하여 응답의 특징을 통한 매칭
4. 각 서비스에 명령어나 질의를 던져 그에 대한 응답값을 확인하여 서비스 판별
   
이러한 방법을 2~3가지를 사용하여 각 서비스 별 판별을 진행하였습니다.

그러나, 모든 서비스에 대한 판별을 구현하지 못하여 TCP FULL Connect를 통한 스캔에서 아래의 서비스 항목에 대해서만 서비스 판별 로직이 작성되었습니다. 
- HTTP
- SSH
- SMTP
- MySQL
- FTP
- Dovecot
- Telnet
- hl7
- RFB
- finger
- Echo, Chargen, Time, Daytime
- SSL
- DNS
- LDAP

다른 서비스 들에 대해서는 포트 번호를 통한 서비스 매칭과 단순 배너 그래빙 매칭 정도만 시도합니다. 

스텔스 스캔 기능에서는 단순 작동 유무만 판단 합니다.
