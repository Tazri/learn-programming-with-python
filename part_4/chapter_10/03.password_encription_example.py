# register the password with user
def register(user, password):
    ecrypted_password = encrypt_password(password);
    save_user(user, ecrypted_password);

# login logic
def login(user,password):
    stored_password = get_password_from_db(user);
    encrypted_password = encrypt_password(password);

    if stored_password != encrypted_password:
        return "Incorrect Password!";

def get_password_from_db():
    pass;

def save_user():
    pass;

# logic of encrypt password
import hashlib

# encrypt logic
def encrypt_password(password):
    m = hashlib.sha256();
    m.update(password.encode());
    return m.hexdigest();

