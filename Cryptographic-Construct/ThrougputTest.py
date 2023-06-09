from operator import xor
from cryptography.fernet import Fernet
import random
import string
import threading
import hashlib, SigningPhasePerf, os, subprocess, cpabe, keygenerator, timeit, time, base64, charm
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair,extract_key

def main():


    rv1name = "test1"
    numberOfPolicy = 5
    dataSizeInKb = 40
    policy = createPolicy(numberOfPolicy)

    numberOfRequests = 10000
   
    threadArr = []

    # creating thread
    for i in range(numberOfRequests):
        threadArr.append(threading.Thread(target=updatePolicy))
    
    start_sym_time = timeit.default_timer()


    for i in range(numberOfRequests):
        threadArr[i].start()

    for i in range(numberOfRequests):
        threadArr[i].join()    

    stop_sym_time = timeit.default_timer()
    
    # All threads completely executed
    print("Done!")
    sym_time = stop_sym_time - start_sym_time #Timer
    print("Total Run Time " + str(sym_time)) 
   
def createData(size):
   n = 1024 * size   # 1024 = 1 Kb of text
   return ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

def createPolicy(amount):
   policies = ""
   for x in range(1, amount):
      policies = policies + "TEST" + str(x) +  " and "
   return policies + "TEST"+str(amount)

def createPolicyKey(amount):
   policies = ""
   for x in range(1, amount):
      policies = policies + "TEST" + str(x) +  " "
   return policies + "TEST"+str(amount)

def utf8len(s):
    return len(s.encode('utf-8'))

def updatePolicy():

    cpabe_keyName = "TEST"

    cpabe.decrypt(rv1name, cpabe_keyName) #CPABE Decryption

    cpabe.encrypt_key(rv1name, policy) #CPABE Encryption

main()
