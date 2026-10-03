EVALUATION_QUESTIONS = [
    {
        "question": "How does user authentication work?",
        "expected_symbols": [
            "authenticate_user",
        ],
        "expected_files": [
            "auth.py",
        ],
    },
    {
        "question": "Where is the database connection created?",
        "expected_symbols": [
            "create_database_connection",
        ],
        "expected_files": [
            "database.py",
        ],
    },
    {
        "question": "How is a new user created?",
        "expected_symbols": [
            "create_user",
        ],
        "expected_files": [
            "user_service.py",
        ],
    },
    {
        "question": "What happens when login is called?",
        "expected_symbols": [
            "login",
            "authenticate_user",
            "create_user",
        ],
        "expected_files": [
            "main.py",
            "auth.py",
            "user_service.py",
        ],
    },
]