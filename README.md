# lightNet (Yes, I mimicked Darknet instruction style) 
An ultimate universal customizable object detector based on YOLO v2.

<img src="examples/stopsign_result.png" alt="stopsign_result" height="250px" width="250px"> <img src="examples/dumpling_result.jpg" alt="dumpling_result" height="250px" width="250px"> <img src="examples/hamburger_result.png" alt="hamburger_result" height="250px" width="250px">

## Installing The Base lightNet

First clone the lightNet git repository here. This can be accomplished by:
```
git clone https://github.com/AlexHtZhang/lightNet.git
cd lightNet
cd darknet
make clean
make
```
If this works you should see a whole bunch of compiling information fly by:
```
mkdir -p obj
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast....
.....
gcc -I/usr/local/cuda/include/  -Wall -Wfatal-errors  -Ofast -lm....
```
If you have any errors, try to fix them? (CUDA and OpenCV section can be helpful) If everything seems to have compiled correctly,
Great! Now you can go to the 'Detection Using A Pre-Trained Model' to try out the pretrained weight on stopsign, hamburger and dumpling.

## Detection Using A Pre-Trained Model
This section will guide you through detecting objects with our costomized YOLO system using a pre-trained model. If you don't already have Darknet installed, you should do that first.

You already have the config file for YOLO in the cfg/ subdirectory. You will have to download the [pre-trained  weight file here for dumplings](https://drive.google.com/file/d/1nupjnT9uaWSCmNOj6lD-nBcxww2LEMnG/view?usp=sharing). And just run this:
```
./darknet detector test test/dumpling.JPEG cfg/yolo-obj.cfg yolo-obj_3000_dumpling.weights
```
Assuming your dumplings weight file is in the base directory, and you 'dumpling' is the only class in your 'data/names.list' file you will see something like this:
```
0: Crop Layer: 448 x 448 -> 448 x 448 x 3 image
1: Convolutional Layer: 448 x 448 x 3 image, 64 filters -> 224 x 224 x 64 image
....
27 route  26 24
28 conv   1024  3 x 3 / 1    13 x  13 x3072   ->    13 x  13 x1024
29 conv     30  1 x 1 / 1    13 x  13 x1024   ->    13 x  13 x  30
30 detection
mask_scale: Using default '1.000000'
Loading weights from yolo-obj_3000_dumpling.weights...Done!
Enter Image Path:
```
Need enter the image path again
```
Enter Image Path: test/dumpling.JPEG
```
```
test/dumpling.JPEG: Predicted in 0.428406 seconds.
dumpling: 87%
dumpling: 88%
dumpling: 89%
dumpling: 90%
dumpling: 89%
Enter Image Path:
```
Not compiled with OpenCV, saving to predictions.png in the darknet folder instead
![Alt text](examples/dumpling_result.jpg?raw=true "dumpling_result")

Darknet prints out the objects it detected, its confidence, and how long it took to find them. Since we are using Darknet on the GPU, it's fast. If we use the CPU it takes around 6-12 seconds per image.

We didn't compile Darknet with OpenCV so it can't display the detections directly. Instead, it saves them in predictions.png. You can open it to see the detected objects.

### I want  more pretrained weight files please!
*** make sure to change 'dumpling' in the 'data/names.list' to the new name (ex. stopsign) you want to detect or it will show everything as 'dumpling' ***
[pre-trained  weight file here for stopsign](https://drive.google.com/open?id=1q2AN3JfhXLYAGZ95S3uswXspNmT1tmut).
[pre-trained  weight file here for hamburger](https://drive.google.com/file/d/12x9N_zUoNk_M4_20tba3YZ35L60s9Bsy/view?usp=sharing).

## CUDA and OpenCV (by default our code use CUDA)

### Compiling With CUDA
Darknet on the CPU is fast but it's like 500 times faster on GPU! You'll have to have an Nvidia GPU and you'll have to install CUDA. I won't go into CUDA installation in detail because it is terrifying.

Once you have CUDA installed, change the first line of the Makefile in the base directory to read:
```
GPU=1 (GPU=1 by default)
```
Now you can make the project and CUDA will be enabled. By default it will run the network on the 0th graphics card in your system (if you installed CUDA correctly you can list your graphics cards using nvidia-smi). If you want to change what card Darknet uses you can give it the optional command line flag -i <index>, like:
```
./darknet -i 1 imagenet test cfg/alexnet.cfg alexnet.weights
```
If you compiled using CUDA but want to do CPU computation for whatever reason you can use -nogpu to use the CPU instead:
```
./darknet -nogpu imagenet test cfg/alexnet.cfg alexnet.weights
```
Enjoy your new, super fast neural networks!

### Compiling With OpenCV
By default, Darknet uses stb_image.h for image loading. If you want more support for weird formats (like CMYK jpegs, thanks Obama) you can use OpenCV instead! OpenCV also allows you to view images and detections without having to save them to disk.

First install OpenCV. If you do this from source it will be long and complex so try to get a package manager to do it for you.

Next, change the 2nd line of the Makefile to read:
```
OPENCV=1 (OPENCV=0 by defalt)
```
You're done! To try it out, first re-make the project. Then use the imtest routine to test image loading and displaying:
```
./darknet imtest test/dumpling.JPEG
```
## If you want to train your own network please see the paper in 'additional' folder.
