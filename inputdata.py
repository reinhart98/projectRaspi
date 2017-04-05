import urllib
import urllib2

url ="https://republic-of-iot.000webhostapp.com/david_API/addEmp.php"

values = {'name' : 'david',
          'desg' : 'parepare',
          'salary' : '9999'} 


data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

