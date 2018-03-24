# lightNet
An ultimate universal customizable object detector based on YOLO v2.

## Installing The Base lightNet

First clone the lightNet git repository here. This can be accomplished by:

git clone https://github.com/AlexHtZhang/lightNet.git
cd lightnet
cd darknet
make

If this works you should see a whole bunch of compiling information fly by:

mkdir -p obj
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
.....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast -lm....

If you have any errors, try to fix them? If everything seems to have compiled correctly, try running it!

./darknet
You should get the output:

usage: ./darknet <function>
Great! Now you can go to the 'Detection Using A Pre-Trained Model' to try out the pretrained weight on stopsign, hamburger and dumpling.

## Detection Using A Pre-Trained Model
This section will guide you through detecting objects with our costomized YOLO system using a pre-trained model. If you don't already have Darknet installed, you should do that first.

You already have the config file for YOLO in the cfg/ subdirectory. You will have to download the pre-trained weight file here (753 MB). Or just run this:

wget http://pjreddie.com/media/files/yolov1.weights
./darknet yolo test cfg/yolov1/yolo.cfg yolov1.weights data/dog.jpg
I've included some example images to try in case you need inspiration. Try data/eagle.jpg, data/dog.jpg, data/person.jpg, or data/horses.jpg! Assuming your weight file is in the base directory, you will see something like this:

./darknet yolo test cfg/yolov1/yolo.cfg yolov1.weights data/dog.jpg
0: Crop Layer: 448 x 448 -> 448 x 448 x 3 image
1: Convolutional Layer: 448 x 448 x 3 image, 64 filters -> 224 x 224 x 64 image
....
27: Connected Layer: 4096 inputs, 1225 outputs
28: Detection Layer
Loading weights from yolo.weights...Done!
data/dog.jpg: Predicted in 8.012962 seconds.
0.941620 car
0.397087 bicycle
0.220952 dog
Not compiled with OpenCV, saving to predictions.png instead
Darknet prints out the objects it detected, its confidence, and how long it took to find them. Since we are using Darknet on the CPU it takes around 6-12 seconds per image. If we use the GPU version it would be much faster.

We didn't compile Darknet with OpenCV so it can't display the detections directly. Instead, it saves them in predictions.png. You can open it to see the detected objects.



## If you want to use CUDA or OpenCV (by default our code use CUDA)
Compiling With CUDA
Darknet on the CPU is fast but it's like 500 times faster on GPU! You'll have to have an Nvidia GPU and you'll have to install CUDA. I won't go into CUDA installation in detail because it is terrifying.

Once you have CUDA installed, change the first line of the Makefile in the base directory to read:

GPU=1 (GPU=1 by default)
Now you can make the project and CUDA will be enabled. By default it will run the network on the 0th graphics card in your system (if you installed CUDA correctly you can list your graphics cards using nvidia-smi). If you want to change what card Darknet uses you can give it the optional command line flag -i <index>, like:

./darknet -i 1 imagenet test cfg/alexnet.cfg alexnet.weights
If you compiled using CUDA but want to do CPU computation for whatever reason you can use -nogpu to use the CPU instead:

./darknet -nogpu imagenet test cfg/alexnet.cfg alexnet.weights
Enjoy your new, super fast neural networks!

Compiling With OpenCV
By default, Darknet uses stb_image.h for image loading. If you want more support for weird formats (like CMYK jpegs, thanks Obama) you can use OpenCV instead! OpenCV also allows you to view images and detections without having to save them to disk.

First install OpenCV. If you do this from source it will be long and complex so try to get a package manager to do it for you.

Next, change the 2nd line of the Makefile to read:

OPENCV=1 (OPENCV=0 by defalt)
You're done! To try it out, first re-make the project. Then use the imtest routine to test image loading and displaying:

./darknet imtest data/eagle.jpg

## If you want to train your own network please see the paper in 'additional' folder.
