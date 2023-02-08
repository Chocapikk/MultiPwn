import time
import socket
import argparse


banner = '''


.s5ssSs.                                        .s5SSSs.                       
   SS SS. .s    s.  .s        .s5SSSSs. s.            SS. .s s.  s.  .s    s.  
sS SS S%S       SS.              SSS    SS.     sS    S%S    SS. SS.       SS. 
SS :; S%S sS    S%S sS           S%S    S%S     SS    S%S sS S%S S%S sSs.  S%S 
SS    S%S SS    S%S SS           S%S    S%S     SS .sS::' SS S%S S%S SS `S.S%S 
SS    S%S SS    S%S SS           S%S    S%S     SS        SS S%S S%S SS  `sS%S 
SS    `:; SS    `:; SS           `:;    `:;     SS        SS `:; `:; SS    `:; 
SS    ;,. SS    ;,. SS    ;,.    ;,.    ;,.     SS        SS ;,. ;,. SS    ;,. 
:;    ;:' `:;;;;;:' `:;;;;;:'    ;:'    ;:'     `:        `:;;:'`::' :;    ;:' 



                   Chocapikk
             (https://github.com/Chocapikk)
'''

stripe_banner = ''
for i, line in enumerate(banner.splitlines()):
    for j, char in enumerate(line):
        if (j // 1) % 3 == 0:
            stripe_banner += "\033[1;32;40m" + char 
        elif (j // 1) % 3 == 1:
            stripe_banner += "\033[1;33;40m" + char 
        else:
            stripe_banner += "\033[1;31;40m" + char
    stripe_banner += "\033[0m\n"

print(stripe_banner)


def listen_on_port(port, command):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"\033[1;31;40mServer listening on port {port}\033[0m")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"\033[1;32;40mAccepted connection from {client_address[0]}:{client_address[1]}\033[0m")
            client_socket.recv(1024)
            client_socket.send(command.encode() + b'\r\n')
            time.sleep(0.1)
            response = client_socket.recv(1024)
            print(f"\033[1;33;40mReceived response: {response.decode().splitlines()}\033[0m")
            client_socket.close()
        except KeyboardInterrupt:
            print("\033[1;31;40mServer stopped\033[0m")
            break
        except:
            client_socket.close()
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='multipwn')
    parser.add_argument('port', type=int, help='The port to listen on')
    parser.add_argument('-c', '--command', type=str, default='id', help='The command to send')
    args = parser.parse_args()
    listen_on_port(args.port, args.command)
