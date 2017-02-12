import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('abril-veja', 'f941f7fb036fb2836f08d8fff561b60d')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_api(customer_name, site_id, api_host):
    kellogg_url = 'http://' + api_host + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|e52fa2c5958c48b8bc232c4c189f48c0", "website|1a559720fc9f6e4e584a4f952897b4a1"],
        "caller": "bme",
        "medium": "email",
        "campaign": "%5BTeste%20Pr%C3%A9-Lan%C3%A7amento%5D%20Veja.com%20-%20As%2010%20boas%20do%20dia",
        "batch": "6a056caf16166f76a9683c83560c938e_1485993600",
        "sections": [{
                "name": "article",
                "count": 11,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
