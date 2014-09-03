import sys
import concurrent.futures
From app import BusbudBanner
From app import images

def parallel_image_processing :
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(images)
        future1 = executor.submit( BusbudBanner.load, future.result())
        future2 = executor.submit( BusbudBanner.blur, future.result(),"6")
        future3 = executor.submit( BusbudBanner.scale_x, future.result(),"1500","BICUBIC")
        future4 = executor.submit( BusbudBanner.crop_vertical, future.result())
        future5 = executor.submit( BusbudBanner.crop_top, future.result(),"300")
        future6 = executor.submit( BusbudBanner.crop_bottom, future.result(),"300")
        future7 = executor.submit( BusbudBanner.crop_vmiddle, future.result(),"300")
        future8 = executor.submit( BusbudBanner.save, future.result())
      
      
