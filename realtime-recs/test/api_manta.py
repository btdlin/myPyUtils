import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('manta', 'ed6e6b11168e3880f61e111016d10d9a')
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
        "exclude": ["article|d4eec3604fdc8d074acca588da415a5f", "article|8c3fc7b9c25419e76b2dfb264ad34a2a", "article|3cbc71a1038cb5c6b336adb4e7c8b669"],
        "caller": "bme",
        "medium": "email",
        "campaign": "SBT%2002032017",
        "batch": "c62da1fa256c84f231bcb7a70229dc48_1486080000",
        "sections": [{
                "name": "article",
                "count": 4,
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
