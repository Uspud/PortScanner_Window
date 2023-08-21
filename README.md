# PortScanner_Window
using Pyqt6 UI PortScanner that Service detection logic using double service detection was used. (service list matching, banner grabbing, Response Message-Based Identification)

portdetail 파일은 응답 값을 확인 해 볼 수 있는 개별 작동하는 코드 입니다.
port_scanner_7.2.py 파일을 동작 시키면, 사용할 수 있는 PyQt6를 사용하여 UI를 구성하여 Window에서만 작동하는 포트 스캐너 입니다.

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
