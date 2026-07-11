# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Daisy", color="3AA2DF")
define d_thoughts = Character("Daisy", color="3AA2DF", what_italic=True)

define s = Character("Samyaza", color="DB9B66")

define unknown = Character("???", color="DB9B66")

define a = Character("Anya", color="FF0000")

define audio.sad_music = "audio/by_your_side.ogg"

# The game starts here.

image daisy idle:
    "images/daisy idle.png"
    zoom 0.4
    yoffset 100
image daisy idle smile:
    "images/daisy idle smile.png"
    zoom 0.4
    yoffset 100
image daisy anxious:
    "images/daisy anxious.png"
    zoom 0.4
    yoffset 100
image daisy crying:
    "images/daisy crying.png"
    zoom 0.4
    yoffset 100
image daisy happy:
    "images/daisy happy.png"
    zoom 0.4
    yoffset 100
image daisy nervous:
    "images/daisy nervous.png"
    zoom 0.4
    yoffset 100
image daisy sappy:
    "images/daisy sappy.png"
    zoom 0.4
    yoffset 100
image daisy surprised:
    "images/daisy surprised.png"
    zoom 0.4
    yoffset 100
image anya idle:
    "images/mob.png"
    zoom 0.4
    yoffset 100

image black_alpha:
    "images/black screen.png"
    alpha 0.5

transform flip:
    xzoom -1.0
label start:

    #EXT. UNIVERSITY PARK - DAY
    scene yuri_park_01 with fade

    show anya idle at scene_center_offleft
    a "You know, I really think you should come and meet my friends. They’re really funny. God, I remember one time where……"

    show daisy anxious at scene_center_offright
    d_thoughts "She talks so much. I just wish she’d ask about me… I picked up scrapbooking again… I jut out my scrapbook to be within her line of sight."

    a "….Then, I remember when he even started to eat the rice even though it…."


    d_thoughts "I mean, I should listen.. It’s been a while since we’ve seen each other. But I really don’t want to meet these people. I doubt we’d have anything in common anyways. She’s been in university for a while now, and I’m her age and only just getting started."


    a "….And when he helped me move back in my freshman year. Oh God! {p} Right, you moved in today, didn’t you? How was it?"
    a "Oh wow, now I feel bad that I couldn’t help you much. Is there any other way I could help? I feel really bad, my internship had some stupid orientation thing I had to be at, but. I would’ve much rather helped you.{w} God, I feel really bad…"

    d_thoughts "…"

    a "….And we had a whole thing about changing our language and stuff for a “professional work environment”... so annoying. {w}Wait! Your move-in. Tell me about it!"

    show daisy idle 
    d "It was OK..."


    d_thoughts "It was kind of hard having to do everything myself, but I liked having the place to myself. I’d be kind of embarrassed having a new person see me get all sweaty and out of breath."
    show daisy nervous
    show black_alpha behind daisy
    d_thoughts "The image of myself out of breath and sweaty popped up into my head. My bangs were pinned back, revealing my ugly forehead, my hairline frames my face terribly. My glasses kept sliding down like I was an old man."
    hide black_alpha
    show daisy idle
    d_thoughts "I returned back to earth, only now noticing the grimace on my face. Quickly, I have to relax. Anya will notice and pester me."
    show daisy anxious
    d_thoughts "...{p}...{p}She isn’t even {b}looking{/b}{w=0.2} at me."

    
    a "Just that? How’s your new place? Show me pictures! I bet your dorm is gonna look super cute… Wait, did your mom help out? Oh-  Sorry, I shouldn’t have asked that…"

    show daisy idle
    d "No, it’s okay. She couldn’t help me because she's been weak lately. It was just me."

    a "Oh my god! You should’ve told me! I could’ve helped you."
    show daisy idle
    d "Really, you don’t have to sweat it…."

    show daisy anxious
    d_thoughts "I don’t know why she’s lying to me. We both know that I would just get on her nerves with how clumsy I am; I’m so sore from dropping stuff onto my feet, and I’m sure having her just be in the same vicinity would increase my anxiety tenfold."
    d_thoughts "I can already imagine it, her staring at all of my trinkets and making an extremely thinly veiled comment about how I “oughta declutter now that I’m starting a new leaf.” Yeah right."

    d_thoughts "I remember when we worked on a science project together back in high school. I was kind of bad with putting our presentation together.{w} I could just {b}tell{/b}{w=0.2} she didn’t want to stay after school with me."
    d_thoughts "She was so quiet- it was offputting for her. {p}Her silence could only mean that her mind was filled with all sorts of insults about me."

    a "You sure? I'm worried about you!" 
    #(laugh sprite) 
    extend "This may be mean, but I was thinking… You’re so out of shape that you might snap in half while picking up heavy boxes! We should really go to the gym together…"

    show daisy nervous
    d_thoughts "I can’t help but to make a face…{w}Does Anya really see me like that? Does she really think I can't lift a few boxes on my own? I'm not dumb; I know what people have said about me behind my back and even to my face- I guess I just didn't expect Anya to be like that too.."

    a "…By the way, I’m hosting a welcome back party this Sunday. You should totally come! I really think you’d like Hannah. You guys are both artists! She’s actually graduating this fall, and has an animation job lined up! Wait. Have you chosen your major yet? "

    d_thoughts "I fiddle around with my fingers. The last thing I want to hear right now is a person around my age who is doing far better than I ever will. I didn’t really think I would get this far. I can barely get myself out of bed, choosing a major is beyond me."

    d "Uhm.{p}...{p}I’m still undecided."

    a "Daisy! You have to make sure you pick one out, Okay? You can’t just be cruising through life like that forever!"


    d "{size=*.75}I’m sorry…{/size}"

    a "Don’t worry! I’ll just make sure to check up on you."
    hide anya
    show daisy idle at flip,scene_center
    d_thoughts "I look away, deciding to focus on the leaves as they sway. I hate that I have to acknowledge that Anya looks down on me. "
    show anya idle at scene_center_offright, flip
    extend "She leans in and smiles at me. It feels like a sneer."

    d_thoughts "My entire body sinks. Bitter feelings gnaw at my heart. I try to tune back into Anya’s lecture but I can’t ignore the resentment. I wish I could be her equal, but I’ve let myself fall behind."

    d_thoughts "While deep in thought, I felt a hand touch my shoulder. My body stiffens for a moment."

    a "Daisy, I think you’ll have a great time here, really. It’s nothing like home. People are a lot nicer here, I swear."
    show daisy idle smile
    d_thoughts "I give her an awkward smile.{p} One that doesn’t reach my eyes. {p}I look down, fiddling with my fingers.{w} Anya is the type of person everyone likes."


    d "..Thanks.."

    scene black screen with dissolve

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

    
