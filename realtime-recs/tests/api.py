import requests, json, pytest

HOST = 'recommendations-e.magic.boomtrain.com'
# HOST = 'recommendations.api.boomtrain.com'

testdata = [
    ('YP Canada EN', '593964c3c0f76bc59c65b324f9dbf869'),
    ('Atlanta Black Star', 'atlanta-black-star'),
    ('Hubspot', 'hubspot-blog'),
    ('Gazette', 'e9cd7a8ae2406275f6afb01b679ebf69'),
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('THG', 'fe3d1b4f09f60315d2bbfb27557a10e3'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631')
]

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Cache-Control': 'no-cache',
           'Postman-Token': '96779af4-01ad-02ef-f010-f47f9a8f3665'}

USERS = {
        'rich.shartzer@gmail.com',
        'andre.duarte@bancovotorantim.com.br',
        'kevinaudri1593@gmail.com',
        'j.chasse@live.ca',
        'kimwedd87@gmail.com'
    }

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_no_filter_no_exclude(customer_name, site_id):
    _url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "November%20subscribers%20%282%20of%202%29",
        "batch": "8e9e1cbe962d96e61fb4594a81872955_1479513600",
        "sections": [{
            "name": "all",
            "count": 2,
            "filters": []
        }]
    }

    urls = [_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_no_filter_with_exclude(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["article|2a9897b9f56088c2916bb3403cfff631", "research|4647", "research|4650", "research|4643",
                    "article|4648"],
        "caller": "bme",
        "medium": "email",
        "campaign": "November%20subscribers%20%282%20of%202%29",
        "batch": "8e9e1cbe962d96e61fb4594a81872955_1479513600",
        "sections": [{
            "name": "all",
            "count": 2,
            "filters": []
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_with_filter_with_exclude(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": ["website|ba9b8c3a04eaf7476656467a60a5a6b7", "website|ba9b8c3a04eaf7476656467a60a5a6b7", "article|e8ff11e9ec17d64e4042fff4deac7790", "deal|e91806bf5fceed4f4b55a69e546e577e", "deal|b787167a87761e4aff1c92233ab9ba13", "|217ac1efda778f901ce68af15bcc647a", "Plan_Tool|bbe905eb2929b5cc5ae352eca3ef95cf", "|217ac1efda778f901ce68af15bcc647a", "website|ba9b8c3a04eaf7476656467a60a5a6b7"],
        "caller": "bme",
        "medium": "email",
        "campaign": "Copy%20of%20Thursday%20Send%20-%20to%20sign%20ups%20and%20validated%20users%204%2F14",
        "batch": "15647e05ade9b107dce9516b0e57d5cf_1479772800",
        "sections": [{
                "name": "News",
                "count": 5,
                "filters": [{
                    "name": "resource-type",
                    "values": ["News"]
                }]
            }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_with_filter_with_exclude_group(customer_name, site_id):
    kellogg_url = 'http://' + HOST + '/v1/' + site_id + '/email/'
    payload = {
        "exclude": [],
        "caller": "bme",
        "medium": "email",
        "campaign": "BT%3A%20Filters%20added",
        "batch": "d4804179278238152a35d51f6b69637d_1481155200",
        "sections": [{
            "name": "pw_bid_cat",
            "count": 2,
            "filters": []
        }, {
            "name": "pw_bid_fam",
            "count": 2,
            "filters": []
        }, {
            "name": "pw_bid_ind",
            "count": 2,
            "filters": []
        }, {
            "name": "pw_watch_cat",
            "count": 1,
            "filters": []
        }, {
            "name": "pw_watch_fam",
            "count": 1,
            "filters": []
        }, {
            "name": "pw_watch_ind",
            "count": 1,
            "filters": []
        }, {
            "name": "pw_nofilter",
            "count": 9,
            "filters": [{
                "name": "closed",
                "values": ["0"]
            }]
        }]
    }

    urls = [kellogg_url + email + '?test=false' for email in USERS]

    for url in urls:
        print(url)
        r = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        assert r.status_code == 200
