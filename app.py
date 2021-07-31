import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('docs/index.html')


@app.route("/blog")
def blog():
    blog_posts = []
    for filename in os.listdir('posts'):
        if filename.endswith(".html"):
            with open(os.path.join('posts', filename)) as f:
                blog_posts.append(f.read())
        else:
            continue

    return render_template('docs/blog.html', blog_posts=blog_posts)


@app.route("/guides")
def guides():
    return render_template('docs/guides.html')


@app.route("/projects")
def projects():
    return render_template('docs/projects.html')


@app.route("/bookclub")
def bookclub():
    return render_template('docs/bookclub.html')


@app.route("/about")
def about():
    return render_template('docs/about.html')


if __name__ == "__main__":
    app.run(debug=True)
