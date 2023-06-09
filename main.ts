input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})
basic.forever(function () {
    if (input.logoIsPressed()) {
        basic.showIcon(IconNames.Heart)
    }
})
