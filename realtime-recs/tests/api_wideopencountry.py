import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'

testdata = [
    ('Wide Open Country', 'wide-open-country')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com.tw'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_with_filter_with_exclude_group(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|b862ef9a1b505b3f18a75325288347b8", "object|23481fcf4e923fc654dfdcd44f84c429", "object|ddbc88aa1f23d2d722b16c3d6f64fc35", "object|dfff53bf3fa56162e4ed431487f400e8", "object|27a956f79a2678d7663c265851e33e20", "object|d42f2819e8522a4d175ec24cf6738342", "object|db8325e29b290919cd4c0d39d542c5f3", "article|395a352d41e7a715805e37eb610b9e11", "article|f5a7724e70755df6b91de7aae5d55988", "article|ee4799644995ebab098e9f4b9288bea7", "article|5084bcc8b8d3f3ee19782dd46491a23a", "article|f4d8f9ec46ff82b0af5d7ec07bde5af8", "article|817c3d3ed8bb51217093b16f2011ee56"],
        "caller": "bme",
        "medium": "email",
        "campaign": "WOC-Daily3-1.29",
        "batch": "677522a7d619fb45707a9c0b265aae95_1485648000",
        "sections": [{
                "name": "articles",
                "count": 15,
                "filters": []
        }, {
                "name": "featured",
                "count": 1,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P4D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
