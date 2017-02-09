import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('mic', '75471913db291cdd62f3092709061407')
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
        "exclude": ["|2708816a3f1a36b0bb793c4e7ab83eab", "trending|167417", "trending|167336", "trending|166814", "trending|167368", "|2708816a3f1a36b0bb793c4e7ab83eab", "trending|167417", "trending|166814", "trending|167165", "trending|167524", "trending|167477", "trending|167425", "trending|166933", "trending|167433"],
        "caller": "bme",
        "medium": "email",
        "campaign": "miccheck%202%2F2",
        "batch": "97871b7d10f789fdce1d308938092467_1486080000",
        "sections": [{
                "name": "trending",
                "count": 1,
                "filters": [{
                        "name": "resource-type",
                        "values": ["trending"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
