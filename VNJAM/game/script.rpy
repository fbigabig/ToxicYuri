# The script of the game goes in this file.


define config.default_textshader = "typewriter"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character("Daisy", color="#3AA2DF")

define narrator = Character(color="#3AA2DF", what_italic=True)

define s = Character("Samyaza", color="#DB9B66")

define unknown = Character("???", color="#DB9B66")
define au = Character("???", color="#ab3f3f")

define a = Character("Anya", color="#ab3f3f")
define creature = Character(color="#000000")

define audio.sad_music = "audio/by_your_side.ogg"
define config.fadeout_audio = 0.3

init python:
  renpy.music.register_channel("sound2", "sfx",loop=False,tight=True)

# The game starts here.

image daisy idle:
    "images/daisy idle.png"
    zoom 0.4
    yoffset 100
image daisy idle smile:
    "images/daisy idle smile.png"
    zoom 0.4
    yoffset 100
image daisy idle closed eyes:
    "images/daisy idle closed eyes.png"
    zoom 0.4
    yoffset 100
image daisy anxious:
    "images/daisy anxious.png"
    zoom 0.4
    yoffset 100
image daisy pain and sweat:
    "images/daisy pain and sweat.png"
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
image daisy blush:
    "images/daisy neutral blush.png"
    zoom 0.4
    yoffset 100
image daisy upset:
    "images/daisy upset.png"
    zoom 0.4
    yoffset 100
image daisy angry:
    "images/daisy angry.png"
    zoom 0.4
    yoffset 100
image daisy surprised:
    "images/daisy surprised.png"
    zoom 0.4
    yoffset 100

image anya idle:
    "images/anya idle.png"
    zoom 0.4
    yoffset 100

image anya upset:
    "images/anya upset.png"
    zoom 0.4
    yoffset 100
image anya happy:
    "images/anya happy.png"
    zoom 0.4
    yoffset 100
image anya suspicious:
    "images/anya suspicious.png"
    zoom 0.4
    yoffset 100


image angel idle:
    "images/angel idle.png"
    zoom 0.4
    yoffset 100
image angel idle closed eyes:
    "images/angel idle closed eyes.png"
    zoom 0.4
    yoffset 100
image angel confused:
    "images/angel confused.png"
    zoom 0.4
    yoffset 100
image angel desire:
    "images/angel desire.png"
    zoom 0.4
    yoffset 100
image angel frown:
    "images/angel frown.png"
    zoom 0.4
    yoffset 100
image angel pain:
    "images/angel pain.png"
    zoom 0.4
    yoffset 100
image angel pain open nowing:
    "images/angel pain open nowing.png"
    zoom 0.4
    yoffset 100.25
    xoffset -.5
image angel pain closed nowing:
    "images/angel pain closed nowing.png"
    zoom 0.4
    yoffset 100.25
    xoffset -.5
image angel happy:
    "images/angel happy.png"
    zoom 0.4
    yoffset 100
image angel happy big:
    "images/angel happy big.png"
    zoom 0.4
    yoffset 100
image angel obsessed:
    "images/angel obsessed.png"
    zoom 0.4
    yoffset 100
image angel sad:
    "images/angel sad.png"
    zoom 0.4
    yoffset 100
image angel scary:
    "images/angel scary.png"
    zoom 0.4
    yoffset 100
image angel pain scary nowings:
    "images/angel pain scary nowings.png"
    zoom 0.4
    yoffset 100
image angel shadowed:
    "images/angel shadowed.png"
    zoom 0.4
    yoffset 100


layeredimage angel idle wings:

    always:
        "images/wings.png"
    always:
        "images/angel idle.png"
        xoffset 360

    zoom 0.4
    yoffset 100
layeredimage angel pain open:
    always:
        "images/wings.png"
    always:
        "images/angel pain open nowing.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel pain closed:
    always:
        "images/wings.png"
    always:
        "images/angel pain closed nowing.png"
        xoffset 360
    zoom 0.4
    yoffset 100

layeredimage angel confused wings:
    always:
        "images/wings.png"
    always:
        "images/angel confused.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel desire wings:
    always:
        "images/wings.png"
    always:
        "images/angel desire.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel frown wings:
    always:
        "images/wings.png"
    always:
        "images/angel frown.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel pain wings:
    always:
        "images/wings.png"
    always:
        "images/angel pain.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel happy wings:
    always:
        "images/wings.png"
    always:
        "images/angel happy.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel happy big wings:
    always:
        "images/wings.png"
    always:
        "images/angel happy big.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel obsessed wings:
    always:
        "images/wings.png"
    always:
        "images/angel obsessed.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel sad wings:
    always:
        "images/wings.png"
    always:
        "images/angel sad.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel scary wings:
    always:
        "images/wings.png"
    always:
        "images/angel scary.png"
        xoffset 360
    zoom 0.4
    yoffset 100
layeredimage angel pain scary wings:
    always:
        "images/wings.png"
    always:
        "images/angel pain scary nowings.png"
        xoffset 360
    zoom 0.4
    yoffset 100



image black alpha:
    "images/black screen.png"
    alpha 0.5
layeredimage yuri_living_room_night:
    always:
        "black screen.png"
    always:
        "yuri_living_room.png"
        alpha 0.5
layeredimage room daisy night:
    always:
        "black screen.png"
    always:
        "room daisy.png"
        alpha 0.5
layeredimage yuri_park_night:
    always:
        "black screen.png"
    always:
        "yuri_park_01.png"
        alpha 0.5
transform flip:
    xzoom -1.0
transform unflip:
    xzoom 1.0




transform small_wobble:
    perspective True
    subpixel True
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    zoom 1.1
    ypos 650
    xpos 1200
    block:
        linear 1.5 xoffset 5 yoffset 3 rotate 3 blur 10
    block:
        linear 1.5 xoffset 0 yoffset 0 rotate 0 blur 3
    block:
        linear 1.5 xoffset -5 yoffset -3 rotate -3 blur 10
    block:
        linear 1.5 xoffset 0 yoffset 0 rotate 0 blur 3
    repeat


label start:

    #EXT. UNIVERSITY PARK - DAY
    scene yuri_park_01 with fade
    play music wav_theres_no_heart_like_yours
    play sound bird_chirping volume 0.1 loop

    show anya happy at scene_center_offleft
    a "You know, I really think you should come and meet my friends. They're really funny. God, I remember one time where......"

    show daisy anxious at scene_center_offright
    "She talks so much. I just wish she'd ask about me... I picked up scrapbooking again... {nw}"
    show scrapbook_inspect with {'master':dissolve}
    extend "I jut out my scrapbook to be within her line of sight."
    hide scrapbook_inspect with dissolve

    a "....Then, I remember when he even started to eat the rice even though it...."


    "I mean, I should listen.. It's been a while since we've seen each other. But I really don't want to meet these people. I doubt we'd have anything in common anyways. She's been in university for a while now, and I'm her age and only just getting started."


    a "....And when he helped me move back in my freshman year. Oh God, right, you moved in today, didn't you? How was it?"
    show anya idle
    a "Oh wow, now I feel bad that I couldn't help you much. Is there any other way I could help? I feel really bad, my internship had some stupid orientation thing I had to be at, but. I would've much rather helped you.{w} God, I feel really bad..."

    "..."
    show anya happy
    a "....And we had a whole thing about changing our language and stuff for a “professional work environment”... so annoying. {w}Wait! Your move-in. Tell me about it!"

    show daisy idle 
    d "It was OK..."


    "It was kind of hard having to do everything myself, but I liked having the place to myself. I'd be kind of embarrassed having a new person see me get all sweaty and out of breath."
    show daisy nervous
    show black alpha behind daisy
    "The image of myself out of breath and sweaty popped up into my head. My bangs were pinned back, revealing my ugly forehead, my hairline frames my face terribly. My glasses kept sliding down like I was an old man."
    hide black
    show daisy idle
    "I returned back to earth, only now noticing the grimace on my face. Quickly, I have to relax. Anya will notice and pester me."
    show daisy anxious
    "...{p}...{p}She isn't even {b}looking{/b}{w=0.2} at me."

    show anya idle
    a "Just that? How's your new place? Show me pictures! I bet your dorm is gonna look super cute... Wait, did your mom help out? Oh-  Sorry, I shouldn't have asked that..."

    show daisy idle
    d "No, it's okay. She couldn't help me because she's been weak lately. It was just me."

    a "Oh my god! You should've told me! I could've helped you."
    show daisy idle
    d "Really, you don't have to sweat it...."

    show daisy anxious
    "I don't know why she's lying to me. We both know that I would just get on her nerves with how clumsy I am; I'm so sore from dropping stuff onto my feet, and I'm sure having her just be in the same vicinity would increase my anxiety tenfold."
    "I can already imagine it, her staring at all of my trinkets and making an extremely thinly veiled comment about how I “oughta declutter now that I'm starting a new leaf.” Yeah right."

    "I remember when we worked on a science project together back in high school. I was kind of bad with putting our presentation together.{w} I could just {b}tell{/b}{w=0.2} she didn't want to stay after school with me."
    "She was so quiet- it was offputting for her. {p=1}Her silence could only mean that her mind was filled with all sorts of insults about me."
    show anya suspicious
    a "You sure? I'm worried about you! {w=1}" 
    show anya happy
    extend "This may be mean, but I was thinking... You're so out of shape that you might snap in half while picking up heavy boxes! We should really go to the gym together..."

    show daisy nervous
    "I can't help but to make a face...{w=1}Does Anya really see me like that? Does she really think I can't lift a few boxes on my own? I'm not dumb; I know what people have said about me behind my back and even to my face- I guess I just didn't expect Anya to be like that too.."

    a "...By the way, I'm hosting a welcome back party this Sunday. You should totally come! I really think you'd like Hannah. You guys are both artists! She's actually graduating this fall, and has an animation job lined up! Wait. Have you chosen your major yet? "

    "I fiddle around with my fingers. The last thing I want to hear right now is a person around my age who is doing far better than I ever will. I didn't really think I would get this far. I can barely get myself out of bed, choosing a major is beyond me."

    d "Uhm.{p}...{p}I'm still undecided."
    show anya upset
    a "Daisy! You have to make sure you pick one out, Okay? You can't just be cruising through life like that forever!"


    d "{size=*.75}I'm sorry...{/size}"
    show anya idle
    a "Don't worry! I'll just make sure to check up on you."
    #hide anya
    show daisy upset at flip
    "I look away, deciding to focus on the leaves as they sway. I hate that I have to acknowledge that Anya looks down on me. {w=1.0}"
    show anya happy at scene_center with {'master': moveinright}
    extend "She leans in and smiles at me. It feels like a sneer."

    "My entire body sinks. Bitter feelings gnaw at my heart. I try to tune back into Anya's lecture but I can't ignore the resentment. I wish I could be her equal, but I've let myself fall behind."

    "While deep in thought, I felt a hand touch my shoulder. My body stiffens for a moment."
    show anya idle
    a "Daisy, I think you'll have a great time here, really. It's nothing like home. People are a lot nicer here, I swear."
    show daisy idle smile at unflip
    "I give her an awkward smile.{p=.5}One that doesn't reach my eyes. {p=.5}I look down, fiddling with my fingers.{w=1} Anya is the type of person everyone likes."


    d "..Thanks.."
    stop music
    scene black screen with dissolve
    play sound ac_hum volume 0.1 loop
    play music wav_stay_with_me volume 2
    "The stale air of the hallway was suffocating.{w=.5} The scent of wet carpet and dust filled my nose as I tried to shut out all of the sounds of the oncoming students jestering with their peers."
    "I wanted to rush home, I couldn't stand the noise.{w=.5} Honestly, it's better for me to head home anyways.{w=.5} Anya was getting tired of me." 
    "I finally get to my door, it's a simple two bedroom one bathroom.{w=.5} Luckily the school is more accommodating since I started school a bit later than my peers."
    "I hope my roommate is the same as me.{w=.5} Or at least just someone who is never in the house."

    "Turning the door knob, a loud creaking greets my ears. The scent of old fabric and mildew wafts in from the AC, which is already running on full blast."
    scene yuri_living_room with fade
    "My pupils adjust to the brightness in the apartment."

    "Huh..? I don't remember leaving the lights on when I left."

    "...Whatever. I'm just tired. I'm going to turn the light off."
    show black alpha
    
    "The AC was blasting."
    show daisy idle behind black at scene_right, flip with dissolve
    " I put my bag down on the dining room chair. " #add extend here if u can figure out transitions

    "I made my way to enjoy the living room. Finally, I can relax on a couch without being on edge."
    #add sfx here 
    show angel shadowed behind black at scene_center, flip with vpunch 
    "A shadow in the corner of my eye leans towards me."
    show daisy nervous at unflip
    "A small yelp escapes from my mouth. Every single hair on my body that I forgot to pluck out just raised up. Fearfully, I {cps=*.25}slowly look up at the figure. My heart beats out of my chest.{/cps}"

    unknown "Hey, what took you so long?"

    "What..?"

    stop music


    "I stop in my tracks like a doe in the headlights and make eye contact with the most beautiful woman I've ever seen. "

    show angel idle at scene_center
    play music wav_midnight
    "She stands tall before me, her strong build illuminated by the moonlight. I can't make out her entire face right now, but she's giving me a sweet smile and I can see the golden glint of her eyes through the darkness."
    "I don't know what it is about her, but her aura made my entire body go weak-{p}"
    show daisy sappy
    extend "I'm at her mercy."
    show daisy anxious
    "She stuns me. But, despite her beauty, my eyes went straight to her cross necklace. My stomach is in knots."
    #play music wav_blessing
    show angel happy
    unknown "I was going crazy thinking I was gonna live alone in this 2x1. Good thing you ended up filling this spot last minute. I was trying to ask them about you but they couldn't say anything."

    d "Oh... uhm... right. Sorry I got the email but never reached out to you."
    show angel confused
    unknown "Email?"

    show daisy idle smile
    d "Uhm... maybe they sent it to the wrong address or something.... {w}That happens to me too...{w} sometimes.."
    #sprite here
    show angel happy
    show daisy idle
    "She smiles at me, waiting for something." #" (her sprite changing to a blank smile)
    show daisy idle smile
    d "Oh sorry, I'm Daisy."
    show angel happy big
    s "I'm Samyaza, nice to meet you!"

    show daisy idle #never smile for long!
    "She confidently reaches her hand out... Her voice is a bit too loud for my liking, but that's fine, she seems nice otherwise. Hopefully I can stay out of her way."

    "I shyly reach my hand out to hers, and she grips it with a vigorous smile and level of enthusiasm that is unnatural. She's acting like a used car salesman, each shake felt performed. She seemed as if she was trying to be relaxed, but her smile twitched in exhaustion."

    "She feels a bit more... sympathetic? Earlier today, I was practicing my greeting to Anya in the mirror. Performing my smile in the mirror to make sure there wasn't any underlying strangeness that she could pick up on."
    "...I didn't want to worry Anya with how bad things had been recently."
    show angel desire
    s "Cool.. You have such a cute face. Has anyone ever told you that?"

    show daisy nervous
    d "Thanks.... Uhm, I think so?"
    show angel idle
    show black screen behind daisy:
        alpha 0.25
    show angel idle behind black
    "I shift uncomfortably, I really want to get back into my room and hide in bed. But no matter how much I try to break eye contact, my eyes just keep meeting with hers."
    show black screen behind daisy:
        alpha 0.5
    "I know that she's analyzing my face, each and every single one of my pores- my ugly acne scars, and my long overdue-to-be-tweezed eyebrows..."
    show black screen behind daisy:
        alpha 0.75
    "She's already thinking about how terrible of a roommate I'm going to be, that I'll be dirty and weird, how I probably won't wash the dishes, or can't even socialize with her or her friends properly."
    show black screen behind daisy:
        alpha 1
    show daisy crying
    "I can already imagine it. She invites her new friends over, they're loud as hell in the living room."
    "I work up the courage to leave my room to get a glass of water, something to eat, anything- as soon as I step out they immediately go silent, briefly sneaking glances at me from the corners of their eyes. "
    "The second I slam my door, they go back to laughing, whispering about how weird Samyaza's roommate is."
    "Quiet enough to feign ignorance (“We were talking about someone else!”- yeah right, bitch.) but loud enough that the roommate in question can still hear it even if she tries her absolute hardest to pretend they're not there."
    "They're absolutely hysterical, shrieking like hyenas over how weird Samyaza's roommate is. She'd laugh and agree, and talk about how much she couldn't wait to move out."
    show daisy anxious
    "I can't let that happen this time. I have to prove to her that I'm good at all of these things.{p}That I can function as a human being for once."

    hide black screen
    show angel confused
    s "Did you hear me? What's your major?"
    d "Uh. Oh, sorry. I'm undecided."

    #SAMYAZA (happy/genuine sprite)
    show angel happy big
    s "Oh wow, really? Me too. There's just so much to choose from, I couldn't decide either. What classes are you taking? Hopefully we'll have some together?"
    show daisy idle
    "I scroll briefly through my gallery and hand her my phone, on it a screenshot of my class schedule."
    show angel sad
    s "Aw man, only three. That {i}sucks{/i}."

    d "Well... I'm only taking 4 classes anyways.. "
    show daisy anxious
    "I look down, hoping her energy dies down soon enough. I let out a long, loud, and very drawn out yawn. She's still observing me."
    #sprite here?
    show angel happy
    s "Maybe I can switch into your fourth? I'd love to have a friend in all four classes."
    
    "A friend? I can't believe this girl is already considering us to be friends. I feel bad for her, when she sees who the real me is, she'll hop on over to whatever better, well-adjusted friend group she'll make. I don't know their faces yet, but I'll know them soon enough."

    d "Uh. Yea. That's okay."
    stop music
    scene black screen with fade 

    scene yuri_living_room_night
    play music wav_jonquil
    show daisy idle at scene_left, flip
    show angel happy at scene_right
    with Fade(1,2,1)
    "It feels like Samyaza could go on forever. It's the evening now, but she still has the energy to talk to me about anything and everything, even the things that aren't necessarily...{w=.5} important?"
    "Well, I guess that's not the right word, but some of the things she pointed out were so mundane that I can't help but wonder where she's from that doesn't have these things."

    s "I saw a salamander earlier. It was my first time seeing one in person, it was sick."
    d "...Yea, there's a bunch around here."
    show angel idle
    s "Have you ever had a taco?"
    
    d "Yes."
    show angel happy big
    s "Earlier today, I had one for the first time."

    show daisy anxious
    "..."
    show angel confused
    s "..."
    "What is she waiting for?"
    show angel idle
    s "What kind of foods do you like?"

    d "Uhh..{p}I don't know, pasta I guess?"
        #sprite here
    show angel happy
    s "Before I had it, I swam for the first time too."

    d "Uhm, yea I've heard that there's a lake nearby campus.. I think."
    
    s "Do they have this stuff where you're from?"

    d "{i}{shader=jitter:u__jitter=1.0, 3.0}..What..? {/shader}{/i}{nw}"
    d "{i}..What..? {/i}{fast}Like salamanders, tacos and lakes?"
    show angel big happy
    s "Yea! It's so cool."

    d "...Well yea, I'm from the state.."
    "Does she ever stop asking questions? Please, get bored of me already. But on the other hand, it's a little... {w=0.5}nice. Nice that she cares so much about what I have to say."
    "Starting a new leaf is nice... I think... Entertaining this makes my stomach hurt. But I kind of want her to like me..."
    "She's a better listener than Anya. Even though my answers are curt, she treats each word as if it is better than the last."
    "Maybe my initial reaction was too cruel. I barely know this girl and I am already assuming the worst in her. I might be the worst person in the {b}world{/b}."
    show daisy upset
    "I nip my lip in frustration. I could be extending some kindness to her, I could be trying to make conversation with her- but instead I act like everyone else I know."
    "The teeth on my lip sink in harder."
    "She's so nice, and maybe that's just for now- who knows. I can feel the familiar taste of copper on my tongue. My lip is trembling, but I don't  really care about that right now. She's probably just being nice to trick me, waiting for me to let my guard down and- "
    
    #i wanna semi cry sprite here
    show angel confused
    s "Hey? Are you alright? Your lip is bleeding."
    show daisy surprised
    d "{size=*1.2}Oh shit! {/size}Oh, I'm so sorry, don't worry about me, I'll go clean myself up in the bathroom."
    show daisy at unflip, scene_left_far
    show angel frown at scene_center_offleft 
    "Shuffling in a panic, I am stopped before I can do anything. Samyaza's as strong as she looks, holding onto my wrist-{w=0.2} she locks me in place."
    "Samyaza takes out a folded up hankerchief from her pocket."
    "{b}And presses it on my lip.{/b}"
    camera:
        perspective True
        zpos -700
        xpos -450
        ypos -250
    show angel desire
    "She is really close, her breaths are strong and steady as she applies the right amount of pressure on my lip."
    show daisy sappy
    "My breath stops in my throat."
    "I'm looking away, I'm looking away."
    show angel idle
    "Her lips purse in concentration, my heart skips a bit."
    "No, no, no.. {w=0.5}she's just my roommate.{p}That's {b}all{/b}."
    show angel frown
    s "That doesn't look too bad. But you really have to be careful, alright? "

    show daisy blush
    show angel desire
    "Her breath heats up my face. Her finger is warmer than any others I've felt before. Her presence lights up the dark room, like a bright comforting light shining on me. Contemplative eyes penetrate each and every pore on my face."
    "Playing with my hair, I look away and try to distract myself. Just look away already! Stop staring at my face..!"
    show daisy nervous
    extend " I'm so ashamed, I hate how fiercely she's scanning into me. I want to curl up into a ball, and roll away."

    show angel sad
    s "Alright, you should be fine now. Take care of yourself, Daisy, alright?"


    d "Y-yea, thank you!"


    scene black screen with dissolve
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    "I shuffle off to my room with the cloth. I think...{w=0.3} I'll clean myself up...{w=0.3} sometime tomorrow...{w=0.3} maybe, a little later than I usually do."

    stop music
    window hide dissolve
    pause 1.0

    scene room daisy night with fade
    play music wav_stay_with_me volume 2
    window show dissolve

    "I sat still in my bed, looking up into the ceiling."

    "The exhaustion from the day began to kick in. I rub my sore muscles. If only I had someone to massage me. I sigh at the door, oh well."

    "I need to stop getting ahead of myself! It's been a while since I talked to someone so much, I can feel myself getting excited and thinking ahead."
    "I need to be realistic here, I definitely gave off a terrible first impression."
    "Instead of massaging, I press down hard into my back. Nails dig into my skin. I press {b}harder.{/b}"
    "A little part of me wants to live alone. If I didn't have a roommate, I would stay lying here. Honestly, rotting here sounds better than waking up for classes tomorrow...{w=1}"
    "I press down even harder. I can't think this way. This is the only chance I have to change my life for the better."
    window hide dissolve
    pause 3.0
    window show dissolve
#add sfx
    "I almost did lie in bed forever. Only until my phone alarm went off. I totally forgot about my estrogen shot. Shoot."
    "Today was such a drag, I should've done this hours ago."
    show estrogen_inspect with dissolve
    "As I unbox the syringe and sanitizing wipes, I notice that I left the blood-stained handkerchief on my side table. "
    hide estrogen_inspect with dissolve
    "I use it as a mat to set down some of the injection supplies."
    "The weekly ritual somewhere other than home feels off."
    "I inject {nw}"
    window show
    #hahahaha got it
    show red screen onlayer master with {"master": Dissolve(0.1)}:
        alpha  0.25
    window show
    extend "the needle into the sanitized site."
    "Everything about this place feels off.  No loud TV drowning out the oppressive silence, no loud sighing from my mother, interrupted by her growling to herself about some chore I forgot to do."
    "Even my brain felt...{w=0.5} quiet."
    "I take it out.{nw}"
    hide red screen
    #hide red screen onlayer master with {"master": Dissolve(0.1)} doesnt work :(
    extend " I have to cherish this peace and quiet while I still have it- it's only a matter of time until Samyaza brings over her friends."
    "Instead of my mother's sighs, I'll be terrorized by piercing laughter. "
    "The thought of it made me scream into my pillow. I don't want to go through that feeling again. "
    "My head is flat on the pillow. But I felt my hand guide itself over to the handkerchief."
    "I looked at the small splotch of dried blood against the pristine white fabric. A small golden eye was embroidered on the side. "
    "Slowly, I bring the handkerchief off the bedside drawer,{cps=*.5} {w=.5}then lead it up my leg,{w=.5} then right to my face. {w=.5} {i}I take a whiff.{/i} {w=.5}My free hand makes its way down,{w=.5} from my chest,{w=.5} to my stomach,{w=.5} to my crotch.{w=1}{nw}{/cps}"
    stop music #here?

    "{cps=*.5}My hand reaches for the zipper.{/cps}{nw}"

    window hide dissolve
    pause 1.0
    window show vpunch
    "I throw the handkerchief to the other side of the room."
    "{shader=jitter:u__jitter=1.0, 3.0}What the fuck am I doing?{/shader}{nw}"
    "What the fuck am I doing?{fast}"
    "Something in me, a divine presence, picks me up, and I walk over to pick the handkerchief up."
    "I lay it down next to me again. And drift to sleep."


    #stop music
    stop sound
    window auto

    scene yuri_living_room with  Dissolve(4.0)
    play music wav_blessing
    show angel idle at scene_right with dissolve

    "Samyaza is up bright and early. She eats a strange resinous bread, and gives me a relaxed grin. I rub my eyes while I grab a cup of yogurt."

    s "Good morning, I was worried that you were going to miss class."
    show daisy blush at scene_left with dissolve
    d "Thanks.. But you really didn't have to wait for me."
    show daisy idle
    s "It's no biggie."
    show angel happy
