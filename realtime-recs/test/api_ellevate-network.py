import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('ellevate-network', '68a7f0c35a48725efb301ae3dc791c2e')
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
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "The%20Morning%20Boost%20-%20LIVE",
        "batch": "d501cc7e51dae9d89028715ff30c9ac2_1486080000",
        "sections": [{
                "name": "articles",
                "count": 2,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article"]
                }]
        }, {
                "name": "jam_sessions",
                "count": 2,
                "filters": [{
                        "name": "resource-type",
                        "values": ["jam_session"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
