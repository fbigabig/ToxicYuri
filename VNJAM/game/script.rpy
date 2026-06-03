# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bea = Character("Beatrice", color="ffcc00")
define bat = Character("Battler", color="ff0000")

image beatrice cackle = Image("beatrice cackle.png", oversample = 0.5)
image beatrice neutral = Image("beatrice neutral.png", oversample = 0.5)
image beatrice pout = Image("beatrice pout.png", oversample = 0.5)
image beatrice smirk = Image("beatrice smirk.png", oversample = 0.5)
image beatrice smile = Image("beatrice smile.png", oversample = 0.5)

image battler neutral = Image("battler neutral.png", oversample = 0.5)
image battler objection = Image("battler objection.png", oversample = 0.5)
image battler foolish = Image("battler foolish.png", oversample = 0.5)
image battler smile = Image("battler smile.png", oversample = 0.5)

image witch room = Image("witch room.webp", oversample = .3)

transform superleft:
    xpos -400

image deltarune fountain = Movie(
    play="images/deltarune fountain.ogg",
    size=(1920, 1080)
)
image lines = Movie(
    play="images/lines.webm",
    size=(1920, 1080)
)

# The game starts here.


label start:

    scene witch room
    play music fishy_aroma
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show battler neutral at left 
    bat "Where the fuck am I"

    show beatrice smirk at right with Dissolve(1.0)
    play audio cackle

    show battler foolish at left 
    bat "Oh god not this again"

    show beatrice smile at right

    bea "What's the problem here?."

    show battler objection at superleft
    bat "You killed my family a zillion times or something"

    show beatrice smirk
    play audio cackle

    bea "oh yea i did that"

    scene lines with dissolve
    pause
    show beatrice pout
    pause

    bea "oh what now"
    # This ends the game.

    return
