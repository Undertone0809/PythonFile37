import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import random
from matplotlib.widgets import Slider


class Scope(object):
    def __init__(self, ax, maxt=1, dt=1 / 100):
        # plt.subplots_adjust(left=0.25, bottom=0.25)
        # self.axindex = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        # self.slider = Slider(self.axindex, 'frames', 1, self.frames, valinit=1, valstep=1)
        self.frames = 1
        self.min = 0
        self.max = 50
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(self.min, self.max)
        self.ax.set_xlim(0, self.maxt)
        self.ax.set_title('Simulate Curve')

    def update(self, y):
        lastt = self.tdata[-1]
        # if lastt > self.tdata[0] + self.maxt:  # reset the arrays
        #     self.tdata = [self.tdata[-1]]
        #     self.ydata = [self.ydata[-1]]
        #     self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)

        if (y < self.min):
            self.min = y - 0.2 * y
            self.ax.set_ylim(self.min, self.max)
            self.ax.figure.canvas.draw()

        elif (y > self.max):
            self.max = y + 0.2 * y
            self.ax.set_ylim(self.min, self.max)
            self.ax.figure.canvas.draw()

        if lastt > self.tdata[0] + self.frames * self.maxt:
            self.frames += 1
            self.ax.set_xlim(0, self.frames * self.maxt)
            self.ax.figure.canvas.draw()

        # self.ax.figure.canvas.draw()

        return self.line,

    def slider_update(self):
        pass

    def get_data(self):
        return self.tdata, self.ydata


if __name__ == "__main__":
    fig, ax = plt.subplots()
    scope = Scope(ax)


    def sin_output():
        dat = random.randint(0, 100)
        scope.update(dat)


    timer = fig.canvas.new_timer(interval=10)
    timer.add_callback(sin_output)
    timer.start()
    plt.show()

import os
import matplotlib.pyplot as plt
import numpy as np
import serial
import serial.tools.list_ports
'''from scope_my'''
# import Scope
import struct
import matplotlib.animation as animation


def port_receive(ser):
    data_buffer = [0] * 4
    index_buffer = 0
    data = struct.unpack('B', ser.read(size=1))
    while ((data[0] != 0xf0) and (data[0] != 0xf7)):  # 读到标志位为止
        print("waiting for logo Out: ", data[0])
        data = struct.unpack('B', ser.read(size=1))
    if index_buffer == 4:
        dat_parse = parse_data(data_buffer[:4])
        index_buffer = 0
        print('first dat_parse: ', dat_parse)
        yield dat_parse

    while True:
        data = struct.unpack('4B', ser.read(size=4))
        dat_parse = parse_data(data)
        if dat_parse != None:
            yield dat_parse
        else:
            data = struct.unpack('B', ser.read(size=1))
            while ((data[0] != 0xf0) and (data[0] != 0xf7)):  # 读到标志位为止
                print("waiting for logo ln: ", data[0])
                data = struct.unpack('B', ser.read(size=1))


def port_init():
    ser = serial.Serial()
    port_list = list(serial.tools.list_ports.comports())
    port_all = []  # 测试,实际为空
    for pp in port_list:
        port_all.append(pp[0])
        print(pp[1])
    if (len(port_all) == 0):
        print('no port exist')
        exit()
    input_port_num = input('input port number:')
    print(port_all[int(input_port_num)])
    ser.port = port_all[int(input_port_num)]
    ser.baudrate = 800000
    ser.bytesize = 8
    ser.stopbits = 1
    ser.parity = 'N'
    ser.timeout = 3
    try:
        ser.open()
    except:
        print('serial open fail')
        exit()

    print('\n******************\n')
    print('Port %s Opening ' % input_port_num)
    print('\n******************\n')
    return ser


def parse_data(data):
    HB = data[0]
    MB = data[1]
    LB = data[2]
    if (data[3] == (0xf0 or 0xf7)):
        return (HB * 2 ** 16 + MB * 2 ** 8 + LB - 0x800000)
    else:
        return None


if __name__ == "__main__":
    ser = port_init()
    fig, ax = plt.subplots()
    scope = Scope(ax)

    ani = animation.FuncAnimation(fig, scope.update, frames=port_receive(ser), interval=10,
                                  blit=True)

    plt.show()