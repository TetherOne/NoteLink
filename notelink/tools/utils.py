import base64
import re
import uuid


def generate_public_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    public_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:6]
    return public_id


def generate_private_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    private_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:48]
    return private_id


def create_public_and_private(note_create):
    if note_create.is_public:
        private_id = None
        public_id = generate_public_id()
    else:
        public_id = None
        private_id = generate_private_id()
    return public_id, private_id
