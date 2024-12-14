# NetWiki - CTCL 2024
# File: /routes.py
# Purpose: Routes
# Created: November 11, 2024
# Modified: November 23, 2024

from flask import Blueprint, redirect, current_app
# Currently, Lysine is literally just Jinja2 under a different name
from lysine import Environment, PackageLoader, select_autoescape
from netwiki.config import Config
import pymysql
import markdown

env = Environment(
    loader = PackageLoader("netwiki", "templates", "utf-8"),
    autoescape = select_autoescape()
)

bp = Blueprint("routes", __name__)


@bp.route("/")
def root():
    return redirect("/main/main_page/", code = 302)

@bp.route("/main/<path:path>/")
def main(path):
    # Add trailing slash
    path += "/"


    template = env.get_template("page.lish")

    config: Config = current_app.config.get("APPCONFIG")

    conn = pymysql.connect(
        host = config.db.server,
        user = config.db.username,
        password = config.db.password,
        database = config.db.dbname,
        cursorclass = pymysql.cursors.DictCursor
    )

    with conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `pages` WHERE `page_path`=%s"
            cur.execute(sql, (path,))
            result = cur.fetchone()
    
    if not result:
        # To-Do: replace this with a proper 404 page
        return "page not found", 404

    title = result["page_title"]
    content = markdown.markdown(result["page_content"])

    return template.render(content = content, title = title)

@bp.route("/debug/")
def debug():
    raise Exception