#sprite
    "She leans back on her chair and smiles, stuffing a piece of bread into her mouth. "
    show daisy anxious
    "I can't respond. I shove the yogurt into my mouth, the thick texture and sour taste stay stuck in my throat as I try to avoid her." # Her eyes are so bright, almost like a blinding car headlight.
    show angel idle
    "Once I finish with the yogurt, she quickly takes the bowl and spoon and puts it in the sink, and cleans it immediately."

    d "Uh.. {w=0.5}you really didn't have to do that, I'm ok with washing it."

    #SAMYAZA (happy/genuine) sprite
    show angel happy big
    s "Really, it's no big deal. Just wanted to help."
    "Her smile shines on my face. It kind of hurts, like I'm looking directly at the sun on a hot summer day."

    "We take our bags and begin to walk over to our class."
    play sound footstep_shuffle volume 0.2
    window auto
    scene yuri_classroom_01 with Fade(1,2,1)
    #INT - CLASSROOM - DAY
    #(sfx of people shuffling out/talking)

    "As our class gets out, I get up and yawn."

    show daisy happy  at scene_right_far with dissolve
    d "Man, that was boring."
    $ renpy.music.set_pause(True, channel="music") 

    show angel idle at scene_left with dissolve
    "Samyaza stares at me for a second, like the cogs in her brain are shifting.{p}She.. seems to be genuinely thinking about.. something? It's kind of hard to read her expression right now."
    show daisy anxious
    "I'm going to go with the safest bet that I said something that annoyed her, and she's just trying to be nice because she knows she has to deal with me for the next year."
    show daisy nervous
    "My face heats up. I quickly sit back down, and began to pack my stuff. I need to run to my next class and act like she didn't just ignore me."

    d "...Or maybe it was interesting.."

    "It doesn't matter how much I try to steer my mind away from her lack of response, my hands are clammy and slippery. {w=.5}A couple loose pencils ricochet against my fingers and fall straight to the ground as I quickly try to pack. I freeze."

    d "Oh...{w=.5} wow... "

    "The familiar pang of anxiety and shame wells up inside of me, my face must be bright as a tomato right now.."
    d "Guess I just can't do {i}anything{/i} today, huh!"
#sprite
    show angel happy
    "Samyaza smirks at me, creasing her eyes and showing her teeth."
    s "Nah, it wasn't boring."
    show angel idle at scene_center with moveinright
    "She gets up, and helps me put the stuff into my bag."
    $ renpy.music.set_pause(False, channel="music") 

    show angel happy big
    s "It was SUPER boring."
    show daisy anxious
    d "You really didn't ha-{w=1}{nw}"
    show angel desire
    s "{b}I want to.{/b}"
    show daisy sappy
    "My eyes widen as if they are going to burst out of my skull."

    show daisy blush
    s "That's what roomies are for..{w=0.5} Right?"
    #sprite
    #show angel happy
    #"She nonchalantly grins." #cut this line?
    show daisy at unflip,  scene_right_far
    show angel happy at flip, scene_center_offright with moveinright
    camera:
        perspective True
        linear 1.0 zpos -700 xpos 450 ypos -250
    show daisy blush
    "As she wraps her arms around me, into a hug, my face moves on its own, contorting into a matching smile as my hands lay flat by my side."
    



#MONTAGE
    scene black screen with Dissolve(0.5)
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0

    scene yuri_classroom_01 
    show daisy anxious at unflip, scene_front_center_offright:
        ypos 1500
    show angel idle at scene_front_center_offleft, flip:
        ypos 1500
    camera:
        perspective True
        zpos -200
        xpos 0
        ypos 000
    show black screen
    hide black screen with Dissolve(0.5)
    play music wav_roadtrip
    play sound crowd_noise volume 0.1
    "Samyaza slyly hands me over notes for the upcoming lecture. She must be a good student if she's already this far ahead. Way better than me."

    "Sheepishly, I grab the notes and begin to copy them down."
    show daisy surprised
    "I notice a cute little drawing on the corner. Poorly drawn versions of me and her diligently studying."
    show daisy happy
    "I rip it out to add to my scrapbook."
   

    scene yuri_park_01 
    show daisy idle at scene_right_far
    show anya happy at scene_center, flip
    
    play sound2 bird_chirping volume 0.1

    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    show mob_dress at scene_center_offleft
    show mob_walk at scene_left_far
    show black screen
    hide black screen with Dissolve(0.5)

    "I try to hang out with Anya and her friends. They howl with laughter at Anya's joke."

    "I lounge a bit further away from them. {p=1}{nw}"
    show anya idle at scene_center_offright,unflip with {'master': moveinright}

    extend "Anya sympathetically looks my way and scoots closer to me."
    show anya at flip
    "She tries to include me in the conversation, {nw}"
    show daisy idle smile
    extend "but all I can do is weakly laugh."
    show daisy anxious 
    "I tense a bit, staring at the leaves of the same tree I did all those weeks ago when I first transferred."
    show anya happy at unflip
    "In the middle of her conversation, I hear Anya spontaneously jump up, and grab something from that tree."
    show anya idle
    "She hands me a little flower. I gingerly reach out to it."
    show anya idle
    show daisy surprised
    d "Is this for.. My scrapbook?"

        #ANYA (smile sprite)
    show anya happy
    a "Duhh!"
    show daisy blush
    d "You remembered?"
    show daisy happy
    "Anya noogies me."
    show anya idle
    a "Who do you think I am?"

    

    stop sound
    stop sound2

    scene black screen with fade
    camera:
        perspective True
        zpos -500
        xpos 350
        ypos -200
    scene yuri_living_room with dissolve
    
    #INT- APARTMENT LIVING ROOM -  DAY

    show daisy idle at flip, scene_right_far
    "I scroll through my phone as I eat my yogurt bowl, {nw}"
    show angel idle at scene_center_offright, flip with {'master': dissolve}
    extend "Samyaza appears from behind, snatches my phone and holds it above me as {nw}"
    show daisy happy at unflip
    extend "I giggle at her to give it back. She gives in and pats my head."
    scene black screen with Dissolve(0.5)
    camera:
        perspective True

        zpos 0
        xpos 0
        ypos 0
    
    scene yuri_park_01
    show daisy anxious at unflip, scene_right_far
    show angel idle at flip,scene_center_offright
    show black screen
    hide black screen with Dissolve(0.1)
    pause 1.0
    play sound bird_chirping volume 0.1

    camera:
        perspective True

        zpos 0
        xpos 0
        ypos 0
        ease 2.0 zpos -600 xpos 450 ypos -250

    pause 2.0
    "Samyaza and I sit down and eat sandwiches she made."
    show black alpha behind daisy
    show angel behind black
    extend " I feel like a sore thumb."
    show daisy nervous
    "Could I really live a normal college life? I stare at the sandwich. I shouldn't eat this, I don't belong here."
#sprite
    $ renpy.music.set_pause(True, channel="music") 

    show angel happy
    "Samyaza brings the sandwich to my mouth, but it just falls against my cheek."

    stop sound

    show angel sad
    "I'm such an alien, and aliens don't eat human food. "
    show daisy upset
    "The physical weight of my body takes up the space, suffocating everyone else enjoying their day outside."
    hide black
    show angel desire
    "Samyaza opens my mouth{nw} "
    show daisy surprised
    extend "like she's opening a trash chute and puts the sandwich in it."
    
    play sound bird_chirping volume 0.1

    $ renpy.music.set_pause(False, channel="music") 

    show daisy happy at unflip, scene_right_far
    "I start to cackle."

    stop sound
    scene room daisy night with fade
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    show angel idle at scene_right
    "Samyaza helps string up some fairy lights, she's tall enough to do so. I sit on my bed and watch her. The fabric of her vest stretches across her back, it traces the lines of her muscles with every movement. "

    show daisy anxious at scene_left with dissolve
    d "I'm really sorry for being unable to help..."
#sprite
    show angel desire
    s "No worries, sit your pretty little self down. Ladies shouldn't do this work."
    show daisy blush
    "I bite my nails and enjoy the view."
    scene room daisy with dissolve
    #INT- DAISY'S ROOM - DAY
    show scrapbook_inspect with dissolve
    "I cut out pieces of Samyaza's handkerchief into little stars and hearts."
    "Making absolutely sure I get the parts with my bloodstains"

    "With my pink tape, I paste it onto the scrapbook."

    scene yuri_living_room_night with Fade(1.0,1.0,1.0)
    play music wav_intuition
    show daisy anxious at scene_left_far
    "I'm typing away at my computer with urgency. The first big project of the semester is coming up. My brain feels like it's filled with fog as the document just can't seem to fill up."
    "In 30 minutes, I have to meet up with my group members for this class. I want to make sure the presentation is done by then. I'm hoping I can just make the presentation, and write the content."
    "...I'd rather {i}die{/i} than present and be under the microscope of the entire class."

    "I can't afford to do poorly, my groupmates already think I'm irritating. They're always asking if I have any questions after our meetings."
    "I can't ever look them in the eye when I do have questions, though. I feel the awkward glances they give each other as I try to talk."
    show black screen behind daisy with dissolve:
        alpha 0.8
    "If I do poorly, I'll disappoint Anya. I already hear the scolding I'd receive if I failed."
    "After that, it'll only be a matter of time until she realizes that everyone was right, and that she ought to cut me off instead of using me like some charity case."
    "She'll be sick of me even more than before."
    #sfx
    
    "My stomach rumbles, but I continue to furiously type. I'm never able to get work done, so I ignore it. I catch a whiff of myself too... I guess the shower will wait."
    show angel idle at scene_right behind black with dissolve
    "Samyaza comes into the apartment, her last class today ends rather late."

    s "Daisy, how was your day?"

    "I don't deserve to talk to her until I finish. I focus in on my laptop screen."
    show angel confused
    s "Daisy?"
    show daisy angry
    d "Sorry, I'm busy."

    s "You wanna chat about your day while you work on your thing?"

    d "No."

    #SAMYAZA (frown sprite)
    show angel sad
    s "Aw, you sure?"

    "I stop typing."
    show daisy upset at flip, scene_left_far
    show angel at scene_center_offleft with moveinleft
    camera:
        perspective True
        ease 1.0 zpos -600 xpos -450  ypos -250
    "Samyaza sits down in front of me."
    
     
    s "Come on, tell me about your day."
    hide black with dissolve
#sprite
    show angel happy
    "She softly grins, leans forward and holds her face in anticipation."
    show daisy anxious
    "I take my hands off of the keyboard, and rub my fingers together. I am completely blank, how {i}was{/i} my day?"
    show black alpha behind daisy
    show angel behind black
    "It's like I'm watching someone else go through my days. What's the right way to answer her, I want to give her an answer that will make her happy.."
    hide black
    s "Sooo? "

    d "Uh.. sorry! Uhm, it was okay... I guess."
#sprite
    show angel confused
    "She tilts her head, and gets a little closer to me."

    s "{cps=*.25}Anddd...?{/cps}"

    d "I...{p=1} I really need to get back to work."
    show angel frown
    "Samyaza slowly closes my laptop until it's halfway open."
    show daisy surprised
    d "Hey!"

    s "I'll open it up again... once you tell me about your day!"

    d "I mean, I studied then I scrapbooked."
#sprite
    show angel happy
    s "...Scrapbooked? Do tell."
    show daisy anxious
    "I sink into my feet, and rub my hands with more intensity, I want  to feel any sort of friction. In the back of my mind, the project feels like an unbearable itch that I can't scratch."

    d "{cps=*2}The other day I was hanging out with my friend- Anya, and she knows I like scrapbooking... so uhm she drew a little cat on a receipt. We went to a coffee shop.{/cps}"
    
    s "And? How was the coffee?"

    d "It was okay. Nothing to write home about."
#sprite
    s "What did you get?"
    
    d "Just an iced vanilla latte. I  really wanted to try this place cause I know they have specialty beans."
    d "Back at home we don't have anything cool like this. Honestly, there's nothing cool at home. The interior was really cute too, and also the..."
    show angel confused
    s "The?"

    show daisy angry
    d "Samyaza. I really need to do this assignment. It's due {b}soon.{/b}"
    show angel sad
    s "Make sure to talk to me after, okay? It's so lonely here."

    "I hesitate to open up my laptop."

    d "Yeah..{w=0.5} it really can be."
    
    "I open up my laptop. I don't know how but thirty minutes have passed."
    "I checked my phone, for some reason the ringer didn't go off at all."
    "My classmates spammed me with multiple inquisitive texts. "
    show daisy surprised
    d "Holy shit."
    show angel confused
    s "What?"
    show daisy upset
    d "Oh man, I totally fucked up."

    show angel at scene_center_offleft
    "Samyaza leans further in."
    "Just go away!"
    "I press into my skin, holding myself back from swatting her away."
    show angel frown
    "Samyaza gets up, her face close to mine."

    s "What happened?? Tell me??"
    show daisy crying
    "I scream and pull my hair. I so desperately want to curse her out but I only pathetically groan. I knew it. I knew it, I knew it, I knew it. This is what she was trying to do all along."
    show angel confused
    "Samyaza gets up in my face, her hand brushes against mine and I push her away."

    show daisy angry
    d "Ugh... it's because of you! They {b}hate{/b} me because of you!"

    s "Huh- What do you mean?! I don't understand! I can't help you if I don't know what's going on!!"

    show daisy at offscreenleft with moveinright
    "I turn my laptop off and run into my room. I shut the door behind me. "

    play sound door_slam_multiple
    stop music
    hide daisy

    #lingerrr
    show angel sad
    pause 1.0
    scene black screen with Dissolve(0.5)
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    scene room daisy night with Dissolve(0.5)
    #[BANG SFX 3X]
    play music wav_wasteland
    "The slamming is deafening. I curl up into bed and cover my ears with the pillow."

    s "Daisy! Open up, please!"

    "{b}Go away!{/b} My entire face hurts with the intensity of how hard I'm squeezing my eyes shut."

    d "You're only making it worse!!!"


    "Samyaza's voice quivers more and more. The knocking increases in intensity. "

    #[DOOR KNOB OPEN BUT ITS LOCKED SFX]
    play sound door_handle_jiggle


    "My pillow is becoming damp with my tears."

    "Why am I lashing out? She's not going to like me if I keep this up."

    "I guess I'm saving myself. At least I'll know {i}exactly{/i} why she hates me. I'm ripping the bandaid clean off."
    stop music
    scene black screen with dissolve 
    play music wav_by_your_side
    #INT - APARTMENT - NIGHT

#[BLACK SCREEN + SOMBER MUSIC]

    "My hand is stuck on the apartment doorknob. Something deep inside my soul is working against me. Do I {i}have{/i} to open the door? I don't know if I can face Samyaza. "

    "I really am the worst of the worst. Ignoring Samyaza for the past day? I don't think I deserved to talk to her after yesterday."

    "But, as horrible as it sounds, I like that I can finally say she really cares about me. She was miserable the entire day today. Cartoonishly so- like she learned how to look sad through sitting down and watching Saturday morning cartoons."
    "She looked like an abandoned puppy."

    "Standing still like a statue, not knowing whether to open the door and accept the punishment I deserve, or run away and prolong it. Samyaza deserves better than me."

    "Regardless, I opened the door, not because I was brave- but because I was a coward who wanted the comfort of my own bed after a terribly long day."
    stop music
#[MUSIC STOPS]
#[DOOR OPENING SFX]
    #INT. APARTMENT LIVING ROOM - WHITE SCREEN
    scene yuri_living_room
    show white screen:
        alpha 0.8
    show black screen
    hide black screen with dissolve
    play sound door_open volume 0.5

    "A searingly bright white light is spilling from the bathroom door, the rest of the apartment is barely legible as the blinding light swallows it up."
    "My eyes {b}burn.{/b}"
    "It takes me seconds to process the gurgling that echoes through the house."

    show daisy surprised behind white at scene_right with dissolve
    d "Samyaza??!"

    "No response. I drop my bag and run to the bathroom, preemptively covering my eyes."
    scene yuri_bathroom_01
    show red screen:
        alpha 0.8
    show white screen
    hide white screen with dissolve
    #[SKIN-ISH RED LIKE WHEN YOU CLOSE YOUR EYES WHEN ITS REALLY BRIGHT OUT]
    play music wav_dissociation
    s "Glglg... daisylglgl.." #shader pass?


    d "Samyaza, what's going on????"


    "My heart beats faster and faster as my eyelids tremble in fear."
    scene white screen
    show red screen:
        alpha 0.8
    "My body glues them shut. And even if I want to, I'm too afraid to open my eyes."
    "It's sweltering here and it's hard to breathe."
    "My entire body clenches up."

    "Samyaza grabs my wrist, her gurgling continues. She guides me to some sort of tubed object."
    "Her hand sears my skin."
    "Her fingers, like a branding iron."
    "I bite my lip to hold in my whimpers of pain."
    "The pain helps ground me-{p=1.0} it helps me realize that whatever is happening is real. "

    "She opens the cap to the object, and guides my hand to draw a circle."


    d "Mmph...!"

    "My nails are digging into my hand, as my other hand is drawing a series of shapes I can't figure out."

    #[MUSIC STOPS]
    #[FADE TO BLACK]
    scene black screen with dissolve
    "The light instantly goes out, Samyaza coughs and wheezes, like something big is coming out of her.."

    scene yuri_bathroom_01
    show daisy anxious at scene_left, flip
    show angel pain open nowing at scene_right


    "I tentatively open my eyes- her eyes are red, with a less vibrant light seeping out of her orifices. Her veins are pulsating and golden."

    camera:
        perspective True
        linear 1.0 zpos -500 xpos 300  ypos -175
    show daisy nervous at scene_center with moveinleft
    "I gently kneel down by her side, rubbing her back with my other hand. The other one stings too much, I left it limp beside me. My hand blisters as if it is stuck into a nuclear reactor."

    camera:
        zpos -500 xpos 300 ypos -175

    show sigil_air with {'master':dissolve}:
        zpos -500 xpos 300 ypos -175
    "Timidly, my head makes its way to the mirror.. Some sort of... sigil-like drawing. A large circle with strange lettering was drawn with lipstick."
    hide sigil_air with dissolve
    "Samyaza weakly clenches onto my hand, she gently pets my burn mark. Still feeling the residual heat, I bite my lip to hold in the pain."
    show angel pain closed nowing
    s "...We should do something about this..."
    stop music fadeout 2
    show daisy nervous
    "I sigh, exhaustion catches up to me.{nw} "
    show daisy blush at scene_center_offright with moveinleft
    #show angel sad
    show angel pain open nowing
    extend "Maybe that sigil has some sort of effect on me too, because I sheepishly lay my head on her shoulder."

    "I'm so selfish, but I don't care.{w=1} She lights a fire within me.{w=.5} I want the heat to melt us into each other at this moment."

#INT. APARTMENT LIVING ROOM - NIGHT
    scene black screen with Dissolve(2)
    play music wav_midnight
    camera:
        perspective True
        ease 2 zpos -600 xpos -450  ypos -250
    scene yuri_living_room_night 
    show daisy anxious at scene_center_offleft
    show angel sad at scene_left_far , flip
    show black screen
    hide black screen with Dissolve(2)
    "Samyaza sits, she's hunched over, still catching her breath.{p=1.0}Her exhaustion is palpable."

    "I walk over, handing her a warm cup of tea. I'm so useless, I can never really help people. I want to do more for her, but I'm still frazzled from whatever the hell just happened. I dig my nails into my legs."


    s "Hey, Daisy..{w=1} Don't worry about it."

    d "...."

    s "Really, it's not your fault."

    #DAISY (sad gay puppy eye etc sprite)
    show daisy anxious
    d "Well...{w=1} maybe...{w=1} if I didn't ignore you all day...{w=1} this wouldn't have happened.."

    s "No, it's not that...{w=1} It's fine. "

    "I can't bear to look at her."
    camera:
        perspective True
        ease 2.0 zpos 0 xpos 0  ypos 0
    show daisy at scene_center,unflip with MoveTransition(2.0, leave=offscreenleft, leave_time_warp=_warper.easeout) #tbd define this
    "I uncomfortably scooch away. I still feel the heat emitting from her, but I'm far enough to be edged by it."
    show angel at flip
    s "I should tell you about something."
    show daisy nervous at unflip
    "My head is hung down. I peep in her direction."

    s "I'm not... really what I say I am. {nw}"
    #[happy/genuine sprite]
    show angel happy
    extend "Hah. that must be obvious by now."


    "My expression is unchanged. Trust me Samyaza,{i} whatever it is {/i}, it can't be any worse than me."

    show angel sad
    s "I'm not from here, like...{w=1.0} from Earth. "
    $ renpy.music.set_pause(True, channel="music") 

    show daisy surprised
    "Huh?"

    d "..An Alien..?"
