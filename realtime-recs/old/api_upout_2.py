import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('upout', '7a0f18a6274829b2e0710f57eea2b6d0')
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
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "Tue%2FFri_Insiders_Newsletter_Chicago",
        "batch": "e4e5b3d5a149431c412485dbf407b40a_1485648000",
        "sections": [{
                "name": "chicago_insider",
                "count": 6,
                "filters": [{
                        "name": "resource-type",
                        "values": ["chicago_insider"]
                }]
        }, {
                "name": "chicago_contest",
                "count": 3,
                "filters": [{
                        "name": "resource-type",
                        "values": ["chicago_contest"]
                }]
        }, {
                "name": "chicago",
                "count": 3,
                "filters": [{
                        "name": "resource-type",
                        "values": ["chicago"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
