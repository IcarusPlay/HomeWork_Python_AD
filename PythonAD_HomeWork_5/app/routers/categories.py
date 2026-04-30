from flask import Blueprint, jsonify, request
from app.models import db, Category
from pydantic_core import ValidationError

from app.schemas.questions import CategoryCreate, CategoryResponse

categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/', methods=['GET'])
def get_categories():
    """Получение списка всех категорий."""
    cats = db.session.query(Category).all()
    cats_data = [CategoryResponse.model_validate(c).model_dump() for c in cats]
    return jsonify(cats_data), 200


@categories_bp.route('/', methods=['POST'])
def create_category():
    """Создание новой категории."""
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Название категории не указано'}), 400

    cat = Category(name=data['name'])
    db.session.add(cat)
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(cat).model_dump()), 201


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Обновление категории по ID."""
    cat = db.session.query(Category).filter(Category.id == id).one_or_none()
    if cat is None:
        return jsonify({'message': 'Категория не найдена'}), 404

    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Название категории не указано'}), 400

    cat.name = data['name']
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(cat).model_dump()), 200


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Удаление категории по ID."""
    cat = db.session.query(Category).filter(Category.id == id).one_or_none()
    if cat is None:
        return jsonify({'message': 'Категория не найдена'}), 404

    db.session.delete(cat)
    db.session.commit()

    return jsonify({'message': f'Категория с ID {id} удалена'}), 200
