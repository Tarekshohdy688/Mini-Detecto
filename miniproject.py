#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from keras.models import load_model
import time
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2
from tensorflow.keras.applications.resnet50 import preprocess_input



def capture_and_publish():
    model = load_model('./fruits/ANN_model/ANN.h5')
    rospy.init_node('miniproject', anonymous=True)
    pub = rospy.Publisher('banana_orange_topic', Bool, queue_size=10)
    rate = rospy.Rate(10)
    cam_live=cv2.VideoCapture(0)

    i=5
    m=0
    n=0
        # orange = 1
        # banana = 0
    success_index = 1
    success_of_fruit=0
    for n in range(3):
        for m in range(5):
            if n==0:
                name = './fruits/data/live/ROS/ANN/fruit'+str(i)+'.jpg'
            elif n==1:
                name = './fruits/data/live/ROS/CNN/fruit'+str(i)+'.jpg'
            elif n==2:
                name = './fruits/data/live/ROS/ResNet50/fruit'+str(i)+'.jpg'
            frame = cam_live.read()[1]
            cv2.imwrite(name, frame)
            frame = cv2.resize(frame, (400,800))
            img=image.load_img(name, target_size=(400,800))
            x=image.img_to_array(img)
            x=np.expand_dims(x, axis=0)
            predictions=model.predict(x)
            x=preprocess_input(x)
            print ('Creating...' + name)
            i-=1
            print('class:',np.argmax(predictions[0]))
            rospy.sleep(1)
            if np.argmax(predictions[0]) == success_index:
                success_of_fruit+=1
            else:
                continue

        print(success_of_fruit)
        if success_of_fruit > 2: #so it's an orange
            pub.publish(True)
            print('This is Orange')
        else: # so it's a banana
            pub.publish(False)
            print('This is Banana')

        success_of_fruit=0 # reinitialize to 0 to start the next model
        i=5

    cam_live.release()        
    rospy.signal_shutdown("End Process")

if __name__ == '__main__':
    try:
        capture_and_publish()
    except rospy.ROSInterruptException:
        pass