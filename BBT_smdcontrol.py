from smd.smd import Master, Index
import socket
import copy
import sys
import traceback
import struct
import time
import concurrent.futures as cf

from queue import Queue


s_q = Queue(1)

class Server():
    IP = '127.0.0.1'
    bufferSize = 4

    def __init__(self, port):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = port
        self.socket.bind((self.IP, self.port))
        self.client = None

    def receive(self):
        data, address = self.socket.recvfrom(self.bufferSize)
        self.client = address
        return (data, address)


def loop_server(s: Server):
    while True:
        data = None
        try:
            data, _ = s.receive()   # receive positon data
            #print(data)
        except Exception:
            pass

        if data is not None:
            try:
                s_q.put_nowait(data)    # share it with master via queue
            except Exception:
                pass



def loop_smd(m: Master, s: Server):
    while True:

        m.send(m.Actuators[0].Read(params=[Index.JoystickX, Index.JoystickY]))
        time.sleep(0.005)
        m.pass2buffer(m.receive())
        m.findPackage()

        data = [m.Actuators[0].Sensors.data.joystickX.data, 1023 - m.Actuators[0].Sensors.data.joystickY.data]
        print(data)
        if data == [0, 0]:
            print('Joystick zero error')
        try:
            data = struct.pack('!hh', *data)
            sock.sendto(data, 0, ('localhost', 8001))
        except Exception:
            pass

        data = None
        try:
            data = s_q.get_nowait()
        except Exception:
            pass

        if data is not None:
            data = struct.unpack('!hh', data)
            #print(list(data))

            localsmd = copy.deepcopy(m.Actuators[0])
            localsmd.Configuration.data.torqueEnable.data = 1
            localsmd.PositionControl.data.setpoint.data = data[1]
            m.send(m.Actuators[0].Write(localsmd, [Index.TorqueEnable, Index.SetPosition]))
            time.sleep(0.0015)

            localsmd = copy.deepcopy(m.Actuators[1])
            localsmd.Configuration.data.torqueEnable.data = 1
            localsmd.PositionControl.data.setpoint.data = data[0]
            m.send(m.Actuators[1].Write(localsmd, [Index.TorqueEnable, Index.SetPosition]))
            time.sleep(0.0015)


try:
    smd_port = 'COM5'
except IndexError:
    print('Enter correct number of commandline arguments ')
except Exception as exc:
    raise exc


m = Master(4096, smd_port)
s_in = Server(8000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(False)
sock.settimeout(0.001)
print(m.AutoScan())


with cf.ThreadPoolExecutor(max_workers=6) as executor:
    s_exec = executor.submit(loop_server, s_in)
    m_exec = executor.submit(loop_smd, m, s_in)

    try:
        data = s_exec.result()
    except Exception:
        print('UDP server generated an exception: %s' % (traceback.format_exc()))

    try:
        data = m_exec.result()
    except Exception:
        print('Master daemon generated an exception: %s' % (traceback.format_exc()))
