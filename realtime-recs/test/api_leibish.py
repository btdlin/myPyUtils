import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('leibish', '8bf9fa832a2cf351cf1a19098038459d')
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
    if api_host == 'recommendations.api.boomtrain.com':
        kellogg_url = 'https://' + api_host + '/v1/' + site_id + '/email/'
    else:
        kellogg_url = 'http://' + api_host + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["home_page|998c8eea5f4d7325b772a00d63dfae7e", "|2f6dfeaed24dc4db3a9ae80a6efc1d9d", "|f54ff3aa81e108897940e32fa82af533", "|ea6c06dd8e2c8b7ce643709c7584c0d6", "|4b722b38361e853b384aba9cf29c126a", "|d9991f15e6e5a4b83c3ed94d0f2ed057"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Monthly%20Automated%20Newsletter",
        "batch": "74b369dc709b3112bbac3223242af637_1486080000",
        "sections": [{
                "name": "article_en",
                "count": 4,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article_en"]
                }]
        }, {
                "name": "product_en",
                "count": 4,
                "filters": [{
                        "name": "resource-type",
                        "values": ["product_en"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
