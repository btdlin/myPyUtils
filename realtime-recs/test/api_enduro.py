import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('enduro', '73007f3ae1ca2c1c94a3f99644769d6a')
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
        "exclude": ["article_de|119264", "article_de|147017"],
        "caller": "bme",
        "medium": "email",
        "campaign": "ENDURO%20Newsletter%20DE%2C%20user%20with%20names",
        "batch": "0a06b29a1ab9ac2988173b01c2078c92_1485648000",
        "sections": [{
                "name": "article_de",
                "count": 6,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article_de"]
                }]
        }, {
                "name": "video_de",
                "count": 2,
                "filters": [{
                        "name": "resource-type",
                        "values": ["video_de"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
