import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://moodle.fei.edu.br/login/index.php')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o site no momento')
else:
    print('\033[32mConsegui acessar o site!!\n')
    #print(site.read())
