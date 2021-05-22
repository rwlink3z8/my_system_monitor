import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent, sensors_temperatures, virtual_memory
import numpy as np



'''
get the current value of the temp of the graphics card
dict key is nouveau, 
access the tuple from the list at index 0 
and current temp is position 1
'''
gpu_temp = sensors_temperatures(fahrenheit=True)['nouveau'][0][1]
critical_gpu_temp = sensors_temperatures(fahrenheit=True)['nouveau'][0][3]

'''
get the current value of the cpu temp for the AMD cpu
k10temp is the sensor provided by the k10temp kernal module
access the tuple from the list at index 0 
and current temp is position 1
'''
cpu_temp = sensors_temperatures(fahrenheit=True)['k10temp'][0][1]
critical_cpu_temp = sensors_temperatures(fahrenheit=True)['k10temp'][0][3]

'''
RAM is a named tuple so total is at position 0, 
available at position 1, 
percent at postion 2
used position 3
'''
total_ram = round(virtual_memory()[0]/1000000000, 1)
ram_usage = round(virtual_memory()[3]/1000000000, 1)
ram_usage_percent = virtual_memory()[2]

%matplotlib notebook
plt.style.use('dark_background')
frame_length = 200
y = []
fig = plt.figure(figsize=(6,2))
def animate(i):
    y.append(cpu_percent())
    if len(y) <=frame_length:
        plt.cla()
        plt.plot(y, 'cyan', label=f'CPU Usage {y}%')
        #plt.fill_between(x, y, color='cyan', alpha=.3)
        plt.axhline(25, color='gainsboro', alpha=0.3)
        plt.axhline(50, color='gainsboro', alpha=0.3)
        plt.axhline(75, color='red', alpha=0.6)
    else:
        plt.cla()
        plt.plot(y[-frame_length:], 'cyan', label=f'CPU Usage {y}%')
        plt.axhline(25, color='gainsboro', alpha=0.3)
        plt.axhline(50, color='gainsboro', alpha=0.3)
        plt.axhline(75, color='red', alpha=0.6)
    plt.ylim(0,100)
    plt.xlabel('Time (seconds)')
    plt.title(label=f'CPU Usage {y[-1]}%', loc='left')
    plt.tight_layout()

animation = FuncAnimation(plt.gcf(), animate, interval=1000)

# ram plot
frame_length = 200
y = []
fig = plt.figure(figsize=(6,2))
def animate1(i):
    y.append(ram_usage_percent)
    if len(y) <=frame_length:
        plt.cla()
        plt.plot(y, 'green', label=f'RAM Usage {y}%')
        #plt.fill_between(x, y, color='cyan', alpha=.3)
        plt.axhline(25, color='gainsboro', alpha=0.3)
        plt.axhline(50, color='gainsboro', alpha=0.3)
        plt.axhline(75, color='red', alpha=0.6)
    else:
        plt.cla()
        plt.plot(y[-frame_length:], 'green', label=f'RAM Usage {y}%')
        plt.axhline(25, color='gainsboro', alpha=0.3)
        plt.axhline(50, color='gainsboro', alpha=0.3)
        plt.axhline(75, color='red', alpha=0.6)
    plt.ylim(0,100)
    plt.xlabel('Time (seconds)')
    plt.title(label=f'RAM Usage {y[-1]}%                                                      {ram_usage}/{total_ram} GB', loc='left')
    plt.tight_layout()

animation1 = FuncAnimation(plt.gcf(), animate1, interval=1000)

# cpu temp plot
frame_length = 200
y = []
fig = plt.figure(figsize=(6,2))
degrees= u'\N{DEGREE SIGN}F'
def animate(i):
    y.append(cpu_temp)
    if len(y) <=frame_length:
        plt.cla()
        plt.plot(y, 'm', label=f'CPU Temp {y}{degrees}')
        #plt.fill_between(x, y, color='cyan', alpha=.3)
        plt.axhline(critical_cpu_temp*.25, color='gainsboro', alpha=0.3)
        plt.axhline(critical_cpu_temp*.5, color='gainsboro', alpha=0.3)
        plt.axhline(critical_cpu_temp*.9, color='red', alpha=0.6)
    else:
        plt.cla()
        plt.plot(y[-frame_length:], 'm', label=f'CPU Temp {y}{degrees}')
        plt.axhline(critical_cpu_temp*.25, color='gainsboro', alpha=0.3)
        plt.axhline(critical_cpu_temp*.5, color='gainsboro', alpha=0.3)
        plt.axhline(critical_cpu_temp*.9, color='red', alpha=0.6)
    plt.ylim(0,critical_cpu_temp+10)
    plt.xlabel('Time (seconds)')
    plt.title(label=f'CPU Temp {y[-1]}{degrees}', loc='left')
    plt.tight_layout()

animation = FuncAnimation(plt.gcf(), animate, interval=1000)

# gpu temp plot
frame_length = 200
y = []
fig = plt.figure(figsize=(6,2))
degrees= u'\N{DEGREE SIGN}F'
def animate(i):
    y.append(gpu_temp)
    if len(y) <=frame_length:
        plt.cla()
        plt.plot(y, 'y', label=f'GPU Temp {y}{degrees}')
        #plt.fill_between(x, y, color='cyan', alpha=.3)
        plt.axhline(critical_gpu_temp*.25, color='gainsboro', alpha=0.3)
        plt.axhline(critical_gpu_temp*.5, color='gainsboro', alpha=0.3)
        plt.axhline(critical_gpu_temp*.9, color='red', alpha=0.6)
    else:
        plt.cla()
        plt.plot(y[-frame_length:], 'y', label=f'GPU Temp {y}{degrees}')
        plt.axhline(critical_gpu_temp*.25, color='gainsboro', alpha=0.3)
        plt.axhline(critical_gpu_temp*.5, color='gainsboro', alpha=0.3)
        plt.axhline(critical_gpu_temp*.9, color='red', alpha=0.6)
    plt.ylim(0,critical_cpu_temp+10)
    plt.xlabel('Time (seconds)')
    plt.title(label=f'GPU Temp {y[-1]}{degrees}', loc='left')
    plt.tight_layout()

animation = FuncAnimation(plt.gcf(), animate, interval=1000)
