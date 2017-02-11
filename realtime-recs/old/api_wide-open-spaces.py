import requests, json, pytest

HOST = 'recommendations-g.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('wide-open-spaces', 'wide-open-spaces')
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
        "exclude": ["website|c972225e243fb274666555b8af5fb18a", "article|131276", "object|7525e80c230d724d0ab7cc3988505881", "object|7f1b8c48c03c0b2f9b70918b49e6c3bf", "object|4816bf074ca1b073fed9e9b6d464f83c", "object|87d3512f1821418f8920345aa980a25f", "article|37ccf98f56befbe6a97fc78e1aa38c34", "article|b622d75b3f0b6860c10051ee487a14b3"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Daily-2.3-PIB",
        "batch": "9d442e3cabbd86e563324bee082d8860_1486080000",
        "sections": [{
                "name": "articles",
                "count": 15,
                "filters": [{
                        "name": "resource-type",
                        "values": ["all"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
