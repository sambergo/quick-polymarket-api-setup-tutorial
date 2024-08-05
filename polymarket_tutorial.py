from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY

HOST = "https://clob.polymarket.com"
CHAIN_ID = POLYGON
# Private key we exported from polymarket UI
KEY = "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Funder we got from polymarket UI
FUNDER = "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create CLOB client and get/set API credentials
client = ClobClient(
    HOST,
    key=KEY,
    chain_id=CHAIN_ID,
    funder=FUNDER,
    signature_type=1,
)
client.set_api_creds(client.create_or_derive_api_creds())


print(client.get_orders())

resp = client.create_and_post_order(
    OrderArgs(
        price=0.10,
        size=10.0,
        side=BUY,
        token_id="34731657770883441140875001518098751138877095477683682718012432921110142479972",  # from events.json
    )
)
print(resp)

print(client.get_orders())
print("-" * 25)
print(client.cancel_all())
print("-" * 25)
print(client.get_orders())
