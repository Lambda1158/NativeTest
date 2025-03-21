from functools import wraps
from flask import redirect
from app import sp_oauth, cache_handler  

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not sp_oauth.validate_token(cache_handler.get_cached_token()):
            auth_url = sp_oauth.get_authorize_url()
            return redirect(auth_url)
        return f(*args, **kwargs)
    return decorated_function