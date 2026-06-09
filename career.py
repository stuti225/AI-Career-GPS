def recommend_career(skills):

    if "machine learning" in skills:
        return "Data Scientist"

    elif "react" in skills:
        return "Frontend Developer"

    elif "java" in skills:
        return "Java Developer"

    elif "sql" in skills:
        return "Data Analyst"

    else:
        return "Software Developer"