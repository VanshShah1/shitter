import reflex as rx

class ShitterConfig(rx.Config):
    pass

config = ShitterConfig(
    app_name="shitter",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)