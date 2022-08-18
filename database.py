import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('movies.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE MOVIES
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             SCORE            REAL,
             DIRECTOR_NAME        TEXT,
             DEFINITION         TEXT,
             POSTER_PATH    TEXT,
             DASH_URL      TEXT,
             HLS_URL        TEXT,
             LOCAL_URL      TEXT);''')
    print("Table created successfully")
    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (1, 'Shawshank Redemption',9.2,'Frank Darabont',"
                 "'Two imprisoned men bond over a number of years,finding solace and eventual redemption through acts "
                 "of common decency.',"
                 "'images/The Shawshank Redemption.jpg',null,null,'Front/local_dash/1/manifest.mpd' )")
    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (2, 'The Godfather', 9.2, 'Francis Ford Coppola','The aging patriarch of an organized crime "
                 "dynasty in postwar New York City transfers control of his clandestine empire to his reluctant "
                 "youngest son.', "
                 "'images/The Godfather (1972).jpg',null,null,'Front/local_dash/2/manifest.mpd' )")
    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (3, 'The Dark Knight', 9.0, 'Christopher Nolan','When the menace known as the Joker wreaks "
                 "havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and "
                 "physical tests of his ability to fight injustice.', "
                 "'images/The Dark Knight (2008).jpg',"
                 "'https://mm-dash-amir.arvanvod.com/WzOgxq0v8l/7Eg8JLnO5V/h_,144_200,240_400,360_800,480_1469,"
                 "k.mp4.list/manifest.mpd',null,null)")

    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (4, 'The Godfather Part II', 9.0, 'Francis Ford Coppola','The early life and career of Vito "
                 "Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip "
                 "on the family crime syndicate.', "
                 "'images/The Godfather Part II (1974).jpg',"
                 "'https://mm-dash-amir.arvanvod.com/WzOgxq0v8l/vNXd2BdYre/h_,144_200,240_400,360_800,480_1500,"
                 "k.mp4.list/manifest.mpd',null,null)")

    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (5, '12 Angry Men', 8.9, 'Sidney Lumet','The jury in a New York City murder trial is "
                 "frustrated by a single member whose skeptical caution forces them to more carefully consider the "
                 "evidence before jumping to a hasty verdict.', "
                 "'images/12 Angry Men (1957).jpg',null,"
                 "'https://mm-dash-amir.arvanvod.com/WzOgxq0v8l/zLx08a4BA7/h_,144_200,240_400,360_800,480_1500,"
                 "k.mp4.list/master.m3u8',null )")

    conn.execute("INSERT INTO MOVIES (ID,NAME,SCORE,DIRECTOR_NAME,DEFINITION,POSTER_PATH,DASH_URL,HLS_URL,LOCAL_URL) "
                 "VALUES (6, 'Schindlers List', 8.9, 'Steven Spielberg','In German-occupied Poland during World War "
                 "II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after "
                 "witnessing their persecution by the Nazis.', "
                 "'images/Schindlers List (1993).jpg',null,"
                 "'https://mm-dash-amir.arvanvod.com/WzOgxq0v8l/myAYLPYWVn/h_,144_200,240_400,360_800,480_1458,"
                 "k.mp4.list/master.m3u8',null)")

    conn.commit()
    conn.close()