#sprite here
    show angel happy
    "Samyaza weakly laughs."

    s "You're so cute.. No, like...{w=1.0} well, why don't I show you."
    show angel at unflip
    $ renpy.music.set_pause(False, channel="music") 

    "After that, she takes off her vest. Two painful bumps, almost like large hard cysts infested themselves on her back. Her sweat glistens under the light of the cheap ikea lamp."

    s "Feel them."
    show daisy at scene_center_offleft with moveinleft
    show white screen with dissolve:
        alpha 0.25
    show daisy sappy
    "I slowly bring my hand over, it's softer than I expected. But extremely hot, a bright light peeks through one orifice."
    "My hand stings, but I won't dare pull away, the thought of it weighs down my heart."

    show daisy surprised
    d "This looks really painful..."

    s "It's not that bad. What must be really painful is your wrist. I'm sorry about that."
    show angel idle
    d "No, it's okay...{w=1} as long as you're alright."

    show daisy nervous with None
    show angel behind daisy
    show white behind daisy
    show black behind daisy:
        alpha 0.8
    with dissolve
        
    "I caress the cysts, hoping it'd soothe her pain. After how much misery I've caused her, it's the least I could do."

    "What even is she? What's even fucking happening? I don't want to bother her anymore than I already had either, so I suck it up."
    show black behind daisy with dissolve:
        alpha 0.95
    "My body feels compelled to get on the ground, and beg for her forgiveness."
    "Humiliating myself with tears, and repeating myself so much that my mouth shrivels up."
    "The only thing I can do is withstand the pain of her searing skin as I pat her wounds."
    show daisy behind white
    hide black
    with dissolve
    
    show angel sad
    s "I'm scared to tell you the truth..{w=1} But just now, I really want to go back home. I'm not reacting well to this new body.."

    show daisy surprised
    "I tilt my head."
    show angel sad
    s "Sorry. I don't mean to worry you."

    d "No..{w=.5} I'm just..{w=.5} Confused."

    #SAMYAZA (frown sprite)
    show angel frown
    s "Don't worry about it..."

    "I gather up all my strength, I spit out the words, stuck like phlegm, in my throat."

    show daisy anxious
    "No, Samyaza.. I want to help you, please tell me what it is."
    #sprite time
    #show angel frown
    show angel at flip
    "Her face twists into a mix of satisfaction, and concern."

    stop music fadeout 1.0
    s "Can I tell you a story?"

    "I bob my head."

    hide white
    scene black screen with dissolve
    show angel frown at scene_center_offleft, flip
    show daisy anxious at scene_center_offright
    with dissolve
    play music wav_long_ago
    
    s "Let's say heaven is real.{nw}"
    show yuri_angel_painting behind daisy, angel with {'master': Dissolve(3)}
    extend"{p=1}{b}{i}Would that drive you mad?{/b}{/i}"

    show daisy happy
    "That's a question..!"
    show daisy idle
    show angel sad
    s "Well..?"
    show daisy anxious
    d "I don't know... I never had the best relationship with that stuff. I guess it depends?"
    show angel frown
    s "{cps=*.5}{b}Would you want to die?{/b}{/cps}"
    
    show daisy surprised
    "I raise my eyebrows at her."
    show angel confused
    d "What??"

    show daisy nervous
    "She's so intense and sweltering. I shrink into myself."

    d "...Sorry..."
    show daisy surprised
    show angel frown at scene_center with moveinleft
    camera:
        perspective True
        easein 0.5 zpos -400 xpos 150 ypos -150
    "Samyaza grabs my burnt wrist. It hurts less now after she bandaged it."

    s "Don't apologize."

    "She doesn't blink." 

    d "I don't know...{w=1.0} I mean, I guess I've thought about dying before..."
    show daisy anxious
    "I grit my teeth through the lie, hoping beyond hope that she wouldn't dig further."
    show angel sad
    s "Daisy..."
    show daisy idle smile
    d "No! Don't worry! That's all in the past...{w=1.0} things have been fun lately."

    show black alpha as ba behind daisy with dissolve
    show angel behind ba
    show daisy anxious at flip
    "I look away, hoping she doesn't read me for what I am."
    "I mean, who knows what she can do."
    "I should be scared, shouldn't I?"
    "I'm stepping too close to a flame that I know nothing about."
    pause 1.0
    show daisy blush
    hide ba with dissolve
    "But I can't resist its warmth."

    show daisy at unflip
    show angel frown
    s "I will always, always be here for you. You are my first real human friend. You don't know how much you mean to me."

    show daisy idle
    "Her grip is tight. I hold in my confusion at her passion."

    d "Do you want to go back to the story?"


    s "Oh.{p=1}Right."

    show angel sad
    # camera:
    #     perspective True
    #     easein 1 zpos 0 xpos 0 ypos 0
    # pause 1
    s "Well, let's say there {i}is{/i} a heaven. And amongst its denizens, guardian angels exist. Their sole purpose is to protect humans with their brethren."

    s "Now...{w=0.5} let's say that one particular guardian angel failed. Her love for humans is far too strong for her to handle."

    s "The angels send her away. She now lives her days with a maddening silence. An emptiness that's impossible to fill."

    hide black with dissolve
    #(FADE BACK TO INT - LIVING ROOM)

    show daisy idle
    d "What will the angel do now?"

    s "After a while..{w=2} {nw}"
    #sprite
    show angel frown
    extend "After a while of living aimlessly, with her days blending in together, she remembers something she heard a long time ago; about a human who tried to reach the angel's level...{w=1.0} Maybe, this could help her return home.."

    show daisy anxious
    d "So...{w=1} you'll leave?"

    #SAMYAZA (sighs)
    show angel sad
    s "I'm unsure, I'll have to see. "
    show daisy nervous
    d "I don't know if I like this story."

    show daisy crying at flip
    "I tear up, facing away."
    show angel confused
    s "You don't want to help me?"
    #show angel pain
    show daisy surprised at unflip
    
    d "{b}{shader=jitter:u__jitter=1.0, 3.0}No, that's not what I meant!{/b}{/shader}{nw}"
    show angel confused
    d "{b}No, that's not what I meant!{/b}{nw}{fast}"
    show angel sad
    show daisy anxious
    s "I need a human to help me with this ritual. The only person I want to help me is you."

    show angel desire #at scene_center_offleft with moveinright
    "She beams at me, but I feel like I'm sinking.{p=1.0}Some stupid girl like me would probably just mess it up. "

    s "You're the most beautiful human I've ever met.{p=1.0}You have the brains to do this."
    show daisy blush
    "I blush. She's probably just trying to fool me. I won't fail for these tricks. Something as ethereal as her could never love me."

    d "...{w=1}I'll help."

    stop music
    scene black screen with dissolve
    play music wav_reasoning
    camera:
        xpos 0 ypos 0 zpos 0
    scene yuri_classroom_01 with dissolve
    show angel idle at scene_left,unflip with dissolve
    "Samyaza drew a bunch of strange looking sigils and letters on the board. She points to each of them."
    s "Air, Earth, Water and Fire."
    s "For Air, we use an incense burner and breathing techniques to solidify our bond. With this ritual, I can go back to Heaven."

    "Go back to Heaven... My chest felt tight."

    show daisy upset at scene_right, unflip with dissolve
    d "{size=*.5} Is this all I am to you?{/size}"

    show angel confused at flip
    s "What did you say?"

    show daisy anxious
    d "...Nothing, sorry. Continue."

    show angel frown at unflip
    s "Next, is Earth, which requires a burial."

    "I figure I should ask about the details for that, but before I can open my mouth,{nw}"
    show angel sad at scene_center,flip with {'master': moveinright}
    extend " Samyaza walks over to me, holding my injured hand."

    
    s "Don't worry, I will make sure you are safe."
    show daisy surprised
    "I raise my eyebrow. Have I said anything?"
    show angel frown at scene_left, unflip with moveinleft
    s "Anyways, the next ritual is water. It involves a cleansing bath with holy elixirs."

    show daisy blush
    d "A bath with just you?"
    show angel desire at flip
    s "No, you'll be in there too anyway-"

    show daisy nervous
    d "No, no, I can't possibly do that."
    show angel frown
    s "If we mess up on anything there will be {b}serious{/b} consequences. We have to follow everything precisely. You {i}have{/i} to do it if you want to help me."

    "I fidget with my fingers, a familiar anxiety beginning to build up deep within my core.."

    show daisy upset
    d "Okay, fine."
    show daisy at flip
    "I turn my head and sulk, trying to see if she'll look at me with concern.{p=1}She's so hard to read, focused like this."
    
    show angel at unflip
    s "Now, this last one is the most important. A fire ritual."
    show daisy surprised at unflip
    "I open my mouth to ask what it entails, {nw}"
    show daisy anxious
    extend "but I decided to stay quiet."

    show angel idle at flip
    s "Well? Any questions?"

    d "..."
    show angel frown
    s "It's really important that you help me out with this, okay?{p=1.0}{nw}"
    show angel sad
    extend "...It means a lot to me that you do."
    show daisy at flip
    "I don't peep, but I turn away."

    show angel sad at scene_center,flip with {'master': moveinright}

    s "Please? You'd be the best fit for this. I don't like it when you don't talk."
    show daisy idle
    "I feign a calculating look." #cut for ...?

    #    SAMYAZA (sprite up close)
    show angel confused
    s "Stop ignoring me.. What did I do?"

    d "I'm thinking about it."

    show angel sad
    s "..."
    d "I said, I'm thinking about it.."


    "Samyaza holds my burnt wrist once again, softly petting it. A small smile began to escape my lips." #gets closer, she 
    show daisy blush at unflip
    d "I think.. I'll help you out."
    #sprite here

    camera:
        ease 0.5 xpos 300 ypos -150 zpos -400
    show angel happy big at scene_center_offright with moveinright
    show daisy
    "Samyaza grinned and pulled me into a tight hug. {nw}"
    show daisy sappy
    extend "She smells and feels like a warm and fuzzy lightbulb."

    "An intense nagging tugs at my heart, but it doesn't matter.{p=1}I can't afford having Samyaza hate me."
    stop music fadeout 1.0

    "Samyaza needs me. I need her."
    scene black screen with dissolve
    camera:
        xpos 0 ypos -0 zpos -0
    #INT. OCCULT STORE - DAY
    scene yuri_occult
    show daisy idle at scene_left
    show angel idle at scene_right
    show black screen
    hide black screen with dissolve
    play music wav_roadtrip
    "The scent of incense overwhelms. We both carry baskets filled with incense, candles, and books."

    "Samyaza and I browse the aisles, we look for the perfect incense burner. She's so particular about it, but I don't really notice any difference the same to me."

    "It is a little odd, though. I've always thought that new-age spirituality places like this are considered...{w=.5} blasphemous? In religion."
    show daisy anxious
    d "How'd you hear about this store?"

    show angel confused
    s "Oh! Um...{p=1}You know! Just got it recommended to me on the apps!"

    d "Hm."
    show daisy idle
    "I guess it isn't that important."
    show angel idle at flip
    "Samyaza looks through the incense burners, deeply engrossed. It's all Greek to me, so my attention ends up being caught by a jar of crystals."
    "I slowly sink my hand into it; there were both smooth and ragged crystals inside, all pleasantly cool to the touch."
    "Before my mind fully fogs up, and before I could descend deeper into the jar, {nw}"
    show angel desire at scene_center, unflip with {"master": moveinright}
    extend "I feel Samyaza {nw}" 
    show daisy surprised at flip
    extend "grab my wrist sharply, taking me away from the crystals. {nw}"
    #sprite here
    show angel happy big
    extend " She looks at me and smiles."


    d "Oh, sorry."

    s "No worries."
    window hide
    pause 1.0
    window auto
    "Her smile lasted a bit too long. I shook my wrist, making sure she could see it."
    show angel idle
    #show daisy at scene_center, flip with moveinright
    "I gaze at burners with her. I find a gold one, with a beautiful little cross on the top."
    show daisy surprised
    d "Could this one work?"

    "I grab it and hold it out to her."
    #sprite here
    show angel happy
    s "It's perfect. "
    show angel desire
    camera:
        perspective True
        linear 3.0 zpos -400 xpos -250 ypos -150
    "She places her hands over mine. I want to look away but her eyes are so intense. {nw}"
    show daisy blush
    extend "My heart begins to beat quickly."

    show angel desire
    s "This is why I need you, Daisy."
    show daisy surprised
    "I sit there staring at her wide eyed, I expect her to end that comment with a chuckle to keep it casual. But her intensity remains."

    show daisy anxious 
    d "Really? Even if I have sweaty hands?"
    #sprite
    show angel happy big
    "She laughs and nods, taking the burner away from my hands. She also grabs my basket of things."


    s "Then, a pretty girl like you shouldn't need to carry these things, right?"


    show daisy sappy
    d "{cps=*.25}That isn't true...{/cps}"


    show angel confused
    s "Do you want to carry it?"

    show daisy blush
    d "No, no no. Everything you're saying... I'm sure there's someone out there...{nw}{w=1}"
    show daisy anxious
    extend " better suited for this."
    show angel idle
    stop music

    s "Well God brought us together, didn't He?"

    "I shift to the side a bit."
    
    d "Uhm. I guess. You're such a romantic."

    show angel confused
    s "Not really. I think He wanted me to redeem myself. I think He saw something within you, and brought us together."
    s "This is all His plan."

     
    d "Huh. He must've made a mistake then."
    show angel scary
    #sprite here
    s "He doesn't make mistakes."
    show angel frown
    show daisy at scene_left_far, unflip with moveinright
    "I look to the side and walk a bit further from her. I pick at my fingers as she keeps browsing. "
    show angel at flip
    "She fervently analyzes the chalices. There is a large variety of them, some gold, some silver, some round, and some square."

    window hide
    pause 2
    window auto
    #[PHONE RING SFX]

    play sound phone_ring volume 0.5 
    show phone_inspect at scene_center with dissolve:
        zpos -400 xpos -250 ypos -150

    "My phone rings, cutting through the silence."
    show angel at unflip
    "Samyaza quickly turns, she patiently waits for me to answer."

    hide phone_inspect with dissolve
    #[fucky camera offset stuff is here]
    show daisy nervous
    d "Hello? Anya?"

    "I shift my focus to my feet. Occasionally glancing to the corner. Samyaza is watching me like a hawk. "
    show angel at scene_center with moveinright
    #[SAMYAZA'S SPRITE GETS CLOSER. NERVOUS DAISY SPRITE.]

    d "{cps=*2}Uhm, yea, I'm able to make it tonight. Yea. That sounds good. Yea, yea I'll see you.{w=.1}{/cps} Bye."
    #sprite
    show angel happy
    "Samyaza doesn't have to say anything, she gives me her typical smile."
    show daisy at flip
    d "Sorry, I forgot to tell you, Anya has a party tonight..{w=1} I guess we'll have to start the stuff for the ritual tomorrow."
    play music wav_why_did_you_leave
    #SAMYAZA (strained smile) sprite
    show angel sad
    s "That's okay... Just make sure you're free tomorrow."
    show daisy idle smile
    d "It's okay. I finished all my homework yesterday, so there shouldn't be any distractions like before. I'm free."
    show angel idle
    "We rigidly smile at each other, my eyes crinkling as I struggle to sell it."
    
    scene black screen with dissolve
    "As Samyaza checks out, her free hand grazes mine. My hand moves like something else possesses my body, and my finger curls into hers."
    

    "She hands me the receipt paper."

    d "Oh.. it's for me?"

    s "I thought it had a cute logo. And you can put it in your scrapbook thing."

    "My free hand covers my face with the receipt. "
    stop music fadeout 2
    window hide
    pause 1.0
    window auto
    camera:
        perspective False
        zpos 0 xpos 0 ypos 0
    scene anya_house with Dissolve(4.0)
    show mob_dress at scene_center_offleft
    show mob_walk at scene_left, flip:
        xoffset -100
    show mob_dress as mob_dress2 at scene_left_far:
        xoffset -100
    with dissolve
    play music wav_whispers
    show daisy anxious at scene_right_far with Dissolve(3)
    #crowd sfx
    #Ambient music plays.
    "Joyful chatter fills the house, the scent of oversprayed vanilla perfume and cigarette smoke blows sharply into my nose."
    "I linger uncomfortably by the table with the drinks."
    
    "Everytime I felt like the partygoers' eyes wandered onto me, I would take another swig of my drink."
    "...{w=1.0}I hate this music."
    show anya happy at scene_center, flip with dissolve

    "I spot Anya, she walks around like she's a waitress, doing her rounds, changing up her personality to each guest.{p=1.0} Like she's known them for years."
    "My face hides behind the cup I was holding."
    #sprite
    show anya idle at scene_center_offright, unflip with moveinleft
    "Anya notices me, and makes her way over here."
    show daisy upset
    "I'm just another obligation I guess."
    show daisy angry
    "Look how nice Anya is for inviting the mood-killing freak."

    show daisy idle
    show anya happy
    a "Hey! I'm so glad you came!"
    "Nodding at her, I drink a bit more. "

    d "Thanks. "
    show anya upset
    a "Hey, seriously. Chin up, I'm happy to see you."

    show daisy happy
    d "Uhh... Yeah! I'm glad to see you too."
    show daisy anxious
    "I feel her looking down at the red solo cup in my hands for just a split second, with an expression that I can't make out. "
#sprite
    show anya happy
    a "Don't drink too much, kay?"
    show anya idle
    "Lying to her, I nod. {p=1}My nerves feel like they are begging for more liquor. "

    show daisy idle smile
    d "Hah, when have you ever seen me get crazy anyways?"

    #sprite
    show anya happy
    a "You know what? Yeah, you definitely need to loosen up a bit, you know!"

    show daisy happy
    d "Here's to me loosening up!"
    show black screen with dissolve
    show anya idle
    "We take a shot together. Liquid trails down my mouth, and as I reopen my eyes, {nw}"
    show anya_house behind daisy at small_wobble
    hide black screen with {'master': dissolve}
    extend "everything around me begins to move."
    show anya happy
    #ANYA (smile sprite)
    a "Heh! You're so funny.{p=1}{nw}"
    show anya idle
    extend "Oh, wait."

    show daisy anxious
    d "...hm?"


    a "I have a junior showcase for one of my clubs tomorrow, I haven't told the others...{w=2} {nw}"
    show anya happy
    extend "I'm kind of shy, haha. But, I'd {i}really{/i} like for you to come."
    show anya idle
    #[DAISY CONFUSED SPRITE]
    show daisy anxious
    pause 1.0
    d "..."
    a "{cps=*2}No, don't worry about it, it's emb-{w=1}{nw}{/cps}"

    show daisy nervous
    d "No, I'll go, I'll go."
    show anya happy
    #[ANYA SMILE SPRITE]
    #[DAISY AWKWARD SMILE SPRITE]
    show daisy idle smile
    "I fall into her, she laughs as she helps prop me up."
    show black screen behind daisy:
        alpha 0.25
    show anya behind black
    show daisy upset
    "I should fall down again and see what she does next."
    show black screen behind daisy:
        alpha 0.5
    "Or, maybe I'll open the cabinets and get the fancy glass cups out."
    show daisy angry
    show black screen behind daisy:
        alpha 0.75
    "Maybe I'll smash it on the ground and see how she reacts."
    show black screen behind daisy:
        alpha 1
    show anya idle
    "What she'll do when she sees the glass pierce my skin."
    hide black with dissolve
    a "Wait, here."
    show daisy anxious
    show pamphlet_inspect with dissolve
    "She hands me a little pamphlet."
    hide pamphlet_inspect with dissolve
    show anya happy
    a "I designed it, I thought it'd be cute for your scrapbook collection!"
    show daisy surprised
    show anya idle
    d "You remembered?"
#sprite 
    show anya happy

    a "How could I not! I remember how the others gave you so much shit for it back in the day. I bet they were just jealous!"

    show daisy anxious
    d "..."
    show anya suspicious
    a "You're better off without those jerks. None of them went to college after high school either. They're all stuck in our home town."
    show anya idle
    show daisy upset
    "Really? Of course."
    show black screen behind daisy:
        alpha 0.15
    show anya behind black
    "This is the catch."
    show black screen behind daisy:
        alpha 0.3
    "I can't let my guard down for even just a second."
    show black screen behind daisy:
        alpha 0.45
    show daisy angry
    "She always has to bring up those jerks, even when I'm having a good time."
    show black screen behind daisy:
        alpha 0.6
    "Why do I still even talk to her when she enjoys tormenting me, she's no different than my old friends-{nw}"
    show black screen behind daisy:
        alpha 0.75
    extend " she's probably just waiting for me to crash and fall and she can laugh at me all she wants."
    show black screen behind daisy:
        alpha 0.9
    "I'll just drink more and more.{p=1.0}That'll prove her wrong."
    hide black with dissolve
    #sprite
    show anya upset
    a "Daisy! Chill with the alcohol, seriously."
    show daisy upset
    "My eyes well up for no reason."
    "I mean, this is what she was waiting for."
    "I bet Anya couldn't wait for this."
    show daisy angry
    "{b}She's asking for this.{/b}"
    show daisy crying
    d "Nngg.. sorry..."
    show anya idle
    a "Hey, hey it's ok!"
#sprite
    "She wipes my tears gently."
    show daisy blush
    "I want to lean in, it feels good."
    show daisy anxious
    "But this is reserved to Samyaza."
    show daisy nervous
    "Wait, no it doesn't feel good, I'm deluding myself."
    show daisy upset
    "It's bad, so so bad."
    "I have to step away."
    show daisy at flip
    "Wiping my own tears, I can't fall apart."
    "Here and now I have to be strong."
    show daisy idle
    "Tomorrow Samyaza and I are going to do the ritual."
    show daisy anxious
    "{cps=*3}But I don't wanna do it, I really don't, maybe if I get hungover enough we can delay it.{/cps}"
    "{cps=*3}The idea of her leaving me as quickly as she met me is too much for me right now.{/cps}"
    "{cps=*3}I wonder how Anya would feel about her- the fact that I have someone else besides her now.{/cps}"
    show anya happy
    "Anya grabs my wrist- the same one that was burnt by Samyaza. {nw}"
    show daisy angry
    show anya upset
    extend"I want to rip my arm away from her. {nw}"
    show daisy at flip
    "It's not meant for her, the shape of the burn is Samyaza's hand, {b}not hers.{/b}"

    show anya idle
    a "...{w=.5}Why don't I introduce you to my friends? They're a lot nicer than the group from home, that'll make you feel better."
    show anya at flip
    "Anya thankfully turns away from me and releases her hand from my wrist."
    "{b}Good.{/b}"
    "{b}It's not hers.{/b}"
    "{cps=*3}Her grip isn't as good as Samyaza's, Samyaza feels strong, maybe it's because she's an angel or whatever she is I don't even know but it's magical and beautiful.{/cps}"
    "She makes me feel safe. {b}Nothing like Anya.{/b}"

    show black screen with dissolve
    "As she introduces me to everyone, I dart around looking for more alcohol."
    "{cps=*3}They don't care about me anyways, they only care about Anya. I don't care about anyone here, I wish I had invited Samyaza with me. Why didn't I invite her?{/cps}"
    "Maybe because I want her for myself, how terrible."
    "{cps=*3}I'm so bad I wish I could bash my head in with my glass right now and bleed out everyone would be so shocked but then Anya would call Samyaza and Samyaza would take care of me."
    
    hide daisy
    show black behind daisy

    show daisy sappy at scene_right_far with dissolve 
    "She'd heal me, she'd make me feel {b}so good..{/b}"
    show daisy upset
    hide black screen with dissolve
    #sprite
    show anya at unflip
    a "Hey, Daisy. Why don't you tell them about that time we had that science experiment back in high school?"
    stop music fadeout 2

    pause 2
    show daisy angry

    play music wav_dissociation
    window hide
    pause 2
    window auto
    "Is she {b}seriously{/b} trying to get me to talk about {b}that?{/b}"
    "What is {b}wrong{/b} with her?"
    "I could just see her mouth flapping... {w=3}{nw}"
    #camera zoom in later
    show anya behind daisy
    show red screen behind daisy with dissolve:
        alpha 0.1
    "\"Daisy, Why don't you talk about your first breakup?\"{w=3}{nw}"
    show red screen behind daisy with dissolve:
        alpha 0.2
    "\"Why don't you talk about that funny story about you and your mom.\"{w=3}{nw}"
    show red screen behind daisy with dissolve:
        alpha 0.3
    "\"Don't you remember that one where she cried because you asked to have a sleepover with girls when you were ten?\"{w=3}{nw}"
    show red screen behind daisy with dissolve:
        alpha 0.4
    "\"Saying that you're abandoning her?\"{w=3}{nw}" 
    show red screen behind daisy with dissolve:
        alpha 0.5
    "\"Rejecting her? \"{w=3}{nw}"
    show red screen behind daisy with dissolve:
        alpha 0.6
    "\"That was sooooo funny, Daisy.\""
    show red screen behind daisy with dissolve:
        alpha 0.7
    "How about that time {b}you{/b} missed school for a few months and everyone thought you were dead?"
    show red screen behind daisy with dissolve:
        alpha 0.8
    "{cps=*3}How will she feel if I ask her to talk about the funny story about her senior year boyfriend? How will she feel if I ask her to talk about that one ex-friend of hers?{/cps}"
    hide red screen with dissolve
    show daisy upset
    d "Uh. I don't remember that one. Sorry."

    "Her friends look at me, smiles do not meet their hearts. "
    show anya at flip, scene_center with moveinleft
    "Anya goes on to talk about some other story from when we were 18."
    "It was during her first spring break."

    "Fingers dig their way into my wrist."
    "Anya is socializing {nw}"
    #[HAPPY SPRITE] 
    extend "with her {b}real friends.{/b}"
    "They shriek and squeal at almost every other thing Anya says."
    "{cps=*3}She's so so much funnier than me she's so much prettier so they can laugh at her and look at her cause she's so easy on the eyes.{/cps}"
    show daisy angry
    "I'm a fucking eyesore next to her."
    show daisy upset
    "{cps=*3}I want to stay in the group. No, I don't want to. No, I think I want to. I don't know.{/cps}"
    show daisy angry

    "{cps=*3}When I'd talk they'd just wait for Anya to start talking because Anya is better, why don't they go ahead and rip the bandaid off, tell me to shut up.{/cps}"
    
    "{cps=*3}I would lose balance and every time I did I was just waiting to feel everyone's hands on me, as they pushed me down.{/cps}"
    "{cps=*3}{b}It's bound to happen.{/b}{/cps}"

    show daisy upset
    d "I need to go to the bathroom."

    #ANYA (shocked sprite, text is fast and she cuts out quickly)
    show daisy at offscreenright with moveinleft
    a "Dais- {w=.5}{nw}"
    
    "I ran off before she could say my name." 
    pause 2.0
