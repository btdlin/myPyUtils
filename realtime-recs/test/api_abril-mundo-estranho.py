import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('abril-mundo-estranho', 'abril-mundo-estranho')
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
        "exclude": ["website|d70fcffcdd983cf0582a91e90c872536", "website|f121b2a56ab2d4caae254bf2126ae557"],
        "caller": "bme",
        "medium": "email",
        "campaign": "ME%20-%20Semanal%20Autom%C3%A1tico",
        "batch": "2a2a1247e635f92527b1da35f60363de_1485993600",
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
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
