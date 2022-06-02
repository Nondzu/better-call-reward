# better-call-reward
Script calling 'reward'  for Livepeer orchestrator



usage: better-call-reward.py [-h] [-url [URL]] [-delay [DELAY]]

Optional app description

optional arguments:
  -h, --help      show this help message and exit
  -url [URL]      URL for your Orchestrator
  -delay [DELAY]  delay between next try of call "reward"

example usage: 
./better-call-reward.py  -url http://localhost:7935
or use 

some error:
Orchestrator URL: http://192.168.137.103:7935
Connection success
---Info---
Orchestrator Version: 0.5.31-ec920c67
GolangRuntimeVersion: go1.18.1

Transcoders:
[1] Address: 127.0.0.1:54396 Capacity:14

[ 2022-06-02 10:33:26.291112 ] Orchestrator status: online
[ 2022-06-02 10:33:26.291156 ] Last reward round: 2584
[ 2022-06-02 10:33:26.291175 ] Current round: 2585
[ 2022-06-02 10:33:26.291189 ] Call reward!
[ 2022-06-02 10:33:26.292445 ] <Response [404]>
[ 2022-06-02 10:33:26.292469 ] Call reward fail. Error: <Response [404]>