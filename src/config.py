import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PREFIX = "."

DEVICES = {
    "speakers": "{0.0.0.00000000}.{5bd86efe-825a-4742-8157-eaeee4a42e1d}",
    "headphones": "{0.0.0.00000000}.{3da14658-a745-476b-a7f8-a01352d34372}",
}
