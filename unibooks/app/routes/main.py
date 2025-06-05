from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, User, Sales_Listing

# Renders html pages at a given route


main_bp = Blueprint("main", __name__)


# Index / home page
@main_bp.route("/")
def index():
    return render_template("index.html")


# Curriculum page
@main_bp.route("/curriculum")
def curriculum():
    return render_template("curriculum.html", active_page="curriculum")


@main_bp.route("/buy_books")
def buy_books():
    sales_listings = Sales_Listing.query.all()
    return render_template(
        "buy_books.html",
        active_page="buy_books",
        user=current_user,
        sales_listings=sales_listings,
    )


@main_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Update username
        if username is not None:
            if username != current_user.username:
                if User.query.filter(
                    User.username == username, User.id != current_user.id
                ).first():
                    flash("Brugernavn er allerede i brug.", "error")
                    return redirect(url_for("main.profile"))
                current_user.username = username
                db.session.commit()
                flash("Brugernavn opdateret!", "success")
                return redirect(url_for("main.profile"))

        # Update email
        if email is not None:
            if email != current_user.email:
                if User.query.filter(
                    User.email == email, User.id != current_user.id
                ).first():
                    flash("Email er allerede i brug.", "error")
                    return redirect(url_for("main.profile"))
                current_user.email = email
                db.session.commit()
                flash("Email opdateret!", "success")
                return redirect(url_for("main.profile"))

        # Update password
        if password is not None and password != "":
            current_user.set_password(password)
            db.session.commit()
            flash("Adgangskode opdateret!", "success")
            return redirect(url_for("main.profile"))

    user_sales = Sales_Listing.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "profile.html", active_page="profile", user=current_user, user_sales=user_sales
    )


@main_bp.route("/create-listing", methods=["GET", "POST"])
def create_listing():
    if request.method == "POST":
        # handle form submission here
        pass
    return render_template("sales_listing.html")
