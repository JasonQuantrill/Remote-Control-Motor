import socket
import pygame
import sys

pygame.init()
display = pygame.display.set_mode((300, 300))

#function to select the speed of the rover
def select_speed():
    selectingSpeed = True
    speed = ""
    while selectingSpeed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
            # checking if a key is pressed
            if event.type == pygame.KEYDOWN:
                   
                # checking if 0 was pressed
                if event.key == pygame.K_0:
                    print("Key 0 has been pressed")
                    speed = "0"
                    selectingSpeed = False

                # checking if 1 was pressed
                if event.key == pygame.K_1:
                    print("Key 1 has been pressed")
                    speed = "1"
                    selectingSpeed = False
                   
                # checking if 2 was pressed
                if event.key == pygame.K_2:
                    print("Key 2 has been pressed")
                    speed = "2"
                    selectingSpeed = False
                   
                # checking if 3 was pressed
                if event.key == pygame.K_3:
                    print("Key 3 has been pressed")
                    speed = "3"
                    selectingSpeed = False
                 
                # checking if 4 was pressed
                if event.key == pygame.K_4:
                    print("Key 4 has been pressed")
                    speed = "4"
                    selectingSpeed = False

                # checking if 5 was pressed
                if event.key == pygame.K_5:
                    print("Key 5 has been pressed")
                    speed = "5"
                    selectingSpeed = False

        encoded_speed = speed.encode() #encode data to allow it to be sent over TCP
        s.sendall(encoded_speed)       #send data
        speed = ""

def select_direction():
    direction = ""
    # creating a running loop
    while True:
           
        # creating a loop to check events that
        # are occuring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                   
                # checking if key "w" was pressed
                if event.key == pygame.K_w:
                    print("Key w has been pressed")
                    direction = "w"
                   
                # checking if key "a" was pressed
                if event.key == pygame.K_a:
                    print("Key a has been pressed")
                    direction = "a"
                   
                # checking if key "s" was pressed
                if event.key == pygame.K_s:
                    print("Key s has been pressed")
                    direction = "s"
                 
                # checking if key "d" was pressed
                if event.key == pygame.K_d:
                    print("Key d has been pressed")
                    direction = "d"

                # checking if key "d" was pressed
                if event.key == pygame.K_ESCAPE:
                    print("Key ESC has been pressed")
                    direction = "quit"

            encoded_direction = direction.encode()
            s.sendall(encoded_direction)
            direction = ""

#TCP DATA
TCP_IP = '127.0.0.1'
TCP_PORT = 65432
BUFFER_SIZE = 1024

#connecting to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#program flow
select_speed()
select_direction()
