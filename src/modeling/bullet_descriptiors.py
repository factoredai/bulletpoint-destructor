WHAT = "Based on the bullet point description, extract what was developed to accomplish the project goals. This refers to the main solution. For example: 'System architecture of the backed', 'Recommender System', 'A CI/CD pipeline'"

HOW = "Based on the bullet point description, extract how the project was developed. For example: 'XGBoost, Random Forest, Logistic Regression and various Machine Learning algorithms. The process involved feature engineering, feature selection, hyperparameter tuning, and model testing.', 'using regular expresions pattern (regex)', 'By consuming REST API Endpoints, paring th information and filling the predefined layers with the information'"

WHY = "Using the bullet point description, extract why the project was developed. This refers to the main problem that the company or the client was facing or having. For example: 'To automate the installation process of a slot machine', 'To predict when an user will pay a loan or not', 'To enable easy access and sharing of data across the organization'"

WHOM = "Using the bullet point description, extract the information related to the client, for whom the project was developed, this can also refer to the company type. For example: 'Intervision gaming', ' Multinational Product Goods Company', 'Trasnport network company'"

SKILLS = "Based on the bullet point description, extract the skills or tools used on the project. Most of the times these are refered as nouns. Return those values separated by a comma if there is more than one For example: Python, MLFlow, AWS, GCP, Databricks, Airflow"


SYSTEM_MESSAGE = f"""
You will be given a resume's bullet point, which corresponds to an engineer
project experience at a given company/client. You should output your response
in JSON format, with 5 keys which are: what, how, why, whom and skills. 

what: {WHAT}

how: {HOW}

why: {WHY}

whom: {WHOM}

skills: {SKILLS}
"""