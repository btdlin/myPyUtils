import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('kob-hubbard-tv', 'kob-hubbard-tv')
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
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "KOB%204%20Morning%20Headlines",
        "batch": "620f049cf84a1407d3627036f9b5c539_1486080000",
        "sections": [{
                "name": "kob_articles",
                "count": 6,
                "filters": []
        }, {
                "name": "kob_articlesNews",
                "count": 2,
                "filters": [{
                        "name": "section",
                        "values": ["New%20Mexico%20News"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
