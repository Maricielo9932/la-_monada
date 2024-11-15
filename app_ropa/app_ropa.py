import reflex as rx

def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("LA MONADA!", size="9",color="white"),
        rx.hstack(
            rx.vstack(
                rx.text(
                "¡La Monada! Tu app para encontrar la ropa que te hace sentir como una reina (o un rey). 👑  Con La Monada, olvídate de las búsquedas interminables y encuentra el estilo perfecto para ti, sin importar tu presupuesto.",
                size="5", color="white"
            ),
            rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",background="white",color="black"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    
                    rx.link(
                        rx.button("categoria!",background="white",color="black"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),background="white",color="black"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),background="white",color="black"),
                        href="",
                        is_external=True,
                    ),
                    rx.image(src="https://i.pinimg.com/736x/70/4e/3b/704e3bd4968a677a69741cf34712aa1c.jpg"),
                ),
            ),
             
            rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",background="white",color="black"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
            ), 
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        bg="black"
    ),


app = rx.App()
app.add_page(index)