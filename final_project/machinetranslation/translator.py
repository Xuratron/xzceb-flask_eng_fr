''' This is a transalator using IBM Watson'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('wNgDnA6r6NlxLaJzLmUNIAb_PgyZtrQVhBrpZmX44_7M')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/19326445-79a7-42fa-9cfd-f269ac37ab16')

def english_to_french(englishText):
    '''English to French Translator'''
    #write the code here
    translation_response = language_translator.translate(text=englishText,model_id='en-fr')
    translation = translation_response.get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    '''French to English Translator'''
    #write the code here
    translation_response = language_translator.translate(text=frenchText,model_id='fr-en')
    translation = translation_response.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText