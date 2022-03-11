from email.mime import image
from pathlib import Path
from typing import List
from PIL import Image;
from enum import Enum



import typer

global my_list
my_list = [1,2,3,...]

global m_list
m_list = [1,2,3,...]

app=typer.Typer(help=" Image Resizer-Converter CLI ")

@app.command(help="resize the images all to same size")
def resize(files: List[Path] = typer.Argument(..., help="The path of image in double quotes"), width: float = typer.Option(..., help="The required width of image ", prompt= "The required width of image"), height: float = typer.Option(..., help="The required height of image ", prompt= "The required height of image")):
    """
    resize the images with the given path/list of paths.
    """
    for path in files :
        if path.is_file():
            i = str(m_list[0])
            pathnamea = str(path)
            img = Image.open(path)
            print("initial dimensions  : "+str(img.width)+' x '+str(img.height))
            img = img.resize((int(width),int(height)))
            if pathnamea.endswith(".png"):
                pathnamea2 = pathnamea[0:-4] 
                newpath = pathnamea2+'_resized'+ str(img.width) +'x'+ str(img.height)     
                img.save(newpath +'.png')
                print("resized file "+i+": "+newpath+'.png')
            elif pathnamea.endswith(".jpg"):
                pathnamea2 = pathnamea[0:-4]  
                newpath = pathnamea2+'_resized'+ str(img.width) +'x'+ str(img.height)    
                img.save(newpath +'.jpg')
                print("resized file "+i+": "+newpath+'.jpg')
                img.show()
            elif pathnamea.endswith(".jpeg") :
                pathnamea2 = pathnamea[0:-5]
                newpath = pathnamea2+'_resized'+ str(img.width) +'x'+ str(img.height)      
                img.save(newpath +'.jpeg')
                print("resized file "+i+": "+newpath+'.jpeg')
                img.show()
            elif pathnamea.endswith(".tiff") :
                pathnamea2 = pathnamea[0:-5]
                newpath = pathnamea2+'_resized'+ str(img.width) +'x'+ str(img.height)      
                img.save(newpath +'.tiff')
                print("resized file "+i+": "+newpath+'.tiff')
                img.show()
            else:
                img.save(pathnamea)
                print("resized file "+i+": "+pathnamea)
                img.show()

            del m_list[0]

@app.command(help="convert  images with the given path/paths to same formats.")
def convert(files: List[Path] = typer.Argument(..., help="The path of image in double quotes"), required_type : str = typer.Option(..., help="The required file format of image", prompt="The required file format of image") ):  
    """
    converts the file formats of the images with the given path/list of paths.
    """  
    for path in files:
        if path.is_file():     
            
            pathname = str(path)
            if pathname.endswith(".png"):
                pathname2 = pathname[0:-4]
            elif pathname.endswith(".jpg"):
                pathname2 = pathname[0:-4]
            elif pathname.endswith(".jpeg") :
                pathname2 = pathname[0:-5]
            elif pathname.endswith(".tiff") :
                pathname2 = pathname[0:-5]


            j = str(my_list[0])
            img = Image.open(path)
            if required_type == 'jpg': 
                img.show()
                rgb = img.convert('RGB')
                rgb.show()
                rgb.save(pathname2+'.jpg')
                print("resized file  "+j+": "+pathname2+'.jpg')
            elif required_type == 'jpeg':
                img.show()
                rgb = img.convert('RGB')
                rgb.show()
                rgb.save(pathname2+'.jpeg')
                print("resized file  "+j+": "+pathname2+'.jpeg')
            elif required_type == 'png':
                img.save(pathname2+'.png')
                img.show()
                print("resized file  "+j+": "+pathname2+'.png')
            elif required_type == 'tiff':
                rgb = img.convert('RGB')
                rgb.show()
                img.save(pathname2+'.tiff')
                print("resized file "+j+": "+pathname2+'.tiff')
            else:
                typer.echo("Error: Invalid value for requird file format: invalid choice:" + required_type + ". (choose from png, jpeg, jpg, tiff) ")
                raise typer.Exit()


            del my_list[0]

if __name__=="__main__":
    app()                           