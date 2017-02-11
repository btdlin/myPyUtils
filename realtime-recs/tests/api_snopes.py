import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('snopes', 'snopes')
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
        "exclude": ["website|5546e6d05228e32e558fcaf78964199b", "website|c0dd2a7d1029d637c1d530b8a0a145ee", "website|7b267bf79aba7e6bd7b7dac9a38ff03e", "website|eb99349392137d784db5eff86e48bf85"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Legacy%20Users%20-%20Wednesday%20%2B%20Saturday",
        "batch": "3d75826e9215bf476b33cd99fa04687c_1485734400",
        "sections": [{
                "name": "article",
                "count": 5,
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
