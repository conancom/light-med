import subprocess

def encrypt_key(id, policy):
    p = subprocess.run(['cpabe-enc', '-k','./pub_key', './Symkeys/{}_key.txt'.format(id), '{}'.format(policy)])

def encrypt_text(dir, policy):
    p = subprocess.run(['cpabe-enc','./pub_key', './LightMed/{}'.format(dir), policy])

def decrypt(file, key):
    p = subprocess.run(['cpabe-dec', '-k','./pub_key', './cpabe_keys/{}_priv_key'.format(key), './Symkeys/{}_key.txt.cpabe'.format(file)])

def keygen(id,policy):
    p = subprocess.run(['cpabe-keygen','-o','./cpabe_keys/{}_priv_key'.format(id),'./pub_key','./master_key', '{}'.format(policy)])
