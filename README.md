# Imagic
Image Converter - Resizer Cli

This project is a command line tool that made using python and typer. It is used to resize the images and converts the file formats of the image.It is really difficult and tedious when you have hundrends of images to process them one by one. so this cli accepts a path of an image or a list of path of an multiple images in your system to process it. It can process the group of images to make it all the same dimensions or same format an it can also process each of them separately. It is an easy to handle cli in which everything you need to enter has explained in the help arguments ang in the prompts.


## Team members
1.Aiswarya Pradeep [https://github.com/aiswaryapradeep]
2.Haripriya S[https://github.com/Haripriya7012]


## Team Id
Python / 254


## Link to product walkthrough

https://loom.com/share/96c685df72614ed3938160070f1c8b19

## How it Works ?
1.for viewing the help argument use the command-

python .\main.py [command] --help

2.for processing images use the command-

python .\main.py [command] [list of path to the images or sing path] 

3.enter the values according to the prompts that appears.
width, height should be integer or float.
required_type should be a string


[command] are convert, resize

each of the resized/converted file will be saved as a new file in the same folder as the initial images


## Libraries used

image from email.mime 
Path from pathlib 
List from typing
Image from PIL 
Enum from enum import 


## How to configure

install and import typer using

pip install typer


## How to Run

open terminal, navigate through the files to reach the main.py
enter the command

python .\main.py [--help]




# What files can be used ?
### png, jpg,jpeg, tiff
Personally i convert a lot of .psd , .TIF and .dng files !!! 
