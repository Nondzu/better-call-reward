#!/bin/python3
from asyncio import constants
from pyclbr import Function
import requests
import time
import sys
import argparse
from datetime import datetime

# set your Orchestrator url
URL_DEFAULT = 'http://localhost:7935'  # default

retryTimeOffline = 60  # delay  when O is offline, in seconds
retryTimeReward = 60 * 60  # time retry call "reward ", in seconds


def parseArgs():
    # Instantiate the parser
    parser = argparse.ArgumentParser(
        description='Script to resolve problem with livepeer "reward" call. ')
    parser.add_argument('-url', type=str, nargs='?',
                        help='URL for your Orchestrator')
    # todo: ? add delay params
    # parser.add_argument('-delay', type=int, nargs='?',
    #                     help='delay between next try of call "reward"')
    # Parse the argument
    args = parser.parse_args()
    if args.url is None:
        url = URL_DEFAULT
    else:
        url = args.url
    print("Orchestrator URL: " + url)
    return url
# end  parseArgs()


def statusOrch(url):    # /status ,  check O status and get some info
    try:
        r = requests.get(url + '/status')
        responseStatus = r.status_code
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Error during connection to '" + url +
              "'. Please check your Orchestrator url.")
        exit(0)
    print("Connection success")
    print("---Info---")
    print("Orchestrator Version: " + r.json()['Version'])
    print("GolangRuntimeVersion: " + r.json()['GolangRuntimeVersion'])
    print("")

    # transcoders info
    print("Transcoders:")
    i = 1
    for t in r.json()['RegisteredTranscoders']:
        print("["+str(i) + "] Address: " + t['Address'] +
              " Capacity:" + str(t['Capacity']))
# end  statusOrch(url) ----------------------------------------------


def pingOrch(url):  # /status
    try:
        requests.get(url + '/status')
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Error during connection to '" + url +
              "'. Please check your Orchestrator url.")
        return False
    return True
# end pingOrch() ----------------------------------------------


def getLastRewardRound(url):  # /orchestratorInfo
    try:
        r = requests.get(url + '/orchestratorInfo')
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Error: can't get 'Last Reward Round' round info.")
        return -1

    if r.status_code != 200:
        print("Can not get last reward round info. Error: " + str(r))
        return -2
    return r.json()['Transcoder']['LastRewardRound']
# end getLastRewardRound() ----------------------------------------------


def getCurrentRound(url):  # /currentRound
    # get current Round value
    try:
        r = requests.get(url + '/currentRound')
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Error: can't get 'current Round' info.")
        return -1

    if r.status_code != 200:
        print("Error: can't get 'current Round' info."+" ERROR: " + str(r))
        return -2

    currentRound = int(r.content.hex(), 16)
    return currentRound
# end getLastRewardRound() ----------------------------------------------


def log(info):
    print("[", datetime.now(), "]", info)
# end log(info) ----------------------------------------------


url = parseArgs()
statusOrch(url)
print("")

while True:
    lastRewardRound = getLastRewardRound(url)
    currentRound = getCurrentRound(url)

    log('Orchestrator status: ' + ('online' if pingOrch(url) else 'offline'))
    if (currentRound < 0 or lastRewardRound < 0):
        log("Is Orchestrator online ?")
        delay = retryTimeOffline
    else:
        log('Last reward round: ' + str(lastRewardRound))
        log('Current round: ' + str(currentRound))

        if currentRound != lastRewardRound:
            log('Call reward!')
            r = requests.get(url + '/reward')  # call reward
            log(r)
            if r.status_code == 200:
                log('Call to reward success.')
            else:
                log('Call to reward fail. Error: ' + str(r))

        else:
            log('Do not call reward. ' + 'Reward for current round ' +
                str(currentRound) + ' already called.')
        delay = retryTimeReward

    while delay > 0:
        print(". Next call: " + str(delay) + "s      " + "\r", end="")
        sys.stdout.flush()
        delay = delay - 1
        time.sleep(1)
    print("                    ")
    sys.stdout.flush()
    print("----------------------------")
