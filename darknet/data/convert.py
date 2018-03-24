# -*- coding: utf-8 -*-
"""
This script is to convert the txt annotation files to appropriate format needed by YOLO 

Input classes is a list of classes in string format ex. ['stopsign', 'yieldsign']
Check the code under if __name__ == "__main__": for example.
"""

import os
from os import walk, getcwd
from PIL import Image


def multi_class_convert(classes):
    '''convert the txt annotation files to appropriate format needed by YOLO

    Input classes is a list of classes in string format ex. ['stopsign', 'yieldsign']
    Check the code under if __name__ == "__main__": for input example.

    File path format example, if you want to convert the "class": 
    input path = "labels/class_original/"
    output path = "labels/class/"
    image folder path/naming and path example can be seen in the same folder 
    of convert.py

        param: classes
        type: list of string
        return: None
        type: None
    '''

    def convert(size, box):
        '''convert the txt annotation files to appropriate format needed by YOLO'''
        dw = 1./size[0]
        dh = 1./size[1]
        x = (box[0] + box[1])/2.0
        y = (box[2] + box[3])/2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        return (x,y,w,h)
        
        
    """-------------------------------------------------------------------""" 

    for cls in classes:

        """ Configure Paths"""   
        mypath = "original_labels/" + cls + "_original/" # path of original labels
        outpath = "labels/" + cls +'/' # path of converted labels

        if cls not in classes:
            exit(0)
        cls_id = classes.index(cls)

        wd = getcwd()
        list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

        """ Get input text file list """
        txt_name_list = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            txt_name_list.extend(filenames)
            break
        print(txt_name_list)

        """ Process """
        for txt_name in txt_name_list:
            # txt_file =  open("Labels/stop_sign/001.txt", "r")
            
            """ Open input text files """
            txt_path = mypath + txt_name
            print("Input:" + txt_path)
            txt_file = open(txt_path, "r")
            lines = txt_file.read().split('\n') #for ubuntu, use "\r\n" instead of "\n"
            
            """ Open output text files """
            txt_outpath = outpath + txt_name
            print("Output:" + txt_outpath)
            txt_outfile = open(txt_outpath, "w")
            
            
            """ Convert the data to YOLO format """
            ct = 0
            for line in lines:
                #print('lenth of line is: ')
                #print(len(line))
                #print('\n')
                if(len(line) >= 2):
                    ct = ct + 1
                    print(line + "\n")
                    elems = line.split(' ')
                    print(elems)
                    xmin = elems[0]
                    xmax = elems[2]
                    ymin = elems[1]
                    ymax = elems[3]
                    #
                    img_path = str('%s/images/%s/%s.JPEG'%(wd, cls, 
                        os.path.splitext(txt_name)[0]))
                    #t = magic.from_file(img_path)
                    #wh= re.search('(\d+) x (\d+)', t).groups()
                    im=Image.open(img_path)
                    w= int(im.size[0])
                    h= int(im.size[1])
                    #w = int(xmax) - int(xmin)
                    #h = int(ymax) - int(ymin)
                    # print(xmin)
                    print(w, h)
                    b = (float(xmin), float(xmax), float(ymin), float(ymax))
                    bb = convert((w,h), b)
                    print(bb)
                    txt_outfile.write(str(cls_id) + " " + " ".join([str(a) 
                        for a in bb]) + '\n')

            """ Save those images with bb into list """
            if(ct != 0):
                list_file.write('%s/images/%s/%s.JPEG\n'%(wd, cls, 
                    os.path.splitext(txt_name)[0]))
                        
        list_file.close()   

def generate_training_list(classes):
    ''' Run generate_training_list after multi_class_convert, this will 
    combine all the classes text file 'class_list.txt' into one 'training_list.txt'
    file

    Input classes is a list of classes in string format ex. ['stopsign', 'yieldsign']
    Check the code under if __name__ == "__main__": for input example.

        param: classes
        type: list of string
        return: None
        type: None
    '''
    filenames = []
    for cls in classes:
        filenames.append(cls + '_list.txt')
    with open('train.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())

# won't excute when importing this file

classes = ['dumpling']
multi_class_convert(classes) # convert all classes txt annotation files to appropriate format needed by YOLO 
generate_training_list(classes) # generate training_list.txt in the training_list folder