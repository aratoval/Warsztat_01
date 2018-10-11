from flask import Flask, request
from random import randint, shuffle


app = Flask(__name__)

answer = randint(1, 100)

form = """
<center>
<h1>Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.</h1>
<h2>Zgaduję {}</h2>
<form action="/" method="POST">
        <button type="submit" name="malo">za mało</button>
        <button type="submit" name="end">zgadłeś</button>
        <button type="submit" name="duzo">za dużo</button>
        
        <input type="hidden" name="max" value="1000">
        <input type="hidden" name="min" value="0">
</form>
</center>
"""


@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return form.format("500")
    else:
        maks = request.form.get("max")
        mins = request.form.get("min")
        if request.form["button"] == "malo":
            request.form("max")
        return form.format(str(maks))


if __name__ == "__main__":
    app.run()
