def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if input.logo_is_pressed():
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
