def get_missing_skills(career, user_skills):

    role_skills = {
        "Data Scientist":[
            "python",
            "statistics",
            "machine learning",
            "sql",
            "power bi"
        ],

        "Data Analyst":[
            "sql",
            "excel",
            "power bi"
        ]
    }

    required = role_skills.get(career, [])

    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return missing