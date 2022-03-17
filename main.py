qdee.qdee_Init()

def on_forever():
    if input.magnetic_force(Dimension.STRENGTH) > 1500:
        qdee.qdee_setMotorSpeed(0, 0)
basic.forever(on_forever)

def on_forever2():
    if qdee.qdee_ultrasonic(qdee.ultrasonicPort.PORT2) < 10:
        qdee.qdee_setMotorSpeed(-70, -70)
        basic.pause(500)
        qdee.qdee_setMotorSpeed(-70, 70)
        basic.pause(500)
        qdee.qdee_setMotorSpeed(-70, 70)
        basic.pause(randint(500, 2000))
basic.forever(on_forever2)

def on_forever3():
    if input.magnetic_force(Dimension.STRENGTH) > 1500:
        qdee.qdee_setPixelRGB(QdeeLights.ALL, QdeeRGBColors.GREEN)
        qdee.qdee_showLight()
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        basic.pause(100)
        qdee.qdee_clearLight()
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        basic.pause(100)
    else:
        qdee.qdee_setPixelRGB(QdeeLights.ALL, QdeeRGBColors.RED)
        qdee.qdee_showLight()
        basic.pause(100)
        qdee.qdee_clearLight()
        basic.pause(100)
basic.forever(on_forever3)

def on_forever4():
    qdee.qdee_setMotorSpeed(70, 70)
    basic.pause(randint(1000, 4000))
    qdee.qdee_setMotorSpeed(70, -70)
    basic.pause(randint(1000, 3000))
    qdee.qdee_setMotorSpeed(-70, -70)
    basic.pause(randint(500, 1000))
    qdee.qdee_setMotorSpeed(-70, 70)
    basic.pause(randint(1000, 3000))
basic.forever(on_forever4)
