import paramiko
import signal

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect("0.0.0.0",9090,"root","12345678")
stdin,stdout,stderr = client.exec_command("su arian")
# stdout.channel.setblocking(False)
stdout.channel.settimeout(1)
# print(stdout.readlines())

def handle(signum,frame):
    print("closing\n")
    client.close()
    return frame

signal.signal(signal.SIGTERM,handle)
signal.signal(signal.SIGINT,handle)