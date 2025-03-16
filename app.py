from flask import Flask, request, jsonify
from models import tours_collection

app = Flask(__name__)

# створити новий тур
@app.route('/api/tours', methods=['POST'])
def create_tour():
    data = request.json
    if not data or not all(key in data for key in ["заголовок", "опис", "ціна"]):
        return jsonify({"error": "Missing required fields (заголовок, опис, ціна)"}), 400

    tour = {
        "заголовок": data.get("заголовок"),
        "опис": data.get("опис"),
        "ціна": float(data.get("ціна")),
        "додатковий_опис": data.get("додатковий_опис", ""),
        "тривалість": data.get("тривалість", ""),
        "що_включено": data.get("що_включено", ""),
        "що_не_включено": data.get("що_не_включено", "")
    }
    result = tours_collection.insert_one(tour)
    return jsonify({"id": str(result.inserted_id)}), 201

# переглянути всі тури
@app.route('/api/tours', methods=['GET'])
def get_all_tours():
    tours = list(tours_collection.find())
    for tour in tours:
        tour["_id"] = str(tour["_id"])
    return jsonify(tours)

# переглянути конкретний тур
@app.route('/api/tours/<tour_id>', methods=['GET'])
def get_tour(tour_id):
    try:
        tour = tours_collection.find_one({"_id": tour_id})
        if tour:
            tour["_id"] = str(tour["_id"])
            return jsonify(tour)
        return jsonify({"error": "Tour not found"}), 404
    except:
        return jsonify({"error": "Invalid tour ID format"}), 400

# відредагувати тур
@app.route('/api/tours/<tour_id>', methods=['PUT'])
def update_tour(tour_id):
    data = request.json
    if not data or not all(key in data for key in ["заголовок", "опис", "ціна"]):
        return jsonify({"error": "Missing required fields (заголовок, опис, ціна)"}), 400

    try:
        result = tours_collection.update_one(
            {"_id": tour_id},
            {"$set": {
                "заголовок": data.get("заголовок"),
                "опис": data.get("опис"),
                "ціна": float(data.get("ціна")),
                "додатковий_опис": data.get("додатковий_опис"),
                "тривалість": data.get("тривалість"),
                "що_включено": data.get("що_включено"),
                "що_не_включено": data.get("що_не_включено")
            }}
        )
        if result.matched_count:
            return jsonify({"message": "Tour updated"})
        return jsonify({"error": "Tour not found"}), 404
    except:
        return jsonify({"error": "Invalid tour ID format"}), 400

# видалити тур
@app.route('/api/tours/<tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    try:
        result = tours_collection.delete_one({"_id": tour_id})
        if result.deleted_count:
            return jsonify({"message": "Tour deleted"})
        return jsonify({"error": "Tour not found"}), 404
    except:
        return jsonify({"error": "Invalid tour ID format"}), 400

# головна сторінка
@app.route('/')
def index():
    search_query = request.args.get('q', '')
    if search_query:
        tours = list(tours_collection.find({
            "$or": [
                {"заголовок": {"$regex": search_query, "$options": "i"}},
                {"опис": {"$regex": search_query, "$options": "i"}}
            ]
        }).limit(20))
    else:
        # 20 туріов
        tours = list(tours_collection.find().sort("_id", -1).limit(20))

    # головна html
    tours_html = ""
    if not tours:
        tours_html = '<div class="alert alert-warning" role="alert">Турів немає</div>'
    else:
        for tour in tours:
            tour_id = str(tour["_id"])
            заголовок = tour.get("заголовок", "Тур без назви")
            ціна = tour.get("ціна", "Н/Д")
            опис = tour.get("опис", "Опис відсутній")
            tours_html += f"""
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">{заголовок}</h5>
                        <p class="card-text">{опис}</p>
                        <p class="card-text"><strong>Ціна:</strong> {ціна}$</p>
                        <a href="/tour/{tour_id}" class="btn btn-primary">Детальніше</a>
                    </div>
                </div>
            </div>
            """

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Туристичне Агентство</title>
        <!-- Bootstrap 5 CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="text-center mb-4">Останні Тури</h1>
            <form method="GET" class="mb-4">
                <div class="input-group">
                    <input type="text" name="q" class="form-control" placeholder="Пошук турів..." value="{search_query}">
                    <button type="submit" class="btn btn-primary">Пошук</button>
                </div>
            </form>
            <div class="row">
                {tours_html}
            </div>
        </div>
        <!-- Bootstrap 5 JS (для інтерактивних компонентів, якщо потрібно) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return html

# веб деталі туру
@app.route('/tour/<tour_id>')
def tour_detail(tour_id):
    try:
        tour = tours_collection.find_one({"_id": tour_id})
        if not tour:
            return """
            <!DOCTYPE html>
            <html lang="uk">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Тур не знайдено</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container mt-5">
                    <div class="alert alert-danger" role="alert">
                        Тур не знайдено
                    </div>
                    <a href="/" class="btn btn-primary">Повернутися на головну</a>
                </div>
            </body>
            </html>
            """, 404

        # html тур
        заголовок = tour.get("заголовок", "Тур без назви")
        опис = tour.get("опис", "Опис відсутній")
        ціна = tour.get("ціна", "Н/Д")
        додатковий_опис = tour.get("додатковий_опис", "Додатковий опис відсутній")
        тривалість = tour.get("тривалість", "Тривалість не вказана")
        що_включено = tour.get("що_включено", "Не вказано")
        що_не_включено = tour.get("що_не_включено", "Не вказано")

        html = f"""
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{заголовок}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1>{заголовок}</h1>
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Короткий опис</h5>
                        <p class="card-text">{опис}</p>
                        <h5 class="card-title">Ціна</h5>
                        <p class="card-text">{ціна}$</p>
                        <h5 class="card-title">Деталі туру</h5>
                        <p class="card-text">{додатковий_опис}</p>
                        <h5 class="card-title">Тривалість</h5>
                        <p class="card-text">{тривалість}</p>
                        <h5 class="card-title">Що включено</h5>
                        <p class="card-text">{що_включено}</p>
                        <h5 class="card-title">Що не включено</h5>
                        <p class="card-text">{що_не_включено}</p>
                    </div>
                </div>
                <a href="/" class="btn btn-primary mt-3">Повернутися на головну</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """
        return html
    except:
        return """
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Помилка</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <div class="alert alert-danger" role="alert">
                    Некоректний формат ID туру
                </div>
                <a href="/" class="btn btn-primary">Повернутися на головну</a>
            </div>
        </body>
        </html>
        """, 400

if __name__ == '__main__':
    app.run(debug=True)