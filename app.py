from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"]) 
def search():
    data = request.json
    words = get_possible_words(data)
    return jsonify(words)

def get_possible_words(data):
    guess_letters = list(data["guess"])
    not_in_letters = list(data["not_in"])
    spot_letters = [data["spot1"] or '', data["spot2"] or '', data["spot3"] or '', data["spot4"] or '', data["spot5"] or '']

    with open('biggest_list.txt', 'r') as words:
        possible_word_list = []
        lines = words.readlines()

        for line in lines:
            y = line.split()
            possible_word_list.append(y[0])

    result_words = []

    for word in possible_word_list:
        in_word = True
        word_letter = list(word)

        for letter in guess_letters:
            if letter.lower() in word and in_word is True:
                in_word = True

                for i in range(5):
                    if word_letter[i] == spot_letters[i] and spot_letters[i] != '' and in_word is True:
                        in_word = True
                    elif spot_letters[i] == '' and in_word is True:
                        in_word = True
                    else:
                        in_word = False
                        break
                    not_in_spot_key = f"not_in_spot{i + 1}"
                    if data[not_in_spot_key] is not None:
                        letters = list(data[not_in_spot_key])

                        for l in letters:
                            if l == word_letter[i]:
                                in_word = False
                                break
            else:
                in_word = False

        for bad in not_in_letters:
            if bad.lower() in word:
                in_word = False

        if in_word is True:
            result_words.append(word)

    return result_words

if __name__ == "__main__":
    app.run(debug=True)