#INT. BATHROOM - NIGHT
    scene anya_bathroom with fade
    "All I could do was stare at the mirror. "
    show daisy upset at scene_center with dissolve
    "I repeat the words I'd say to the rest of the group just so I can understand their horror as they saw my mouth move."
    show daisy with moveintop:
        ypos 1400
    "Dejected, I sit on the bathroom floor."
    show daisy blush
    "I miss Samyaza. "
    show daisy angry
    "{cps=*3}I slap myself, I don't want to linger on her, no, I want Samyaza to come, I don't believe in God but maybe I do now.{/cps}"
    show daisy anxious
    "I prayed, God {b}please please please{/b} send Samyaza to come get me."
    show daisy upset
    "{cps=*3}I miss her so much I want to bite my lip so hard that blood bursts out and this entire bathroom becomes stained, but it's okay because she'll come-{w=4.0}{nw}{/cps}"
    show daisy blush
    "{cps=*3}-and she'll hold me and she'll heal me. No one here matters except for her. I really, really, really, really, {b}really{/b} miss her.{/cps}"
    hide daisy with dissolve
    "I curl up into a ball, and begin to hug my legs tightly, anything to get even a fraction of comfort."
    "{cps=*3}I miss her, I miss her, {b}I miss her.{/b}{/cps}"
    "{cps=*3}I feel like such a kid as the tears stream down my face, maybe even snot too, {nw}{/cps}"
    show red screen with {'master':dissolve}:
        alpha 0.25
    extend "{cps=*3}I bite even harder on my lip. I'll make myself uglier- {/cps}{cps=*.25}{b}I'll be a pile of tears, mucus, and blood.{/b}{/cps}"
    "{cps=*3} I'll put Samyaza up to the test. Maybe she's the one if she can clean me up.{/cps}"

#(KNOCK SFX. KNOCK SFX)
    "I hear a knock at the door" #cut ater
    "{b}Not now, not now.{/b}"
    play sound door_knock
#ANYA (through the door)
    a "{size=*.75}Hey.. Daisy?{/size}"
    "Why don't I have the the strength within me to yell {shader=zoom}{b}“FUCK OFF!”{/b}{/shader} at her." #took out what

    show daisy crying at scene_center with dissolve
        
    
    d "{cps=*.5}...what..?{/cps}"

    a "{size=*.75}Are you...{w=1.0} okay?{/size}"
    show daisy angry
    "{shader=jitter:u__jitter=1.0, 3.0}{b}Is she fucking serious?{/b}{/shader}{nw}"
    "{b}Is she fucking serious?{/b}{fast}"
    
    a "{size=*.75}It's okay if you don't want to talk about it now...{w=1} but I'm here for you..{/size}"
    show daisy upset
    "It takes me a minute to register what she wants from me. {p=1}{nw}"
    show daisy angry
    extend "I scoff into my legs, and crane my head up against the wood of the door to reply, but ..."

    a "{size=*.75}Hey... um...{/size}"
    show daisy angry
    "Oh god, what else now?"
    stop music fadeout 1.5
    a "{size=*.75}...{p=1}Your roommate is here.{/size}"
    show daisy surprised
    "...{w=.75}{b}What?{/b}"


    
    a "{size=*.75}She said that she's looking for you? But I can tell her you're busy if you need some t-{w=3}{nw}{/size}"

    #(QUICK CUT TO INT. ANYA HOUSE - NIGHT. DAISY SPRITE IS SERIOUS) [SLAM SFX]
    play sound door_slam
    scene black screen with Dissolve(.1)

    scene anya_house
    show anya idle at scene_left
    show black screen
    hide black screen with Dissolve(.1)
#add crowd?
    show daisy upset at scene_right_far with moveinright
    
    d "{b}Where is she?{/b}"
#sprite
    a "Oh, she's over b-{w=2.0}{nw}"
    show angel sad at scene_center, flip with dissolve
    s "Daisy!"
    d "Aza!"
    play music wav_okaeri
    "Every stupid little thing that is eroding my brain flies out as I {nw}"
    show daisy crying at scene_center_offright with {"master": moveinleft}
    extend "run into her arms."
    "My snot and tears stain her shirt."
    show daisy sappy with None
    show black screen behind daisy, angel:
        alpha 0.5
    show anya behind black
    with {"master": dissolve}
    "I look up at her, it's like I came home."
    show angel happy
    #sprite
    "She wipes my tears, and wipes my mucus with her vest."
    "It looks like something out of a soap opera, but I don't {b}care{/b}."
    show daisy angry
    "I don't care about what any of these people think."
    show daisy sappy
    "I can die happy."

    show anya suspicious
    a "...Okay, I'll just leave you two alone then. {p=2}Daisy, text me when you get home, okay?"

    show daisy upset
    "Whatever."
    "Yeah, yeah."
    "Who cares."
    "Keep showing others just how caring you are."
    show daisy angry
    "I know the real you."


    #EXT. UNIVERSITY PARK - NIGHT
    scene yuri_park_night with fade
    show daisy nervous at scene_center
    show angel idle at scene_center_offleft, flip
    with dissolve

    "It's not like I could walk straight."
    "I definitely couldn't, but I would be lying if I said that I didn't make myself tumble more than I should've, because everytime I did, Samyaza would hold me back up."
    "She's so strong and so beautiful and so warm."
    "{cps=*3}It feels so good to have my body make any kind of contact with her whatsoever and I just want to feel more and more and {b}more{/b}. I just want her {w=.5}{nw}"
    "{cps=*3}It feels so good to have my body make any kind of contact with her whatsoever and I just want to feel more and more and {b}more{/b}. I just {fast}to become a part of her so that I can be hers and only hers."

    show angel frown
    s "Hey, drink some water."

    "{cps=*3}I don't  want to drink it. Let it drip down all over me. Like the water ritual. I wanted the water she touches to fall down on me.{/cps}"

    show daisy blush
    d "...More, please."
    show angel happy big
    "Samyaza laughs, and holds my head up. {nw}"
    show daisy sappy
    extend "Her eyes are so dazzling. I want to swim in them. I'm lying. I want to swim with {b}her{/b}.{w=1} ...Maybe...{w=1} maybe I shouldn't say that."

    show daisy sappy
    d "I'm so tired."

    "I lay my head on her, she's much taller than me and {cps=*3}it feels so good.{/cps}{p=1}Her arm around me feels so good."
    "God, please don't let it end."
    "I'm {b}begging{/b} you."

    show angel frown
    s "We're almost home."

    "She grips me tighter. "

    show daisy anxious
    "This isn't enough."
    show angel confused
    #SAMYAZA (confused sprite)
    show daisy sappy
    d "I want to melt into you...{w=1} right now...."
    show angel idle
    "{cps=*3}I'm stupid, I'm so so stupid but I don't care because I want this now. Consciously, unconsciously, whatever it was I felt my body weight shift more and more towards her side. {b}Pure Ambrosia.{/b}{/cps}"
    "{cps=*3}I don't think I've ever felt so good in my life. I {b}need{/b} her and I {b}need{/b} her to do things for me and I don't {b}care{/b} how wrong that is. I just want nothing more in my life right now.{/cps}"
    show angel desire
    "She holds me tighter."

    d "Only you make me feel good."

    "Even tighter. It hurts, but I don't care, I weakly cling to her back."
    show daisy anxious
    d "I'm going to hate myself tomorrow."
    show angel happy
    s "It's okay, you're okay."
    show daisy sappy
    "I melt into her. No, I can't, our skin is keeping us apart."

    d "Say that again...{p=1.0}{i}...please...{/i}"


    #SAMYAZA (satisfied? Smug? sprite)
    show angel desire
    s "{b}You're okay.{/i}"

    "{cps=*3}She keeps patting my head but it isn't enough. I want so much more. I wish her hand would sink in through my head, reach into my brain and that she'd pick, unwind it, lay it flat, and just destroy it all.{/cps}"

    d "I wish you could've been my mother, Aza"

    #SAMYAZA (serious sprite)
    show angel sad
    s "...Me too."

    "I snuggle further into her. More and more. I need {b}more.{/b}"

    d "If you were my mother, what would you do?"

    "She caresses my head. I lean into it."
    "I'm all hers."
    "God, please make my next life bring us even closer together."
    "It's still not {b}enough.{/b}"

    show angel confused
    s "What would you want me to do?"
    show daisy anxious
    "I pout at her, stepping on her toe."

    #flips
    s "Daisy, I want you to teach me. I don't {b}know.{/b} All of the angels in my order, we are...{w=1} Well, different. I'd hear their voices all the time, we were always able to know we weren't alone, {b}we had each other's voices.{/b}"
    show daisy sappy
    "I look up at her, she can't see the face I'm making. I'm too drunk to understand where she's going with this."
    show angel sad
    s "We {b}were each other.{/b} Our purpose was each other, and the humans we took care of."
    s "My last human...{w=1} She didn't have a mother. And all the other humans I've taken care of had lacked that presence in their lives."

    s "I guess ... that's something I should've looked more into during my time as an angel."

    s "I loved watching them, I wanted to be a part of them. "

    show daisy surprised
    d "The last human...{p=1}Was she the one that...?"

    show angel scary
    s "Yes."

    #SAMYAZA (somber)
    show angel sad
    s "Maybe...{w=.5} she wouldn't have...{w=.75} erased herself...{w=1} If I could've been like that for her."
    show daisy anxious
    d "Is that... why..{w=1} she..."

    s "Yes, after I told her about heaven, she wanted to go. Maybe to see her mother in heaven. If I could've been that for her, she would still be here, and I'd be with my sisters."
    show daisy upset
    d "But...{w=.5} you wouldn't have {size=*.75}me.{/size}"

    "{cps=*3}You don't have to think about her anymore because you have me, you don't have to go back there because you have me, am I really so disposable? I can be anything and everything for you, everything that she couldn't have been for you, I'll do anything for you.{/cps}"
    "{b}So please, don't leave me.{/b}"

    "She pets my head, and I sulk into her."
    stop music fadeout 2
    #INT. DAISY'S ROOM - DAY.
    #[AC BLASTING SFX]
    scene room daisy with Fade(1,1,1)
    play music baz1_2 volume 3
    play sound ac_hum volume 0.1 

    "Mouth agape, I stare up at my ceiling. My head's absolutely pounding."

    "I hold my forehead, God, I don't even want to {b}remember{/b} what I said last night."

    #[KNOCK SFX]
    play sound2 door_knock
    "I hear knocks." #cut
    #[♫ 1-2 GAZ]
    "The only way to not die of embarrassment is clearly to hide under my covers."
    "Every time bits and pieces of the night before pop into my head, I want to disappear and die."

    d "Just give me a-{w=1}{nw}"
    show angel happy at scene_left,flip with moveinleft

    "She's halfway through the door before I can ask her to leave."
    "In her hands, she holds a steaming warm cup of tea and an anti-nausea pill."
    #[WARM CUP OF TEA POPUP]
    #[NAUSEA PILL]
    show daisy upset at scene_right with dissolve
    "Peeking my head out of the blanket, I give her an irate glance."

    s "I got you some stuff. I hope this medicine works."

    "Sitting up, I take the pill, uncomfortably pulling my knees in."

    d "Sorry...{p=1}My room is such a mess..."

    show angel happy big
    s "No worries. Do you remember anything about last night?"

    show daisy blush
    "Sinking into myself, I blush."
    show daisy anxious
    #DAISY (sad sprite)
    d "Yes..."
    show angel at scene_center with moveinleft
    "Samyaza laughs, and pats my head as I pout at her."
    show angel desire
    s "Don't be embarrassed, it was cute."
    show angel sad
    s "...Did that drink hurt you?"

    show daisy surprised
    d "Huh?{p=1}Oh, the alcohol? Uh...{w=1} No, not really."

    show angel confused
    s "How does it make you feel?"

    show daisy nervous
    d "I feel like it's supposed to make you feel good? But I just got more in my head...{w=1} Well..{w=1}{nw}"
    show daisy blush
    extend " before you came.."

    s "Hmm, interesting. I always wondered. Angels can't really get inebriated like that,{nw}"
    show angel happy
    extend " hah."

    show daisy anxious
    d "Oh.{w=.5} Um.{w=.5} Aza.{w=.5} Could you not throw the packet for the nausea meds away.."

    show angel confused
    "Her eyebrows raise as she hands me the package."
    s "Sorry... It slipped my mind."

    show daisy idle smile
    d "It's okay."

    show angel sad
    s "No. I'm really sorry.."
    window hide
    pause 2
    window auto
    "Awkward silence fills the room. {nw}"

    show angel happy big
    extend "Samyaza's face lights up as she remembers something."
    s "Oh right! I forgot, we have to do the ritual today."

    show daisy anxious
    d "Uhm... does it have to be today?"

    show angel scary
    s "{b}Yes.{/b}"

    d "{size=*.8}Well..{/size} {size=*.6}I do have something...{w=1}{/size}{size=*.4}I might need to do t-{w=1}{nw}"
    stop music fadeout 3
    show angel frown
    s "You're the only one who can help me."

    #[♫MUSIC STOP♫]
    #[UNCOMFORTABLE SPRITE] 
    show daisy nervous at scene_right_far with moveinleft
    "I sink further into my bed."

    d "{size=*.75}It can't be later..?{/size}"

    s "No, it needs to be now."

    "But Anya..."

    s "We need to do the first step now. It's what helps connect the human and angel that undergoes the ritual. It's necessary that we start it sooner than later."

    d "{shader=jitter:u__jitter=1.0, 3.0}{size=*.75}...So did yesterday mean nothing to you...{/shader}{/size}{nw}"
    d "{size=*.75}...So did yesterday mean nothing to you...{/size}{fast}"

    show angel confused
    s "What did you say?"

    d "{size=*.75}...Nothing..{/size}"
    show angel at scene_center_offright with moveinleft
    show angel happy
    "Samyaza scoots in closer, both of her hands cupping mine."

    s "Also, the first two steps are restorative...{w=1} {nw}"
    show angel desire
    extend "I think it'll help you feel better."

    
    "Tentatively,{w=.5}{nw}"
    show daisy blush
    extend " I put my other hand on hers."
    #[BLACK SCREEN]
    #[♫WHO ARE YOU♫]
    scene black screen with Dissolve(2)
    play music wav_who_are_you
    play sound phone_ring
    #sfx
    "Samyaza's preparing the incense and the candles in the living room. I wish I could focus on the noise of her moving around instead of the {nw}"
    #sfx
    show phone_inspect with {'master':dissolve}
    extend "shrill ringing of my phone."
    hide phone_inspect with Dissolve(1)
    "Begrudgingly, I accept the call."

    show white line at center:
        alpha 0.5
    show anya upset at scene_left
    with dissolve
    a "Hey, Daisy. Are you coming? It's almost done."

    show daisy anxious at scene_right with dissolve
    d "Sorry...{w=.5} {size=*.75}I planned something with Samyaza...{w=1}{/size} {nw}"
    show daisy nervous
    extend "{size=*.5}I forgot to tell you...{/size}"
#sprite
    show anya suspicious
    a "Oh..."

    "The silence worsens my already terrible nausea."
    show anya upset
    a "Well, I really wanted you to come...{w=1} {nw}"
    show anya idle
    extend "I'm glad you have a new friend though."

    show daisy angry
    d "{cps=*2}What, like I can't make friends without {/cps}{cps=*.1}{b}you{/b}?{/cps}"
    show anya suspicious

    show daisy surprised
    "I cover my mouth."
    "...The weird tinge of guilt and anxiety from finally expressing that thought overwhelms me."
    show daisy nervous
    "I want to hit my head against the wall."
