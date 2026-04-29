from flask import Blueprint

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    return "Список всех вопросов"


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    return "Вопрос создан"


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Получение деталей конкретного вопроса по его ID."""
    return f"Детали вопроса {id}"


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    return f"Вопрос {id} обновлен"


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    return f"Вопрос {id} удален"
