import socket
import readline

server_address = ('0.0.0.0', 1337)  # Замените на IP-адрес и порт вашего сервера чата

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        s.sendall(command.encode())
        data = s.recv(1024)
    return data.decode()

def complete_login(text, state):
    if not text:
        completions = send_command('cows').split()
    else:
        completions = [cow for cow in send_command('cows').split() if cow.startswith(text)]
    try:
        return completions[state]
    except IndexError:
        return None



readline.parse_and_bind("tab: complete")
readline.set_completer_delims(' \t\n;')
readline.set_completer(complete_login if 'login' in readline.get_line_buffer() else complete_say)

while True:
    command = input('> ')
    response = send_command(command)
    print(response)
