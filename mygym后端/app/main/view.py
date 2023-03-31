import base64
from flask import jsonify, request
from flask_cors import CORS

from app import db
from app.main import view
from app.model import users

CORS(view, supports_credentials=True)


@view.route('/home', methods=['get'])
def get():
    return jsonify(code=200, message="成功", data=[
        {
            "categoryChild": [
                {
                    "categoryChild": [
                        {
                            "categoryName": "子子标题",
                            "categoryId": 1
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 2
                        }
                    ],
                    "categoryName": "子标题",
                    "categoryId": 1
                },
                {
                    "categoryChild": [
                        {
                            "categoryName": "子子标题",
                            "categoryId": 5
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 6
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 7
                        }
                    ],
                    "categoryName": "子标题",
                    "categoryId": 2
                }
            ],
            "categoryName": "健身类型1",
            "categoryId": 1
        },
        {
            "categoryChild": [
                {
                    "categoryChild": [
                        {
                            "categoryName": "子子标题",
                            "categoryId": 61
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 62
                        }
                    ],
                    "categoryName": "子标题",
                    "categoryId": 3
                },
                {
                    "categoryChild": [
                        {
                            "categoryName": "子子标题",
                            "categoryId": 63
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 64
                        }
                    ],
                    "categoryName": "子标题",
                    "categoryId": 4
                },
                {
                    "categoryChild": [
                        {
                            "categoryName": "子子标题",
                            "categoryId": 67
                        },
                        {
                            "categoryName": "子子标题",
                            "categoryId": 68
                        }
                    ],
                    "categoryName": "子标题",
                    "categoryId": 5
                }
            ],
            "categoryName": "健身类型2",
            "categoryId": 2
        }]
                   )
