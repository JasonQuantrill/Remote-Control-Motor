Using keyboard as input method.

![image](https://user-images.githubusercontent.com/91751222/138609154-d3341b63-0bce-43ff-ac23-2e3c68248e46.png)


Client (input.py) connects to server (output.py).
Client accepts user-input and sends that data to server.

Output first asks the client to specify a speed, from 0 to 5. If client inputs anything other than 0,1,2,3,4,5 then nothing is registered, and the program continues waiting for appropriate input. Once correct input is entered, the speed is set. This speed is the pwm and will be used to scale from 0 (stopped) to 255 (max speed).

After speed is accepted, direction input is then asked for from client. Valid input is w, a, s, d, ESC. No other input is registered from user. Direction is used to assign which wheels rotate forward and which wheels rotate in reverse. 

Speed and direction are given to function assign_motor_speed, which appropriately assigns the speed and direction of each motor/wheel. This information is then printed. The server then waits for the next input from the client. If ESC is pressed, the loop is exited, server connection severed, and program ends.
