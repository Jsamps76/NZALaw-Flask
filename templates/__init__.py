from app import routes, models

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
