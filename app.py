from App import createwebsite


app = createwebsite()

if __name__ == "__main__":
    # app.run(debug="True", host="0.0.0.0")
    app.run(debug=True)