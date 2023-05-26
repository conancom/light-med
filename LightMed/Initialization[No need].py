from cryptography.fernet import Fernet
import random
import string
import hashlib, SigningPhasePerf, os, subprocess, cpabe, keygenerator, timeit,time


def main():

    policy = 'sysadmin it_department'
    cpabe.keygen("TEST", policy) #Create Key

main()