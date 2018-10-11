from flask import Flask, request
from random import randint, shuffle


app = Flask(__name__)

answer = randint(1, 100)

form = """
<center>
<h1>Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.</h1>
<h2>Zgaduję {}</h2>
<form action="/" method="POST">
        <button type="submit" name="button" value="malo">za mało</button>
        <button type="submit" name="button" value="end">zgadłeś</button>
        <button type="submit" name="button" value="duzo">za dużo</button>
        
        <input type="hidden" name="max" value="{}">
        <input type="hidden" name="min" value="{}">
</form>
</center>
"""


@app.route("/", methods=["GET", "POST"])
def game():

    if request.method == "GET":
        mins = 1
        maks = 1000
        answer = int((maks - mins) / 2) + mins

        return form.format(answer, mins, maks)

    else:
        action = request.form["button"]
        maks = int(request.form.get("max"))
        mins = int(request.form.get("min"))
        answer = int((maks - mins) / 2) + mins

        if action == "end":
            return "<center><h1>Wygrałem!</h1></center>"

        elif action == "malo":
            maks = answer
            answer = int((maks - mins) / 2) + mins

        elif action == "duzo":
            mins = answer
            answer = int((maks - mins) / 2) + mins

        return form.format(answer, maks, mins)


if __name__ == "__main__":
    app.run()
