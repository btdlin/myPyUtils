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
        "exclude": ["blog-sf|a44b4290f8c5248bbe57b7b5194dbf39", "blog-sf|2b213321dee5fe7e83b7e76ffe317691", "blog-sf|a1f964a95de5c5888fdb6897fb6d11e5", "blog-sf|64987274ed5a2dcd90d68e17bf8c7c8b", "sf|200829", "sf_contest|2571", "sf_contest|2580", "sf_contest|2610", "sf_contest|2599", "sf|200110", "sf|199867", "sf|200258", "sf|199962", "sf|200107", "sf|199988", "sf|200093", "sf|200012", "sf|200092", "sf|200522", "sf|200346", "sf|200566", "sf|200681", "sf|200816", "sf|200923", "sf|200875", "sf|200325", "sf|200830", "sf|200924", "sf|196023"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Thursday_Newsletter_SF_Culture_Blog",
        "batch": "d89e3f99929d5bd4dfe47e741a8c1cb4_1485648000",
        "sections": [{
                "name": "sf",
                "count": 7,
                "filters": [{
                        "name": "resource-type",
                        "values": ["sf"]
                }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
