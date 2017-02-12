import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('business-value-exchange', 'f1c5057684a426566c7ac9984eae544b')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'jlieberman@forbes.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_api(customer_name, site_id, api_host):
    kellogg_url = 'http://' + api_host + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|4a741b31598b5c20089110cd2efc486e", "article|2e8aeeff27819080915bafc8c080ec2d", "article|adaea9e340a30bd0e8cda5038707d122", "article|4697ea91e3e04b2730d9794088164c83", "article|082a0f93e1aadae67d5aaf2aba2c9de8", "article|7c1a152c1f49b9cf2823478fce6d65a6", "article|6df264902a4d3b45c802a8290f729b81", "article|9257813cce8b2fed1630a8c47e409ad9"],
        "caller": "bme",
        "medium": "email",
        "campaign": "6.2.2017",
        "batch": "1d79ed46ad4e03fccc86354a7810db0f_1486166400",
        "sections": [{
                "name": "all",
                "count": 4,
                "filters": []
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
