def write_grayscale(filename,pixels):
    height = len (pixels)
    width = len(pixels[0])

    with open(filename, 'wb')as bmp:
        bmp.write(b'BM')
        size_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')
          
        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')    

        bmp.write(b'\x28\x00\x00\x00') 
        


