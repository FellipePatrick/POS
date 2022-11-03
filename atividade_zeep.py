import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"


client = zeep.Client(wsdl=wsdl_url)

capital= str(input('Digite a sigla do país que você quer saber a capital:'))
result = client.service.CapitalCity(
	sCountryISOCode=capital
)

print(f"O código de telefone do {capital} é {result}")

