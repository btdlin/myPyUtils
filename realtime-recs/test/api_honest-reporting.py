import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('honest-reporting', 'honest-reporting')
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
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "Test",
        "batch": "6a691dbcb09c40245d5b7f2c11f32c0f_1485993600",
        "sections": [{
                "name": "hr_recent",
                "count": 1,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P2D"],
                        "operator": "AFTER"
                }]
        }, {
                "name": "hr_all",
                "count": 5,
                "filters": []
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
