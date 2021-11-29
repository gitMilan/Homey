from flask import render_template
from flask import Blueprint
from flask import Flask, jsonify, request, render_template
from qbittorrent import Client
from apscheduler.schedulers.background import BackgroundScheduler

bp = Blueprint('torrent', __name__)

try:

    qb = Client("http://127.0.0.1:8080/")
    qb.login("admin", "adminadmin")
    # deletes torrents every hour
    def sensor(*args):
        qb.delete_all()



    sched = BackgroundScheduler(daemon=True)

    sched.add_job(sensor, 'interval', minutes = 60, args=('milan',))
    sched.start()
except:
    print("qbittorrent is not running")
    pass





@bp.route('/torrent')
def show_torrent_page():
    return render_template('torrent/index.html')


@bp.route('/start_torrent', methods=['POST', 'GET'])
def start_torrent():

    if request.method == 'POST':
        magnet_link = request.form['magnet_link']
        video_type = request.form['langs[]']

        print(video_type)

        try:
            qb.download_from_link(magnet_link, savepath = "/media/milan/DATA1/Documents/video/" + video_type)
        except:
            print("cannot download torrent, qbittorrent not running?")

    return render_template('torrent/index.html')