#sprite
    show anya upset

    a "{cps=*.25}...What...?{/cps}"

    d "{cps=*3}Oh. Sorry...{w=.2} Uh...{w=.5} Sorry, I didn't mean that. I'm so hungover. I don't know what got into me.{/cps}"
    show anya suspicious
    a "Right...{w=1} Well, have fun with {i}{b}Samyaza.{/i}{/b}"
    show daisy upset
    "I can nearly taste the venom in her words."
    show daisy angry
    "Biting my lip, I hold back the curses I have for her."

    d "Well, yeah. Good luck with your showcase. {b}Bye.{/b}"
    hide white line
    hide anya
    with {'master':Dissolve(0.2)}
    "I hang up quickly, and throw my phone on the bed."
    stop music
    #INT. LIVING ROOM - DAY
    scene yuri_living_room 
    show angel idle at scene_center
    show angel:
        ypos 1500
    with fade
    play music wav_pale_moon_bright_eyes
    #[♫PALE MOON, BRIGHT EYES♫]

    "Samyaza looks ethereal."
    "Seeing her intensely calm demeanour brings me back to Earth."
    show angel happy big at flip
    show daisy anxious at scene_right_far with moveinright
    "She lights up as I leave my room."
    "In the middle of a large cloth, she sits oddly still."

    #[AIR SIGIL POPUP]
    show sigil_air with {'master':dissolve}

    "A large sigil with strange characters is drawn on it. "
    hide sigil_air
    s "Hey!"

    d "Hi..."
    show angel at scene_center_offright with moveinright
    "Samyaza stands up, {nw}"
    show angel desire 
    extend "holds my hand in hers, then starts petting my wrist with the other."

    s "Let's get started."
    show black screen with Dissolve(.25)
    show angel idle at scene_center
    show angel:
        ypos 1500
    show daisy idle at scene_center_offright
    show daisy:
        ypos 1500
    hide black screen with Dissolve(.25)
    #smoke v
    show black screen with {'master': Dissolve(2)}:
        alpha 0.3
    "Smoke from incense fills the air, clouding the small living room."
    "The incense is smooth and woody."
    "It's what I imagine an ancient temple would smell like."
    camera:
        
        perspective True
        xpos 0 ypos 0 zpos 0
        ease 2.0 xpos 150 ypos 150 zpos -500
    "Samyaza's face is lit by the candles...{p=1}She's {b}perfect.{/b}" 
    show angel frown
    "Her face stiffens as focus overtakes her. {nw}"
    show daisy sappy
    extend "Her hair falls perfectly on her shoulder, some strands framing her furrowed brows."
    "Oh, God."
    show daisy anxious
    "I bite my lip and push the thoughts away."

    "Our faces are close. {cps=*3}Could angels smell emotions? Is that a dog thing?{/cps} I don't know, but I'm glad the incense is masking the {b}stench{/b} I'd be putting out right now."
    show angel happy
    s "Repeat after me."
    show angel idle
    "Her smile hardens- she crosses her legs, she lays her hands open out on her knees...{p=1}She closes her eyes- like she's been waiting her whole life to perform this."
    show daisy surprised
    show black screen with dissolve:
        alpha 0.7
    "Following suit, one of my eyes trembles as I try to keep it open, gawking at Samyaza's process."
    #eyes closed sprites
    s "In position?"
    "I nod."
    show angel confused
    s "Daisy?"

    d "Sorry!!! I forgot you couldn't see me."
    show angel frown
    #SAMYAZA [CLOSED EYE SPRITE]
    s "Make sure your eyes are closed, okay?"

    show daisy nervous
    d "...Sorry..."
    show daisy anxious with None
    show black screen:
        alpha .9
    show white screen behind black

    with dissolve
    "The incense comforts me as Samyaza begins to hum incantations in a strange language."

    s "You're so cute."

    "I want to keep my mind clear, but Samyaza makes it so hard. I wish I could open my eyes and see her."

    "I feel her hands on mine."
    "I feel her breath."
    "I want to lean into her so bad."

    d "Sorry...{w=.5} they're sweaty..."

    s "You apologize so much...{w=.5} It's so cute."

    d "...Sorry..."

    s "{b}No more sorries!{/b} Even if it makes you cuter."
    pause .5
    s "Okay, now breathe in and out. Follow my lead, okay? "

    "I nod...{w=.5} then remember that she can't see me."

    d "Okay."
    show black screen:
        alpha 1
    with {'master': dissolve}
    "I close my eyes tighter, and try to shut out all distractions."
    "Focus on one thing, Daisy...{p=1}I hold my breath for a split second before joining Samyaza."
    "In...{w=1} and out."
    "In...{w=1} and out."
    "In...{w=1} and out."
    " We steadily reach a rhythm, becoming one."

    s "Mmngggh...!"
    play music wav_paranormal_investigation
    #[♫PARANORMAL INVESTIGATION♫]
    show white screen
    show black screen :
        alpha .7
    show red screen:
        alpha .5
    with dissolve
    "Her grip tightens as she {b}digs{/b} her fingernails into mine."
    "I hold her hands tighter in return."
    "I can't tell if the wetness in my palms was from sweat, or blood or both."

    d "{b}Samyaza!{/b}"

    s "Keep breathing! Don't open your eyes!"

    "{cps=*.7}My lungs are battling against me- breathing in and out is like swimming through molasses. "

    s "{b}{i}Aaagggnhh!{/i}{/b}"
    hide red screen
    with dissolve
    "The pain of squinting my eyes shut is interrupted by the tickling of hair- Samyaza's head lays on my shoulder."
    "She pants heavily...{p=1}Her breath comes in..{w=1} and out..{p=1}In...{w=1} and out."
    "{b}My mind goes somewhere it shouldn't.{/b}"

    s "You can open your eyes."
    show daisy sappy
    show angel idle
    hide black screen
    hide white screen
    with dissolve
    "She winces, and tries to give her usual smirk."
    show daisy anxious
    show angel pain open nowing
    "Her agony seeps through."
    
    "My heart aches."
    "Sweat trickles down her forehead."
    "I want to avert my gaze."
    "My fingers dig deeper into my legs."
    show daisy nervous
    "Her lips are calling to me."
    "I can see a small sliver of her cleavage." 
    show daisy blush
    "My breath shakes."
    show daisy nervous
    "There's something really wrong with me, who the {b}hell{/b} thinks about their roommate this way?"

    s "You're redder than me..{w=1} Ha."
    show angel with {'master': moveintop}:
        ypos 2500
    "She collapses into my lap. Blood seeps through her vest and small bulges appear through the fabric. {nw}"
    show white screen with {'master': dissolve}:
        alpha 0.2
    extend "A light glows through it."

    show daisy nervous
    d "Samyaza..{w=1} What's wrong?"
    show daisy with {'master': moveintop}:
        ypos 2500
    scene black screen with {'master': dissolve}

    "She traps me on the ground."
    "I squirm and try to leave- to look for any sort of measly first aid materials we have."
    "I haven't done this since...{p=1}God, since before I transitioned.{p=1}{size=*.5}Back when mom...{/size}"

    s "...It worked...{p=1}Don't worry about it, you don't have to do anything..."
    scene yuri_living_room_night
    #[♫BY YOUR SIDE♫]
    show angel happy at scene_center
    show angel:
        ypos 1500
    show daisy anxious at scene_center_offright
    show daisy:
        ypos 1500
    camera:
        xpos 150 ypos 150 zpos -500
    stop music fadeout 2
    show black screen
    hide black screen with Dissolve(2)
    play music wav_by_your_side
    "She takes me out of it. {nw}"
    show daisy idle
    extend"I hover my hands over her vest...{p=.5}I guess, there's nothing else for me to do...{p=.5}{nw}"
    show daisy sappy
    extend "Other than to massage her wing bumps."

    "Something I always had to do for mom, feels {b}so{/b} much better when it's her."
    "This is...{w=1} {b}normal.{p=1}{/b}Yeah."

    show angel desire
    s "Mm...{w=.5} you're {i}good{/i} at this..."
    show daisy blush
    show red screen with Dissolve(4.0):
        alpha 0.2
    "My face feels so hot that I don't think about how my hands are being burned as I massage her."
    show angel pain
    "She whimpers as I keep going. {nw}"
    show angel desire
    extend "I apply more pressure."
    "My legs feel...{w=.5} jiggly."

    s "{size=*.75}...Take it off...{/size}"

    "I..{w=1} {size=*.75}I couldn't...{w=1}{/size}That's too crass, she's {b}just my roommate.{/b}"

    "..."
    show red screen with dissolve:
        alpha 1
    "My hands were covered in blood and sweat."
    show daisy anxious
    show angel pain open behind daisy
    hide red screen 
    show red screen as rs:
        alpha 0.2
    with dissolve
    "Her wings were a crimson, wet red."
    "They were jutted halfway out, like a bone sticking out of the body."
    "The beam from the light...{w=5} inside her skin..{w=.5} was also leaking out."

    s "I'm sorry."
    show daisy surprised
    d "{cps=*.5}..For what..?{/cps}"
    scene black screen with dissolve
    "She leans up quickly, and kisses me."
    "Her hands wrap around me, going lower, and lower..."

    "Her lips are hot.{p=.5}Are mouths supposed to be this warm?"
    "It felt like my lips were on fire."
    "Our tongues begin to collide."
    "{b}This still isn't enough.{/b}"
    "I went deeper and deeper into her."
    "We'd occasionally pull away, to look at each other's face."
    show angel desire at scene_center 
    show angel:
        ypos 1500
    with dissolve
    "Her skin was perfect, she wasn't blinking at all."
    hide angel with dissolve

    "We pulled back into each other. This. {size=*1.25}Isn't{/size} {b}{size=*1.5}enough.{/size}{/b}"
    "{cps=*3} I want to collide with her. Her heat isn't enough.{p=0.2}No matter how close I get, I keep getting frustrated. {/cps}"

    "She pulls away, petting my face."
    camera:
        xpos 0 ypos 0 zpos 0
    show white screen
    show black screen:
        alpha 0.6
    show red screen:
        alpha 0.2
    with dissolve
    "I lean in."
    "I want to feel my tongue {b}burn.{/b}"
    "I want ashes to mix in with the liquids from the night."
    "I rub her wings as she quivers."
    "The bodily fluids lubricate my hands."
    "I stroke the oil through her feathers, letting them open up."
    hide daisy
    show white screen behind daisy, angel:
        alpha 0.5
    show red screen behind daisy, angel:
        alpha 0.1
    show yuri_living_room_night behind daisy, angel, red 
    hide black 
    with dissolve
    show daisy sappy at scene_center
    show angel pain open behind daisy at scene_left
    with {'master': Dissolve(3)}
    camera:
        ease 5 xpos -300 ypos -250 zpos -600
    "As I up the intensity, she {b}trembles{/b} into me."
    show angel at flip
    "We softly whimper into each other- the kiss muffles any noises that could come out."
    "I feel like I'm on fire."
    "I pant."
    "I stroke her wings."
    show angel at scene_center_offleft, flip with moveinright
    "She leans further into me."
    "Further and further."
    stop music
    #[♫MUSIC ABRUPT STOP♫]
    #[♫ HEARTBEAT♫]
    show daisy nervous with None
    show yuri_living_room_night
    hide white 
    hide black 
    hide red 
    with dissolve
    camera:
        ease 3 xpos -0 ypos -0 zpos -0
    show angel at scene_left with moveinleft
    "I push her away."
    play music wav_heartbeat

    show daisy upset at flip

    d "I..{p=1}I'm sorry."

    s "...It's okay."
    show daisy upset
    show angel behind daisy
    
    show black screen as bs behind daisy:
        alpha 0.2
    with dissolve
    "She looks at me with so much adoration my stomach feels like it's collapsing."
    show black screen as bs behind daisy:
        alpha 0.4
    with dissolve
    show daisy nervous
    "My whole body feels like it could turn in on itself."
    show black screen as bs behind daisy:
        alpha 0.6
    with dissolve
    "I'll become a pile of meat and blood."
    show black screen as bs behind daisy:
        alpha 0.8
    with dissolve

    d "No...{w=1} {cps=*2}No. I shouldn't have. I need to {i}help{/i} you now.{/cps}"

    hide black screen as bs 
    show yuri_living_room_night behind daisy, angel
    with dissolve 
    show angel frown
    with dissolve
    s "No. You're not going to. {nw}"
    show angel desire
    extend "A cute lady like you should just sit herself down and look pretty."
    show angel frown 
    "She gets up, {w=.5}{nw}"
    show angel at unflip with {'master': moveinleft}:
        xpos -600
    extend "and heads to the bathroom. {p=1}{nw}"
    play sound door_slam
    extend "The door slamming shut rings throughout the entire apartment."
    scene room daisy night with Fade(1,2,1)
    #INT. DAISY'S ROOM - NIGHT

    "Viscous hands stick to my knees."
    "The smell of blood permeates through my room."
    "It's thick, like I'm in an angelic slaughterhouse."
    show daisy anxious at scene_center_offright with {'master': dissolve}
    "I sit up."
    
    "I open drawers, aimlessly searching for any kind of familiar cold steel."
    "I look through the pile of stuff in my corner- not here.{p=.5}I look through my desk- nothing there either.{p=.5}I look thr-{w=.5}{nw}"

    stop music fadeout 1
    #[♫MUSIC STOP♫]
    #[DOOR CREAK SFX]
    play sound door_open
    show angel sad at scene_left, flip with moveinleft
    s "...Daisy..."
    show daisy nervous
    "Why did she have to walk in?{p=1}Frozen, I stare like a deer in headlights."
    show angel sad at scene_center with moveinleft

    "She walks towards me." 
    "Tensing my entire body, I brace myself."
    show red screen with dissolve:
        alpha 0.2
    "A hot hand gently touches my face."
    "It burns."
    show daisy sappy

    "And yet, I tilt into the touch."
    show daisy anxious
    "Samyaza is clean, and her wings have been tucked back inside of her body."
    "I should ask if she's okay, or what even happened."

    "...{w=1}I shouldn't pull the stunt I did earlier.{p=1}{nw}"
    show daisy upset
    extend "I'm {b}disgusting.{/b}"
    show daisy blush
    show black screen with dissolve
    "I kiss her hand."
    hide black screen with dissolve
    #sprite?
    s "Are you ok?"

    show daisy anxious
    d "What about you?"

    #SAMYAZA (scary sprite)
    show angel scary
    s "That doesn't matter."
    show red screen with {'master': Dissolve(1)}:
        alpha 0.2
    "I let her hand sear my cheek. "
    show daisy nervous
    d "Oh."

    show angel confused
    s "...?"

    d "Um.{p=1}I have to do a medical thing."

    "Standing there, I wait for her to say something."
    "I should kick her out.{p=.2}She doesn't need to be here for my routine."
    play music wav_by_your_side
    #[♫BY YOUR SIDE♫]
    show angel happy
    s "I'll help!"

    show daisy surprised
    d "Have you...{w=.5} {i}ever{/i} administered a shot before?"
    show angel confused
    "Tilting her head, she furrows her brows."

    s "...No...?{w=.5} Or..{w=.5} I think..?{p=.5}I don't remember if I've seen my humans in the past do something like that."

    show daisy idle smile
    d "Oh, then, don't worry! I can do it myself."
    show angel scary
    "She swiftly pulls my wrist away from the supplies I was about to grab."

    s "I got it."
    window show
    scene black screen with {'master': dissolve}
    "She places a hand on my thigh and sits me down onto my bed." 
    "The contact makes something deep within my core...{w=1} {b}tremble.{/b}"
    "Without a word, I watch her as she picks up the vial and cleans the top of it with an alcohol wipe."
    #[SYRINGE AND VIAL POP UP]
    show estrogen_inspect with {'master': dissolve}

    "Unwrapping the packaging of the syringe, she spins a pink thick-gauge needle on top."
    hide estrogen_inspect with dissolve
    "Despite her lack of confidence earlier, she's like a nurse, methodical and precise."

    s "How much?"

    d "Oh, uh .3 mL, but really it's oka-{w=1}{nw}"

    "She doesn't answer me, instead flipping the vial over and closing one of her eyes to focus on coaxing out the exact dosage into the syringe."
    "Not even I could do that when I first started out...{p=1}She switches out the needle for a skinnier, orange one and stares at my legs."
    scene room daisy night
    show angel idle at scene_center, flip:
        ypos 1500

    show daisy nervous at scene_center_offright:
        ypos 1500
    camera:
        xpos 150 ypos 150 zpos -500

    show black screen
    show daisy blush
    hide black screen 

    with {'master': Dissolve(2)}

    #"Her gaze me out of it. {nw}"
    " I'm painfully aware of her gaze on me."
    "I slowly ride my skirt up."
    show daisy nervous
    "Being careful to make sure it covers my old scars." 
    "She taps the air bubbles out of the syringe."
    show daisy sappy
    show red screen with dissolve:
        alpha 0.2
    "I can't handle the heat I'm feeling within me."
    hide red screen with dissolve
    "She holds the syringe in her mouth while she pats around my leg." 
    "Her warm hand is on my thigh."
    "Roommates do things like this, {b}totally{/b}."
    show angel frown
    show daisy nervous
    "She feels my thigh up and down, burning with an intense concentration as she looks for a suitable spot."
    show daisy sappy
    "{shader=jitter:u__jitter=1.0, 3.0}{b}Her hands feel so good.{/b}{/shader}{nw}"
    "{b}Her hands feel so good.{/b}{fast}"
    show daisy blush
    "I'm so glad I forgot to do my shot yesterday."

    "She stops at the upper side of my thigh, and wipes down the spot."
    show daisy anxious
    "It's time."
    show daisy nervous
    "I've done this so many times before, {cps=*5}I don't know why my heart just keeps beating faster and faster.{/cps}"

    show angel happy
    s "Ready?"
    "I nod."
    show angel frown
    show red screen with {'master': dissolve}
    "She pinches a spot in my thigh and quickly injects my hormones."
    "My breath hitches in my throat." 
    hide red screen with {'master': dissolve}
    "The needle remains there for a few seconds, but then she takes it out and replaces it with a green bandaid."
    show angel desire
    show daisy idle
    "She pats that spot on my thigh once again.{p=1}I let out a breath that I didn't even realize I was holding."
    show angel happy big
    s "Aand, all done? How was that?"
    show angel sad

    "She notices my expression, or I guess lack thereof."

    s "{cps=*3}Oh no! Did I mess up? I'm so sorry, Daisy-{/cps}{w=1}{nw}"
    show daisy happy
    d "No, no, it's okay, you didn't do anything wrong. Thank you. Really, this is the most anyone has eve-{w=1}{nw}"

    #[PHONE RING SFX] 
    #[♫MUSIC STOP♫]
    play sound phone_ring
    $ renpy.music.set_pause(True, channel="music") 
    show daisy anxious
    "My phone rings." #cut
    show daisy upset
    "It's Anya."
    show phone_inspect at scene_center with dissolve:
        xpos 150 ypos 150 zpos -500
    "I reach out for my phone."

    #[PHONE POP UP]
    show angel scary
    "Maybe the ritual really did work, because with {b}unearthly{/b} speed, {nw}"
    hide phone_inspect with vpunch

    extend "Samyaza grabbed my phone and hung up the call."
    show angel idle
    $ renpy.music.set_pause(False, channel="music") 
    #[♫MUSIC RESUME♫]
    window hide
    pause 3.0
    window auto
    show daisy anxious
    d "I should.. Probably pick that up."

    show angel confused
    s "Why? Wasn't she the one who made you upset yesterday?"

    show daisy surprised
    d "Uh..."

    show angel sad
    s "I...{w=1} missed you a {b}lot{/b} last night..."

    show daisy idle smile
    d "...Yeah. Me too. "


    s "Like, really, really missed you."

    show daisy anxious
    d "...Me too.."

    show angel happy
    s "I want to make you happy, Daisy.{p=1}{nw}"
    show angel happy big
    extend "{b}Let me.{/b}"

    show daisy idle smile
    d "You do, though!"

    show angel frown
    s "You were about to hurt yourself, weren't you?"
    show daisy nervous
    "I look at my fingers, playing with my nails."
    camera:
        linear 2 xpos 150 ypos 100 zpos -700
    "Samyaza's hand rests on mine, and she leans her head in."
    show angel desire

    s "Please.{p=1}Let me make you happy...{p=1}I don't know what I'd do without you.{p=1}I don't know what I'd fill my days with."

    d "..."

    show angel happy
    s "I...{p=1}I can finally make it back to heaven.{p=1}I think."

    s "What you saw earlier, my angelic form is coming back to me."
    show angel desire
    s "With that, you'll {b}have me.{/b} I can help you more than Anya ever has."
    show daisy sappy
    scene black screen with {'master': Dissolve(4)}
    "Exhaustion must've taken over me. My mouth betrays me as I yawn instead of responding to her. I just lay my head on her."

    "I guess I'm going to help Samyaza go back to heaven. She can return to her family.{p=1}Away from me."
    "She needs me so badly, but she also badly needs to leave."

    "You don't know what you'd do without me, but you're using me to leave me."

    "I snuggle up to her, and drift away."
    stop music fadeout 2
    #[♫MUSIC FADE OUT♫]
    #INT. UNIVERSITY PARK - DAY
    scene black screen
    camera:
        xpos 0 ypos 0 zpos 0
    scene yuri_park_01 with Fade(0,2,1)
    #[BUG SFX]
    #[OUTDOORS SFX]
    play sound crickets_cicadas_looped volume 0.1 loop
    show daisy anxious  at scene_right,flip with dissolve
    "The sun is way too hot, which makes my headache throb even more."
    "This past weekend has felt like a dream."
    "I keep replaying the party, the ritual...{p=1}{b}Samyaza.{/b}"
    show daisy nervous
    "Instinctively, I cover my face. I don't want anyone seeing my blushed cheeks and getting the wrong idea."

    au "Daisy."
    #[♫REASONING♫]
    play music wav_reasoning
    show daisy at unflip
    "I turn around. God, this is the last thing I wanna deal with."
    show anya suspicious at scene_left with dissolve
    d "...Hi, Anya."
#sprite
    show anya upset
    a "What happened last night? You got totally drunk at my party, missed my showcase, then ignored me for the rest of the day."
    show daisy anxious
    d "Sorry. I was too hungover."
    show anya suspicious
    a "I mean, like, that's fine? Shit happens. But, you were ignoring me...{p=1}{nw}" 
    show anya upset
    extend "I was worried."

    show daisy nervous
    d "Oh um...{w=1} I had to spend time with Samyaza."
    show anya suspicious
    a "You could've at least let me know? Instead of hanging up all of the, like, five times I called you. {nw}"
    show anya upset
    extend "And what was up with that text..?"

    show daisy surprised
    d "What?? I don't know what you're talking about."
    show anya suspicious
    "She scoffs at me, and rummages through her bag for her phone."

    
    a "Did Samyaza do this?"
#obj 
    show phone_inspect with {'master':dissolve}
    "She lifts the phone to my face. Apparently, \"I\" told her to leave me alone for the night."
    hide phone_inspect with dissolve
    show daisy anxious
    d "Oh. That {i}is{/i} weird..."
    show anya upset
    a "Yeah, it is."

    "She waits for me to continue."
    "My head cranes down and I kick some fallen leaves around."
    "I feel like I'm a child that just got in trouble for something."
    show daisy nervous
    "...I try to scramble for a way to word this."

    
    d "Sorry, she took my phone. I couldn't say anything."
    show anya suspicious
    a "{b}What?{/b}"
    show daisy upset
    "Why is she looking at me like that?{p=1}Like all the other times she has over the years.{p=1}I press my foot onto the ground and ball my hand into a fist."

    show daisy nervous
    d "It was really fast...{w=1} I dunno...{w=1} We were having uhm, a {i}moment{/i} together."
    show anya upset
    a "That doesn't matter. That's really weird."
    show daisy angry
    show anya behind daisy
    show black screen behind daisy with dissolve:
        alpha 0.25
    "What does she know?{p=1}God {i}forbid{/i} someone wants me."
    show black screen behind daisy with dissolve:
        alpha 0.5
    "I'm going to curse her out so fucking bad."
    show black screen behind daisy with dissolve:
        alpha 0.75
    "{cps=*3}She's just jealous she doesn't get to have me to herself anymore, to make her look better by comparison.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 1
    "{cps=*3}I'm my own fucking person and I get to make my own decisions. I'm friends with Samyaza because she actually CARES about me and makes me HAPPY.{p=.3}{b}Unlike Anya.{/cps}{/b}"
    hide black screen with dissolve
    show daisy idle
    d "..."
    show anya suspicious
    a "Daisy, that's {i}weird.{/i} Roommates don't do that shit."

    show daisy idle smile
    d "It's okay, we have that kind of relationship.{p=.2}It's normal for us.{p=.2}Don't worry."
    show daisy anxious
    "I pray that this is it.{p=.2}That she takes the hint.{p=.2}I don't want this to go any further than it already has."
    "Anya pauses, and sulks a bit. She takes a breath, hesitating."
    show anya upset
    a "I don't know. I'm worried...{w=1} Forget it."

    show daisy angry
    d "{cps=*3}Why?? Are you worried because you're not used to seeing someone attracted to me? That it's weird that someone's interested in me, that someone cares enough to look after me? I have a life outside of you too, you know?!"
    show anya suspicious
    a "Stop jumping to conclusions. You know that's not what I mean, Daisy!"
    show daisy upset
    d "Well..?"
    show anya upset
    a "I'm worried.{p=1}Worried that even in a new environment, you're repeating old patterns."

    "My eye twitches. What is she even trying to imply here??"
    stop music
    #[♫MUSIC STOP♫]
    stop sound
    "We stand in silence."

    #[WIND SFX]
    play sound wind

    "I'm deluding myself. I don't want to face the truth."

    show daisy idle
    d "I'm going to class."

    a "...{w=1}Okay."
    show daisy at scene_right_far, flip with moveinright
    "I stomp off. My heart tightens as I try to collect my breathing."
    show anya suspicious
    a "...{w=.5}Wait, Daisy."
    show daisy angry at unflip
    "Furiously whipping my head back to her, I notice her get a bit taken aback."

    d "{b}What.{/b}"
    show anya idle
    a "I care about you...{p=1}I'm here for you, okay?"
    scene black screen with {'master':dissolve}
    "I close my eyes, and roll them to the back of my head."
    "Whatever. She's telling this to herself so she can feel like she did something, put in the bare minimum effort."

    "I storm off, heading wherever the wind takes me."
    stop sound 

    scene yuri_living_room_night with Fade(1,2,1)
    #INT. APARTMENT LIVING ROOM - NIGHT
    #[♫PALE MOON, BRIGHT EYES♫]
    play music wav_pale_moon_bright_eyes
    #sfx

    "Samyaza's door might just collapse with the strength I'm pounding at it."

    s "Give me a second!"

    d "Don't you wanna help me? At any cost?"
