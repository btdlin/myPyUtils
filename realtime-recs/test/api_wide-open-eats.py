import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('wide-open-eats', 'wide-open-eats')
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
        "exclude": ["website|6480a07edb1aaa64b115bb593368c071", "object|9d78e2d20379839e41b08824921f8f42", "object|1e16c31836d171e41558f7e0a8bd5e74", "object|6f5915fe0ba45cc0db3db9860e3b75be", "object|e619e93bdd09b5b3d61d729e73d57d15", "object|5c024e92e968b6967dad8b024c24846a", "article|75bd96a8810610d9128285917005392d", "article|cda2c301b2618cf1aa88e2d115871b1c", "article|437004c736172754a9dc64c6c62f9f7d", "article|c094989f3ccca0a0b0cc4fb6a4269874", "article|b39292aad969b0cea7164cd4fa4c398d"],
        "caller": "bme",
        "medium": "email",
        "campaign": "WOE-Daily2-2.10",
        "batch": "7d71a5f370436d717ea4249f62f0faed_1486684800",
        "sections": [{
                "name": "articles",
                "count": 15,
                "filters": []
        }, {
                "name": "featured",
                "count": 1,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P6D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
