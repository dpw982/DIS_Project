How to run (Docker):

1) Make sure that Docker is installed and running on your machine (no other dependencies are needed)

2) Open a terminal and move to the root directory DIS_Project
    cd /path/to/DIS_Project

3) Build and start the web-app with:
    docker-compose up --build

4) Open your browser and go to:
    http://localhost:5001/

5) When finished the app terminates with Ctrl+C in terminal and 
    docker-compose down

__________________________________________________________________________________

Our web-app UniBooks is a marketplace for selling and buying used University books.
It has signup/login logic, for users, and allows for making sales listings. In sales listings
we utilize a google api for suggesting books based on isbn or title, while also suggesting an
autofilled image of the book. The user is then prompted to enter a price and a description of the book.
Users can Buy books, looking through a selection of books on the home page, or entering the Buy book page.
Here every sales postings are shown, along with some of it's information. If interested the user can press on a listing
to find contact information about the seller. The home page also includes a search field, which uses an regex
to match on posted sales listings.

___________________________________________________________________________________

![alt text](/unibooks/app/static/img/ER.png)