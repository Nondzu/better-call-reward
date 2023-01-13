# better call reward

#### Script to call `reward`  for Livepeer orchestrator.

What this do?
This script uses livepeer API to get info on the last reward call round and current round.
Then compare these numbers and if they are not the same just call to `reward`. 
Script in default is checking numbers every 1h. You can change this value by editing `retryTimeReward`

My Orchestrator has many missing `reward` calls and this was the main motivation to create this script.

#### help:
```
usage: better-call-reward.py [-h] [-url [URL]] [-delay [DELAY]]

Optional app description

optional arguments:
  -h, --help      show this help message and exit
  -url [URL]      URL for your Orchestrator
```


#### example usage: 
`./better-call-reward.py  -url http://localhost:7935`

`./better-call-reward.py ` - this use default url `http://localhost:7935`

#### script output on succes:
```
Orchestrator URL: http://192.168.137.103:7935
Connection success
---Info---
Orchestrator Version: 0.5.31-ec920c67
GolangRuntimeVersion: go1.18.1

Transcoders:
[1] Address: 127.0.0.1:54396 Capacity:14

[ 2022-06-02 10:40:36.105142 ] Orchestrator status: online
[ 2022-06-02 10:40:36.105176 ] Last reward round: 2584
[ 2022-06-02 10:40:36.105190 ] Current round: 2585
[ 2022-06-02 10:40:36.105195 ] Call to reward!
[ 2022-06-02 10:42:32.865710 ] <Response [200]>
[ 2022-06-02 10:42:32.865755 ] Call reward success.
. Next call: 3534s    
```

#### example output from O:
```
I0602 10:40:35.750595  417331 handlers.go:845] Calling reward
2022/06/02 10:41:30 http: TLS handshake error from 208.115.199.25:41434: EOF
I0602 10:42:31.336083  417331 transactionManager.go:119]
******************************Eth Transaction******************************

Invoking transaction: "rewardWithHint". Inputs: "_newPosPrev: 0x86c5A8231712CC8aaa23409B5ad315f304C09531  _newPosNext: 0x22Ae24C2D1f489906266609d14c4C0387909A38a"  Hash: "0x410696c59c24527e9c34323be46470f96694cc870982d674ea1b222ae25c59b5".

***************************************************************************
I0602 10:42:32.508922  417331 handlers.go:855] Call to reward successful
```



#### some error:
```
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
[ 2022-06-02 10:33:26.291189 ] Call to reward!
[ 2022-06-02 10:33:26.292445 ] <Response [404]>
[ 2022-06-02 10:33:26.292469 ] Call to reward fail. Error: <Response [404]>
```
#### Launch using docker compose:
1. Clone this repo and cd into it: `cd better-call-reward/`
2. Run to launch the script `docker-compose up --build -d`
3. Confirm that is working: `docker-compose logs -f --tail=100 script`

**Note** that inside docker-compose file, the network is in host mode to be able to call localhost as the real host and not as the container. If your orchestrator is dockerized, you would need to remove this and point your Orchestrator container using the container IP or the docker compose service name.

Buy me a coffee:  <br />
LPT (Arbitrum): `0xE32971e1a55152A94Fa55DFb80ACdC4bA55679C3`  <br />
AETH (Arbitrum): `0xE32971e1a55152A94Fa55DFb80ACdC4bA55679C3` <br />
ETH:  `0xE32971e1a55152A94Fa55DFb80ACdC4bA55679C3` <br />
DOGE: `D8mJBFdSQscQKce2vnPsKr4dC4sFvypBfU`  <br />

