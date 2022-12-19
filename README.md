# Test Tortoise-Orm, Aerich & Quart App
Some people have asked how to connect Tortoise-Orm, Aerich and Quart. This is a example that works with SQLite (should work with everything else too). Also, a basic jinja2 template is added and a static route.

## How to use?
The usage is straight forward, to test everything and adapt it to your needs. Complex commands were simplified in .sh files, due to bin paths for py packs.

### First use
- After pulling run `pip3 install -r requirements.txt` to install py deps
- Check & Adapt `settings.py` (contains db creds) (optional)
- Use `./aerich_init.sh` to create db schema, and init aerich (if needed, cancel exec after the schema success message)
- Does it work? Run `./run.sh` and visit http://localhost:5000/ (if not working use: http://localhost:5000/1)

### Populate DB
- Visit http://localhost:5000/user
- Visit http://localhost:5000/worker
- It is recommended to create quite a few users and workers, so you can test the pagination
- then check index page http://localhost:5000/ and paginate (e.g. /1 .. /n at route ending)

### Add a migration
- Uncomment in `models.py` the line that contains `testField`
- Use `./aerich_add_migration.sh testMigration yes` (yes=Upgrade schema NOW, leave it out, if manually upgrade wished)
- Does it work? Run `./run.sh` and visit http://localhost:5000/ (if not working use: http://localhost:5000/1)

### How to manually upgrade schemas?
- Use `./aerich.sh upgrade`

### Did you simplify the generate schemas out of the example code?
- Yes, use `./generate_schemas.sh`

### How to find bin paths?
- Use e.g. `locate quart | grep bin` or `find ~ | grep quart | grep bin/` (output will be like `/home/<user>/.local/bin/<app>`)

### Only startup app (e.g. after change in source code)
- Use `./run.sh`

### Help, I receive 500 error on index
- Press F5 to reload the page once

### I did mess, how to cleanup db etc?
- To delete all data that was added by aerich use `./cleanup.sh`

## Used docs, blogs etc. (puzzling ftw)
- https://ashfakmeethal.medium.com/tortoise-orm-migrations-with-aerich-5ebb7238bed5
- https://tortoise-orm.readthedocs.io/
- https://tortoise-orm.readthedocs.io/en/latest/examples/quart.html#example-quart
- https://pgjones.gitlab.io/quart/how_to_guides/routing.html
- https://github.com/tortoise/tortoise-orm/issues/161
- https://github.com/tortoise/tortoise-orm/issues/315

## Who is responsible?
- SAAD-IT 19.12.2022
