import os
import requests


def test_ztf_labels():
    url = 'http://{}/ztf'.format(os.environ['TEST_URL_BASE'])
    q = requests.get(url + '/found?objid=909').json()
    labels = requests.get(url + '/found/labels').json()

    for col in q['data'][0]:
        assert col in labels
