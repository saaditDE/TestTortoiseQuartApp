"""
    Written by SAAD-IT 19.12.2022
"""

import asyncio
import logging

from models import Users, Workers
from quart import Quart, jsonify, render_template, send_from_directory

logging.basicConfig(level=logging.DEBUG)

from settings import dbOptions
from tortoise.functions import Count

app = Quart(__name__)


# Just example pagination code on index, it's not perfect
@app.route('/', defaults={'page_no': 1})
@app.route('/<int:page_no>')
async def list_all(page_no):
    elperPage=5
    repos=2
    pid = (int(page_no)-1) if (page_no > 0) else 0

    # interesting queries are here, gte on id and just without works the same lol; theoretically this is quicker than SELECT (*) which is being used by the count() func
    userQueryCountAll = Users.filter(id__gte=0).annotate(count=Count("id")).values("count")
    workerQueryCountAll = Workers.filter().annotate(count=Count("id")).values("count")

    countAllUsers, countAllWorkers = await asyncio.gather(userQueryCountAll, workerQueryCountAll)

    countAllUsers = int(countAllUsers[0]["count"])
    countAllWorkers = int(countAllWorkers[0]["count"])

    if countAllUsers < 0:
        countAllUsers = 0

    if countAllWorkers < 0:
        countAllWorkers = 0

    totalCountAllUsersWorkers = (countAllUsers+countAllWorkers)

    if totalCountAllUsersWorkers == 0:
        return jsonify ({"error": "no elements found"}), 404
    elif totalCountAllUsersWorkers < elperPage*repos:
        maxpage = 1
    else:
        maxpage = round((totalCountAllUsersWorkers/elperPage*repos),0) + repos

    # maxpage reached? ok, return 400
    if (pid >= maxpage):
        return jsonify ({"error": "maxpage reached"}), 400

    # get Users and Workers
    userQuery = Users.all().limit(elperPage).offset(pid)
    workerQuery = Workers.all().limit(elperPage).offset(pid)
    users, workers = await asyncio.gather(userQuery, workerQuery)

    # count both
    countUsers = len(workers)
    countWorkers = len(users)

    return jsonify(
        {
            "users": list (str(user) for user in users),
            "workers": list (str(worker) for worker in workers),
            "count_users": countUsers,
            "count_workers": countWorkers,
            "count_total": (countUsers+countWorkers),
            "count_all_users": countAllUsers,
            "count_all_workers": countAllWorkers,
            "count_total_all_users_workers": totalCountAllUsersWorkers,
            "elementsPerPage": elperPage,
            "page": (page_no),
            "maxpage": maxpage
        }
    )


@app.route("/user")
async def add_user():
    user = await Users.create(status=Workers.getRandomStatus())
    return str(user)


@app.route("/worker")
async def add_worker():
    worker = await Workers.create(status=Workers.getRandomStatus())
    return str(worker)

@app.route("/testjinja2")
async def testjinja2():
    userQuery = Users.all().limit(10)
    users = await asyncio.gather(userQuery)
    return await render_template('index.html', users=users[0]) # see https://github.com/tortoise/tortoise-orm/issues/161; https://github.com/tortoise/tortoise-orm/issues/315


@app.route('/<path:path>')
async def send_report(path):
    return await send_from_directory('static', path)

dbOptions.init_db (app)


if __name__ == "__main__":
    app.run(port=5000)
