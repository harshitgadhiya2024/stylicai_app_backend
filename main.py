from operations.mongo_operation import mongoOperation
from operations.common_operations import commonOperation
from utils.constant import constant_dict
import os, json
from flask import (Flask, render_template, request, session, send_file, jsonify, send_from_directory)
from flask_cors import CORS
from datetime import datetime, date
from operations.mail_sending import emailOperation
from utils.html_format import htmlOperation
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = constant_dict.get("secreat_key")
UPLOAD_FOLDER = 'static/uploads/'
app.config['BACKGROUND_FOLDER'] = "static/background_images"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Utility to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


client = mongoOperation().mongo_connect(get_mongourl=constant_dict.get("mongo_url"))

@app.route("/stylic/register-user", methods=["POST"])
def register_user():
    try:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        company_name = request.form["company_name"]
        email = request.form["email"]
        password = request.form["password"]
        phone_number = request.form.get("phone_number", "")

        get_all_user_data = mongoOperation().get_all_data_from_coll(client, "stylic", "user_data")
        all_userids = [user_data["user_id"] for user_data in get_all_user_data]

        flag = True
        user_id = ""
        while flag:
            user_id = str(uuid.uuid4())
            if user_id not in all_userids:
                flag = False

        mapping_dict = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "company_name": company_name,
            "email": email,
            "password": password,
            "phone_number": phone_number,
            "photo_coin": 10,
            "photoshoot_coin": 10,
            "is_active": True,
            "type": "user",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        mongoOperation().insert_data_from_coll(client, "stylic", "user_data", mapping_dict)
        response_data_msg = commonOperation().get_success_response(200, {"user_id": user_id})
        return response_data_msg

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again..")
        print(f"{datetime.utcnow()}: Error in register user data route: {str(e)}")
        return response_data

@app.route("/stylic/otp-email-verification", methods=["POST"])
def otp_email_verification():
    try:
        otp = request.form["otp"]
        email = request.form["email"]
        get_all_user_data = mongoOperation().get_all_data_from_coll(client, "stylic", "user_data")
        all_emails = [user_data["email"] for user_data in get_all_user_data]
        if email in all_emails:
            return commonOperation().get_error_msg("Email already registered...")

        html_format = htmlOperation().otp_verification_process(otp)
        emailOperation().send_email(email, "Stylic AI: Your Account Verification Code", html_format)
        response_data = commonOperation().get_success_response(200, {"message": "Mail sent successfully..."})
        return response_data

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in otp email verification: {str(e)}")
        return response_data

@app.route("/stylic/login", methods=["POST"])
def login():
    try:
        email = request.form["email"]
        password = request.form["password"]
        email_condition_dict = {"email": email, "password": password}
        email_data = mongoOperation().get_spec_data_from_coll(client, "stylic", "user_data", email_condition_dict)
        if email_data:
            if email_data[0]["is_active"]:
                return commonOperation().get_success_response(200, {"user_id": email_data[0]["user_id"]})
            else:
                return commonOperation().get_error_msg("Your account was disabled, Contact administration")
        else:
            response_data = commonOperation().get_error_msg("Your credential doesn't match...")
        return response_data

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in login route: {str(e)}")
        return response_data

@app.route("/stylic/forgot-password", methods=["POST"])
def forgot_password():
    try:
        email = request.form["email"]
        otp = request.form["otp"]
        email_condition_dict = {"email": email}
        email_data = mongoOperation().get_spec_data_from_coll(client, "stylic", "user_data", email_condition_dict)
        if email_data:
            if email_data[0]["is_active"]:
                html_format = htmlOperation().otp_verification_process(otp)
                emailOperation().send_email(email, "Stylic: Your Account Verification Code", html_format)
                return commonOperation().get_success_response(200, {"message": "Account Exits..", "user_id": email_data[0]["user_id"]})
            else:
                return commonOperation().get_error_msg("Your account was disabled, Contact administration")
        else:
            response_data = commonOperation().get_error_msg("Account not exits..")
        return response_data

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in forgot password route: {str(e)}")
        return response_data

@app.route("/stylic/change-password", methods=["POST"])
def change_password():
    try:
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        user_id = request.args.get("user_id")
        if password==confirm_password:
            mongoOperation().update_mongo_data(client, "stylic", "user_data", {"user_id":user_id}, {"password": password})
            return commonOperation().get_success_response(200, {"message": "Password updated"})
        else:
            return commonOperation().get_error_msg("Password doesn't match...")

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in change password route: {str(e)}")
        return response_data

