from queue import Queue
import socket
import threading

target = "127.0.0.1"
queue = Queue()
open_ports = []


def portscan(port):
    """
    Verifica se a porta especificada está aberta no alvo.

    Parameters:
    port (int): O número da porta a ser verificada.

    Returns:
    bool: True se a porta estiver aberta, False caso contrário.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def get_ports(mode):
    """
    Insere as portas a serem verificadas na fila de tarefas.

    Parameters:
    mode (int): O modo de verificação escolhido pelo usuário.

    Returns:
    None
    """
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)


def worker():
    """
    Executa a verificação de portas em uma thread.

    Parameters:
    None

    Returns:
    None
    """
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


def run_scanner(threads, mode):
    """
    Executa o scanner de portas.

    Parameters:
    threads (int): O número de threads a serem utilizadas no processo de verificação de portas.
    mode (int): O modo de verificação escolhido pelo usuário.

    Returns:
    None
    """
    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

