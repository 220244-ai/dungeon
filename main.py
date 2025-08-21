def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

scene.set_background_color(7)
steve_skin = sprites.create(assets.image("""
    steve
    """), SpriteKind.player)