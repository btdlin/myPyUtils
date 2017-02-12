import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('Trekaroo', '444d810c69d042082b674f027d106afc')
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
    if api_host == 'recommendations.api.boomtrain.com':
        kellogg_url = 'https://' + api_host + '/v1/' + site_id + '/email/'
    else:
        kellogg_url = 'http://' + api_host + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["article|5755d794736ddfd0ea84b573ff87a126", "article|784892f3e282219c7da9317159c60432", "article|26286fcc0f023a6d826746ee01b7940f", "website|b78e0e8b2ec31594fae91ab18b400aa0", "website|c446fe4e23289a2dfe7b79aa237697f3"],
        "caller": "bme",
        "medium": "email",
        "campaign": "IP%20Warm%20Up%205%20-%20Anytime",
        "batch": "5a821a981a2f1dec110c0604c2bbc8e6_1485648000",
        "sections": [{
                "name": "article",
                "count": 4,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article"]
                }]
        }, {
                "name": "guide",
                "count": 1,
                "filters": [{
                        "name": "resource-type",
                        "values": ["guide"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
