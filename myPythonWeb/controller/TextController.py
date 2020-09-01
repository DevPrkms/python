from flask import Flask, request

import util.CmmUtil as cu
import service.TextService as ta

application = Flask(__name__)

@application.route("/myTextAPI")
def textAnalysis():
    print("textAnalysis")

    print(request.args.get("pText"))

    pText = cu.CmmUtil.nvl(request.args.get("pText"))

    res = ta.TextService.wordAnalysis(pText)

    return res

if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8000)