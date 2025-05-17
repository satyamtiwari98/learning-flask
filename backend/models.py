# --------------------------------------------
# Import db object from the config file
# --------------------------------------------
from config import db

# --------------------------------------------
# Define the Contact model
# --------------------------------------------


class Contact(db.Model):
    # Define the primary key 'id' as an integer column
    id = db.Column(db.Integer, primary_key=True)

    # Define 'first_name' column with a maximum length of 80 characters. It's a required field (nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)

    # Define 'last_name' column with a maximum length of 80 characters. It's a required field (nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)

    # Define 'email' column with a maximum length of 120 characters. This column must be unique and required (nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # --------------------------------------------
    # Method to convert the Contact instance into a dictionary format
    # --------------------------------------------
    def to_json(self):
        return {
            "id": self.id,                      # Return the contact's 'id'
            "firstName": self.first_name,        # Return the contact's 'first_name'
            "lastName": self.last_name,          # Return the contact's 'last_name'
            "email": self.email,                 # Return the contact's 'email'
        }
