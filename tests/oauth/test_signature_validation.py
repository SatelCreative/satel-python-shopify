import pytest

# Initially tested with real data generated by Shopify and
# a valid secret key. Then once passing, swapped characters
# in the query strings out with random & generated a new hmac
# with a fake secret key.

API_SECRET_KEY = 'fake_shopify123secret456key789'

install = 'hmac=fe078eb09b2b418b5db8c4efd2093ccab0855f28b3bc7d99e14c4971cf4ae670&host=XbFtofRsfgmNkF7qz32ytwZKHeAy7LPosJhqt93&shop=example-store.myshopify.com&timestamp=1654212701'
embedded = 'hmac=3ec71fde88e45edee545bd79ff92da068661ec6298dcfbfb9da8f357dc16729b&host=XbFtofRsfgmNkF7qz32ytwZKHeAy7LPosJhqt93&locale=en-CA&session=76ef4wam8rhmm4qdertc5z36qu42i349syobtivqua9ih6hh667akenccbcur9de&shop=example-store.myshopify.com&timestamp=1654212956'
admin_link = 'hmac=38a63775f637952cfcd9ef387367fad7ab0ffec892061c383031aacbb5c881ed&host=XbFtofRsfgmNkF7qz32ytwZKHeAy7LPosJhqt93&id=4729471893592&locale=en-CA&session=76ef4wam8rhmm4qdertc5z36qu42i349syobtivqua9ih6hh667akenccbcur9de&shop=example-store.myshopify.com&timestamp=1654214567'
bulk_link = 'hmac=c1de8aff907271dd12d191f9ba41f1080c630c8b223c7706341a2329f4df2c7f&host=XbFtofRsfgmNkF7qz32ytwZKHeAy7LPosJhqt93&ids%5B%5D=4729471893592&ids%5B%5D=4751729295448&ids%5B%5D=4751914860632&ids%5B%5D=4751918727256&ids%5B%5D=6752260456536&locale=en-CA&session=76ef4wam8rhmm4qdertc5z36qu42i349syobtivqua9ih6hh667akenccbcur9de&shop=example-store.myshopify.com&timestamp=1654214623'

valid_params = [
    pytest.param(install, API_SECRET_KEY, id='install'),
    pytest.param(embedded, API_SECRET_KEY, id='embedded'),
    pytest.param(admin_link, API_SECRET_KEY, id='admin link'),
    pytest.param(bulk_link, API_SECRET_KEY, id='admin bulk link'),
]


@pytest.mark.parametrize('query_string,api_secret_key', valid_params)
def test_signature_validation(query_string, api_secret_key):
    from spylib.oauth import validate_signed_query_string

    validate_signed_query_string(query_string=query_string, api_secret_key=api_secret_key)
