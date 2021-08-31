from spylib.store import Store
from spylib.application import ShopifyApplication
from typing import Dict, Tuple
from fastapi import FastAPI
from fastapi.testclient import TestClient


def initialize_store() -> Tuple[ShopifyApplication, FastAPI, TestClient]:
    tokens: Dict[str, str] = {}

    # These are the methods passed into the store to save the tokens
    def save_token(self, store_name: str, key: str):
        tokens[store_name] = key

    def load_token(self, store_name: str):
        return tokens[store_name]

    # Create a store that we will be accessing
    store = Store(
        store_name='test-store',
        save_token=save_token,
        load_token=load_token,
    )

    # Generate our application which includes the store
    shopify_app = ShopifyApplication(
        app_domain='test.testing.com',
        shopify_handle='test.myshopify.com',
        app_scopes=['write_products', 'read_customers'],
        client_id='test.testing.com',
        client_secret='TESTPRIVATEKEY',
        stores=[store],
    )

    # Generating the fastAPI routes, and the client for testing
    app = FastAPI()

    oauth_router = shopify_app.generate_oauth_routes()

    app.include_router(oauth_router)

    client = TestClient(app)

    return (shopify_app, app, client)
