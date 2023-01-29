import win_magnification as mag
import time

mag_api = mag.WinMagnificationAPI()


DEFAULT = mag.const.COLOR_NO_EFFECT
mag_api.fullscreen.color_effect.raw = DEFAULT
selection = 0

ColorTypes = {
    "No Effect"         :mag.const.COLOR_NO_EFFECT,
    "Inversion"         :mag.const.COLOR_INVERSION_EFFECT,
    "Grayscale"         :mag.const.COLOR_GRAYSCALE_EFFECT,
    "Grayscale Inverted":mag.const.COLOR_INVERTED_GRAYSCALE_EFFECT,
    "Sepia"             :mag.const.COLOR_SEPIA_EFFECT,
    "Deuteranopia"      :mag.const.COLOR_BLIND_DEUTERANOPIA_EFFECT,
    "Protanopia"        :mag.const.COLOR_BLIND_PROTANOPIA_EFFECT,
    "Tritanopia"        :mag.const.COLOR_BLIND_TRITANOPIA_EFFECT
}

def setcolor(type):
    #Apply a specified color filter.
    #mag_api.fullscreen.color_effect.raw = ColorTypes[type]
    #Apply animation
    mag_api.fullscreen.color_effect.make_transition(
    start = DEFAULT,
    end = ColorTypes[type],
    initial_power = 0,
    )

    for i in range(100):
        mag_api.fullscreen.color_effect.transition_power += 0.01
        time.sleep(0.01)
    
    return type

def returncolor(type):

    mag_api.fullscreen.color_effect.make_transition(
        start = ColorTypes[type],
        end = DEFAULT,
        initial_power = 0

    )

    for i in range(100):
        mag_api.fullscreen.color_effect.transition_power += 0.01
        time.sleep(0.01)


def resetcolor():
    #Reset a color filter.
    mag_api.fullscreen.color_effect.reset()
    return ""

def getColor():
    return ColorTypes[type]
