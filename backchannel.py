#!/bin/python3
import json
import sys
import websocket
from time import time
from time import sleep
from datetime import datetime

def on_message(ws, message):
    #print('&&&&&&&&&& MESSAGE!')
    #print("v")
    #print(message)
    data = json.loads(message)
    if 0 <= 2 < len(data):
        print(" *******************************************")
        print(" * dt:'" + str(datetime.fromtimestamp(data[2]['created_at'])) + "'       " + data[2]['pubkey'] + ":")
        print(" *******************************************")
        print(" *")
        print(" *  MSG:")
        output(" *   " + data[2]['content'])
        print("\n *")
        print(" **** END MESSAGE **************************\n\n")
    #else:
        #print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    #data = '["REQ", "ec3e6228-5ef3-4162-899c-a58e88de586a", {"kinds":[1], "since":' + str(round((time() - 1000))) + '}]'
    data = '["REQ", "ec3e6228-5ef3-4162-899c-a58e88de586a", {"kinds":[1], "limit":20}]'
    json_data = json.dumps(data)
    ws.send(data)

def output(outStr):                                                                                                                                                                                                                                      
    for a in outStr:                                                                                                                                                                                                                                     
        print(a,end='')
        if a == "\n":
            print(" *   ", end='')
        sleep(0.01)
        sys.stdout.flush()

if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://nostr.orangepill.dev",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


