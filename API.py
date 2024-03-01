#API---
#SOAP-SIMPLE OBJECT ACCESS PROTOCOL-
#-----#WSDL-WEB SERVICE DISCRIPTION LANGUAGE-(XML FILE)

###
import requests
#Get requests--
response = requests.get("http://216.10.245.166/Library/GetBook.php", {'ID' :'huj878'},)
print(response.text)