import cv2
import multiprocessing as mp
import detect
import time
import sys
import socket




def image_put(q, ip, port, name):
    cap = cv2.VideoCapture("http://192.168.1.101:8080/?action=stream")
    if cap.isOpened():
        print(name)

    while True:
        q.put(cap.read()[1])
        q.get() if q.qsize() > 1 else time.sleep(0.01)
        #print("555" * 25) if cap.read()[0] == False else print(" ")

def get_frames():

    camera_ip, camera_port, camera_name = "192.168.2.119", "554", "stream0"

    mp.set_start_method(method='spawn')  # init
    queue = mp.Queue(maxsize=2)
    processes = mp.Process(target=image_put, args=(queue, camera_ip, camera_port, camera_name)),
    [process.start() for process in processes]
    while True:
        yield queue.get()
        
        
def main():
    address = ('192.168.1.101',8002)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(address)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    
        


    a=detect.detectapi(weights='yolov5s.pt')
    frames=get_frames()
    for frame in frames:
        result,names =a.detect([frame])
        img=result[0][0] 
        cv2.namedWindow("video",cv2.WINDOW_NORMAL)
        cv2.imshow("video",img)
        cv2.waitKey(1)
        send_str=""
        for  cls,(x1,y1,x2,y2),conf in result[0][1]:
            print(cls,x1,y1,x2,y2,conf)
            send_str+=("%d-%d-%d-%d-%d" % (cls,x1,y1,x2,y2))
            sock.send(send_str.encode())
            time.sleep(0.05)

    
if __name__ == '__main__':
      main()
