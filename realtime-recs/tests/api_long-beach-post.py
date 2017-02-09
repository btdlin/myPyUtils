import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('long-beach-post', 'long-beach-post')
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
        "exclude": ["website|b4c6d99eaab70be4d88550facb324cf8"],
        "caller": "bme",
        "medium": "email",
        "campaign": "eALERT%20%28Thursday%2002.02.17%29",
        "batch": "3d7e4d8898c2065c027673f5d4403617_1486080000",
        "sections": [{
                "name": "lbpost",
                "count": 10,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P1D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
