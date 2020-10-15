import requests
import uuid
import re
import time
from flask import Flask, request
from flask_restful import Api, Resource

# Init app
app = Flask(__name__)
api = Api(app)


# Data
list_timer = [
    {
        "id": "1",
        "duration": time.time()
    },
    {
        "id": "2",
        "duration": time.time()
    },
    {
        "id": "3",
        "duration": time.time()
    }
]

# MAC Address
MAC_Address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))


class ListTimer(Resource):
    # 6
    def get(self):
        if len(list_timer) == 0:
            return {'Note': 'No Data'}
        return {"List_timer": list_timer}

    # 1
    def post(self):
        list_timer.append(request.form)
        return {"List_timer": list_timer}


api.add_resource(ListTimer, "/timers")


class Timer(Resource):
    # 7
    def get(self, id):
        return [timer for timer in list_timer if str(timer['id']) == id][0]

    # 4
    def delete(self, id):
        timer = [timer for timer in list_timer if str(timer['id']) == id][0]
        list_timer.remove(timer)
        return {'Note': 'OK'}


api.add_resource(Timer, "/timers/<string:id>")


class Time_Duration(Resource):
    # 2
    def put(seft, id):
        timer = [timer for timer in list_timer if str(timer['id']) == id][0]
        i = None
        for index, value in enumerate(list_timer):
            if str(value['id']) == str(id):
                i = index
        if timer == {}:
            return {'Note': 'Not found'}
        list_timer[i] = request.form
        return {'Note': 'OK'}


api.add_resource(Time_Duration, '/timers/<string:id>/duration')


class Time_Complete(Resource):
    # 3
    def put(seft, id):
        timer = [timer for timer in list_timer if str(timer['id']) == id][0]
        i = None
        for index, value in enumerate(list_timer):
            if str(value['id']) == str(id):
                i = index
        if timer == {}:
            return {'Note': 'Not found'}
        list_timer[i] = {'data': 'From put Time_Complete'}
        return {'Note': 'OK'}


api.add_resource(Time_Complete, '/timers/<string:id>/complete')


class Time_Description(Resource):
    # 5
    def put(seft, id):
        timer = [timer for timer in list_timer if str(timer['id']) == id][0]
        i = None
        for index, value in enumerate(list_timer):
            if str(value['id']) == str(id):
                i = index
        if timer == {}:
            return {'Note': 'Not found'}
        list_timer[i] = request.form
        return {'Note': 'OK'}


api.add_resource(Time_Description, '/timers/<string:id>/description')


class User_Device(Resource):
    # 9
    def get(seft):
        return {'MAC Address': MAC_Address}

    # 8
    def put(seft):
        # MAC_Address = req
        MAC_Address = request.form['MAC Address']
        return {'Note': 'OK'}


api.add_resource(User_Device, '/user/device')

# >> > print(session.cookies.get_dict())
# {}
# >> > response = session.get('http://google.com')
# >> > print(session.cookies.get_dict())


class User(Resource):
    # 11
    def post(seft):
        return {
            'Note': 'OK',
            'Cookie': request.form
        }


api.add_resource(User, '/user')

ff
class Login(Resource):
    # 10
    def post(self):
        return {
            'Note': 'OK',
            'Cookie': request.form
        }


api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True)
