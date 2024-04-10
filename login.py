import os
from instagrapi import Client
import logging


HASHTAGS = ["instacool"]
IG_USERNAME = "_sk_rohit"
IG_PASSWORD = "plmplmQAZQAZ"
IG_CREDENTIAL_PATH = "credential.json"



def VerificationViaSms(challenge):
    code = input("Enter the SMS code: ")
    return code

def Get_Logger(name, **kwargs):
    logging.basicConfig(**kwargs)
    logger = logging.getLogger(name)
    logger.debug(f"start logging '{name}'")
    return logger

def Login():
    try:
        log = Get_Logger(
            "example_media",
            **{
                "level": "DEBUG",
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
            },
        )
        print(log)
    except Exception as e:
        print(e)
    
    cl = Client(challenge_required=True, challenge_resolve_func=VerificationViaSms)
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)
        cl.login(IG_USERNAME, IG_PASSWORD)
    else:
        cl.login(IG_USERNAME, IG_PASSWORD)
        cl.dump_settings(IG_CREDENTIAL_PATH)

  
   