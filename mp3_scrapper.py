import requests
from bs4 import BeautifulSoup

def scrap(link, directory):
    try:
        res = requests.get(link)
        print(res)
        if 'html' in link:
            download_song(link, directory)
            return 1        #return a success status
        elif 'htm' in link:
            soup = BeautifulSoup(res.content, 'html.parser')
            song_div = soup.find('div', class_='songList1')
            _list = song_div.find_all('div', class_='name1 f14')
            for item in _list:
                link = item.find('a', href=True)
                print(link['href'])
                download_song(('http://www.5nd.com'+link['href']), directory)
            return 1        #return a success status
    except:
        return 0

def download_song(link, directory):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    song_div = soup.find('div', class_='songAboutL')
    playBox = song_div.find('div', class_='songPlayBox')
    f = playBox.find('div', id='kuPlayer')
    download_link = 'http://mpge.5nd.com/' + str(f).split()[1].split('=')[1].split('"')[1]


    #data
    
    name_div = soup.find_all('div', class_='songAboutL')
    name = str(name_div[0]).split('<h1>')[1].split('>')[1].split('<')[0]
    i = requests.get(download_link)
    path = directory+'/'+name+'.mp3'
    
    file_object = open(path, 'wb')
    file_object.write(i.content)
    file_object.close()
    print('Successfully downloaded song',name)