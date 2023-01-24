# In order to work with image files we need to open them in binary mode
# That means that we are going to read and write bytes instead of text

# To read and write files in binary mode
# Just put b in r and w
# Example:
# 1) open('file.png', 'rb')
# 2) write('file.png', 'wb')


with open('/home/teknikashi/Pictures/Screenshots/gr.png', 'rb') as image:
    with open('girl.png', 'wb') as new_image:
        for bytes_ in image:
            new_image.write(bytes_)

# Example copy the file with an specific size of data
with open('/home/teknikashi/Pictures/Screenshots/gr.png', 'rb') as image:
    with open('girl1.png', 'wb') as new_image:
        chunk_size = 4096
        image_content = image.read(chunk_size)
        while len(image_content) > 0:
            new_image.write(image_content)
            image_content = image.read(chunk_size)

"""***** IMPORTANT *****"""
# The idea of using a specific size to read a file is that
# when you have big files you cannot store them into a variable
# So you need to read the file by parts using a size, like example shown below
