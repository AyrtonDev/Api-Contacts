from app import db
from app.models.Categories import Categories

class CategoryRepository:
    def all(self):
        try:
            category_list = []
            categories = Categories.query.all()

            for category in categories:
                category_list.append({
                    'id': category.id,
                    'name': category.name,
                })

            return category_list

        except Exception as e:
            raise e

    def create(self, name):
        try:
            new_category = Categories(
                name=name,
            )

            db.session.add(new_category)
            db.session.commit()

            return new_category.id

        except Exception as e:
            raise e

    def delete(self, id):
        try:
            category = Categories.query.filter_by(id=id).first()

            if category is None:
                return "Contact not found"

            db.session.delete(category)
            db.session.commit()

            return id

        except Exception as e:
            raise e
