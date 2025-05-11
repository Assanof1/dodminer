from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    conn.close()

# Функция для получения имени пользователя из Telegram (имитация)
def get_telegram_username(user_id):
    # В реальном проекте имя нужно получать через Telegram API,
    # здесь просто возвращаем строку по user_id для примера.
    if user_id == 1:
        return "User123"
    return "UnknownUser"

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    conn = get_db_connection()
    user_id = request.args.get('user_id') # Получаем user_id из запроса
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    user_id = int(user_id)
    user = conn.execute('SELECT diamonds, energy FROM users WHERE id = ?', (user_id,)).fetchone()
    close_db_connection(conn)

    if user:
        username = get_telegram_username(user_id) # Получаем имя
        return jsonify({'username': username, 'diamonds': user['diamonds'], 'energy': user['energy']})
    else:
        return jsonify({'error': 'User not found'}), 404

# Добавьте эндпоинты для лидерборда (lider.html) и oos.html, если необходимо
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lider')
def lider():
    return render_template('lider.html')

@app.route('/oos')
def oos():
    return render_template('oos.html')
