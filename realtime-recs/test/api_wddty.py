import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('wddty', 'ca946f2ad810df63aaeec9a4c29f7cb8')
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
    "exclude": ["article|0a46afff02", "website|b9e8307fc5", "website|6b6bc4c247", "article|dbc7fdee19", "news|c2ee7e5726", "news|c3fb685e8c", "news|22d56497fc", "article|dbc7fdee19", "article|0a46afff02"],
    "caller": "bme",
    "medium": "email",
    "campaign": "WDDTY%20e-News%2026%2F01%2F2017",
    "batch": "c93250a9551932eaf989000d0cefe819_1485302400",
    "sections": [{
        "name": "news",
        "count": 1,
        "filters": [{
            "name": "resource-type",
            "values": ["news"]
        }]
    }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
