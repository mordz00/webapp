from jinja2 import Environment, FileSystemLoader
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")),
    autoescape=True
)

def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    students = [
        {"ID": 1, "Name": "Mike Catarig", "Course": "Information Technology"},
        {"ID": 2, "Name": "Justin Dollizon", "Course": "Information Technology"},
        {"ID": 3, "Name": "Angel Mae G. Morado", "Course": "Information Technology"},
        {"ID": 4, "Name": "Paul Abao", "Course": "Information Technology"},
    ]

    if path.endswith("/hello"):
        title = "Hello Page"
        message = "Rendered using Jinja2"
    else:
        title = "Student List"

    template = env.get_template("home.html")
    html = template.render(title=title, message=message, students=students)

    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [html.encode("utf-8")]