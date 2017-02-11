import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('cyber-creations', 'cyber-creations')
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
        "exclude": ["website|5d773f65d4b7d0a8e84d0ad60c030dd6", "website|386c3c48c6ed2c35998d39d3d2958938"],
        "caller": "bme",
        "medium": "email",
        "campaign": "MMO%20Daily%20Digest%20-%20Recurring",
        "batch": "02e0c7dbdeeadfb7a3fd6d2e2013ac6c_1485648000",
        "sections": [{
                "name": "rec_articles",
                "count": 3,
                "filters": [{
                        "name": "resource-type",
                        "values": ["game"],
                        "operator": "NOT"
                }, {
                        "name": "pubDate",
                        "values": ["-P1D"],
                        "operator": "BEFORE"
                }, {
                        "name": "pubDate",
                        "values": ["-P90D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
