# Problem Set 5
from PIL import Image, ImageFont, ImageDraw
import numpy

def make_matrix(color):
    '''
    - color: string, with exactly one of the following values:
        'red', 'blue', 'green', or 'none'.
    ---
    #### return:
        matrix, a transformation matrix corresponding to deficiency 
        in that color.
    ---
    Generates a transformation matrix for the specified color.
    '''
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c

def matrix_multiply(m1, m2):
    '''
    - m1, m2: the input matrices.
    ---
    #### return:
        list, matrix product of m1 and m2
        in a list of floats.
    ---
    Multiplies the input matrices.
    '''
    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result

def img_to_pix(filename):
    '''
    - filename: string, representing an image file, such as 'lenna.jpg'.
    ---
    #### return: 
        list, pixel values 
            in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image.
            in form L such as [60,66,72...] for BW image.
    ---
    #### Note:
        For RGB images, each pixel is a tuple containing (R,G,B) values.
        For BW images, each pixel is an integer.
    Don't worry about determining if an image is RGB or BW.\n
    The PIL library functions you use will return the correct pixel values for either image mode.
    
    ---
    Takes a filename (must be inputted as a string with proper file attachment 
    (ex: .jpg, .png) and converts to a list of representing pixels.
    '''
    with Image.open(filename) as img:
        return list(img.getdata())

def pix_to_img(pixels_list, size, mode):
    '''
    - pixels_list: list, pixels such as the output of 
        img_to_pixels.
    - size: tuple, (width,height) representing
        the dimensions of the desired image.
    - mode: 'RGB' or 'L' to indicate an RGB image or a 
        BW image, respectively.
    ---
    #### return:
        img, Image object made from list of pixels.
    ---
    #### Note:
    Assume that size is a valid input such that size[0] * size[1] == len(pixels).
    
    ---
    Creates an Image object from a inputted set of RGB tuples.
    '''
    new_filename = 'Filtered image_15.png'
    img = Image.new(mode, size)
    img.putdata(pixels_list)
    img.save(new_filename)
    
    return img

def filter(pixels_list, color):
    '''
    - pixels_list: list, pixels in RGB form, such as
        [(0,0,0),(255,255,255),(38,29,58)...].
    - color: string, 'red', 'blue', 'green', or 'none', must be a string 
        representing the color deficiency that is being simulated.
    ---
    #### return: 
        list, pixels in same format as earlier functions, 
        transformed by matrix multiplication.
    '''
    m1 = make_matrix(color)
    transf_list = []
    
    # Loop: iterate over each pixel in 'pixel_list'
    for p in pixels_list:
        pix_list = [[p[0]], [p[1]], [p[2]]]
        prod = matrix_multiply(m1, pix_list)
        
        rgb_list = []
        
        # Loop: iterate over each index in matrix product list
        for i in range(len(prod)):
            value = int(prod[i][0])
            rgb_list.append(value)
        
        transf_list.append(tuple(rgb_list))
    
    return transf_list

def extract_end_bits(num_end_bits, pixel):
    '''
    - num_end_bits: the number of end bits to extract.
    - pixel: int, between 0 and 255, or a tuple of RGB values between 0 and 255.
    ---
    #### return:
        the num_end_bits of pixel, as an integer (BW) or tuple of integers (RGB).
    ---
    Extracts the last num_end_bits of each value of a given pixel.
    '''
    # example for BW pixel:
    #     num_end_bits = 5
    #     pixel = 214

    #     214 in binary is 11010110. 
    #     The last 5 bits of 11010110 are 10110.
    #                           ^^^^^
    #     The integer representation of 10110 is 22, so we return 22.

    # example for RBG pixel:
    #     num_end_bits = 2
    #     pixel = (214, 17, 8)

    #     last 3 bits of 214 = 110 --> 6
    #     last 3 bits of 17 = 001 --> 1
    #     last 3 bits of 8 = 000 --> 0

    #     so we return (6,1,0)
    if isinstance(pixel, tuple):
        return tuple(map(lambda x: x % (2**num_end_bits), pixel))
    
    return pixel % (2**num_end_bits)

def reveal_bw_image(filename):
    '''
    - filename: string, input BW file to be processed.
    ---
    #### return:
        an Image object containing the hidden image.
    ---
    Extracts the single LSB for each pixel in the BW input image. 
    '''
    with Image.open(filename) as img:
        size = img.size
        data = list(img.getdata())
    
    # Loop: iterate over each object in 'data'
    bits = [extract_end_bits(1, d) for d in data]
    rescale = [p * 255 for p in bits]
    
    new_filename = 'Unhidden hidden1.bmp'
    new_img = Image.new('L', size)
    new_img.putdata(rescale)
    new_img.save(new_filename)
    
    return new_img

def reveal_color_image(filename):
    '''
    - filename: string, input BW file to be processed.
    ---
    #### return:
        an Image object containing the hidden image.
    ---
    Extracts the 3 LSBs for each pixel in the BW input image. 
    '''
    with Image.open(filename) as img:
        size = img.size
        data = list(img.getdata())
        
    bits_color = []
    
    # Loop: iterate over each object in 'data'
    for d in data:
        bits = extract_end_bits(3, d)
        rgb = []
        
        # Loop: iterate over each item in tuple 'bits'
        for b in bits:
            color = b * 255
            rgb.append(color)
            
        bits_color.append(tuple(rgb))
    
    new_filename = 'Unhidden hidden2.bmp'
    new_img = Image.new('RGB', size)
    new_img.putdata(bits_color)
    new_img.save(new_filename)
    
    return new_img


def reveal_image(filename):
    '''
    - filename: string, input BW file to be processed.
    ---
    #### return:
        an Image object containing the hidden image.
    ---
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a color image) 
    for each pixel in the input image.\n
    Hint: you ca nuse a function to determine the mode of the input image 
    (BW or RGB) and then use this mode to determine how to process the image.
    '''
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)

def draw_kerb(filename, kerb):
    '''
    - filename: string, input BW or RGB file.
    - kerb: string, your kerberos.
    ---
    Saves output image to "filename_kerb.xxx".\n
    Draws the text "kerb" onto the image located at "filename" and return a PDF.
    '''
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return

def main():
    pass
    # Uncomment the following lines to test part 1
    im = Image.open('image_15.png')
    width, height = im.size
    pixels = img_to_pix('image_15.png')

    non_filtered_pixels = filter(pixels,'none')
    im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    im.show()

    red_filtered_pixels = filter(pixels,'red')
    im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')
    im2.show()

    # Uncomment the following lines to test part 2
    im = reveal_image('hidden1.bmp')
    im.show()

    im2 = reveal_image('hidden2.bmp')
    im2.show()
    
    # im1 = 'Filtered image_15.png'
    # im2 = 'Unhidden hidden1.bmp'
    # im3 = 'Unhidden hidden2.bmp'
    
    # print(draw_kerb(im1, 'mykerb'))
    # print(draw_kerb(im2, 'mykerb'))
    # print(draw_kerb(im3, 'mykerb'))

if __name__ == '__main__':
    main()