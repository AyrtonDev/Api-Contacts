from flask import request
from app.repositories.CategoryRepository import CategoryRepository
from app.utils import print_error, is_valid_uuid, build_response, verify_attrb

class CategoryController:
    def __init__(self, category_repository:CategoryRepository):
        self.category_repository = category_repository

    def all(self):
        try:
            return build_response(
                message="Category list",
                data=self.category_repository.all()
            )

        except Exception as e:
            print_error(e)

    def create(self):
        try:
            category = request.get_json()

            if verify_attrb(category, 'name'):
                return build_response(
                    message="Name is required",
                    data=None,
                    status=400
                )

            newCategory = self.category_repository.create(category['name'])

            return build_response(
                message="Category created",
                data={'id': newCategory},
                status=201
            )

        except Exception as e:
            print_error(e)

    def delete(self, id):
        try:
            if is_valid_uuid(id) is False:
                return build_response(
                    message="Invalid category id",
                    data=None,
                    status=400
                )

            category = self.category_repository.delete(id)

            if category == "Category not found":
                return build_response(
                    message="Category not found",
                    data=None,
                    status=404
                )

            return build_response(
                message=f"Category {category} was deleted",
                data=None,
                status=204
            )

        except Exception as e:
            print_error(e)

category_controller = CategoryController(CategoryRepository())
