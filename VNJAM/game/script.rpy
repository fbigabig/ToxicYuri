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
image angel idle:
    "images/angel idle.png"
    zoom 0.4
    yoffset 100
image angel shadowed:
    "images/angel shadowed.png"
    zoom 0.4
    yoffset 100
image black_alpha:
    "images/black screen.png"
    alpha 0.5
layeredimage yuri_living_room_night:
    always:
        "black screen.png"
    always:
        "yuri_living_room.png"
        alpha 0.5


transform flip:
    xzoom -1.0
transform unflip:
    xzoom 1.0
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
    show daisy idle at scene_center
    d_thoughts "I look away, deciding to focus on the leaves as they sway. I hate that I have to acknowledge that Anya looks down on me. "
    show anya idle at scene_center_offright
    extend "She leans in and smiles at me. It feels like a sneer."

    d_thoughts "My entire body sinks. Bitter feelings gnaw at my heart. I try to tune back into Anya’s lecture but I can’t ignore the resentment. I wish I could be her equal, but I’ve let myself fall behind."

    d_thoughts "While deep in thought, I felt a hand touch my shoulder. My body stiffens for a moment."

    a "Daisy, I think you’ll have a great time here, really. It’s nothing like home. People are a lot nicer here, I swear."
    show daisy idle smile
    d_thoughts "I give her an awkward smile.{p} One that doesn’t reach my eyes. {p}I look down, fiddling with my fingers.{w} Anya is the type of person everyone likes."


    d "..Thanks.."

    scene black screen with dissolve

    d_thoughts "The stale air of the hallway was suffocating.{w} The scent of wet carpet and dust filled my nose as I tried to shut out all of the sounds of the oncoming students jestering with their peers."
    d_thoughts "I wanted to rush home, I couldn’t stand the noise.{w} Honestly, it’s better for me to head home anyways.{w} Anya was getting tired of me." 
    d_thoughts "I finally get to my door, it’s a simple two bedroom one bathroom.{w} Luckily the school is more accommodating since I started school a bit later than my peers."
    d_thoughts "I hope my roommate is the same as me.{w} or at least just someone who is never in the house."

    d_thoughts "Turning the door knob, a loud creaking greets my ears. The scent of old fabric and mildew wafts in from the AC, which is already running on full blast."
    scene yuri_living_room with fade
    d_thoughts "My pupils adjust to the brightness in the apartment."

    d_thoughts "Huh..? I don’t remember leaving the lights on when I left."

    d_thoughts "...Whatever. I'm just tired. I'm going to turn the light off."
    show black_alpha
    
    d_thoughts "The AC was blasting."
    show daisy idle behind black_alpha at scene_right, flip with dissolve
    d_thoughts " I put my bag down on the dining room chair. " #add extend here if u can figure out transitions

    d_thoughts "I made my way to enjoy the living room. Finally, I can relax on a couch without being on edge."
    #add sfx here 
    show angel shadowed behind black_alpha at scene_center, flip with vpunch 
    d_thoughts "A shadow in the corner of my eye leans towards me."
    show daisy nervous at unflip
    d_thoughts "A small yelp escapes from my mouth. Every single hair on my body that I forgot to pluck out just raised up. Fearfully, I {cps=*.25}slowly look up at the figure. My heart beats out of my chest.{/cps}"

    unknown "Hey, what took you so long?"

    d_thoughts "What..?"

    stop music


    d_thoughts "I stop in my tracks like a doe in the headlights and make eye contact with the most beautiful woman I've ever seen. "

    show angel idle at scene_center

    d_thoughts "She stands tall before me, her strong build illuminated by the moonlight. I can’t make out her entire face right now, but she’s giving me a sweet smile and I can see the golden glint of her eyes through the darkness."
    d_thoughts "I don’t know what it is about her, but her aura made my entire body go weak-{p}"
    show daisy sappy
    extend "I’m at her mercy."
    show daisy anxious
    d_thoughts "She stuns me. But, despite her beauty, my eyes went straight to her cross necklace. My stomach is in knots."
    #play music wav_blessing
    unknown "I was going crazy thinking I was gonna live alone in this 2x1. Good thing you ended up filling this spot last minute. I was trying to ask them about you but they couldn’t say anything."

    d "Oh… uhm… right. Sorry I got the email but never reached out to you."

    unknown "Email?"

    show daisy idle smile
    d "Uhm… maybe they sent it to the wrong address or something…. {w}That happens to me too…{w} sometimes.."
    show daisy idle
    d_thoughts "She smiles at me, waiting for something." #" (her sprite changing to a blank smile)
    show daisy idle smile
    d "Oh sorry, I’m Daisy."

    s "I’m Samyaza, nice to meet you!"

    show daisy idle #never smile for long!
    d_thoughts "She confidently reaches her hand out… Her voice is a bit too loud for my liking, but that's fine, she seems nice otherwise. Hopefully I can stay out of her way."

    d_thoughts "I shyly reach my hand out to hers, and she grips it with a vigorous smile and level of enthusiasm that is unnatural. She’s acting like a used car salesman, each shake felt performed. She seemed as if she was trying to be relaxed, but her smile twitched in exhaustion."

    d_thoughts "She feels a bit more… sympathetic? Earlier today, I was practicing my greeting to Anya in the mirror. Performing my smile in the mirror to make sure there wasn't any underlying strangeness that she could pick up on."
    d_thoughts "...I didn’t want to worry Anya with how bad things had been recently."

    s "Cool.. You have such a cute face. Has anyone ever told you that?"

    show daisy nervous
    d "Thanks…. Uhm, I think so?"
    show black screen behind daisy:
        alpha 0.25
    show angel idle behind black
    d_thoughts "I shift uncomfortably, I really want to get back into my room and hide in bed. But no matter how much I try to break eye contact, my eyes just keep meeting with hers."
    show black screen behind daisy:
        alpha 0.5
    d_thoughts "I know that she’s analyzing my face, each and every single one of my pores- my ugly acne scars, and my long overdue-to-be-tweezed eyebrows…"
    show black screen behind daisy:
        alpha 0.75
    d_thoughts "She's already thinking about how terrible of a roommate I’m going to be, that I’ll be dirty and weird, how I probably won't wash the dishes, or can’t even socialize with her or her friends properly."
    show black screen behind daisy:
        alpha 1
    show daisy crying
    d_thoughts "I can already imagine it. She invites her new friends over, they’re loud as hell in the living room."
    d_thoughts "I work up the courage to leave my room to get a glass of water, something to eat, anything- as soon as I step out they immediately go silent, briefly sneaking glances at me from the corners of their eyes. "
    d_thoughts "The second I slam my door, they go back to laughing, whispering about how weird Samyaza’s roommate is."
    d_thoughts "Quiet enough to feign ignorance (“We were talking about someone else!”- yeah right, bitch,) but loud enough that the roommate in question can still hear it even if she tries her absolute hardest to pretend they’re not there."
    d_thoughts  "They’re absolutely hysterical, shrieking like hyenas over how weird Samyaza’s roommate is. She’d laugh and agree, and talk about how much she couldn’t wait to move out."
    show daisy anxious
    d_thoughts "I can’t let that happen this time. I have to prove to her that I’m good at all of these things.{p}That I can function as a human being for once."

    hide black screen
    s "Did you hear me? What’s your major?"
    d "Uh. Oh, sorry. I’m undecided."

#SAMYAZA (happy/genuine sprite)
    s "Oh wow, really? Me too. There’s just so much to choose from, I couldn’t decide either. What classes are you taking? Hopefully we’ll have some together?"
    show daisy idle
    d_thoughts "I scroll briefly through my gallery and hand her my phone, on it a screenshot of my class schedule."
    s "Aw man, only three. That {i}sucks{/i}."

    d "Well… I’m only taking 4 classes anyways.. "
    show daisy anxious
    d_thoughts "I look down, hoping her energy dies down soon enough. I let out a long, loud, and very drawn out yawn. She’s still observing me."

    s "Maybe I can switch into your fourth? I’d love to have a friend in all four classes."
    
    d_thoughts "A friend? I can’t believe this girl is already considering us to be friends. I feel bad for her, when she sees who the real me is, she’ll hop on over to whatever better, well-adjusted friend group she’ll make. I don’t know their faces yet, but I’ll know them soon enough."

    d "Uh. Yea. That’s okay."

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

    
