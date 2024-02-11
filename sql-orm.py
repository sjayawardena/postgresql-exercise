from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#exwcuting the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

#create a class-based model for the "artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)
    
#create a class-based model for the "album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))
    
#create a class-based model for the "track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.AlbumId"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)
    

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an atual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)

#Query 1 - select all records from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep = " | ")
    
    
# Query 2 - select only the "name" column from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)
    

# Query 3 - select only "Queen" from the "artist" table
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id,artist.name, sep = " | ")


# Query 4 - select only by "artist_id" #51 from the "artist" table
artist = session.query(Artist).filter_by(artist_id=51).first()
print(artist.artist_id,artist.name, sep = " | ")

# Query 5 - select only the albums with "artist_id" #51 on the "album" table
# albums = session.query(Album).filter_by(artist_id=51)
# for album in albums:
#     print(album.album-id, album.title, album.artist_id, sep = " | ")
    

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(
        track.track_id, 
        track.name, 
        track.album_id, 
        track.media_type_id, 
        track.genre_id, 
        track.composer, 
        track.milliseconds, 
        track.bytes, 
        track.unit_price, 
        sep = " | "
    )
    

