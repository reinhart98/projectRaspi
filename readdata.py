import urllib2
import urllib

url = 'https://republic-of-iot.000webhostapp.com/david_API/getAllEmp.php'

resp = urllib2.urlopen(url)
html = resp.read()
print html
