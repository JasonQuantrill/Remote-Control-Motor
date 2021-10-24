import socket
import time

class Motor:
    def __init__(self, direction, speed):
        self.direction = direction
        self.speed = speed

#receives input from client
def receive_input():
    data = conn.recv(BUFFER_SIZE)
    return data.decode()

#selects speed of rover
def select_speed():
    selectingSpeed = True
    print("Select speed from 0 to 5")
    while True:
        speed = receive_input()
        print(speed)
        if speed >= "0" and speed <= "5": #ensuring valid input from user
            print("Selected speed: ", speed)
            return speed

def assign_motor_speed(direction, mwv):
    #direction: forward
    if direction == "w":
        m1.direction = "f"
        m2.direction = "f"
        m3.direction = "f"
        m4.direction = "f"

    #direction: left   
    elif direction == "a":
        m1.direction = "r"
        m2.direction = "r"
        m3.direction = "f"
        m4.direction = "f"

    #direction: backwards
    elif direction == "s":
        m1.direction = "r"
        m2.direction = "r"
        m3.direction = "r"
        m4.direction = "r"

    #direction: right
    elif direction == "d":
        m1.direction = "f"
        m2.direction = "f"
        m3.direction = "r"
        m4.direction = "r"

    #digital input scaling to 255
    #where 0 corresponds to 0 (stopped), 5 corresponds to 255 (top speed)
    m1.speed = int(mwv * 255 / 5)
    m2.speed = int(mwv * 255 / 5)
    m3.speed = int(mwv * 255 / 5)
    m4.speed = int(mwv * 255 / 5)

def display_motor_speed():
    print("[", m1.direction, m1.speed, "]", sep='', end='')
    print("[", m2.direction, m2.speed, "]", sep='', end='')
    print("[", m3.direction, m3.speed, "]", sep='', end='')
    print("[", m4.direction, m4.speed, "]", sep='', end='\n\n')

#Creating motor objects
m1 = Motor("f", 0)
m2 = Motor("f", 0)
m3 = Motor("f", 0)
m4 = Motor("f", 0)

#TCP data
TCP_IP = '127.0.0.1'
TCP_PORT = 65432
BUFFER_SIZE = 20

#accepting client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

#selecting the speed of rover
speed = select_speed()

while True:
    direction = receive_input()   #selecting direction of rover
    if direction == "quit": break #exit loop, close connection, end program
    assign_motor_speed(direction, int(speed)) #using input to assign motor speed/direction
    display_motor_speed()   #displaying speed/direction of motor
conn.close()
