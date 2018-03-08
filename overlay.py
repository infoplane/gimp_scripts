#!/usr/bin/python

import os,glob,sys,time
from gimpfu import *

def process(infile):
    print ("Processing file %s " % infile)
    image=pdb.gimp_file_load(infile,infile)
    image.scale(int(image.width*.5),int(image.height*.5))

    filename, file_extension = os.path.splitext(infile)

    pdb.gimp_file_save(image, image.active_layer, filename + '_small' + file_extension,filename + '_small' + file_extension)
    pdb.gimp_image_delete(image)

def add_layer(infile):
    print ("Processing file %s " % infile)
    image=pdb.gimp_file_load(infile,infile)

    height = pdb.gimp_image_height(image)
    width = pdb.gimp_image_width(image)

    layer1 = pdb.gimp_layer_new(image,width,height,RGBA_IMAGE,"Overlay",40,NORMAL_MODE) #NORMAL_MODE

    pdb.gimp_context_set_background((96,96,96))

    pdb.gimp_drawable_fill(layer1, BACKGROUND_FILL)

    image.add_layer(layer1,0)

    image.flatten()


    filename, file_extension = os.path.splitext(infile)

    pdb.gimp_file_save(image, image.active_layer, filename + '_overlay' + file_extension, filename + '_overlay' + file_extension)
    pdb.gimp_image_delete(image)

def run(directory, process):
    start=time.time()
    print ("Running on directory \"%s\"" % directory)

    if process == 'test':
        file_Extentsions = ['*.jpg','*.png']
        listoffiles = []

        for extension in file_Extentsions:
            listoffiles.extend(glob.glob(os.path.join(directory, extension)))

        for file in listoffiles:
            print(file)




    if process == 'overlay':

        file_Extensions = ['*.jpg','*.png']
        listoffiles = []

        for extension in file_Extensions:
            listoffiles.extend(glob.glob(os.path.join(directory, extension)))


        for file in listoffiles:
            print(file)
            add_layer(file)



        #for infile in glob.glob(os.path.join(directory, '*.jpg')):
        #    add_layer(infile)



    elif process == 'smaller':
        for infile in glob.glob(os.path.join(directory, '*.jpg')):
            process(infile)


    end=time.time()
    print ("Finished, total processing time: %.2f seconds" % (end-start))




if __name__ == "__main__":
        print ("Running as __main__ with args: %s" % sys.argv)

        run(sys.argv[1], sys.argv[2])


## This file can be run from the command line using the below string
##
# gimp-2.8 -idf --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import overlay;overlay.run('./images','overlay')" -b "pdb.gimp_quit(1)"
