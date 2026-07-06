# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Daisy", color="3AA2DF")
define d_thoughts = Character("Daisy", color="3AA2DF", what_italic=True)

define s = Character("Samyaza", color="DB9B66")

define unknown = Character("???", color="DB9B66")

define audio.sad_music = "audio/by_your_side.ogg"

# The game starts here.


label start:


    play music wav_by_your_side

    scene black screen with fade

    d_thoughts "The stale air of the hallway was suffocating.{w} The scent of wet carpet and dust filled my nose as I tried to shut out all of the sounds of the oncoming students jestering with their peers."
    d_thoughts " I wanted to rush home, I couldn’t stand the noise.{w} Honestly, it’s better for me to head home anyways.{w} Anya was getting tired of me." 
    d_thoughts "I finally get to my door, it’s a simple two bedroom one bathroom.{w} Luckily the school is more accommodating since I started school a bit later than my peers."
    d_thoughts "I hope my roommate is the same as me. or just someone who is never in the house too."

    d_thoughts "The old door creaks open, piercing through the stillness of the apartment."# [descriptions] 
    show daisy idle2 at left
    d_thoughts "The AC was blasting. I put my bag down on the dining room chair. "

    d_thoughts "I was about to sit down on the couch, until I saw the silhouette of a person right in the corner of my eye."

    d_thoughts "I spun around to look behind me.{w} My heart beat out of my chest."

    unknown "Hey, what took you so long?"

    d_thoughts "What."

    stop music


    scene room daisy
    d_thoughts "The light turns on. My eyes take a bit to adjust to the brightness."

    d_thoughts "I stop in my tracks, like a doe in the headlights and make eye contact with a beautiful woman."

    show angel idle2 at left

    play music wav_blessing
    unknown "I was going crazy thinking I was gonna live alone in this 2x1. Good thing you ended up filling this spot last minute. I was trying to ask them about you but they couldn’t say anything."

    show daisy idle2 at right
    d "Oh… uhm… right. Sorry I got the email but never reached out to you."

    unknown "Email?"

    d "Uhm… maybe they sent it to the wrong address or something…. {w}That happens to me too… sometimes.."

    d_thoughts "She smiles at me, waiting for something." #" (her sprite changing to a blank smile)

    d "Oh sorry, I’m Daisy."

    s "I’m Samyaza, nice to meet you!"

    return


    
'''
    play music fishy_aroma

    scene room daisy with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show daisy idle1 at left 
    d "Where the fuck am I"

    show angel idle1 at right with Dissolve(1.0)
    play audio cackle

    d "Oh god not this again"


    s "What's the problem here?."

    d "You killed my family a zillion times or something"

    play audio cackle

    s "oh yea i did that"
'''

    
