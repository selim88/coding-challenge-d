import sys
import concurrent.futures
From app import BusbudBanner
From app import images


#function parallel_image_processing() gets images from images() and process them with different offered functions

def parallel_image_processing :
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(images)
        for fileobject in future.result() :
            future1 = executor.submit( BusbudBanner.load, fileobject)
            future2 = executor.submit( BusbudBanner.blur, fileobject,"6")
            future3 = executor.submit( BusbudBanner.scale_x, fileobject,"1500","BICUBIC")
            future4 = executor.submit( BusbudBanner.crop_vertical, fileobject)
            future5 = executor.submit( BusbudBanner.crop_top, fileobject,"300")
            future6 = executor.submit( BusbudBanner.crop_bottom, fileobject,"300")
            future7 = executor.submit( BusbudBanner.crop_vmiddle, fileobject,"300")
            future8 = executor.submit( BusbudBanner.save, fileobject)
      
      
