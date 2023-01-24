import requests
import os
import datetime
import threading

def download_image(image_amount):
    for num in range(image_amount):
        random_image = f'https://picsum.photos/id/{num}/1920/1080'
        req = requests.get(random_image, stream=True)

        if req.status_code == 200:
            with open(f'images/{num}.png', 'wb') as file:
                for chunk in req:
                    file.write(chunk)

                print(f'{num} downloaded!')


start_time = datetime.datetime.now()
download_image(image_amount=10)
end_time = datetime.datetime.now()
print('File downloaded ', os.listdir('./images'))
print(f'This program took: {end_time - start_time}')


def download_image(image_amount):
    for num in range(image_amount):
        random_image = f'https://picsum.photos/id/{num}/1920/1080'
        req = requests.get(random_image, stream=True)
        if req.status_code == 200:
            with open(f'images/{num}.png', 'wb') as file:
                for chunk in req:
                    file.write(chunk)
            print(f'{num} downloaded! ')



# Execute program with five threads
start_time = datetime.datetime.now()

threads = []

for i in range(5):
    t1 = threading.Thread(target=download_image , args=(10,))
    threads.append(t1)
    t1.start()

for thread in threads:
    thread.join()


end_time = datetime.datetime.now()
print(f'This program took: {end_time - start_time}')