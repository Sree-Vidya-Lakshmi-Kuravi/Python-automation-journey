def build_user_payload(name=None, job=None):
    payload = {}
    if name is not None:
        payload["name"] = name
    if job is not None:
        payload["job"] = job
    return payload

def build_login_payload(email=None, password=None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if password is not None:
        payload["password"] = password
    return payload