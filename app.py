import csv
from flask import Flask, request, render_template
import psycopg2, random

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route("/home")
def render_sets():
    Poster_Link = request.args.get("Poster_Link", "")
    Series_Title = request.args.get("Series_Title", "")
    Released_Year = request.args.get("Released_Year", "")
    Certificate = request.args.get("Certificate", "") 
    Runtime = request.args.get("Runtime", "")
    Genre = request.args.get("Genre", "")
    IMDB_Rating = request.args.get('IMDB_Rating')
    Overview = request.args.get("Overview", "")
    Meta_score = request.args.get("Meta_score", "")
    Director = request.args.get("Director", "")
    Star1 = request.args.get("Star1", "")
    Star2 = request.args.get("Star2", "")
    Star3 = request.args.get("Star3", "")
    Star4 = request.args.get("Star4", "")
    No_of_Votes = request.args.get("No_of_Votes", "")
    Gross = request.args.get("Gross", "")
    sort_by = request.args.get("sort_by", "Series_Title")
    sort_dir = request.args.get("sort_dir", "asc")
    limit = request.args.get("limit", 100, type=int)

    from_where_clause = """
        from movie
        where %(Series_Title)s is null or series_title name ilike %(Series_Title)s
        and ( %(Released_Year)s is null or released_year = %(Released_Year)s )
        and ( %(Runtime)s is null or runtime = %(Runtime)s )
        and ( %(Genre)s is null or genre ilike %(Genre)s )
        and ( %(IMDB_Rating)s is null or imdb_rating = %(IMDB_Rating)s )
        and ( %(Director)s is null or director ilike %(Director)s )
    """

    params = {
        "Poster_Link": f"%{Poster_Link}%",
        "Series_Title": f"%{Series_Title}%",
        "Released_Year": int(Released_Year) if Released_Year else None,
        "Certificate": f"%{Certificate}%",
        "Runtime": f"%{Runtime}%",
        "Genre": f"%{Genre}%",
        "IMDB_Rating": float(IMDB_Rating) if IMDB_Rating else None,
        "Overview": f"%{Overview}%",
        "Meta_score": f"%{Meta_score}%",
        "Director": f"%{Director}%",
        "Star1": f"%{Star1}%",
        "Star2": f"%{Star2}%",
        "Star3": f"%{Star3}%",
        "Star4": f"%{Star4}%",
        "No_of_Votes": f"%{No_of_Votes}%",
        "Gross": f"%{Gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
    }
    
    return render_template("Home.html", params=request.args)
