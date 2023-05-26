from cryptography.fernet import Fernet
import random
import string
import hashlib, SigningPhasePerf, os, subprocess, cpabe, keygenerator, timeit, time, base64, sys
import bplib.bp as bp

def utf8len(s):
    return len(s.encode('utf-8'))

def keyGen(g0, amountOfAttributes):

   
   K = 3 * amountOfAttributes
   alpha = random.randint(0, 10)
   gamma = random.randint(0, 10)

   K = 3 * amountOfAttributes
   g0 = g0._C
   PK = [g0**(alpha**x) for x in range(1, K+1)]
   print(PK)
   MK = (alpha, gamma)
   print(MK)
   return MK, PK


def main():

   # Enc => AES + (AES * (No of Attributes * No of Attributes))
  
   # Dec =>  AES + (AES * (No of Attributes * No of Attributes))
   
   policyMain = 20

   numberOfPolicy = policyMain;
   policy = createPolicy(numberOfPolicy)
   symkeyname = "test1"
   dataSizeInKb = 1000;
   cpabe_keyName = "TEST"
   G = bp.BpGroup()
   g1, g2 = G.gen1(), G.gen2()
   gt = G.pair(g1, g2)
   data = createData(dataSizeInKb) #Create Data
   byte_data = data.encode('utf-8') #Convert to bytes
   rv = os.urandom(32) 
   ct_m = []
   symkey = keygenerator.symkeygenerator(symkeyname) #Create SymKey From RV
   
   start_sym_time = timeit.default_timer()
   ct_m.append(Fernet(symkey).encrypt(byte_data)) #Symmetric Encryption

   for i in range(1, ((numberOfPolicy**2))//2):
      ct_m.append(Fernet(symkey).encrypt(byte_data)) #Symmetric Encryption

   stop_sym_time = timeit.default_timer()
   sym_time = stop_sym_time - start_sym_time #Timer
   print("User Enc Time = " + str(sym_time)) 


   start_cpabe_dec_time = timeit.default_timer()
   for i in range(((numberOfPolicy**2))//2 -1, 0, -1):
      ct_m.append(Fernet(symkey).decrypt(ct_m[i])) #Symmetric Encryption
   m = Fernet(symkey).decrypt(ct_m[0]) #Symmetric Decryption
   stop_cpabe_dec_time = timeit.default_timer()

   cpabe_dec_time = stop_cpabe_dec_time - start_cpabe_dec_time #Timer
   print("Data User Dec Time : " + str(cpabe_dec_time))




   '''
   amountOfAttributes = 10

   G = BpGroup()

   g0 = G.gen1() 

   keyGen(g0, amountOfAttributes)

   rv1name = "test1"
    
   policy = '(sysadmin and it_department and hr_department) or programmer'
   cpabe_keyName = "TEST"

   data = createData(40) #Create 40 Kb of Data
   byte_data = data.encode('utf-8') #Convert to bytes
   '''
   
      
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
   

main()
