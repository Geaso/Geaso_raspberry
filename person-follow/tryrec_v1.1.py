
import socket
import sys
import car_control
import time
   

def car_move():
    pass

if __name__ == "__main__": 
    address = ('0.0.0.0', 8002)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(address)
        sock.listen(5)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    try:
        while True:
            print('waiting for connection...')
            tcpCliSock, addr = sock.accept()
            print('...connnecting from:', addr)
            while True:
                data1 =  tcpCliSock.recv(1024)
                if not data1:
                    break
                str = data1.decode('utf-8')
                cls,x1,y1,x2,y2 = str.split(' ')
                
                
                
                x_mid = float((x1+x2)/2)
                y_mid = float((y1+y2)/2)

                print ("cam middle x y", x_mid,y_mid)
                if x_mid > (160 + 30) and abs(x2-x1) < 150 :
                    print ("cam detected on right turn right")
                    car_control.t_up(80,100)
                    time.sleep(0.05)        
                elif x_mid < (160 - 30) and abs(x2-x1) < 150 :
                    print ("cam detected on left turn left")
                    car_control.t_up(100,80)
                    time.sleep(0.05)
                else :
                    car_control.t_stop(0.05)

                    
                
                '''w = int(x2)-int(x1)
                h = int(y1)-int(y2)
                cx = w/2
                maxarea = 3*w*h
                minarea = w*h/2  

                
                
                if cls == '0':
                    if cx > 3*1024/4:
                        car_control.t_up(100,80)
                        time.sleep(0.05)
                    elif cx < 1024/4:
                        car_control.t_up(80,100)
                        time.sleep(0.05) 
                    elif w*h < maxarea:
                        car_control.t_down(80,80)
                        time.sleep(0.05)
                    elif w*h < minarea:
                        car_control.t_up(80,80)
                        time.sleep()
                    else:
                        car_control.t_stop(0.05)'''
    except socket.error as msg:
        print(msg)
        GPIO.cleanup()
        tcpCliSock.close()
        sys.exit(1)
 