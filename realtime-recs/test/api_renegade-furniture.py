import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('renegade-furniture', '8f03c3ad9457f8228f3d0f88c171d625')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_api(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|3b24f22960dc7cbc9a84eb68bb6a6954", "website|3b24f22960dc7cbc9a84eb68bb6a6954"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Weekly%20Email%20%28Furniture%20Finds%20for%20You%21%29",
        "batch": "af1733086eb97d101350e5b233095016_1485648000",
        "sections": [{
                "name": "product",
                "count": 4,
                "filters": [{
                        "name": "resource-type",
                        "values": ["product"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
