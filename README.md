Prerequisites:

To create virtual environment MACOS run this in the terminal in unibooks directory :
  python3.12 -m venv venv 

Then activate the virtual environment by
  source venv/bin/activate

Install dependencies for the virtual environment by
  pip install -r requirements.txt

To run the project
  python3 run.py

Find the frontend in the browser on http://127.0.0.1:5000
If you keep it running and make changes to the files, you can simply reload to see them in browser.

You will need to add a .env file in the unibooks directory. This should just contain
  DATABASE_URL=postgresql://postgres:passwordtildinpostgresql@localhost:5432/unibooksdb

It works only after creating the database in psql named unibooksdb, then flask when run, will create all relevant tables.

