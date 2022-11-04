import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"


client = zeep.Client(wsdl=wsdl_url)

numero= int(input('Digite um numero para saber como se fala em inglês:'))

result = client.service.NumberToWords(
	ubiNum=numero
)

print(f"O numero {numero} em ingles é {result}")