@app.route("/stylic/request_more_coin", methods=["POST"])
def request_more_coin():
    try:
        user_name = request.form["user_name"]
        email = request.form["email"]
        phonenumber = request.form["phonenumber"]
        user_id = request.args.get("user_id")
        mapping_dict = {
            "user_id": user_id,
            "username": user_name,
            "email": email,
            "phonenumber": phonenumber
        }
        mongoOperation().insert_data_from_coll(client, "stylic", "more_coin", mapping_dict)
        return commonOperation().get_success_response(200, {"message": "Sales team contact will you soon"})

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in request a more coin route: {str(e)}")
        return response_data

@app.route("/stylic/create-photoshoot", methods=["POST"])
def create_photoshoot():
    try:
        user_id = request.args.get("user_id", "")
        garment_type = request.form.get('garment_type', '')
        gender = request.form.get('gender', '')
        age_group = request.form.get('age_group', '')
        garment_description = request.form.get('garment_description', '')
        photoshoot_type = request.form.get('photoshoot_type', '')
        color_type = request.form.get('color_type', '')
        background_id = request.form.get("background_id", '')
        selected_background_image_list = [back["background_image"] for back in constant_dict["background_images"] if back["id"]==background_id]
        selected_background_image = selected_background_image_list[0]

        garment_photo_path = None
        new_filename = ""
        if 'garment_photo' in request.files:
            file = request.files['garment_photo']

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                unique_id = str(uuid.uuid4().hex[:8])
                new_filename = f"{timestamp}_{unique_id}_{filename}"

                # Save the file
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(file_path)
                garment_photo_path = file_path

        garment_data = {
            "user_id": user_id,
            "garment_photo_path": f"https://backendapp.stylic.ai/upload_download/{new_filename}",
            "garment_type": garment_type,
            "gender": gender,
            "age_group": age_group,
            "garment_description": garment_description,
            "photoshoot_type": photoshoot_type,
            "color_type": color_type,
            "background_image": selected_background_image,
            "is_completed": False,
            "is_money": False,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        mongoOperation().insert_data_from_coll(client, "stylic", "photoshoot_data", garment_data)
        return commonOperation().get_success_response(200, {"message": "Photoshoot data generated"})

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in create photoshoot route: {str(e)}")
        return response_data

@app.route("/stylic/background-images", methods=["GET"])
def background_images_stylic():
    try:
        background_images = constant_dict.get("background_images", [])
        return jsonify(background_images)

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in stylic background images route: {str(e)}")
        return response_data

@app.route("/stylic/get-user-data", methods=["POST"])
def get_user_data():
    try:
        user_id = request.form["user_id"]
        get_all_user_data = list(
            mongoOperation().get_spec_data_from_coll(client, "stylic", "user_data", {"user_id": user_id}))
        response_data = get_all_user_data[0]
        del response_data["_id"]
        del response_data["created_at"]
        del response_data["updated_at"]
        response_data_msg = commonOperation().get_success_response(200, response_data)
        return response_data_msg

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in stylic user data route: {str(e)}")
        return response_data

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['BACKGROUND_FOLDER'], filename)

@app.route('/upload_download/<filename>')
def download_upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/stylic/update-user-data", methods=["POST"])
def update_user_data():
    try:
        user_id = request.form.get("user_id")
        email = request.form.get("email")
        mongoOperation().update_mongo_data(client, "stylic", "user_data", {"user_id":user_id}, {"email": email})
        return commonOperation().get_success_response(200, {"message": "Email updated successfully..."})

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in updare user data route: {str(e)}")
        return response_data

@app.route("/stylic/get-all-photoshoot", methods=["GET"])
def get_all_photoshoot():
    try:
        user_id = request.form.get("user_id")
        get_all_photoshoot_data = list(mongoOperation().get_spec_data_from_coll(client, "stylic", "photoshoot_data", {"user_id": user_id}))
        response_data = []
        for data in get_all_photoshoot_data:
            del data["_id"]
            del data["created_at"]
            del data["updated_at"]
            response_data.append(data)
        response_data_msg = commonOperation().get_success_response(200, response_data)
        return response_data_msg

    except Exception as e:
        response_data = commonOperation().get_error_msg("Please try again...")
        print(f"{datetime.now()}: Error in get all photoshoot route: {str(e)}")
        return response_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3030)
