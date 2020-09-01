from flask import Flask, request
application = Flask(__name__)

@application.route("/myAPI")
def hello():

    num1 = int(request.args.get("num1"))

    num2 = int(request.args.get("num2"))

    calType = request.args.get("calType")

    if calType=="add":
        cal = num1 + num2
        res = str(num1) + "+" + str(num2) + "=" + str(cal)

    else:
        cal = num1 - num2
        res = str(num1) + "-" + str(num2) + "=" + str(cal)

    return res

if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8000)