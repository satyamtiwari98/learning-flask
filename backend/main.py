# Import required modules from Flask and other files
# For handling HTTP requests and sending JSON responses
from flask import request, jsonify
# Import the Flask app and SQLAlchemy DB instance from config.py
from config import app, db
# Import the Contact model (database structure)
from models import Contact

# --------------------------------------------
# Route to Get All Contacts
# --------------------------------------------


@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Query all contacts from the database
    contacts = Contact.query.all()
    # Convert each contact object to JSON-friendly format
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    # Return all contacts as JSON
    return jsonify({"contacts": json_contacts})


# --------------------------------------------
# Route to Create a New Contact
# --------------------------------------------
@app.route("/create_contact", methods=["POST"])
def create_contact():
    # Extract data from incoming JSON request
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    # Validate input fields
    if not first_name or not last_name or not email:
        return (
            jsonify({
                "message": "You must include first name, last name and email"
            }),
            400,  # HTTP 400 Bad Request
        )

    # Create new Contact instance
    new_contact = Contact(first_name=first_name,
                          last_name=last_name,
                          email=email)
    try:
        db.session.add(new_contact)    # Add to database session
        db.session.commit()           # Commit changes to database
    except Exception as e:
        # Return error if insert fails
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User Created!"}), 201  # HTTP 201 Created


# --------------------------------------------
# Route to Update an Existing Contact
# --------------------------------------------
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)        # Retrieve contact by ID

    if not contact:
        # HTTP 404 Not Found
        return jsonify({"message": "User not found"}), 404

    # Get updated fields, fallback to existing values if not provided
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()                         # Save changes to database

    return jsonify({"message": "User Updated"}), 200  # HTTP 200 OK


# --------------------------------------------
# Route to Delete a Contact
# --------------------------------------------
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)        # Find contact by ID

    if not contact:
        # If not found, return 404
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)                  # Delete contact from DB
    db.session.commit()

    return jsonify({"message": "User Deleted!"}), 200  # Return success message


# --------------------------------------------
# App Entry Point
# --------------------------------------------
if __name__ == "__main__":
    with app.app_context():
        # Create all tables before running (if not already created)
        db.create_all()

    # Start the Flask development server with debug mode ON
    app.run(debug=True)
