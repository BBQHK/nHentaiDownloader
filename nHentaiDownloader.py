import os
import requests
from bs4 import BeautifulSoup

print('        _    _            _        _   _____                      _                 _           ')
print('       | |  | |          | |      (_) |  __ \                    | |               | |          ')
print('  _ __ | |__| | ___ _ __ | |_ __ _ _  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ')
print(' | \'_ \|  __  |/ _ \ \'_ \| __/ _` | | | |  | |/ _ \ \ /\ / / \'_ \| |/ _ \ / _` |/ _` |/ _ \ \'__|')
print(' | | | | |  | |  __/ | | | || (_| | | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ')
print(' |_| |_|_|  |_|\___|_| |_|\__\__,_|_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ver0.1')
print()

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

url = input("Please input URL (e.g. https://nhentai.net/g/344197/): ")
# os.mkdir('img')
response = requests.get(url)

if response.status_code == requests.codes.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    comicTitle = soup.find('h2', class_ = 'title')
    comicTitle = comicTitle.find('span', class_ = 'pretty').getText()
    
    print('Title: ' + comicTitle)
    imggalleryURL = soup.find_all('a', class_='gallerythumb')
    page = len(imggalleryURL)
    imggalleryURL = imggalleryURL[0].find('img').get('data-src')[:-6]
    imggalleryURL = imggalleryURL[imggalleryURL.find('.'):]
    
    try:
        os.mkdir(comicTitle)
    except:
        pass
        
    print('Processing...')
    printProgressBar(0, page, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for i in range(page + 1):
        imgURL = "https://i" + imggalleryURL + str(i) + ".jpg"

        response = requests.get(imgURL)
        if response.status_code == 200:
            with open(".\\"+ comicTitle + "\\"+ str(i) + ".jpg", 'wb') as f:
                f.write(response.content)
        printProgressBar(i, page, prefix = 'Progress:', suffix = 'Complete', length = 50)
    print('Finish!!')