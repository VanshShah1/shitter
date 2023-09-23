from rxconfig import config
import reflex as rx
from typing import List

class User(rx.Model, table=True):
    item: str

class State(rx.State):
    items: List[str] = []
    new_item: str

    def add_item(self):
        self.items += [self.new_item]

def get_item(item):
    return rx.list_item(
        rx.box(
        rx.vstack(
        rx.hstack(
            rx.avatar(size='sm'),
            rx.text("@vansh", color="white", font_size="1.25em"),
            padding_right="90%",
        ),
        rx.vstack(
            rx.text(item, color="white", font_size="1.25em"),
            rx.hstack(
                rx.button(rx.icon(tag="arrow_up")),
                rx.text("0", color="white"),
            ),
        ),
        padding_left="10%",
        width='80%',
        ),
        
        border="1px",
        width='800px',
        padding_top="20px",
        padding_bottom="20px",
        padding_left="20px",
        padding_right="20px",
        )
    )

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("💩shitter", color="white", font_size="5em"),
        rx.text("shit out your deepest darkest secrets secretly🤫", color="white", font_size="1.5em"),       
        rx.hstack(
        rx.input(
            on_blur=State.set_new_item,
            placeholder="shit here...",
            bg="black",
            width="90%",
            color='white',
        ),
        rx.button(
            "💩", on_click=State.add_item
        ),
        ),
        rx.divider(width="90%"),
        rx.list(
            rx.foreach(
                State.items,
                get_item,
            ),
        ),
        
    )

styles={
    "background_color":"black",
}
# Add state and page to the app.
app = rx.App(State=State, style=styles)
app.add_page(index)
app.compile()