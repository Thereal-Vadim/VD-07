from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Обработка данных (например, сохранение в базу данных)
        print(f"Updated Profile - Name: {username}, Email: {email}, Password: {password}")

        # Перенаправление или вывод подтверждения
        return redirect(url_for('success'))

    return render_template('base.html')


@app.route('/success')
def success():
    return "Profile updated successfully!"


if __name__ == '__main__':
    app.run(debug=True, port=8000)

