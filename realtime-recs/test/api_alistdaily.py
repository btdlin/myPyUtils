import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('alistdaily', '883617d0eb6793113323ba5e36470778')
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
        "exclude": ["website_alist|44224", "website_alist|23013", "website_alist|23012", "website_alist|44224"],
        "caller": "bme",
        "medium": "email",
        "campaign": "%5Ba%5Dlistdaily%20Newsletter%20-%20All",
        "batch": "076e57ebbd9878725a81367bd56c89de_1486080000",
        "sections": [{
                "name": "articles",
                "count": 5,
                "filters": [{
                        "name": "resource-type",
                        "values": ["article_alist"]
                }, {
                        "name": "pubDate",
                        "values": ["-P7D"],
                        "operator": "AFTER"
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
