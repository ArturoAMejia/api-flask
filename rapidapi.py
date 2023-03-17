import requests

url = "https://the-cocktail-db.p.rapidapi.com/search.php"

querystring = {"s":"vodka"}

headers = {
	"X-RapidAPI-Key": "229d4f461bmshc286ab79faa2474p10f6e4jsn8b0c888fbeb6",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)