from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Category).delete()
session.query(Items).delete()
session.query(User).delete()

User1 = User(name="LONG CJ",
              email="CJKGKGKK@slack.com",
              picture='http://placekitten.com/200/300')
session.add(User1)
session.commit()





Category1 = Category(name="Video games",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Miniatures",
                      user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name="Snacks",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Gadgets",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Food",
                      user_id=1)
session.add(Category5)
session.commit()
Item1 = Items(name="Cyberpunk game",
               date=datetime.datetime.now(),
               description="""The Red Strings Club is a cyberpunk narrative experience about fate and happiness
                . Featuring the extensive use of pottery,
                 bartending and impersonating people on the phone to take down a corporate conspiracy. 
""",
               picture="https://goo.gl/4UtDQt",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="RPG game",
               date=datetime.datetime.now(),
               description="The legendary Dugeon and Dragon now in a video game what kind of description you expected? IT IS DUNGEON AND DRAGON",
               picture="https://goo.gl/MThFCi",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item4 = Items(name="Adeptus Miniatures",
               date=datetime.datetime.now(),
               description="""The Adeptus Custodes,
                known as the Legio Custodes before the Horus Heresy,
                is the Imperial Adepta responsible for guarding the Imperial Palace and the physical body of the Emperor of Mankind.
                It is an elite cadre of genetically-engineered transhuman warriors who are even more potent in combat than the Adeptus Astartes""",
               picture="https://goo.gl/pNLGmN",
               category_id=2,
               user_id=1)
session.add(Item4)
session.commit()

Item5 = Items(name="Drakesworn",
               date=datetime.datetime.now(),
               description="""A Drakesworn Templar, the retribution of the heavens given form,
                armed with either a tempest axe,
                 arc hammer, or stormlance and skybolt bow.""",
               picture="https://goo.gl/Wh3V3b",
               category_id=2,
               user_id=1)
session.add(Item5)
session.commit()

Item6 = Items(name="Heresy",
               date=datetime.datetime.now(),
               description="""The air screams as Magnus the Red descends from the skies,
                and stone runs molten beneath his shadow. Cyclopean son of the Emperor of Mankind,
                his very presence is anathema to logic""",
               picture="https://goo.gl/6P3emZ",
               category_id=2,
               user_id=1)
session.add(Item6)
session.commit()

Item7 = Items(name="Japanese Kit Kat Matcha Green Tea Flavour",
               date=datetime.datetime.now(),
               description="""Famous Kit Kat Matcha Green Tea from Japan with 12 delicious flavour filled green tea kit kat made in japan""",
               picture="https://goo.gl/pZQQhq",
               category_id=3,
               user_id=1)
session.add(Item7)
session.commit()

Item8 = Items(name="Japanese Kit Kat Matcha Green Tea Flavour",
               date=datetime.datetime.now(),
               description="""The original YAN YAN bread stick and dips just like how you remember it""",
               picture="https://goo.gl/eKbBAV",
               category_id=3,
               user_id=1)
session.add(Item8)
session.commit()

Item3 = Items(name="COD of duty games",
               date=datetime.datetime.now(),
               description="""When the peace treaty between human and fish was broken by an unexpected attack of a mysterious force
                war between human and fish break out
                .Now blob a fish veteran disguised as a human must fight for peace
                 maybe he'll train a noob and die mid way watting the noob to do the rest of the job.""",
               picture="https://goo.gl/6VkZGK",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

print "Your database has been populated with data! You're Welcome"