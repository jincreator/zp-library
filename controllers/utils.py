import connexion
from google.appengine.ext import ndb

from models.classes import ApiKey


def get_param_from_query(query, target):
    for p in query.split('&'):
        if 0 <= p.find('=') < len(p) - 1:
            p_key, p_value = p.split('=')

            if p_key.lower() == target.lower():
                return p_value

    return None


def get_user_from_key(api_key):
    key_entity = ndb.Key(ApiKey, api_key).get()

    if not key_entity:
        return None

    return key_entity.user.get()


def get_current_user():
    api_key = get_param_from_query(connexion.request.query_string, 'api_key')

    return get_user_from_key(api_key)