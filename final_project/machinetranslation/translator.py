"""
This file to handle language translations
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function helps to translate strings from English language to French
    """
    response = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    data = json.dumps(response, indent=2, ensure_ascii=False)
    trans_tree = json.loads(data)
    trans_list = trans_tree['translations']
    trans_str = trans_list[0]
    french_text = trans_str['translation']
    return french_text

def french_to_english(french_text):
    """
    This function helps to translate strings from French language to English
    """
    response = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    data = json.dumps(response, indent=2, ensure_ascii=False)
    trans_tree = json.loads(data)
    trans_list = trans_tree['translations']
    trans_str = trans_list[0]
    english_text = trans_str['translation']
    return english_text
