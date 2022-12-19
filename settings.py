# DB Settings
"""
    Written by SAAD-IT 19.12.2022
"""

from tortoise.contrib.quart import register_tortoise

class DBOptions:

    def __init__ (self,):

        self.appName="TestTortoiseAerichQuartApp"
        self.dbUrl="sqlite://db.sqlite3" # default uri | mysql://root:@127.0.0.1:3306/quart" # TODO: adapt to your env
        self.models=["models", "aerich.models"] # models or aerich.models # TODO: adapt to your env

        self.TORTOISE_ORM = {
            "connections": {"default": self.dbUrl},
            "apps": {
                self.appName: {
                    "models": self.models,
                    "default_connection": "default",
                },
            },
        }

    def init_db(self, app) -> None:

        register_tortoise(
            app,
            db_url=self.dbUrl,
            modules={"models": self.models},
            generate_schemas=False
        )

    def getORMString (self,):
        return self.TORTOISE_ORM


dbOptions = DBOptions()


def getDbOptions ():
    return dbOptions

TORTOISE_ORM = getDbOptions().getORMString()
