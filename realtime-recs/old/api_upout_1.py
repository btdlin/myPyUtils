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
        "exclude": ["blog-nyc|d807894498e18b40de8429171e793012", "blog-nyc|86c872dd676348a7ba99c93d523dae84", "blog-nyc|4cdf6c96999ba7800acf0493ee237bdb", "nyc_contest|2618", "nyc_contest|2607", "nyc_contest|2584", "nyc_contest|2623", "nyc_contest|2629", "nyc_contest|2568", "nyc_contest|2619", "nyc|200576", "nyc|199978", "nyc|200906", "nyc|200825", "nyc|200571", "nyc|200904", "nyc|200913"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Monday_Newsletter_NYC_Blog",
        "batch": "a00d180cbf5ca11f43a0d0faba6f84ba_1485648000",
        "sections": [{
                "name": "nyc",
                "count": 7,
                "filters": [{
                        "name": "resource-type",
                        "values": ["nyc"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
