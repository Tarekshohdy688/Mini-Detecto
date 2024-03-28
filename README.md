# **Mini-Detecto**

You can find:
Notebook including all models and success rate comparison.
Two fruits testing videos.
Servo arduino code.
Ros1 publisher node.
In fruits folder here: [Fruits Foler](https://drive.google.com/drive/folders/1w-EiEk41VNLbixKq9Yvn83Vhl8y8OTyG?usp=drive_link)
you can find:
The training and testing datasets of Banana and Orange which can you can generate by running the first cell in the Notebook.
The .h5 whole model architecture of ANN.
The .h5 whole model architecture of CNN.
The .h5 whole model architecture of ResNet50 transfer learning.
Live webcam evaluating data.

-----------------

# **Running the Code**

After building your ROS1 workspace and uploading the arduino code to your arduino, run the following commands each in separate terminal:
```
roscore
```

```
rosrun miniproject_package miniproject.py
```

```
rosrun rosserial_python serial_node.py /dev/ttyACM0
```

the /dev/ttyACM0 should be the default running port, if not responding try:

```
rosrun rosserial_python serial_node.py /dev/ttyACM1
```

```
rostopic echo /banana_orange_topic
```
