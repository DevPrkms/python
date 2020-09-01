from konlpy.tag import Hannanum

import re

class TextService():

    def wordAnalysis(text):
        myHannanum = Hannanum()

        print("text : " + text)

        replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

        print("replace_text : " + replace_text)

        analysis_text = (" ".join(myHannanum.nouns(replace_text)))

        return analysis_text