#sfx
    show angel happy at scene_left,flip with {'master':dissolve}

    "Within a heartbeat, Samyaza's door swings upon and she greets me with a smile."
    s "What's up?"

    show daisy upset at scene_right with dissolve
    d "Let's do the second phase.{p=2}Today."

    show angel sad
    s "I'd love to, but I think you have to wait a bit in between phases."

    d "Am I important to you?"

    show angel confused
    s "Of course."
    show daisy anxious
    "I gulp."
    show daisy nervous
    show black screen with {'master':Dissolve(1)}

    d"{size=*.8}...Do you...{w=1}{/size}{size=*.6}love me..?"
    "If I look up, and don't see a look of reassurance, I might as well just sink to the ground and die."

    s "{b}Yes.{b}"
    show angel frown
    hide black screen with {'master': Dissolve(2)}
    "Slowly, I lift my head up towards her."
    "This is the most sure Samyaza has been in her life, despite how long it must've been."


    show daisy anxious
    d "Prove it to me."

    s "It might be dangero-{w=1}{nw}"
    show daisy nervous
    d "What if the ritual also harmed me? Maybe...{w=1} maybe I wanted to hurt myself yesterday.{p=1}Because of its effects on me."

    "It's like my mouth is moving on its own. What the hell am I even saying??"
    s "Okay. {nw}"
    show angel happy
    extend "Let's do it."
    #stop music
    #EXT. UNIVERSITY PARK - NIGHT
    play sound crickets_cicadas_looped volume 0.05 loop
    play sound2 wind volume 0.5 loop
    scene black screen
    show daisy anxious at scene_center
    show angel idle at scene_center_offleft, flip
    with Fade(1,2,1)

    #play music wav_pale_moon_bright_eyes
    #[WIND SFX]
    #[CRICKETS SFX]
    "Samyaza interlocks her pinkie with mine, as we walk in the night."
    "Her free hand carries a tote with different items for the ritual."

    show angel frown
    s "You know, usually you shouldn't do this part of the ritual so early on."

    "..."

    show daisy nervous
    d "Sorry."

    show angel happy
    s "It's okay! Our connection is strong. My wings jutted out much more than I expected them to."

    show daisy sappy
    d "Your wings...{w=1} Are pretty..."

    show angel happy big
    s "Even if you only saw them covered in blood?"
    d "Yeah...{w=1} I don't know...{p=1}{size=*.6}I liked them better that way...{/size}"
    show angel happy

    show daisy anxious
    d "Uhm." 
    d "Oh, are they okay though? Like, did you clean them up?"

    s "Don't worry about it! I've been feeling more like myself since we did the first part of the ritual. This second part will be fineeee."
    show daisy idle
    show yuri_park_night behind daisy with dissolve
    "We end up walking to an area behind one of the main buildings."

    s "I like the nighttime down here."
    show daisy surprised
    d "Oh, yeah?"

    s "The crickets, they're always chirping. I think that they're all communicating with each other. I thought that I'd feel that way with going to public places with humans, and hearing them all chat. But, something about crickets..."
    s "It makes me sad, but also happy."
    show angel sad
    s "...Like I'm missing something."
    s "I think that it reminds me of home."
    show daisy upset
    "I stop in my tracks, she walks a bit more forward then comes back to me. The dread that has been stalking me over and over takes over my body entirely."
    show daisy with {'master': moveintop}:
        ypos 2200
    "I sway down to the ground and bite my swollen lips again, same spot as so many times before."

    show angel confused
    s "{b}Daisy!{/b} What's wrong?"

    "She analyzes my body, like she's a nurse examining me."
    "My nose flares up, my breathing ragged as I stare her down."

    
    s "What's going on? Tell me, please? Don't leave me hanging."
    show daisy crying at scene_center with dissolve
    d "{shader=jitter:u__jitter=1.0, 3.0}{size=*.75}Am I not enough?{/shader}{/size}{nw}"
    d "{size=*.75}Am I not enough?{/size}{fast}"
    show angel sad
    s "..."

    d "You don't see me as home?"

    show angel pain
    s "No. It's not like that, it's like-{w=1.0}{nw}" 

    d "Well, what is it like, then?"
    #movement later
    show angel frown at unflip
    "Her breath quickens, she begins to pace around the clearing."

    s "{cps=*3}Well, it's like. Two homes. Humans, they have two homes too, don't they? The home they were born and raised in, then the one they live the rest of their life in. It's like that. Yeah. Like that.{/cps}"

    d "It's not like that for me...{p=1}...You are my home."
    show angel desire at flip
    "Samyaza pets my head. {cps=*3}She's looking at me like she adores me, but I don't believe her. Why would she want to leave? I'm here. Isn't this the same home that punished her, sent her to Earth? Why am I not enough???{/cps}"

    s "I'll make it work. No matter what happens, this ritual will work for the both of us."

    "{cps=*3}No it won't. It's only benefitting her. She's only using me to get what she wants. {b}Is that why she kissed me?{/i} I'm so mad, my breathing is ragged and dizziness overtakes me. I'll show her my mind.{/cps}{p=1.0}I breathe steady breaths in and out."

    show daisy anxious
    d "Okay.{w=1} I believe you."

    show daisy nervous
    "Samyaza's fingers interlock into mine. I can't look her straight in the eye."

    d "Let's get started."
    show daisy crying
    "Gently, she kisses my head. Tears start welling up but {nw}"
    show daisy upset
    extend "I rapidly blink them away."
    show angel idle at scene_left, flip,with moveinleft
    "Samyaza pulls away, slowly and carefully watching me as she does so. Humans must be fragile compared to what she's used to..."
    show sigil_earth with {'master': dissolve}
    "She takes out a bag of salt, and draws a very large circle, encompassing us. Then, she takes out a shovel."
    hide sigil_earth with dissolve
    #[EARTH SIGIL POPUP]
    #[SHOVEL POPUP(?)]
    
    show daisy surprised
    d "Where did you get that?"

    show angel happy
    s "Oh. The apps."

    "I'm too tired to ask. Instinctively, I go up to her and prepare myself to ask if she needs any help. But...{w=1} I'm not a good person...{w=1} {nw}"
    show angel idle at unflip
    extend "I stand and watch her begin to shovel out some dirt."
    show daisy sappy
    "Her muscles gleam in the moonlight, each movement resembles a practised routine. Her chest rises methodically as she works. I play with my hair, there's no point in trying to look away anymore."

    show angel frown
    s "Originally, this step asks for a sacrifice. Usually something temporary. But I couldn't put you through that."

    show daisy anxious
    "..."
    show daisy blush
    "Would being buried by Samyaza be so bad? Imagining it, my final moments being able to lie down, and be taken care of by her..."
    show daisy idle

    d "So what are you doing now?"

    s "We're getting rid of something with heavy energy."

    "After burying a small hole, {nw}"
    show angel at flip
    extend "she gets up, and holds her hand out."

    s "Give me your phone."

    show daisy surprised
    d "But- I have my school stuff on there..."

    s "Do you want this to work?"
    show daisy anxious
    d "...Yes..."

    s "Do you have something else we could use?"
    
    "My scrapbook. {cps=*3}I should hide it when I get home. It's been something I've been doing forever. I guess it would work better, it's something that grounds me and that's probably what we need for the Earth ritual. I'm not that good at doing it anyway.{/cps}"

    "But, my blood is cold with the idea of throwing that away. Swiftly, I handed her my phone."

    #[PHONE POP UP]

    show angel idle
    "She smiles, but it doesn't reach her eye."
    
    "The phone is thrown into the ground, and I watch as heaps of dirt are piled on top of it by Samyaza. "

    show daisy idle
    d "...I feel better without that."

    show angel happy big
    s "That's exactly what I want to hear."

    "She draws another sigil with the coarse salt, then she takes my hand and sits us down at the center of the sigil. {nw}"
    window show
    scene black screen with {'master': dissolve}
    window auto
    extend "She closes my eyes, then joins our hands together."
    #[BLACK SCREEN]
    #[♫YOU ARE PERFECT♫]
    stop music
    stop sound 
    stop sound2
    #play sound "WAV_You_Are_Perfect.ogg"
    #play sound "wav_you_are_perfect.ogg"
    play music wav_you_are_perfect volume 2
    #play sound "audio/Gore/WAV_You_Are_Perfect.ogg"
    #play sound 
    
    #fix music
    "She begins to recite something in that incomprehensible language again. While our eyes are closed...{w=1} I think of the last time. Our tongues interlocking, her sweltering body mixing into mine.{w=1} ...I have to focus."
    "Our hands are clasped together, I want her to be done with reciting for the ritual."
    "Because I can't stop wishing that her hand would slip down my to my thigh, then come up to-{w=1.5}{nw}"

    #show angel frown
    s "Dammit...!"
    scene white screen
    show red screen:
        alpha 0.8
    with dissolve
    #[SCREEN SLOWLY GETS BRIGHTER, TO THE RED COLOR FROM EARLIER]

    "She groans in pain, I'm unsure if I should keep my eyes closed, but I bite my lip. I want to massage her wings again. I want my sweat and her blood to mix together and for us to become one."


    s "Agh...{w=1} Fuck."

    "Samyaza writhes on the ground. I take deeper breaths and bite my lips. She must be sweaty, on the ground and her face contorting in pain. But she only wants to make me feel better, so even though she's hurting so much, she gets on top of me and kisses me. Our tongues would dan-{w=2}{nw}"

    s "Daisy....gghh.."

    "-ce together. We'd then-{w=1}{nw}"

    s "Daisy... help..."
    camera:
        zpos -500
        xpos 100
        ypos -200
    scene white screen
    show angel pain open at scene_center
    show daisy surprised at scene_center_offright
    with dissolve
    "I'm wide awake. Samyaza is engulfed in a blinding aura. Pockets of lights seep through every hole in her body. It looks like daytime."

    play sound screen_shake
    show angel pain closed with vpunch
    s "AAAGGHH..!"


    "Her wings keep contracting in and out, they're unable to reach past the halfway point. {nw}"
    show red screen with {'master': dissolve}:
        alpha 0.3
    extend "Blood soaks the salt circle. The light that emits from her body burns my pupils."

    show daisy nervous
    d "What do I do??!!!?"
    
    "I kneel down to Samyaza, holding her. Letting my eyes be taken over by the blazing light. Her body is sweltering, my hands burn."

    show angel pain open
    s "E...{w=.3}Erase the circle!! Now!"
    show white screen as ws
    show red screen:
        alpha 0.8
    with {'master':dissolve}
    "I dash to the salt. Kicking everything away. Mix it in with the dirt."

    "I trip on myself, and she lets out a large bellow of pain as I do so."
    "I'm not fast enough."
    "{b}I'm not enough.{/b}"
    "It takes too long to clear it away, so I get down on my knees and mix the salt with the dirt to make it disappear. My fingernails quickly change color."

    "As I pant harder and harder, Samyaza's screaming subsides. I rush over to her, shaking her body."
    hide white screen as ws
    hide red screen
    show daisy nervous
    show angel pain open
    with dissolve
    
    d "Samyaza.. Are you okay??"

    "She's too out of it."
    show daisy upset
    d "SAMYAZA!"
    hide white screen
    show yuri_park_night behind daisy, angel
    with {'master':dissolve}
    "The light begins to dim. She stirs."
    
    s "My... wings."

    "I get to massaging them, moving with the same inhuman speed Samyaza has. It's more tender than usual, and the feathers of her wings fall off a lot quicker."
    show daisy blush
    "As she leans her head into the crook of my shoulder, her whines are muffled. I should move my shoulder, I want her to kiss me so badly that I keep licking my lips."
    show angel desire at flip with dissolve

    s "Mmm...{w=1} that...{w=1} felt...{w=1} {b}better.{/b}"
    show daisy anxious
    "{cps=*3}This isn't fair. I wish I was in her position. Why can't she massage me? It would feel so good. I could imagine her warm fingers working through my back, just how good it would feel and-{w=2}{/cps} Wait."
    show daisy nervous
    "{cps=*3}Why am I even thinking this way, she could've died- or whatever would happen to someone like her.{/cps}"
    stop music
    #[♫MUSIC STOP♫]
    #[WIND SFX]
    #[CRICKETS SFX]
    play sound crickets_cicadas_looped volume 0.05 loop
    play sound2 wind volume 0.5 loop

    d "...You should've had another roommate."

    show angel sad
    s "No. It can only be you."

    "It takes someone nonhuman to like me...{w=1} Hah."

    show daisy crying
    d "No, I don't deserve you."
    show angel happy big
    "Samyaza weakly pets my cheek. Her hands are sticky with blood, my face drenched in sweat. Only a nonhuman could find beauty in whatever horrific state my face is in."

    show daisy blush
    d "I...{w=1} {size=*.6}wanted to... kiss you.{/size} Like last time..."
    show angel idle
    show daisy nervous
    show angel frown

    "She doesn't say anything."
    
    d "You should've buried me."
    scene black screen with dissolve
    play music wav_by_your_side
    "She leans in, once again."
    "My mouth feels like it's on fire."
    "Her hand gently holds onto my jaw as she kisses me deeper and more fervently."
    "{cps=*3}More, more, more {b}please{/b}. Go as deep as you can go, Samyaza. I feel her other hand slide onto the small of my back, then grope me underneath my clothes. I let out a small yelp, the most I could do in my current state.{/cps}"
    "{cps=*3}I can't remember the last time someone has touched me like this, and her warm fingers feel so good, so different than anything I've ever felt. It feels so overwhelming, both physically and mentally. Like a drug.{/cps}"
    "{cps=*3}I could barely kiss back, tears mixing in with the sweat. I wish she could just kiss me like this forever. I wish she could take control of me and make me feel things I'm not allowed to feel but I've instead just been...{/cps}"

    "I need to pull myself together."

    "I push away. Burying my face in my hands, my lip quivers as I start to sob."
    "Samyaza softly showers me with kisses."
    "Each one makes me feel so disgusted with myself."
    "My body is glued to the ground."
    "I try to pull away and accept that I don't deserve this.{p=1}But each peck makes me want to lean into her more and more."

    d "...We should get cleaned up."

    "I get up, pull Samyaza up, and help her walk back to the apartment."

    stop music
    stop sound 
    stop sound2

    camera:
        xpos 0 ypos 0 zpos 0
    #INT. DAISY'S ROOM - DAY
    scene room daisy with Fade(1,2,1)
    play music wav_why_did_you_leave
    #[♫WHY DID YOU LEAVE♫] 
    #OR
    #[AC SFX]
    play sound ac_hum volume 0.1 loop

    "Once Samyaza washes up, she tries to talk to me again."
    "But, do I have the right to accept her love?"
    "Fake or not, I've used her for my own sick satisfaction."
    "I'm taking advantage of her."

    "She repeatedly bangs on the door, her hoarse voice begs for me to come out."

    "She bangs on the door once before she leaves for classes."
    window hide
    show black screen with dissolve
    hide black screen with dissolve
    window auto
    "Once she comes back from her classes, she routinely bangs on the door again. "

    "...I didn't even think about her going through all the trouble to apply and register for classes and housing."
    "What's even the point of her going anyways?"

    "She leaves again, no clue why."
    "It can't be her classes..."
    "I'm the only person she talks to."
    "{cps=*3}Has she found another human? Someone better, probably. The idea of that makes me want to puke, but I know I can't control her. {/cps} Even if Samyaza is my entire world, that's probably not the case for her when she thought of me." 

    "After last night, I didn't even shower or eat. I went straight to bed and locked my room. I smell weird and vaguely of blood, but I don't care."
    "Maybe I should shower, but I can't bring myself to get out of bed."

    "I think Samyaza should get Anya."
    "Anya would see it as some sort of school project, and handle it with efficiency."
    "Me, however, I was counting down the minutes for her to get home. "

    "I think...{w=2} I want to see how long I can continue to not talk to her."
    "Hearing her cries from beyond the door makes a flame in my heart blaze."
    "She cries like a dog missing its owner."
    "She whimpers, snivels, and begs for me to talk to her."
    scene yuri_living_room_night with dissolve
    "Tonight, she sleeps by my door..."
    scene room daisy night with dissolve

    "It's extra hot in my room tonight, and I can't bring myself to sleep."
    show black screen
    show angel pain at scene_center:
        alpha 0.5
    with dissolve
    "Everytime I close my eyes, I picture her weeping, all curled up by my door..."
    "Maybe she talks to herself, just hoping I'll say anything."
    hide black screen
    hide angel
    with dissolve
    "I want to be quiet longer.{p=1}I don't want her to stop saying she loves me{p=1}I wish I had my phone so I could record this, and play it back on a neverending loop."

    "She needs me. Even if I'm not good to her...{w=1} If she acts like this when I'm gone for only a day...{w=1} How much longer could I egg this on?"
    show black screen with dissolve
    "This goes on for another day...{w=1} I think? The increasingly growing ache in my stomach is the only way I can tell the passage of time."
    hide black screen with dissolve
    stop music
    #[♫MUSIC STOP♫]
    #[AC SFX]

    "Eventually, on the second night, she heads out again."
    "I wish I didn't need to eat."
    "I can usually handle hunger pangs, but today, something in my body went on autopilot. "


    #[DOOR OPEN SFX]
    play sound door_open
    scene black screen
    #[BLACK SCREEN]
    #[DOOR CLOSE SFX]


    "I force the yogurt down my throat."
    "I miss Samyaza."
    "Please, God.{p=1}If you're working on our side, please make it so that she's not replacing me with another girl."

    #[KNOCK SFX]
    play sound door_knock

    "I don't even feel myself getting up.{p=1}It's like I'm watching myself through the window."
    "I open the door."

    #[DOOR CREAK OPEN SFX]
    play sound door_open
    scene yuri_living_room with dissolve
    "I don't know who I expected to show up."
    show anya upset at scene_right, flip
    show daisy upset at scene_left, flip
    with dissolve
    a "Daisy.{p=1}We need to talk."
    "Oh, God."
    play music couch_fight_scene_v1 volume 2
    #[♫COUCH FIGHT SCENE V1♫]
    d "No.{w=1} We don't."

    #I try to close the door, she puts her hand in the middle. . #cut, readd?
    show anya suspicious
    a "Daisy, what the {b}hell{/b} is going on."
    show daisy anxious
    d "...Have you ever been in love before?"
