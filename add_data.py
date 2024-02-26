#add data to database
from source import db, app
from source.models import  Video, Game

def add_video_and_game_data():
    # create video data
    videos = [
        Video(title='The Grand Adventure', category='Movie', director='John Smith', is_borrowed=False),
        Video(title='Mystery of the Ancient', category='Movie', director='Linda Johnson', is_borrowed=False),
        Video(title='Laugh Out Loud', category='Show', director='Chris Lee', is_borrowed=False),
        Video(title='Nature Wonders', category='Documentary', director='Sara Wong', is_borrowed=False),
        Video(title='Cooking with Chefs', category='Show', director='Michael Brown', is_borrowed=False)
    ]

    # create game data
    games = [
        Game(title='Chess Master', category='Board Game', platform='Board', is_borrowed=False),
        Game(title='The Quest for El Dorado', category='Board Game', platform='Board', is_borrowed=False),
        Game(title='Space Explorers', category='Board Game', platform='Board', is_borrowed=False),
        Game(title='Fantasy Adventure', category='Video Game', platform='PC', is_borrowed=False),
        Game(title='Racing Champions', category='Video Game', platform='Console', is_borrowed=False)
    ]

    with app.app_context():
        # add video data
        for video in videos:
            db.session.add(video)
        for game in games:
            db.session.add(game)

        db.session.commit()
        print ('Data added successfully!')

if __name__ == '__main__':
    add_video_and_game_data()