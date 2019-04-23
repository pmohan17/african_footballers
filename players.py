from flask import Flask, render_template
from modules import convert_to_dict
app = Flask(__name__)

players_list = convert_to_dict("african_footballers.csv")
@app.route('/')
def index():
    ids_list = []
    name_list = []
    for player in players_list:
        ids_list.append(player['ID'])
        name_list.append(player['Name'])
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="African Footballers")

@app.route('/player/<num>')
def info(num):
    for player in players_list:
        if player['ID'] == num:
            play_dict = player
            break
    return render_template('player.html', play=play_dict, the_title=play_dict['Name'])





if __name__ == '__main__':
    app.run(debug=True)
