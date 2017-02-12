import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('wide-open-pets', 'wide-open-pets')
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
        "exclude": ["website|f85dddf3e1ca270e15fafca82f543513", "website|f85dddf3e1ca270e15fafca82f543513", "object|f4d313850813416f4b1444a53f6b38ba", "object|ac790f3d15859fc9010587b3fb4c9949", "object|6f7029df366501a7b891e302fb340344", "object|83f4fcfaf89d92c8c9e3bdd1eda79f8f", "article|3ac7a94e43f45d6c1edbbbb18fb76200", "article|e5a5fda951cd6d86e88efc9dd555fd77"],
        "caller": "bme",
        "medium": "email",
        "campaign": "WOP-Daily2-2.4",
        "batch": "f005c991a2da5ab1d9773f993f45bcbe_1486080000",
        "sections": [{
                "name": "articles",
                "count": 15,
                "filters": []
        }, {
                "name": "featured",
                "count": 1,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P6D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
