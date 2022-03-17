qdee.qdee_Init()
basic.forever(function () {
    if (input.magneticForce(Dimension.Strength) > 1500) {
        qdee.qdee_setMotorSpeed(0, 0)
    }
})
basic.forever(function () {
    if (qdee.qdee_ultrasonic(qdee.ultrasonicPort.port2) < 10) {
        qdee.qdee_setMotorSpeed(-70, -70)
        basic.pause(500)
        qdee.qdee_setMotorSpeed(-70, 70)
        basic.pause(500)
        qdee.qdee_setMotorSpeed(-70, 70)
        basic.pause(randint(500, 2000))
    }
})
basic.forever(function () {
    if (input.magneticForce(Dimension.Strength) > 1500) {
        qdee.qdee_setPixelRGB(QdeeLights.All, QdeeRGBColors.Green)
        qdee.qdee_showLight()
        music.playTone(698, music.beat(BeatFraction.Whole))
        basic.pause(100)
        qdee.qdee_clearLight()
        music.playTone(698, music.beat(BeatFraction.Whole))
        basic.pause(100)
    } else {
        qdee.qdee_setPixelRGB(QdeeLights.All, QdeeRGBColors.Red)
        qdee.qdee_showLight()
        basic.pause(100)
        qdee.qdee_clearLight()
        basic.pause(100)
    }
})
basic.forever(function () {
    qdee.qdee_setMotorSpeed(70, 70)
    basic.pause(randint(1000, 4000))
    qdee.qdee_setMotorSpeed(70, -70)
    basic.pause(randint(1000, 3000))
    qdee.qdee_setMotorSpeed(-70, -70)
    basic.pause(randint(500, 1000))
    qdee.qdee_setMotorSpeed(-70, 70)
    basic.pause(randint(1000, 3000))
})
