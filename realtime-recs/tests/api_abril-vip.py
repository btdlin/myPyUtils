import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('abril-vip', 'abril-vip')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_with_filter_with_exclude_group(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|f0672524065736c4f0267d14d7e0ceb2", "website|ab91be568ec8a6424ef47e67eed05032"],
        "caller": "bme",
        "medium": "email",
        "campaign": "%5BTeste%5D%20VP%20-%20Semanal%20Autom%C3%A1tico",
        "batch": "ecf402363e0ba1acda60bfdfedb4a483_1485648000",
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
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200