#sprite
    show anya upset
    "Anya gives me a confused look for a brief moment, and then scoffs at me.{p=1}Good, she's not pretending anymore."

    a "What..?{w=1} Yes, but that's not what this is ab-{w=1}{nw}"
    show daisy upset
    d "You don't understand. You pretend to understand what I go through so you can make yourself feel better about being a part of the group that tore me apart."
    show anya suspicious
    a "Daisy, stop it. Screw your head back on, this is not what I'm talking abo-{w=1}{nw}"
    show daisy angry
    d "Stop talking to me like that! I'm not fucking stupid."

    a "Daisy. {b}Calm down!{/b}{p=1} What the hell is going on with you and your {i}roommate{/i}, you're acting insane."


    "My lips press together as my nostrils flair out."
    show anya upset
    a "You haven't answered any of my calls in two days!"

    "My nails press into my hands.{p=1} I want to tear through every single layer, to feel the bone."
    show anya suspicious
    a "You don't show up to any of your classes, but I see her around campus like nothing happened.{p=.5}Daisy, you need to go to therapy, seriously."
    a "You're not living with your mother anymore- you're in an environment where you can heal.{p=.5}But instead, you're just regressing!"

    d "You're just jealous! "

    a "This is what I mean! Y-{w=1}{nw}"

    show daisy upset
    d "{cps=*2}You'll never understand the love I have for Samyaza, and the love she has for me. You're jealous that something like me can find love.{/cps}"
    show anya upset
    a "{b}No!{/b} No, Daisy, that's not it! Samyaza must be putting some controlling shit in your head or something. Daisy, this relationship is not healthy."
    
    a "...{w=1}Please stay a night with me, we can get you the help you need, I promise! Please I'm just looking out for you as a friend-.{w=3}{nw}"
    show daisy at offscreenleft with moveinleft
    scene black screen with {'master':dissolve}
    play sound door_slam
    "I roll my eyes, go to my room, and slam the door."

    "She never tried helping me while we were in our hometown."
    "All of my cries for help, and all she could do was offer faux sympathy."

    "But...{w=1} she's the only one who stuck with me."

    "I slide down the floor, and weep."
    "I feel her presence on the other side of my door."

    "I cry until I hear the front door creak open and closed."
    stop music fadeout 3
    "Talking to Anya always saps the energy out of me, as my tears dry up, I slowly drift off."
    scene black screen with dissolve
    camera:
        perspective True
        xpos 150 ypos 150 zpos -500
    scene room daisy night with Fade(0,2,1)
    #INT. APARTMENT LIVING ROOM - NIGHT
    #[AC SFX]
    play sound ac_hum volume 0.1 loop
    "I must have forgotten to lock my door."
    "I wake up to a hot hand holding mine, and an embrace like a warm blanket."
    "Stirring, I see Samyaza crouched next to me. Her lips slightly parted."
    #[♫STAY WITH ME♫]
    play music wav_stay_with_me volume 2

    show angel sad at scene_center
    show angel at flip:
        ypos 1600
    show daisy anxious at scene_center_offright
    show daisy:
        ypos 1600
    with dissolve
    s "...Hi."
    show daisy idle
    d "...Hey."

    s "I missed you."
    show daisy upset
    "My lips quiver.{p=1}I try to keep myself together, {nw}"
    show daisy crying
    extend "but the floodgates burst. I cover my face and start sobbing uncontrollably."

    s "No.. Daisy, sweet Daisy."
    show angel happy
    "She pets my head."
    "I lean into her touch.{p=1}No more resistance."

    s "My Daisy, I missed you.{p=1}Please, tell me what's wrong." 

    "I open my mouth but I can only let out hiccups."

    "Where do I even start?"

    d "I...{w=1} I'm terrible."

    show angel sad
    s "No, the world has been hard on you."
    show angel desire
    s "I can ease your pain, Daisy.{p=1}I promise you'll never feel sad, or lonely ever again."

    "I cry even harder. With a free hand, I grab her wrist that's petting my head, and press it down further."
    show angel happy
    s "Silly girl, what are you doing?"

    show daisy sappy
    d "I wish you could reach through my body."

    show angel frown
    s "Ah... Right, humans can't do that. Huh."

    show daisy surprised
    d "Angels can? "

    show angel happy big
    s "Yes. "
    show daisy anxious
    show scrapbook_inspect with {'master': dissolve}:
        xpos 150 ypos 150 zpos -500
    "As my lips tighten, I look around and notice my scrapbook under Aza's arm."
    show daisy nervous with {'master':moveintop}:
        ypos 1500
    hide scrapbook_inspect with vpunch

    "I jump up, my shoulders stiffening."
    show daisy angry
    d "What is {b}that{/b} doing here?"

    show angel sad
    s "...I wanted to find something that made you happy."


    "I need to lock my door next time I leave the house."
    "I don't like the idea of her looking through my stuff."
    show daisy anxious
    "Maybe...{p=1}Maybe Anya was right."
    "Not entirely- Anya doesn't understand Samyaza like I understand her, but she needs to be gently taught that she can't do these things."
    "She's not from here, after all."
    "I should tell her."

    d "Anya and I got into an argument."

    show angel scary
    s "What happened?{p=1}{nw}"
    show angel sad
    extend "Tell me, please."
    show daisy with {'master':moveinbottom}:
        ypos 1600
    show daisy anxious
    d "I don't know, she doesn't like you. She's so obsessed with bringing my past up, connecting it to everything I do-{p=.3}It's like she held onto it harder than I have."

    show angel sad
    s "How could she say such hurtful things?"

    show daisy nervous
    d "Well...{w=1} I guess...{w=1} I was kind of mean, too."

    "I curl into myself, pressing my head into my knees."
    show angel frown
    s "{b}No.{/b} You were defending yourself."
    show daisy surprised
    #Curiously, I face her.

    d "I guess? I don't really think...{w=1} I've {i}done{/i} that before."

    "I was right. Anya doesn't know what she's talking about.{p=1}Samyaza has given me a sense of strength that she could only wish to have."

    show angel frown
    s "She wants to keep you down. Keep you weak and easy."

    show daisy anxious
    d "...{w=1}Yeah...{w=1} I think...{p=1}I think she's jealous."

    s "Of course she is. Daisy, don't {i}ever{/i} feel bad for speaking up for yourself. This Anya, she's only been causing you problems, haven't you noticed? Every time you're with her, you end up upset."

    d "{size=*.75}Yeah...{/size}"

    
    s "She reminds you of bad times, doesn't she?"

    show daisy surprised
    d "..."

    s "She was in the orbit of your ex-friends.{p=1}The ones that treated you like you were a monster."

    
    d "...{w=1}How do you know that?"

    s "She was a bystander to them, to your mother.{w=1} And now she's trying to act like she cares about you."

    show daisy upset
    d "...{w=1}She was..."

    s "What right does she have to talk about {b}us{/b}, then?"

    show daisy blush
    d "..."
    #pink?
    show angel desire
    "Samyaza kisses me on the cheek."
    show daisy anxious
    d "Do you think I did something wrong?"

    show angel frown
    s "No. Never."
    show daisy nervous
    d "Do you think I've been bad?"
    show angel happy
    s "God brought us together. How could the Holy Father bring me to someone who is wicked?"
    show daisy crying
    d "{shader=jitter:u__jitter=1.0, 1.0}{size=*.75}Can you...{w=.5} tell me how I've been... {/shader}{/size}{nw}" #fix history later
    d "{size=*.75}Can you...{w=.5} tell me how I've been... {/size}{fast}"
    show angel desire
    s "You've been so good, {i}my sweet Daisy.{/i}"

    "I sniffle. I can't hold back the tears."
    "I look like such a mess.{p=1}My hair is unwashed and snot is dripping from my nose.{p=1}And yet, she still looks at me like I'm the most beautiful thing she's seen."
    "...She makes me believe that I am."
    "Samyaza hugs me tight."

    s "I'm so happy to have you back. I went {i}insane{/i} without you."
    show daisy sappy
    "I lean into her hug. I could die in her arms."
    stop music fadeout 2.0
    stop sound
    #[♫MUSIC FADES OUT♫]
    scene black screen with dissolve
    camera:
        xpos 0 ypos 0 zpos 0
    scene yuri_classroom_01 with Fade(0,2,1)
    #INT. CLASSROOM - DAY
    #[♫LOVE YOU LOVE ME♫]
    play music wav_love_you_love_me
    "I don't see the point of going to class anymore. But Samyaza insists we go together."
    show daisy idle at scene_center_offright
    show angel idle at scene_center_offleft,flip
    with dissolve
    "We sat all the way in the back of the classroom, not taking notes."

    s "I want to experience school for a little bit more, until I turn back."
    show daisy anxious
    "I tune her out for a little.{p=1}It's been so long since I've been in class that the lesson feels like gibberish. "

    s "I've always watched the humans I've taken care of go to school.{p=1}It's funny, everything is so different now that I'm here."

    show daisy surprised
    d "In a bad way?"

    show angel confused
    s "I honestly...{w=1} don't know?{p=1}Every day, my body hurts, and my mind feels like it's going to explode. But..."
    show angel desire
    "Tilting her head, she walks her fingers over to me."
    show daisy blush
    s "It's okay.{p=1}Because you're here."

    "I bring my finger to hers.{p=1}Holding it tight."

    show daisy anxious
    d "...{w=1}Can we wait until tomorrow to do the water one..."

    s "Mhm."
    show daisy sappy
    "Mindlessly doodling, I look over to her.{p=1}Strands of hair gently fall on her face as she presses her cheek onto the desk.{p=1}She's taking notes. "

    show daisy surprised
    d "...{w=1}You don't need to do that, y'know.{p=1}...The notes, I mean."

    show angel sad
    s "I won't get to do it again...{w=1} So..."

    show daisy anxious
    d "I guess.."
    show angel idle
    show daisy anxious
    "I lean into my seat. Class is so boring, but I'm not even looking forward to it ending.{p=1}Am I looking forward to doing the next steps?{w=.5} Probably not.{p=.5}Maybe I should just pay attention."
    show angel desire
    s "The water ritual will be a bath."

    show daisy surprised
    "..?"
    show angel idle
    s "With elixirs. I've been collecting some."

    "Right, when she was leaving the house."
    show daisy anxious
    d "Oh."

    show angel desire
    s "We'll have to get in together."
    show scrapbook_inspect at scene_center with dissolve
    show daisy blush
    "I take my scrapbook and cover my face."
    hide scrapbook_inspect with dissolve

    d "{shader=jitter:u__jitter=1.0, 3.0}{size=*.75}{b}Like...{w=0.5} naked???{/b}{/shader}{/size}{nw}"
    d "{size=*.75}{b}Like... naked???{/size}{fast}{/b}"
    show angel happy
    s "Preferably. There might be some interference if you're clothed."
    show daisy nervous
    "We've already kissed...{w=1} but...{w=1} the idea of her seeing my body makes me want to rip my skin off."
    "What if it's the final straw?{p=1}If God doesn't accept me in this form, why would an angel?"

    show angel frown
    s "For fire, you have to burn something important to you.{p=1}To let go."

    "... I don't want to do that."
    show daisy upset
    d "{shader=jitter:u__jitter=1.0, 3.0}{size=*.75}Is it too late to stop...{/shader}{/size}{nw}"
    d "{size=*.75}Is it too late to stop...{/size}{fast}"
    show angel confused
    s "Huh? What did you say?"

    d "...Nevermind."

    
    #EXT. UNIVERSITY PARK - DAY
    scene yuri_park_01
    show daisy idle at scene_right
    with Fade(1,2,1)
    "The air is crisp. It's beginning to cool down.{p=1}I wish Samyaza could stay long enough so she could feel the cold air hitting her skin on a fall day." #Or to feel the snow.

    
    stop music fadeout 1
    au "Daisy!"
    show anya idle at scene_left with moveinright
    #[♫MUSIC STOP♫]
    #[WIND BLOWING SFX]
    show daisy nervous
    "...Not again."
    show angel scary at scene_center with dissolve
    "Before I can even respond, Samyaza comes in between us."
    #[♫STRANGER♫]
    play music wav_stranger
    play sound wind
    s "Daisy, is she bothering you?"
    
    "I.. don't know what to do."

    show anya upset
    a "Daisy, I saw you walking around, I just...{w=1} I just wanted to make sure you were okay."
    show anya suspicious
    "She shoots Samyaza an interrogative gaze. {nw}"
    show anya idle
    extend "But she makes sure to look back at me."

    d "I've b-{nw}"
    #SAMYAZA [cuts out last textbox]
    show angel obsessed
    s "{b}She's fine.{/b}"

    show anya suspicious
    a "I'm not asking {b}you.{/b}"
    show anya idle
    a "Daisy, I'm glad to see you back in classes."
    show daisy upset
    "I look over to Samyaza, unsure what to do."

    
    s "If she hasn't answered your texts, maybe she doesn't want to talk to you, have you thought of that?"
    show anya happy
    a "Why don't you let {i}Daisy{/i} answer."

    show daisy nervous
    show angel frown at flip
    show anya idle
    d "Uhh..."
    
    "Both of them stare at me.{p=1}Anya's gaze makes my chest feel heavy.{p=1}Even when she's trying to \"help\" me, I still feel like she's judging me, scrutinizing me for being {b}weak. {/b}"

    show daisy idle smile    
    d "I'm fine. Anya, could you please leave us alone?"

    show anya upset
    a "Well...{w=.5} if that's what y-{nw}"
    show daisy anxious
    show angel scary at unflip
    s "Haven't you realized that {i}you{/i} might be the reason that she's not doing well?"

    "Anya closes her eyes, and takes a deep breath.{p=1}She hesitates before giving her response."

    show anya idle
    a "Ok. I'll respect that."
    show anya at flip
    "She turns away, {nw}"
    show anya upset with {'master':moveinleft}:
        xoffset -200
    extend "and begins to walk off. {nw}{w=1}"
    show anya upset at scene_center_offleft, unflip with {'master':moveinright}
    extend "Until, suddenly she runs back towards me."

    a "Daisy, let's talk one last time.{p=1}{nw}"
    show daisy surprised
    show anya suspicious
    extend"Without her.{p=1} {nw}"
    show anya idle
    extend "Meet me here tomorrow, okay?"
    show angel frown
    show daisy nervous
    "Samyaza grips my shoulder.{p=1}{nw}"
    show angel scary
    extend "She scowls at Anya so intensely that some nausea wells up within me."
    show anya upset at flip with {'master':moveinleft}:
        xoffset -800
    "Anya walks off again.{p=1}Guess she didn't care about my answer."
    show angel frown at flip
    s "She's such a bad influence on you. I hope you never see her again."

    d "..."

    s "You're better off without her.{w=.5} I mean it.{w=.5} She's not good for you.{w=.5} All she does is make you doubt yourself.{w=.5} {i}She doesn't treat you like a human being.{/i}"

    stop music fadeout 2
    scene black screen with Dissolve(2)
    #[♫MUSIC STOP♫]
    #[♫WIND SFX♫]
    play sound wind volume 0.5 loop


    "The walk back is silent. Occasionally, Aza asks me questions about human experiences."

    "Honestly, everything since that confrontation is a blur.{p=1}Did I answer Aza's questions correctly?{p=1}To her, everything I say is perfect."

    "Anya...{w=1} she's been such a sore spot for me for so long, but not having her in my life fills me with an indescribable feeling.{p=1}Some kind of bitterness, maybe- but anytime I try  think about it, I feel hot tears threaten to burst."
    scene black screen with Dissolve(1)
    #[FADE TO BLACK]
    scene white screen with Dissolve(1)
    #[FADE TO LIGHT]
    scene yuri_park_01
    show white screen:
        alpha 0.3
    with Dissolve(2)
    #EXT. UNIVERSITY PARK - DAY [a bit brighter to indicate morning?]
    #[♫WIND SFX]
    show anya idle at scene_right,flip
    with dissolve
    "Anya's waiting on a bench.{w=1} She looks peaceful, looking up at the tree, illuminated by the early morning light."# Her face is resolute.

    show daisy anxious at scene_left,flip with dissolve
    d "Hi..."

    show anya upset
    a "Hey.{p=2}...We need to talk."

    show daisy idle
    d "About what?"

    show anya suspicious
    a "The way you've been...{w=1} you know."

    show daisy surprised
    d "What about it?"

    show anya upset
    a "You talk about being in love and whatnot-{w=.2} look, I'm happy for you, {i}really.{/i1}"

    show daisy idle
    d "And..?"

    play music couch_fight_scene_v1 volume 2
    show anya suspicious
    a "Listen, I keep saying this, but you're really freaking me out. You're isolating yourself, you look like shit, I don't know, I'm just worried...{w=1} It feels like you might be...{p=.3} relapsing."

    "I sigh, rolling my eyes."
    
    d "And, so what? {w=.5}{nw}"
    show daisy upset
    extend "What if I was relapsing? What would you do? {nw}"
    show daisy angry
    extend "{cps=*2}I'm happier than I've ever been! Are you saying I look like shit when I'm happy? {size=*1.5}What the {b}hell{/b} do you want from me?{/size}{/cps}"

    show anya upset
    a "Daisy, you don't have to get so defensive!{cps=*2} A week ago you literally had a bandage on your wrist, how am I not supposed to get freaked out? You're acting like {/cps}how you did...{w=.5} once the friend group cut you off...{w=.5} And honestly, I don't think Samyaza is helping much!"

    d "{cps=*3}You always have to go back to that! It's in the past! And you don't know {i}shit{/i} about how I was back then! You were barely there for me! Unlike Samyaza, {i}she{/i} has a sixth sense for me.{/cps}"

    a "I know... And for that I'll forever be sorry."
    show anya suspicious
    a "But I can't lie to myself. You look like you're slipping back into... into whatever place you were in, back then.{w=2} I failed you before, Daisy, I don't want to fail you again."

    show daisy crying
    d "{size=*2}{b}I DON'T NEED HELP!{/b}{/size}"
    show anya upset
    window hide
    pause 2.0
    window auto

    a "{b}Daisy!{/b} Daisy, calm down! I'm not trying to attack you!"
    show daisy upset at unflip
    #"I sulk, looking away from her."

    d "She...{w=3}{nw}"
    show daisy idle
    "I purse my lips before I can say anything. I squeeze my fists tight as I try to find the words for my feelings."
    show anya suspicious
    a "She... ?"
    show daisy anxious at flip
    d "...{w=1}She promised to ease my pain...{p=1}...She said I don't have to be lonely anymore."

    show anya upset
    "I watch Anya sigh, and roll her eyes.{p=1}Does she respect me at all?{p=1}Respect my choices?{p=1}Does she even consider me human?"

    show daisy idle smile
    d "It's okay! You've clearly never felt love like this, and I feel so sorry for you."

    show anya suspicious
    a "..?"

    d "You've only ever had that one ex-{i}boy{/i}friend. The {b}cheater.{/b} {i}He didn't really love you, so you'd never understand.{/i}"
    show anya upset
    "I don't {b}care{/i} if that's low hanging fruit.{p=1}She's done it to me so many times before.{p=1}{b}Poor little Anya{/b} will live."

    
    a "Daisy, what the fuck!"
    show daisy surprised
    show black screen behind daisy with Dissolve(3):
        alpha 0.4
    "I'm caught slightly off guard- She's actually angry, for once."
    "I'm so used to her sucking up to me, playing the role of my fucking social worker.{p=.5} I rarely see her show an emotion that isn't passiveness or faux-niceness.{p=.5} My rottenness brings out this side of her, I guess." 
    show daisy pain and sweat
    "I flinch for a second."
    hide black screen
    show red screen behind daisy:
        alpha 0.7
    with Dissolve(3)
    show daisy angry
    "Fuck it.{p=1}I'm all in.{p=1}This is {b}my{/b} fucking grave and I'll dig it as deep as I fucking want." 
    hide red screen with dissolve
    show daisy idle
    d "I feel sorry for you, really"

    show anya suspicious
    a "You're insane. You did not need to bring that up."
    show daisy angry
    d "{cps=*3}I'm insane for bringing it up, when you love putting me back to the worst years of my life!?{/cps}"
    show anya upset
    a "That's because I'm fucking {b}worried{/b} about you, alright!? {w=.5}I don't want you to fall back into that space. What about that is so hard to understand?"

    d "{cps=*.25}If you were so worried, where were you before?{/cps}"

    "She sighs.{w=2} It's too late for her to back out now."

    show anya suspicious
    a "I've failed you before.{w=1} I know.{w=1} Daisy, I don't know how to get you to believe me when I say how sorry I am."

    d "{b}No.{/b} You only help me when it makes you {i}look good.{/i} If you {i}really{/i} cared you, would've actually stuck around to support me. Where the {b}fuck{/b} were you after high school."

    show anya upset
    a "You're acting like your mother."

    show daisy idle
    d "There it is."
    a "...What."

    d "This whole fucking friendship bullshit between us, it was just an act, right? You don't care, you never did."
    show anya suspicious
    a "...{w=2}And do you believe that?"
    show daisy upset
    show red screen behind daisy with Dissolve(7):
        alpha 0.5
    d "Yes.{i}I always have!{/i} Since the beginning. Every {b}single{/b} thing that you've done and said for me has been backhanded, and I'm not even talking about when we were in high school!"
    d "The past few weeks, all you've been doing is reminding me about just how stunted my fucking life is, with how much you just bring up shit that doesn't fucking matter!"
    d "You don't listen to me, at ALL! Anytime you talk to me, it's just about what YOU did or what YOU think about MY situation!"
    d "Have you even thought about letting me speak for myself, or would that ruin your image of me as some helpless little bitch that needs to be coddled all the fucking time?"
    d "Do you think I exist to make you {i}look better{/i} to all of your {b}dumbass{/b} friends that talk about how much of a mental case I am?"
    show daisy angry
    "{cps=*2}{b}God, I'm so fucking sick of you!{/b} I'm the happiest I've ever been in my life and it's because I'm with Aza and because stopped talking to {size=*2}you.{/size} {/cps}"

    show anya happy
    a "Okay."
    window hide
    pause 1.0
    window show
    show daisy upset
    "My breathing rags as I stare her down, waiting for her to continue.{p=1}She just sits there, unreadable."

    show anya upset at flip
    hide red screen with {'master':dissolve}
    a "...I'm done with this. {nw}"
    show anya upset at unflip

    extend "You clearly aren't taking me in good faith."

    show daisy angry
    d "You're proving me right!"

    "She doesn't even look at me. {p=1}{nw}"
    show anya at offscreenright with moveinleft
    extend "She gathers her things, and walks away."
    stop music fadeout 3
    #[♫MUSIC FADE OUT♫]
    #[WIND SFX AFTER FADEOUT]
    play sound wind

    show daisy idle
    "A crisp wind blows past me." 
    "I watch her go further and further into the horizon."
    show daisy pain and sweat
    "My entire body {cps=*.1}constricts{/cps} as an intense wave of nausea washes over me."



    #INT. APARTMENT LIVING ROOM - NIGHT
    #[AC SFX]
    scene black screen with Dissolve(2)
    scene yuri_living_room_night with {'master': Fade(0,3,2)}
    stop sound
    play sound ac_hum volume 0.1 loop
    "The past few hours had melded together in my mind."
    "I don't know if I stood there in that park for hours, or absentmindedly attended class."
    "I don't even know. Some moments I feel anxious, and other times I feel nothing at all."
    "I just feel numb."

    "I guess Samyaza and I are doing the water ritual today."
    "The muffled sounds of water flowing can be heard from the bathroom."
    show daisy anxious at scene_right with moveinleft
    "I slouch into the dining room.{p=1}Staring up into the ceiling I just.{w=5} Wait."

    "My mind feels like it's betraying itself. Every time I play back the fight from earlier, it's like some third party comes in and {b}scribbles it out.{/b}"
    play sound door_open

    #[DOOR OPEN SFX]
    #[♫STAY WITH ME♫]
    play music wav_stay_with_me
    show angel confused at scene_left,flip with dissolve
    s "Hey, where were you?"

    d "..."
    show daisy nervous with None
    show angel behind daisy
    show black screen behind daisy
    with {'master': Dissolve(2)}

    "Would Aza get mad if I told her the truth?{p=.5}I feel like I shouldn't.{p=.5}She was defending me, telling me Anya would just hurt me.{p=.5}She was right..."
    "I should just lie."

    window hide
    pause 3.0
    window auto
    hide black screen 
    show daisy anxious
    with dissolve
    d "...{w=1}{size=*.4}I was with Anya.{/size}"

    show angel scary
    s "Really?"
    show daisy nervous
    "I hunch in on myself."

    #DAISY [neutral]
    show daisy idle
    d "Uhm.{w=1} Sorry."

    #SAMYAZA [scary]
    s "{b}Make sure you don't see her again.{/b}"
    show daisy anxious
    d "...{w=1}{size=*.4}Okay.{/size}"
    show angel frown
    
    s "I don't want her upsetting you ever again."

    d "...{size=*.6}Okay.{/size}"
    show angel desire at scene_center_offright with {'master': moveinright}:
        xoffset -100
    "She walks over to me, and kisses my forehead."

    s "{i}I{/i} like happy Daisy."
    show daisy idle
    #[daisy neutral sprite.]

    show angel idle
    s "Also, I need happy Daisy.{p=1}The bath is ready."
    show daisy nervous
    "I clutch my cardigan.{p=1} I knew it was going to happen, but I don't feel ready."

    d "...{size=*.6}Do I have to go naked..?{/size}"

    show angel frown
    s "Do you want the spell to work?"

    "{b}No.{/b}"# I don't."

    show daisy idle
    d "{size=*.8}I guess..."

    #INT. BATHROOM - NIGHT
    scene yuri_bathroom_01
    show black screen:
        alpha 0.3
    show daisy anxious at scene_right_far
    show angel idle at scene_center_offright, flip
    with Fade(1,1,1)
    camera:
        perspective True
        ease 3.0 zpos -700 xpos 450 ypos -250
    window hide
    pause 1.0
    window auto
    "Samyaza undresses first."

    show angel desire 
    s "I'm okay with waiting. I'll wait as long as I need."

    d "No...{w=1} It's ok."

    "I begin to take my cardigan off, but when I get to my shirt, {nw}"
    show daisy surprised
    extend "I feel Samyaza beginning to take it off me."
    show daisy blush
    
    s "Let me help."
    show daisy upset
    "My heart is crawling out of my chest. Tears well up."
    show angel confused
    s "Should I stop?"

    d "{size=*.7}...No. Go ahead.{/size}"
    show angel desire
    "Gently, she takes my shirt off.{p=1}Admiration fills her eyes, like I'm the most beautiful girl in the world."
    show angel happy
    "We take off my skirt together.{p=1}{nw}"
    show daisy nervous at flip
    "I look away, biting my lip once it's off. Bracing myself for a comment."
    window hide
    pause 1.0
    window auto
    show angel desire
    
    s "...You're so beautiful, Daisy"
    show daisy crying at flip
    "My eyes must be faulty, water uncontrollably leaks out.{p=1}She wipes my tears."
    show purple screen with Dissolve(1):
        alpha 0.3
    show daisy idle
    "We head into the warm bath.{p=.3}I notice a slight purple sheen."
    show daisy idle smile
    "I splash the water a bit. The candles from the first ritual are lit up, {nw}" 
    show sigil_water at center with {'master': dissolve}:
        zpos -700 xpos 450 ypos -250
    extend "and there's a sigil drawn on the tiles."
    hide sigil_water with dissolve
    
    show angel idle closed eyes
    "Samyaza does the usual- speaking in the strange language, starting the ritual."

    show daisy anxious
    d "Is there anything else we need to do?"

    show angel idle
    s "Not really, this is the preparation for the next step."
    show angel idle closed eyes

    show daisy idle
    d "Ah."
    #show daisy with moveintop:
    #    ypos 1800
    show daisy at flip
    "I sink into the water." #{p=1}It covers half of my face. 
    show angel desire
    s "We can clean each other up, though.{p=1} Here, use this."

    "She grabs a waxy substance, and starts rubbing it on my back. {p=.5}{nw}"
    show daisy sappy
    extend "I sink into her.{p=.5}I can't see her face, but cheeks feel warm as she rubs my back."

    d "This is nice..."

    "She doesn't say anything, and just keeps cleaning me up.{p=1}The smell of herbs and the warm water make my eyes begin to flutter shut."
    show daisy blush
    "Every time I feel like I'm going to fall asleep, she touches the small of my back, or cleans a sensitive area near my chest. "
    show daisy at unflip
    show angel idle wings behind daisy at unflip with dissolve
    "After she's done, she starts cleaning herself.{p=.5}I lay back and watch.{p=.5}Will her final angel form be any different?{p=.5}I hope she looks the same."

    show daisy sappy
    d "...{w=.5}I can clean your wings."

    show angel happy wings 
    s "It's okay, I got it."

    show daisy blush
    d "No, really, I really want to."
    show angel idle wings 
    "She holds the wax away from me, but I reach up and grab it.{p=1}Our movement splashes water onto the floor mat."
    show daisy sappy
    "I take a glob of the substance and start to massage it into her half grown wings.{p=1}There's some dried off blood on spots that would be easy to miss."

    show angel frown wings
    s "Really, Daisy, I could've done it."

    show daisy happy
    d "Nope. It's my turn~"
    show angel desire wings
    "Her breathing becomes uneven as I rub her wings."

    show daisy sappy
    d "They're so sensitive."

    show angel pain wings
    s "...{w=1}{size=*.75}They hurt...{/size}"

    "I keep massaging.{p=1}{nw}"
    show daisy blush
    extend "She softly whines."

    show daisy idle
    d "...{w=.5}When you go back to heaven, you'll have no one to do this for you."

    show angel sad wings
    s "..."
    show daisy anxious
    d "...{w=.5}I wish you'd stay.{p=1}...I could spend the rest of my life doing this."

    show angel frown wings
    s "Daisy, You can't have that mindset while doing this."

    show daisy nervous with {'master': moveinleft}:
        xoffset 100
    "I pull away."

    show daisy upset
    d "Why not?!"
    show angel idle wings at flip
    "Samyaza contemplates, then {nw}"
    show angel desire wings with {'master': moveinleft}:
        xoffset 100
    extend "smiles at me. {p=.5}She leans in for a kiss.{p=1}It's not as inviting as the last ones.{p=2}I don't kiss her back."
    show angel idle wings
    show daisy idle
    s "..."


    d "..."

    #SAMYAZA
    show angel happy wings
    s "I think we're clean enough.{w=.5} Let's get out."
    scene black screen
    #[BLACK SCREEN]
    #[WATER DRAIN SFX]
    #[♫MUSIC FADE OUT♫]
    play sound water_draining

    stop music fadeout 2

    #INT. APARTMENT LIVING ROOM - DAY
    #[AC SFX]
    play sound ac_hum volume 0.1 loop

    scene black screen with Dissolve(1)
    camera:
        xpos 0 ypos 0 zpos 0
    scene yuri_living_room 
    show daisy anxious at scene_center
    with Fade(0,4,1)
    "Samyaza is out on one of her supply runs again."


    #ohhh my god
    show black screen behind daisy with dissolve:
        alpha 0.1
    show daisy nervous
    "Why doesn't she invite me?"
    show black screen behind daisy with dissolve:
        alpha 0.2
    show daisy crying
    "Did I upset her last night?"
    show black screen behind daisy with dissolve:
        alpha 0.3
    show daisy nervous
    "{cps=*3}I keep replaying it in my head, scared that the whole Anya thing set me on edge, that I finally pushed Samyaza out.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.4
    show daisy idle
    "{cps=*3}But, isn't this what I expected?{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.5
    show daisy anxious
    "{cps=*3}This is what I've always hypothesized would happen if someone becomes involved with me.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.6
    show daisy pain and sweat
    "{cps=*3}They'd get close enough to see within me, see my rotting core.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.7
    show daisy nervous
    "{cps=*3}They hear my heart, it doesn't beat like normal people's hearts, it squelches.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.8
    show daisy angry
    "{cps=*3}It's disgusting, once you open me up that's when you smell the stench.{/cps}"
    show black screen behind daisy with dissolve:
        alpha 0.9
    show daisy crying
    "{cps=*3}Samyaza smelled it, she realized I'm too much for her.{/cps}"

    window hide
    pause 1.0
    window show

    show daisy nervous
    hide black screen with Dissolve(3)
    "I pace around the living room.{p=.5}Or, she could just be doing private angel stuff?{p=.5}Who the hell am I kidding, maybe she wants to sacrifice me?{p=.5}...That doesn't sound as bad."

    play sound door_knock

    show daisy surprised at flip, scene_right, with {'master': moveinright}
    "I whip my head around, and run to the door."

    #[CREAK SFX]
    play sound door_open

    show daisy happy at flip, scene_center_offright, with {'master': moveinleft}
    d "Samyaza!"


    show daisy upset
    "...Oh."
    show anya idle at flip, scene_right_far with dissolve
    a "...Hey."
    #[♫FOUND YOU♫]
    play music wav_found_you
    show daisy angry
    "I try to close the door, but she stops it with her foot."

    show anya upset
    a "I think...{p=1}I think I owe you this."


    show daisy surprised
    d "...What is it?"

    show anya suspicious
    a "I...{w=1} how do I put this..."
    show anya upset
    "She loudly gulps."

    a "{cps=*3}I think we should take some time apart.{/cps}"
    show daisy upset at scene_center with {'master': moveinleft}
    "...What..?"
    show anya suspicious

    a "...I want you in my life, Daisy.{w=.5} But right now, the things you've said to me are unacceptable.{w=.5} And honestly, I don't know if {i}you{/i} want {i}me{/i} in your life."

    d "What...{w=1} are you saying..?"


    a "I already told you. We need to spend some time apart."
    show daisy anxious at flip
    "I stand there.{p=1}Unable to move."
    show daisy nervous 
    "I'm sick, I want to puke.{p=1}I just blink at her."
    show daisy upset
    "My throat is dry.{p=1}I can't yell. "

    show anya upset at scene_center_offright with {'master': moveinleft}
    a "But...{w=1} I wanted to give you these."
    show pamphlet_inspect with {'master': dissolve}

    "She hands me support group pamphlets."
    show daisy angry

    hide pamphlet_inspect with dissolve

    "Are you...{w=1} serious?"
    show anya suspicious
    a "Daisy. You need serious help, and you need to stay away from Samyaza.{w=.5} But, I can't control you. I think this is the most I can do now."
    show daisy upset
    "The pamphlets fall from my hand. I don't have the strength within me to grab hold of them."

    
    d "I..."
    show anya upset
    a "I'm sorry, Daisy."
    show anya upset at scene_center, unflip with {'master': moveinright}:
        xoffset 1200
    "She walks off.{w=.5} Again.{p=1}She doesn't even close the door."
    stop music fadeout 2
    window hide
    pause 0.5
    window show

    "The cool air brushes into the house."
    window hide
    pause 0.5
    window show
    "I stand there for... I don't know how long."

    play music wav_you_taste_so_good
    show black screen behind daisy with {'master':Dissolve(2)}:
        alpha 0.5
    d "{cps=*.6}My heart feels like stone. I feel so much pressure within myself, it's like my entire body is going to turn in. Like a black hole."
    show daisy at flip
    "I guess this is what I deserve.{w=.5} It always ends like this with me.{p=.5}Showing her who I am horrified her."
    show daisy surprised
    show pamphlet_inspect with {'master': dissolve}

    "I look down. The pamphlets are all for some mental health service on campus. Slowly, I pick one up, and look it over."
    hide pamphlet_inspect with {'master': vpunch}

    play sound paper_rip 

    show red screen:
        alpha 0.5
    hide black screen
    with dissolve
    #[RED PULSATING SCREEN idk what its called eri u know] #i wish i could do a pulse so bad i need fucking time
    show daisy anxious
    "At some point, the suffocating dread that has been stalking me for...{w=.5} God knows how long, comes back. I don't like Anya. She's not good for me. She's not. She's just doing this shit to keep up appearances. That's all she's doing."
    
    "I pick up one of the pamphlets, and skim through it carelessly. Picture-perfect people smiling and laughing at each other. Bright colors and friendly, inoffensive text..."
    show daisy angry with None
    show red screen:
        alpha 0.2
    with dissolve
    "Like a rubber band snapping. I rip the pamphlet into as many pieces as I can. The pieces of paper are flying everywhere out the doorway.{b} I don't care.{/b}"
    show daisy upset
    "At some point, I hear a slam. ...The door, maybe? My throat feels coarse and dry... Did I scream? I can't tell. I'll deal with it later."

    hide yuri_living_room
    hide red screen
    show yuri_living_room_torn behind daisy
    with Dissolve(2.0)

    "At some point, the amount of ripped paper at my feet increases."
    "Paper towels. The painting in the living room. I feel some unbearable itch being scratched by destroying and ripping anything, but as soon as it goes away it comes right back to my mind."
    "I just keep ripping. Junk mail. Old textbooks. Syllabuses. Random pamphlets. I don't care about the mess, I'll clean it up later."
    show red screen:
        alpha 0.2
    with Dissolve(3)
    show black screen with {'master': dissolve}
    "I lay down, panting. The room is a mess. My breath is uneven. How long has it been?{w=.5} I don't care, I don't care. The itching in my brain subsides."
    show daisy nervous at scene_center with dissolve
    "What would Samyaza think of this?"
    show daisy pain and sweat
    "I'm too tired to care. If she comes back. If she hasn't left me yet, she will now."
    show daisy anxious
    "I crawl up to the couch, and lie down."
    
    "{cps=*3}My entire body feels fuzzy, like when my hands fall asleep, but it's my entire body. Why did I react that way in the first place? I stare at the ceiling. Have I gone to class? Have I done my assignments? I don't know. I don't care.{/cps}"
    "I wonder how many messages my phone has gotten since we buried it?{p=1}...Probably more of just Anya. {b}Being herself.{/b}"
    show daisy nervous
    "I know I should clean this mess up. I can't let Samyaza come back to this."
    "{cps=*3} She already has so many things to do, and she even shows up to her classes which is more than I've ever done and I'm the one that has to get a degree here and not her.{/cps}"
    show daisy pain and sweat
    "Both my mind and my body feel like they're running on empty.{w=1} I physically can't stand back up.{w=1} All I can do is stare at the ceiling and fail to form a complete thought."
    play sound door_open

    #[DOOR OPEN SFX]
    #[♫MUSIC STOP♫]
    stop music fadeout 2
    #[WHITE NOISE SFX]

    play sound white_noise volume 0.5 loop

    s "Daisy? Are you alright?"
    scene yuri_living_room_torn
    show daisy anxious at scene_center,flip
    show angel pain open nowing at scene_right
    with {'master': Fade(1,2,1)}
    "I get up groggily.{p=.5}I should've cleaned this mess.{p=.5}I guess time eluded me."
    show angel pain open nowing at scene_center_offright with {'master': moveinright}
    "Samyaza runs towards me, petting my cheek.{p=.5}She's sweating. Her veins are glowing and her eyes look bloodshot."
    #[♫DISSOCIATION♫]
    play music wav_dissociation
    s "{cps=*2}What happened? Daisy?! I shouldn't have left. I'm so sorry.{/cps}"
    show daisy pain and sweat
    "I should ask about her.."
    show daisy idle
    d "I'm okay. Everything's okay"
    
    s "No, it's not. I failed you."
    show daisy anxious
    "She caresses my face with such intensity.{p=.4}She refuses to let go for even a second."

    s "{cps=*2}I'm so, so, so, so, so, so, sorry.{/cps}"
    show angel pain closed nowing
    show white screen with {'master': Dissolve(2)}:
        alpha 0.2
    "Tearing up, she holds onto me. It's so tight it hurts. It burns, her skin is so hot. I weakly look over to her. Please, Aza, hold me tighter, as tight as you can."
    show daisy upset
    d "{cps=*.5}...Anya doesn't want to be friends with me anymore...{/cps}"
    
    show angel scary with Fade(.5,.5,.5,color="FFFFFF")

    "The atmosphere feels different. Thick, and humid."


    s "Good. She wasn't good for you."
    show daisy nervous at unflip
    "I can't face Samyaza. I look away."

    s "She made you {b}miserable.{/b}"

    d "{size=*.8}...{w=.5}I haven't been very nice to her..."

    show angel frown
    s "No.{w=1} No, Daisy, you've been so kind. She never reached you where you were at. She was never there for you."
    show angel sad
    s "I...{w=1} I'm not any better. {i}I should've been there.{/i}{p=.4}{nw}"
    show angel scary
    extend "I would've shown her a piece of my mind."
    show daisy anxious
    "Samyaza doesn't know the full story...{w=.5} I should clarify that to her, maybe."

    d "...Do you really think so?"

    show angel frown
    s "Yes. Whatever you said had to have been justified. {w=.5}{nw}"
    show angel sad
    extend "You poor thing, I should've been there."

    show daisy idle smile at flip
    d "It's okay. You're here now."
    
    "I grab her hand. {nw}" 
    show angel pain
    extend "She lets out a quiet wince of pain.{w=.5} She's trembling."

    show daisy idle
    d "...You'll always be there for me?"

    s "{cps=*5}Yes.{/cps}"

    "Her breathing becomes raggedy and unstable."

    show daisy anxious
    d "Promise me that you won't leave me.{p=.5}{b}Ever.{/b}"

    show angel pain open nowing
    s "Never.{p=1}I failed as an angel. God gave me a second change in you."
    show white screen with {'master': dissolve}:
        alpha 0.4
    "She melts into me.{p=.5}Her skin is scalding."

    show daisy sappy
    "I stroke her head."
    s "{cps=*.2}I'm... sorry... Daisy..{/cps}"

    "She can barely get her words out."
    show angel pain closed nowing

    s "{cps=*.2}I... failed... But I'm here...{/cps}"
    show white screen:
        alpha 0.2
    show red screen:
        alpha 0.2
    with {'master':dissolve}
    "I kiss her. Her breath is humid, condensation forms around us."
    hide white screen
    hide red screen
    with dissolve
    show daisy upset
    d "Never do that again."
    show angel pain open nowing

    s "I.. I won't..."
    show angel pain closed nowing
    d "Stay by my side. I don't care what you need to do."
    show daisy nervous
    d "I...{w=2}{nw}"
    show daisy at scene_left_far with {'master': moveinright}
    "I pull away."

    show daisy angry
    d "{cps=*2}I can't have you abandon me either! {nw}{/cps}"
    show daisy upset
    extend "{cps=*2}I don't want to finish this ritual! {nw}{/cps}"
    show daisy nervous
    extend "{cps=*2}Samyaza, you want to protect me, right? {nw}{/cps}"
    show daisy angry
    extend "{cps=*2} You said I'd never have to be lonely or sad again. {nw}{/cps}" 
    show daisy upset
    extend "{cps=*2} Well, you're failing me! {nw}{/cps}"
    show daisy crying
    extend "{cps=*2} I'm so lonely and sad when you're not here!{/cps}"
    
    d "...{w=1.0}Samyaza, don't go back to heaven. I need you so much."
    show angel pain closed nowing
    pause 0.2
    show angel pain open nowing
    "Samyaza pauses, horror filling her eyes."

    s "I.."

    show daisy angry
    d "It's not fair! Am I not good enough for you? {b}Why can't you stay with me!{/b}"
    show daisy at flip
    "I take a pillow off the couch, and hurl it at the TV."
    hide angel 
    show angel sad at scene_center
    with dissolve
    s "Daisy.."


    show daisy upset
    d "It's just- {w=1}{nw}"

    #[DAISY CRY SPRITE]
    show daisy crying
    "I can't even finish my words. I pull at my hair and bawl."
    stop music fadeout 2
    "Samyaza wipes my tears."
    #[♫MUSIC STOP♫]
    play music wav_who_are_you
    #[♫WHO ARE YOU♫]

    s "I...{w=.5} {nw}"
    show angel frown
    extend"{i}We{/i} will figure something out."
    show angel happy
    s "I think...{w=.5} I think we can change the final ritual."
    show daisy upset
    "Meekly, I put my hands down."
    show angel sad
    s "I don't want to be without you, either. {w=.5}{nw}"
    show angel happy
    extend "I think...{w=.5} {nw}"
    show angel happy big
    extend "I think I know a way to change it.{w=.5}{nw}"

    extend " We can do it tomorrow, if I'm right.{p=.5}We can stay together."
    show daisy idle at scene_center_offleft with {'master': moveinright}
    "Weakly, I smile, and give her a hug.{p=1}{nw}"

    extend "I don't care about the outcome, as long as I can stay with her. "

    show daisy anxious
    d "...Can you sleep with me...{w=.5} Tonight?"

    show angel desire
    s "Of course. I'll never say no to you."
    scene black screen with {'master':dissolve}
    "She helps me up, wipes my tears and softly kisses my cheek. I cry a little more. She pets my head so gently, like I'd break otherwise."
    stop music fadeout 2
    #INT. DAISY'S ROOM (RIPPED) - NIGHT
    scene daisy_room_torn 
    show black screen:
        alpha 0.3
    with Fade(0,2,1)
    #[♫LOVE YOU, LOVE ME♫]
    play music wav_love_you_love_me
    show angel pain closed at scene_center
    show daisy blush at scene_center_offright
    with {'master':dissolve}
    "Samyaza's breath warms me up in the cold room. Her breath occasionally hitches, and she twitches as the pain catches up to her. I rub her wings."
    show daisy sappy
    "I hope tomorrow ends up being okay... I'm so happy, everytime she stirs I feel my chest getting tighter and tighter. "
    show angel pain open
    "I snuggle deeper into her. She convulses a bit. I hug her harder.{p=1}A small sleepy groan escapes her mouth. I go deeper and deeper. I've never needed anyone more."
    show daisy idle closed eyes
    scene black screen with Dissolve(2)
    "I begin to doze off, my body feels like jello. If Samyaza wasn't here tonight...{w=.5} I don't want to think about what I could've done."

    scene daisy_room_torn with Fade(0,2,1)
    #INT. DAISY'S ROOM (RIPPED) - DAY 
    show daisy anxious at scene_right with {'master':fade}
    "My eyes flutter open.{p=.5}My throat feels sore.{p=.5}I have no idea what time it is, other than it being light out."
    show daisy idle closed eyes
    "I yawn, and lethargically get out of bed."

    #INT. APARTMENT LIVING ROOM [RIPPED & DIMLY LIT] - DAY 
    scene yuri_living_room_torn
    show black screen as bkg:
        alpha 0.1
    with Fade(1,1,1)
    #[♫WASTELAND♫]
    play music wav_wasteland
    show daisy anxious at scene_center_offleft, unflip with dissolve
    "Looking around, I can tell that Samyaza had gotten up early, and cleaned up most of the mess I made from yesterday.{p=1}A tinge of guilt cuts through my heart. I feel like shit, and I don't even want to look into the mirror."
    show daisy idle
    "I finally stretch a little bit. Now that I'm more lucid, I notice the trashcan is overflowing with paper. I should at least try to make myself useful and take out the trash."
    show daisy surprised
    "As I approach the bin, I notice a ripped envelope addressed to my name specifically..."
    show black screen with {'master': Dissolve(1)}
    "This letter is to inform you that your financial aid eligibility for the upcoming Spring 20XX academic term has been revoked."
    "All students receiving federal, state, or institutional financial aid must maintain Satisfactory Academic Progress (SAP)."
    "A review of your academic record at the end of the previous Fall 20XX term indicates that you have failed to meet the required cumulative Grade Point Average (GPA) standard."
    hide black screen 
    show angel desire at scene_center, unflip
    show daisy blush
    with {'master': Dissolve(1)}
    camera:
        ease 10 xpos -180 ypos -200 zpos -600
    "Hands wrap around from behind me.{p=1.0}Hair tickles my neck, and I feel a gentle kiss on the back of my neck."

    show angel happy
    s "Good morning, sleepyhead! It's already {i}way{/i} past noon."

    show daisy nervous at unflip
    d "Morning...{w=1} um, hey, listen-{w=1}{nw}"
    show angel idle
    s "Oh, I'm so sorry! I forgot to replace the garbage bag. Let me get that-{w=2}{nw}"

    "She notices what letter I was {i}specifically{/i} looking at."

        #SAMYAZA [obsessive]
    show angel happy
    s "You know, you shouldn't worry about that.{p=.5}You have me, and you didn't even like your classes anyway, did you?"

    show daisy anxious
    d "I guess not.."

    "She's right, but I can't stop looking at the trashcan."


    show angel frown
    s "Daisy. I'll do you more good than school ever could, okay?"

    "I nod."
    show angel obsessed
    #    SAMYAZA [scary obsessed sprite]
    s "I found a way."

    # DAISY
    show daisy surprised
    d "Oh...{w=1} did you?"

    
    s "I work so hard for you, don't I?"

    show daisy anxious
    "...Yes..."
    show angel happy big
    "Samyaza is beaming. She grabs my hands, begging for more approval. "

    s "Are you happy?"
    show daisy surprised
        
    d "Yes... can I ask wha-{w=1}{nw}"

    #    SAMYAZA [scary obsessed]
    show angel scary
    s "No. "

    "The room is beginning to feel smaller, walls closing in between us. {nw}"
    show daisy nervous
    extend "Fiddling with my fingers, I tilt my head at Samyaza."
    
    "She didn't continue the conversation. I hated it. She wasn't blinking."

    d "Uhm...{w=1} Before you go, I kind of want to do something with you...{w=1} If that's okay."

    show angel desire
    s "Anything you want is more than okay."

    show daisy nervous
    d "One second..."
    show black screen with dissolve
    hide daisy
    camera:
        xpos -0 ypos 0 zpos 0
    "I run into my room, frantically scouring the mess. My scrapbook and the supplies must be hidden somewhere amongst my piles upon piles of clothes."
    "It's hard to see, my vision has been getting weaker and weaker lately. I guess I need to update my prescription."
    "Does it really matter now, though?{p=1} Whatever. I finally find my scrapbook and the supplies."
    hide black screen with {'master':dissolve}
    "Samyaza was stuck in her spot. Waiting for me with lovestruck eyes. "
    show daisy nervous at scene_center_offleft with dissolve 

    "I hesitated, hands trembling a bit."

    show daisy idle
    d "I thought it'd be fun if we...{w=1} added something special to my scrapbook."

    show angel happy big
    s "Yes. Anything you want."
    camera:
        ease 5 xpos -180 ypos -200 zpos -600
    "My upper back is tight even as I slump down into the seat. My lower back throbs.{p=1}Aza carefully seats herself. Her movements are feeble, and I look away as I pretend to not notice the wince of pain as she sets her back to the chair."
    #prop here

    show angel confused
    camera:
        xpos -180 ypos -200 zpos -600
    show scrapbook_inspect:
        xpos -400 ypos -350 zpos -600 #god i hope this works
    s "Daisy, How do we do this?"
    hide scrapbook_inspect
    show daisy happy
    d "It depends, usually I like taping mementos and good memories."

    show angel desire
    s "Hmm...{p=1}It'd be nice to shrink you down, and tape you into this."

    show daisy surprised
    d "Like...{p=1}{nw}"
    show daisy sappy
    extend "Like a butterfly.."

    show angel big happy
    s "I think so!"
    show angel pain closed nowing
    "Her laugh turns into a wheeze.{p=1}She tightens her fist, her golden veins popping through."
    show daisy happy
    "I giggle back at her, ignoring how the soreness in my eyes flares up as they crinkle."
    scene black screen with Dissolve(2)
    #[BLACK SCREEN]

    "We've been sitting for so long. I added a strand of Samyaza's hair, her nail clipping, and a piece of the fabric from her shirt. She added the same things, as well as our house key."

    "Looking down at the scrapbook for too long was difficult, my vision kept tearing, causing a massive headache."

    "After a few hours of silently crafting, I noticed that Samyaza drifted off. "

    #INT. APARTMENT LIVING ROOM [RIPPED & DIMLY LIT] - DAY 
    scene yuri_living_room_torn
    show black screen as bkg:
        alpha 0.4
    show daisy sappy at scene_center
    with Fade(1,2,1)
    "She's so cute when she's asleep... I lean forward and watch her snooze away."
    "Her breath hitches in intervals, as she occasionally furrows her eyebrows as a random bout of throbbing pain comes through her."

    "She looks so peaceful resting.{w=.5} I don’t think I’ve ever actually seen her like this before…{w=.5} It couldn’t hurt to wait a few hours, right? Or maybe even a few days...{w=1} She’s been so tired lately, after all."
    scene black screen with dissolve
    "I move my chair towards her, and as I sit, I wrap my leg around hers, and begin to doze off."
    $ renpy.music.set_pause(True, channel="music") 

    pause 3.0
    #INT. APARTMENT LIVING ROOM [RIPPED] - DAY
    scene yuri_living_room_torn 
    show daisy blush at scene_center_offleft
    show angel pain open nowing at scene_center
    with vpunch
    #[SHAKE FX]
    play sound screen_shake 
    $ renpy.music.set_pause(False, channel="music") 

    camera:
        ease 5.0 xpos 0 ypos 0 zpos 0
    "Strong hands clench onto my shoulders, shaking me awake."

    s "Daisy. Daisy. Wake up."


    d "Hmmm.. Aza..?"

    show angel pain closed nowing
    s "We're behind."


    

    show angel pain open nowing
    show angel at scene_center,flip
    show angel at scene_right with {'master':moveinright}

    "She's frantically pacing around, {nw}"

    show angel at scene_center, unflip with {'master':moveinleft}
    extend "her hands anxiously racing through her hair."
    s "We needed to do it yesterday. This is bad. {b}Really bad.{/b}"

    
    d "Mmmgnn?"
    show daisy idle closed eyes
    "I put my head down, eyes slowly closing."

    #show 
    s "Daisy. This is serious! Timing is everything and we messed up enough."

    show daisy blush
    "Leaving one eye open, my cheek is pressed against the cold wooden table. I yawn."

    d "Isn't the strength of the connection...{p=1}Just as important..."

    "It's like our relationship means nothing to her.{p=1}{nw}"
    show angel sad
    extend "She gasps, realizing her mistake."

    show angel happy
    s "Right... And I think that's what matters most with this new method!"
    show angel desire
    "She crouches down, kissing my cheek."
    #   SAMYAZA

    s "Daisy, you're so smart."
    show daisy sappy at flip
    "I pull her down to me, giving her another kiss."

    show daisy anxious
    d "Why didn't you think of that earlier? Why do you keep forgetting about us?"
    "Samyaza kisses me back, {nw}"

    show angel idle at scene_right with {'master':moveinleft}
    extend "gets up, and walks away. She must be starting with the fire ritual."
    show daisy anxious at unflip
    "I roll my head back down. A dull throb makes it impossible for me to close my eyes. "
    show sigil_fire with dissolve
    "Samyaza's drawing her biggest sigil yet. She grabs some rubbing alcohol, raining it down onto the circle. "
    hide sigil_fire
    "The sharp alcohol, mixed with the mildewed floors, make me roll my head back down.{p=1}Samyaza burns some incense, and lights some candles."

    show angel frown
    s "I don't want to hurt your nose."
    show black screen with {'master':dissolve}:
        alpha 0.5
    show angel desire at scene_center with moveinleft
    "She turns off the lights, walk over to me, {nw}"
    show daisy at flip

    extend"and gently grabs my hands."

    show angel happy
    s "Take out your scrapbook."

    show daisy nervous
    d "What..?"

    show angel scary
    s "Do you love me?"
    show scrapbook_inspect at center with dissolve
    show daisy upset
    "{cps=*4}I frantically nod, handing her my scrapbook.{/cps}"
    hide scrapbook_inspect at center with vpunch
    "She throws it in the middle of the circle.{p=1}I'm handed a pen and paper."

    show angel frown    #SAMYAZA [neutral]
    s "Write about how you want to stay with me."
    show daisy anxious
    "I nod.{p=1}It's not even a decision I have to think about making."

    "She also writes down her own, takes the sheets of paper, placing it near us.{p=1} I notice, in the corner of my eye, that my scrapbook is also placed within the sigil."

    show daisy nervous
    d "Why's my-{w=1}{nw}"

    #    SAMYAZA [scary/stern]
    show angel scary
    s "We have to stand for this one."
    show daisy anxious
    show angel happy big
    camera:
        ease 2 xpos -180 ypos -200 zpos -600
    "She holds her hands out, drags me closer to her.{p=1}{nw}"
    show daisy blush
    extend "No matter how long it's been, I still find my hands getting clammy from her touch."
    show angel idle closed eyes
    "As usual, Samyaza hums the incantations of the language.{p=1}Her voice shakes.{w=1} It feels weird, knowing that this will end soon."

    play music wav_quiet volume 2

    "The room starts to gradually get hot."
    show daisy nervous with None

    show red screen:
        alpha 0.4
    hide black screen
    with {'master':Dissolve(5)}
    "The incantation must've triggered some spell, because fire bursts around the sigil.{p=1}I grip tighter onto her hands, attempting to calm my breathing."
    "The candles add to the flames."

    "It feels so hot.{p=1}A lot hotter than before."
    "{cps=*3}I feel sweat come out from every single pore of my body, and the realization of the very real threat that I'll probably be burned alive. Maybe all the other people in this building, too.{nw}"
    show daisy upset
    extend " Well, fuck them, I don't care. They probably all deserve it anyway. {/cps}"
    show daisy surprised
    show angel pain
    "Samyaza almost falls to the ground, but braces herself with her elbow.{p=1}{nw}"
    show angel pain closed nowing
    extend "She scowls, and grits her teeth as she stops pained noises from escaping her lips. {w=.5}{nw}"
    show black screen
    hide yuri_living_room_torn
    show angel pain scary wings
    with {'master':dissolve}
    extend"Eventually she gives in, and falls to the ground, letting out a howl of pain."
    "As she writhes on the ground, she tries to reach her wings.{p=1}Her wings begin to burn, and she screams even louder."
    show daisy nervous with {'master':dissolve}
    "I kneel down and hold her."
    #DAISY
    show daisy upset
    d "Samyaza!"

    "She's not answering me.{p=.5} I shake her, and white hot pain engulfs my hands."

    show daisy nervous
    d "{b}AZA! Come on!{/b}"


        #SAMYAZA
    s "It....It's... working..!"
    scene black screen with dissolve

    "My hand that's on her begins to melt into her.{p=1}Like the candle wax melting all around us."

    "She reaches out one of her hands to me.{p=1}We clutch each other.{p=1}We're the only ones in the entire world."

    "Our hands glue together. Her white wings are getting dark with ash.{p=1}Her aura feels like the first night I met her. I was born to love her.{p=1}God brought us together for me to help her."

    "She's in so much pain. She can barely look at me. Her hair is sizzling. The smell of burnt plastic attacks my nose."

    "I go in for a kiss. Her skin is scalding. It hurts so bad but we can't pull apart."

    "{cps=*2}Everything around me is burning. My scrapbook must be in flames, the remains of Anya's pamphlets are already ash.{p=1}It's okay, I can always pull in further into the kiss.{p=.5}Whatever happens, I know I'll be okay as long as I'm with you, Aza.{/cps}"

    "My head is inside of hers, her head is inside of mine. Our bodies melt together. It's not enough, we need to be closer. I'm-{w=3}{nw}"

    "{b}Closer. Closer.{/b}{p=1} I can't even feel the heat anymore."

    "My skin flexes, our skin is stretched so far thin. Our body is tight, it's so hot that everything in me...{w=1}us? feels frigid."
    scene red screen with {'master':Dissolve(3)}
    "Our arms corrode into each other, our blood oozes, forming into glue. Nails fight for dominance, overgrowing each other, the throbbing pain is felt all over our bodies.{w=2} We scream."

    "The stench of burned hair and flesh takes over from the incense.{p=1}The world around us revolves."

    "{cps=*3}Our lungs fight for space inside our brains spin together our bodies turn into a blender bubbling coming into one our muscles melt and reform two necks becoming one.{w=2}{nw}{/cps}" #allowing our are 

    "It feels like knives are stuck underneath our skin. They struggle to get out, stabbing the lining. Our back feels like it's going to cave in from all the pressure."
    "The wings struggle to drill their way out.{w=2}{nw}"
    
    "The wings {b}burst{/b} their way out, a sharp burning sensation is felt all throughout our body, until it settles."
    scene black screen with {'master':Dissolve(2)}
    "We drop to the ground, our body spasms.{p=.5}Wings hitting the residual flames.{p=.5}It hurts. It hurts so much."

    stop music fadeout 1

    "The flames subside. Our body pulsates as we lay exhausted on the ground. Our body sore."
    camera:
        xpos 0 ypos 0 zpos 0
    window hide
    pause 5.0
    window auto
    scene yuri_living_room_burnt with Dissolve(2)
    #[♫WHO ARE YOU♫] (..id really like for it to be theendNEW esp if we drag out the following few lines)
    play music wav_who_are_you
    creature "I get up. The living room is burnt, ashes litter the space, my belongings are no longer able to be found."

    creature "My wings flag the ash and blood off."

    creature "I walk to the TV, and see my reflection."
    window hide
    #[FUSION SPRITE]
    scene black screen
    show fusion cg 1 with Dissolve(1):
        zpos 130
        ypos 40
    pause 2
    window auto
    show fusion cg 2 with {'master':dissolve}:
        zpos 130
        ypos 40
    #$ style.narrator_text.what_italic=False
    creature "{cps=*.1}I smile.{/cps}"
    creature "{cps=*.1}My wings flap, I feel so beautiful.{/cps}"

    creature "{cps=*.1}{b}I'm so happy.{/b}{/cps}"

    window show
    #stop music
    scene black screen with Dissolve(10)
    $ style.centered_text.size = 50
    $ style.centered_text.color = "#FFFFFF" #guh
    "{b}{p=0}{p=0}{p=0}THE END.{/b}"
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

    
