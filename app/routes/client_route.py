from flask import Blueprint, render_template, redirect, request, url_for
from app.db import db
from app.models.client_model import Client

client_router = Blueprint("client_router", __name__)


# Start App Client
@client_router.route("/")
def index():
    client_list = Client.query.all()
    return render_template("index.html", client_list=client_list)


# Add Client
@client_router.route("/add", methods=["POST"])
def add():
    # Add data from form
    name = request.form.get("name_input")
    document = request.form.get("document_input")
    address = request.form.get("address_input")
    phone = request.form.get("phone_input")
    status = request.form.get("status_input")

    new_client = Client(
        name=name, document=document, address=address, phone=phone, status=status
    )

    db.session.add(new_client)
    db.session.commit()
    return redirect(url_for("client_router.index"))


@client_router.route("/client/", defaults={"id": None})
@client_router.route("/client/<int:id>")
def client(id=None):

    if id == None:
        return redirect("/")

    client = Client.query.get(id)
    if client == None:
        return redirect(url_for("client_router.index"))

    return render_template("detail.html", client=client)


@client_router.route("/done", methods=["POST"])
def done():
    client_id = request.form.get("id")
    next = request.form.get("next")
    client = Client.query.get(client_id)
    if client == None:
        return redirect("/")
    # Si existe la tarea:
    # client.doneAt = datetime.now()
    client.name = request.form.get("name_input")
    client.document = request.form.get("document_input")
    client.address = request.form.get("address_input")
    client.phone = request.form.get("phone_input")
    client.status = request.form.get("status_input")

    db.session.commit()
    # finish:
    if next != None:
        return redirect(next)
    return redirect("/client/" + str(client_id))

