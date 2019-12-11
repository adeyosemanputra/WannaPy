import os
from cryptography.fernet import Fernet
import requests
import ctypes
key = raw_input("Enter your decryption key:\n")

if os.name == 'nt':
    username = str(os.getenv('username'))
    path = 'C:/Users/' + username
    pass
elif os.name == 'posix':
    path = '/home/user/Desktop/'
    pass

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith('.encrypted'):
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    try:
        with open(f, 'rb') as fileByte:
            data = fileByte.read()
    
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        if f.endswith(".encrypted"):
            filename = os.path.splitext(f)[0]
        # Write the decrypted file
        with open(filename, 'wb') as fileByte:
            fileByte.write(decrypted)
            fileByte.close()
            os.remove(f)
    except Exception as e:
        print(e)
        pass

if os.name == 'nt':
    img_data = requests.get("https://newevolutiondesigns.com/images/freebies/yellow-wallpaper-6.jpg").content
    with open('C:/Users/' + username + '/Pictures/background1.jpg', 'wb') as handler:
        handler.write(img_data)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:/Users/' + username + '/Pictures/background1.jpg' , 0)
    pass
elif os.name == 'posix':
    pass