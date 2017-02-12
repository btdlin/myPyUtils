import requests, json, pytest

api_host = 'recommendations-g.magic.boomtrain.com'
# api_host = 'recommendations.api.boomtrain.com'

testdata = [
    ('finder', 'finder')
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
        "exclude": ["website|919945", "article|204549", "article|297", "article|132387", "article|174749", "article|391663", "article|921507", "article|143557", "article|920585", "article|124798", "website|919945", "article|109128", "article|2519", "article|63", "article|121448", "article|569091"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Technology%20newsletter%20eDM1386",
        "batch": "b744639e60d296bed218393cd0a74b1e_1486166400",
        "sections": [{
                "name": "finder_tech",
                "count": 6,
                "filters": [{
                        "name": "pubDate",
                        "values": ["-P7D"],
                        "operator": "AFTER"
                }, {
                        "name": "tag",
                        "values": ["lead story", "top story"]
                }, {
                        "name": "section",
                        "values": ["technology", "gaming", "wearables", "internet tv", "streaming", "apps", "mobile phones", "music streaming", "broadband plans", "nbn tracker", "mobile plans", "software", "cheap phones", "virtual privacy network"]
                }]
            } 
        ]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        #print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
