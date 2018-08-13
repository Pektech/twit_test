from app import app


@app.route('/')
def index():
    return 'hello pek and monkey'

@app.route('/test')
def test():
    return "and not for getting mr pip"