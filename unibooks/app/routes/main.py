from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, User, Sales_Listing, Book
import os
from werkzeug.utils import secure_filename

# Renders html pages at a given route


main_bp = Blueprint("main", __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Index / home page
@main_bp.route("/")
def index():
    sales_listings = Sales_Listing.query.all()
    return render_template("index.html", sales_listings=sales_listings)


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
        phone_number = request.form.get("phone_number")

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
        
        if phone_number is not None:
            if phone_number != current_user.phone_number:
                current_user.phone_number = phone_number
                db.session.commit()
                flash("Telefonnummer opdateret!", "success")
                return redirect(url_for("main.profile"))

    user_sales = Sales_Listing.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "profile.html", active_page="profile", user=current_user, user_sales=user_sales
    )


@main_bp.route("/create-listing", methods=["GET", "POST"])
@login_required
def create_listing():
    if request.method == "POST":
        title = request.form.get("title") or request.form.get("search-input-title")
        author = request.form.get("author") or request.form.get("search-input-author")
        isbn = request.form.get("isbn") or request.form.get("search-input-isbn")
        price = request.form.get("price")
        description = request.form.get("description")
        # Find or create the book
        book = Book.query.filter_by(isbn=isbn).first()
        if not book:
            book = Book(isbn=isbn, title=title, author=author)
            db.session.add(book)
            db.session.commit()

        # Create the sales listing (reference book by book_id)
        listing = Sales_Listing(
            book_id=book.id,
            user_id=current_user.id,
            price=price,
            description=description
        )
        db.session.add(listing)
        db.session.commit()
        flash("Din bog er nu sat til salg!", "success")
        return redirect(url_for("main.index"))

    return render_template("sales_listing.html")

@main_bp.route("/sales_listing/<int:listing_id>")
@login_required
def listing_detail(listing_id):
    sale = Sales_Listing.query.get_or_404(listing_id)
    seller = User.query.get(sale.user_id)
    return render_template(
        "listing_detail.html", sale=sale, seller=seller, user=current_user
    )
