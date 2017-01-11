import requests, json, pytest

HOST = 'recommendations-e.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('Gazette', 'e9cd7a8ae2406275f6afb01b679ebf69')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'rdfulle@gmail.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_with_filter_with_exclude_group(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["thegazette_default|d73d63b3e436abc37a658e5837352f02", "website|a4564eeeac1a79fa5539044fb98f4185"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Daily%3A%20News%20%26%20Sports",
        "batch": "6532223ff8bc68b956f085fd77c886ae_1484006400",
        "sections": [{
            "name": "thegazette_default",
            "count": 4,
            "filters": [{
                "name": "resource-type",
                "values": ["thegazette_default"]
            }]
        }, {
            "name": "thegazette_sports",
            "count": 4,
            "filters": [{
                "name": "resource-type",
                "values": ["thegazette_sports"]
            }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
