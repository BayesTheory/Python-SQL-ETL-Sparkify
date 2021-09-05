import glob
import os
import numpy as np
import pandas as pd
import psycopg2
from sql_queries import *


def process_song_file(cur, filepath):

    df = pd.read_json(filepath, lines=True)

    song_data = df[['song_id', 'titulo', 'artist_id', 'ano', 'duracao']].values
    song_data = song_data[0]
    cur.execute(song_table_insert, song_data)

    artist_data = df[['artist_id', 'artist_nome', 'artist_localizacao', 'artist_latitude', 'artist_longitude']].values
    artist_data = artist_data[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):

    df = pd.read_json(filepath, lines=True)

    df = df.loc[df['page'] == 'NextSong']

    t = pd.to_datetime(df['ts'], unit='ms')
    df['start_time'] = t.dt.to_pydatetime()

    time_data = (t.dt.to_pydatetime(), t.dt.hora, t.dt.dia, t.dt.week, t.dt.mes, t.dt.ano, t.dt.dia_da_semana)
    column_labels = ('start_time', 'hora', 'dia', 'semana', 'mes', 'ano', 'dia_da_semana')
    time_df = pd.DataFrame(np.column_stack(list(time_data)), columns=list(column_labels))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_data = [df['userId'], df['firstName'], df['lastName'], df['genero'], df['nivel']]
    column_labels = ['userId', 'firstName', 'lastName', 'genero', 'nivel']
    user_df = pd.DataFrame(np.column_stack(list(user_data)), columns=list(column_labels))

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():

        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (
            row.start_time, row.userId, row.level, songid, artistid, row.sessionId, row.localizacao, row.userAgent)
        print(songplay_data)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
  
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=localhost dbname=testedb user=postgres password=rian")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
