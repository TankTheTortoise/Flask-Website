from datetime import datetime, date, timedelta

import requests
import json
import random


def random_chuck(num):
    images = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaKTsn7E7YvV0CbLGllKGpW3PQsHKGhrnUHZ1vv35zLe3QFnGjb0U_gHveNx7GaFnjWdw&usqp=CAU",
        "data:image/png;base64,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",
        "https://www.slashfilm.com/img/gallery/chuck-norris-needed-a-push-from-steve-mcqueen-to-even-consider-a-career-in-acting/intro-1662649398.webp",
        "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2014%2F11%2Fchuck-norris_612x380_1.jpg&q=60",
        "https://www.gannett-cdn.com/presto/2022/08/17/NAAS/9b7e8577-a80e-4b71-b6ea-2d06c70ba9b4-Chuck_Norris_Watch_Texas_1.jpg?width=1200&disable=upscale&format=pjpg&auto=webp",
        "https://express-images.franklymedia.com/6616/sites/262/2021/01/13051327/CHUCK-NORRIS-TWITTER-PHOTO-e1610536121831.jpg",
        "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/04/Chuck-Norris-featured-Image.jpg",
        "http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcS7ZaoshRRR_a1swqIcneodV6UPQRdp7GmpxAMhkLbh4St_asx5iTqQU2MFu5KA7_QqdKyXeQSpFaGyncs",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfZojU0VDnC1cNt7k6OcSTQFIPsWT8LxFeBQ&usqp=CAU",
        "https://static1.srcdn.com/wordpress/wp-content/uploads/2022/12/why-chuck-norris-only-wanted-to-do-one-bruce-lee-movie.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTA3Jbo5oLFN4GyDGyFJSdTSEkAuzxiVTb-MQ&usqp=CAU",
    ]
    returns = []
    for i in range(num):
        if len(returns) > 0:
            if (n := random.choice(images)) != returns[i - 1]:
                returns.append(n)
            else:
                returns.append(random.choice(images))
        else:
            returns.append(random.choice(images))
    return returns


def chuck_joke():
    f = r"https://api.chucknorris.io/jokes/random/"

    data = requests.get(f)
    tt = json.loads(data.text)
    return tt.get("value")


def nasaPictureDay(date):
    params = {"date": date}
    thing = r"https://api.nasa.gov/planetary/apod?api_key=IyUHwPeym6twr5Q61nmwddZuZZ8xuIeMZLel6aOM"
    data = requests.get(thing, params=params)
    tt = json.loads(data.text)
    return tt


def randomDate():
    start_date = date(1995, 6, 16)
    start_date = start_date.toordinal()
    end_date = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    return random_day


def addDay(day1, rand=True):
    if rand:
        day1 = datetime.strptime(day1, '%m/%d/%Y') + timedelta(days=1)
    else:
        day1 = datetime.strptime(day1, '%y/%m/%d') + timedelta(days=1)
    return day1
