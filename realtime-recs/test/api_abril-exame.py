import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('abril-exame', '4e95f0debe3619d4e92b1b9828f17942')
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
        "exclude": ["article|d9a99531c4cdf058b7a3bec3a7421c9a", "website|7779c9c94fb0fa19618502b158443286", "article|2322751", "website|cab5644bb725eedca2493b4fd7f2ce88", "website|f247398bb986fc72ccd5fc3471ca2b1b"],
        "caller": "bme",
        "medium": "email",
        "campaign": "EXAME%20DI%C3%81RIA%20%28AUTOM%C3%81TICO%29",
        "batch": "b326e3c57eb00a0557de93d704a3da33_1485648000",
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
