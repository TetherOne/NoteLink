import base64
import re
import uuid


def generate_public_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    public_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:6]
    return public_id


def generate_private_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    private_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:32]
    return private_id


def create_public_and_private(note_create):
    if note_create.is_public:
        private_url = None
        url = generate_public_id()
    else:
        url = None
        private_url = generate_private_id()
    return url, private_url
