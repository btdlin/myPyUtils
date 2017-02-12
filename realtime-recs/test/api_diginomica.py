import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'

testdata = [
    ('Diginomica', '3c499a166380645f83154eb95983ed96')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com.tw'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_api(customer_name, site_id, api_host):
    kellogg_url = 'http://' + api_host + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "Newsletter%20-%20Daily%20Content",
        "batch": "3d6f71e04f8c18b86ba437c830d22472_1485648000",
        "sections": [{
                "name": "dgn_recent_2d",
                "count": 3,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P2D"],
                        "operator": "AFTER"
                }]
        }, {
                "name": "dgn_all",
                "count": 5,
                "filters": []
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
