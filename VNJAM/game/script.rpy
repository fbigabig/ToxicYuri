# The script of the game goes in this file.


define config.default_textshader = "typewriter"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character("Daisy", color="3AA2DF")

define narrator = Character(color="3AA2DF", what_italic=True)

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
    "images/mob_dress.png"
image angel idle:
    "images/angel idle.png"
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
image angel obsessed:
    "images/angel obsessed.png"
    zoom 0.4
    yoffset 100
image angel sad:
    "images/angel sad.png"
    zoom 0.4
    yoffset 100

image angel shadowed:
    "images/angel shadowed.png"
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

transform flip:
    xzoom -1.0
transform unflip:
    xzoom 1.0
label start:

    #EXT. UNIVERSITY PARK - DAY
    scene yuri_park_01 with fade

    show anya idle at scene_center_offleft
    a "You know, I really think you should come and meet my friends. They’re really funny. God, I remember one time where......"

    show daisy anxious at scene_center_offright
    "She talks so much. I just wish she’d ask about me... I picked up scrapbooking again... I jut out my scrapbook to be within her line of sight."

    a "....Then, I remember when he even started to eat the rice even though it...."


    "I mean, I should listen.. It’s been a while since we’ve seen each other. But I really don’t want to meet these people. I doubt we’d have anything in common anyways. She’s been in university for a while now, and I’m her age and only just getting started."


    a "....And when he helped me move back in my freshman year. Oh God! {p} Right, you moved in today, didn’t you? How was it?"
    a "Oh wow, now I feel bad that I couldn’t help you much. Is there any other way I could help? I feel really bad, my internship had some stupid orientation thing I had to be at, but. I would’ve much rather helped you.{w} God, I feel really bad..."

    "..."

    a "....And we had a whole thing about changing our language and stuff for a “professional work environment”... so annoying. {w}Wait! Your move-in. Tell me about it!"

    show daisy idle 
    d "It was OK..."


    "It was kind of hard having to do everything myself, but I liked having the place to myself. I’d be kind of embarrassed having a new person see me get all sweaty and out of breath."
    show daisy nervous
    show black alpha behind daisy
    "The image of myself out of breath and sweaty popped up into my head. My bangs were pinned back, revealing my ugly forehead, my hairline frames my face terribly. My glasses kept sliding down like I was an old man."
    hide black
    show daisy idle
    "I returned back to earth, only now noticing the grimace on my face. Quickly, I have to relax. Anya will notice and pester me."
    show daisy anxious
    "...{p}...{p}She isn’t even {b}looking{/b}{w=0.2} at me."

    
    a "Just that? How’s your new place? Show me pictures! I bet your dorm is gonna look super cute... Wait, did your mom help out? Oh-  Sorry, I shouldn’t have asked that..."

    show daisy idle
    d "No, it’s okay. She couldn’t help me because she's been weak lately. It was just me."

    a "Oh my god! You should’ve told me! I could’ve helped you."
    show daisy idle
    d "Really, you don’t have to sweat it...."

    show daisy anxious
    "I don’t know why she’s lying to me. We both know that I would just get on her nerves with how clumsy I am; I’m so sore from dropping stuff onto my feet, and I’m sure having her just be in the same vicinity would increase my anxiety tenfold."
    "I can already imagine it, her staring at all of my trinkets and making an extremely thinly veiled comment about how I “oughta declutter now that I’m starting a new leaf.” Yeah right."

    "I remember when we worked on a science project together back in high school. I was kind of bad with putting our presentation together.{w} I could just {b}tell{/b}{w=0.2} she didn’t want to stay after school with me."
    "She was so quiet- it was offputting for her. {p}Her silence could only mean that her mind was filled with all sorts of insults about me."

    a "You sure? I'm worried about you!" 
    #(laugh sprite) 
    extend "This may be mean, but I was thinking... You’re so out of shape that you might snap in half while picking up heavy boxes! We should really go to the gym together..."

    show daisy nervous
    "I can’t help but to make a face...{w}Does Anya really see me like that? Does she really think I can't lift a few boxes on my own? I'm not dumb; I know what people have said about me behind my back and even to my face- I guess I just didn't expect Anya to be like that too.."

    a "...By the way, I’m hosting a welcome back party this Sunday. You should totally come! I really think you’d like Hannah. You guys are both artists! She’s actually graduating this fall, and has an animation job lined up! Wait. Have you chosen your major yet? "

    "I fiddle around with my fingers. The last thing I want to hear right now is a person around my age who is doing far better than I ever will. I didn’t really think I would get this far. I can barely get myself out of bed, choosing a major is beyond me."

    d "Uhm.{p}...{p}I’m still undecided."

    a "Daisy! You have to make sure you pick one out, Okay? You can’t just be cruising through life like that forever!"


    d "{size=*.75}I’m sorry...{/size}"

    a "Don’t worry! I’ll just make sure to check up on you."
    hide anya
    show daisy upset at scene_center
    "I look away, deciding to focus on the leaves as they sway. I hate that I have to acknowledge that Anya looks down on me. "
    show anya idle at scene_center_offright
    extend "She leans in and smiles at me. It feels like a sneer."

    "My entire body sinks. Bitter feelings gnaw at my heart. I try to tune back into Anya’s lecture but I can’t ignore the resentment. I wish I could be her equal, but I’ve let myself fall behind."

    "While deep in thought, I felt a hand touch my shoulder. My body stiffens for a moment."

    a "Daisy, I think you’ll have a great time here, really. It’s nothing like home. People are a lot nicer here, I swear."
    show daisy idle smile
    "I give her an awkward smile.{p} One that doesn’t reach my eyes. {p}I look down, fiddling with my fingers.{w} Anya is the type of person everyone likes."


    d "..Thanks.."

    scene black screen with dissolve

    "The stale air of the hallway was suffocating.{w} The scent of wet carpet and dust filled my nose as I tried to shut out all of the sounds of the oncoming students jestering with their peers."
    "I wanted to rush home, I couldn’t stand the noise.{w} Honestly, it’s better for me to head home anyways.{w} Anya was getting tired of me." 
    "I finally get to my door, it’s a simple two bedroom one bathroom.{w} Luckily the school is more accommodating since I started school a bit later than my peers."
    "I hope my roommate is the same as me.{w} or at least just someone who is never in the house."

    "Turning the door knob, a loud creaking greets my ears. The scent of old fabric and mildew wafts in from the AC, which is already running on full blast."
    scene yuri_living_room with fade
    "My pupils adjust to the brightness in the apartment."

    "Huh..? I don’t remember leaving the lights on when I left."

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

    "She stands tall before me, her strong build illuminated by the moonlight. I can’t make out her entire face right now, but she’s giving me a sweet smile and I can see the golden glint of her eyes through the darkness."
    "I don’t know what it is about her, but her aura made my entire body go weak-{p}"
    show daisy sappy
    extend "I’m at her mercy."
    show daisy anxious
    "She stuns me. But, despite her beauty, my eyes went straight to her cross necklace. My stomach is in knots."
    #play music wav_blessing
    #sprite here
    unknown "I was going crazy thinking I was gonna live alone in this 2x1. Good thing you ended up filling this spot last minute. I was trying to ask them about you but they couldn’t say anything."

    d "Oh... uhm... right. Sorry I got the email but never reached out to you."
    show angel confused
    unknown "Email?"

    show daisy idle smile
    d "Uhm... maybe they sent it to the wrong address or something.... {w}That happens to me too...{w} sometimes.."
    #sprite here
    show angel idle
    show daisy idle
    "She smiles at me, waiting for something." #" (her sprite changing to a blank smile)
    show daisy idle smile
    d "Oh sorry, I’m Daisy."
    #sprite here
    s "I’m Samyaza, nice to meet you!"

    show daisy idle #never smile for long!
    "She confidently reaches her hand out... Her voice is a bit too loud for my liking, but that's fine, she seems nice otherwise. Hopefully I can stay out of her way."

    "I shyly reach my hand out to hers, and she grips it with a vigorous smile and level of enthusiasm that is unnatural. She’s acting like a used car salesman, each shake felt performed. She seemed as if she was trying to be relaxed, but her smile twitched in exhaustion."

    "She feels a bit more... sympathetic? Earlier today, I was practicing my greeting to Anya in the mirror. Performing my smile in the mirror to make sure there wasn't any underlying strangeness that she could pick up on."
    "...I didn’t want to worry Anya with how bad things had been recently."

    s "Cool.. You have such a cute face. Has anyone ever told you that?"

    show daisy nervous
    d "Thanks.... Uhm, I think so?"
    show black screen behind daisy:
        alpha 0.25
    show angel idle behind black
    "I shift uncomfortably, I really want to get back into my room and hide in bed. But no matter how much I try to break eye contact, my eyes just keep meeting with hers."
    show black screen behind daisy:
        alpha 0.5
    "I know that she’s analyzing my face, each and every single one of my pores- my ugly acne scars, and my long overdue-to-be-tweezed eyebrows..."
    show black screen behind daisy:
        alpha 0.75
    "She's already thinking about how terrible of a roommate I’m going to be, that I’ll be dirty and weird, how I probably won't wash the dishes, or can’t even socialize with her or her friends properly."
    show black screen behind daisy:
        alpha 1
    show daisy crying
    "I can already imagine it. She invites her new friends over, they’re loud as hell in the living room."
    "I work up the courage to leave my room to get a glass of water, something to eat, anything- as soon as I step out they immediately go silent, briefly sneaking glances at me from the corners of their eyes. "
    "The second I slam my door, they go back to laughing, whispering about how weird Samyaza’s roommate is."
    "Quiet enough to feign ignorance (“We were talking about someone else!”- yeah right, bitch,) but loud enough that the roommate in question can still hear it even if she tries her absolute hardest to pretend they’re not there."
    "They’re absolutely hysterical, shrieking like hyenas over how weird Samyaza’s roommate is. She’d laugh and agree, and talk about how much she couldn’t wait to move out."
    show daisy anxious
    "I can’t let that happen this time. I have to prove to her that I’m good at all of these things.{p}That I can function as a human being for once."

    hide black screen
    show angel confused
    s "Did you hear me? What’s your major?"
    d "Uh. Oh, sorry. I’m undecided."

    #SAMYAZA (happy/genuine sprite)
    s "Oh wow, really? Me too. There’s just so much to choose from, I couldn’t decide either. What classes are you taking? Hopefully we’ll have some together?"
    show daisy idle
    "I scroll briefly through my gallery and hand her my phone, on it a screenshot of my class schedule."
    show angel sad
    s "Aw man, only three. That {i}sucks{/i}."

    d "Well... I’m only taking 4 classes anyways.. "
    show daisy anxious
    "I look down, hoping her energy dies down soon enough. I let out a long, loud, and very drawn out yawn. She’s still observing me."
    #sprite here?
    show angel idle
    s "Maybe I can switch into your fourth? I’d love to have a friend in all four classes."
    
    "A friend? I can’t believe this girl is already considering us to be friends. I feel bad for her, when she sees who the real me is, she’ll hop on over to whatever better, well-adjusted friend group she’ll make. I don’t know their faces yet, but I’ll know them soon enough."

    d "Uh. Yea. That’s okay."

    scene black screen with fade 

    scene yuri_living_room_night with Dissolve(2.0) 

    show daisy idle at scene_left, flip
    show angel idle at scene_right
    "It feels like Samyaza could go on forever. She talks to me about anything and everything, even the things that aren’t necessarily ... important?"
    "Well, I guess that’s not the right word, but some of the things she pointed out were so mundane that I can’t help but wonder where she’s from that doesn't have these things."

    s "I saw a salamander earlier. It was my first time seeing one in person, it was sick."
    d "...Yea, there’s a bunch around here."
    
    s "Have you ever had a taco?"
    
    d "Yes."

    s "Earlier today, I had one for the first time."

    show daisy anxious
    "..."
    show angel confused
    s "..."
    "What is she waiting for?"

    s "What kind of foods do you like?"

    d "Uhh..{p}I don’t know, pasta I guess?"
        #sprite here
    show angel idle
    s "Before I had it, I swam for the first time too."

    d "Uhm, yea I’ve heard that there’s a lake nearby campus.. I think."
    
    s "Do they have this stuff where you’re from?"

    d "{i}{shader=jitter:u__jitter=1.0, 3.0}..What..? {/shader}{/i}{nw}"
    d "{i}..What..? {/i}{fast}Like salamanders, tacos and lakes?"

    s "Yea! It’s so cool."

    d "...Well yea, I’m from the state.."
    "Does she ever stop asking questions? Please, get bored of me already. But on the other hand, it’s a little... {w=0.5}nice. Nice that she cares so much about what I have to say."
    "Starting a new leaf is nice... I think... Entertaining this makes my stomach hurt. But I kind of want her to like me..."
    "She’s a better listener than Anya. Even though my answers are curt, she treats each word as if it is better than the last."
    "Maybe my initial reaction was too cruel. I barely know this girl and I am already assuming the worst in her. I might be the worst person in the {b}world{/b}."
    show daisy upset
    "I nip my lip in frustration. I could be extending some kindness to her, I could be trying to make conversation with her- but instead I act like everyone else I know."
    "The teeth on my lip sink in harder."
    "She’s so nice, and maybe that’s just for now- who knows. I can feel the familiar taste of copper on my tongue. My lip is trembling, but I don’t  really care about that right now. She’s probably just being nice to trick me, waiting for me to let my guard down and- "
    
    #i wanna semi cry sprite here
    show angel confused
    s "Hey? Are you alright? Your lip is bleeding."
    show daisy surprised
    d "{size=*1.2}Oh shit! {/size}Oh, I’m so sorry, don’t worry about me, I’ll go clean myself up in the bathroom."
    show daisy at unflip, scene_left_far
    show angel idle at scene_center_offleft
    "Shuffling in a panic, I am stopped before I can do anything. Samyaza’s as strong as she looks, holding onto my wrist-{w=0.2} she locks me in place."
    "Samyaza takes out a folded up cloth from her pocket."
    "Pressing it on my lip."
    camera:
        perspective True
        zpos -700
        xpos -450
        ypos -250
    show angel desire
    "She is really close, her breaths are strong and steady as she applies the right amount of pressure on my lip."
    show daisy sappy
    "My breath stops in my throat."
    "I'm looking away, I’m looking away."
    show angel idle
    "Her lips purse in concentration, my heart skips a bit."
    "No, no, no.. {w=0.5}she’s just my roommate.{p}That’s {b}all{/b}."
    show angel frown
    s "That doesn’t look too bad. But you really have to be careful, alright? "

    show daisy blush
    show angel desire
    "Her breath heats up my face. Her finger is warmer than any others I’ve felt before. Her presence lights up the dark room, like a bright comforting light shining on me. Contemplative eyes penetrate each and every pore on my face."
    "Playing with my hair, I look away and try to distract myself. Just look away already! Stop staring at my face..!"
    show daisy nervous
    extend " I’m so ashamed, I hate how fiercely she's scanning into me. I want to curl up into a ball, and roll away."

    show angel sad
    s "Alright, you should be fine now. Take care of yourself, Daisy, alright?"


    d "Y-yea, thank you!"


    scene black screen with dissolve
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    "I shuffle off to my room with the cloth. I think...{w=0.3} I’ll clean myself up...{w=0.3} sometime tomorrow...{w=0.3} maybe, a little later than I usually do."


    window hide dissolve
    pause 1.0

    scene room daisy night with fade

    window show dissolve

    "I sat still in my bed, looking up into the ceiling."

    "The exhaustion from the day began to kick in. I rub my sore muscles. If only I had someone to massage me. I sigh at the door, oh well."

    "I need to stop getting ahead of myself. It’s been a while since I talked so much to someone. I’m getting excited and thinking ahead. I need to be realistic here, I gave off a terrible first impression."
    "Instead of massaging, I press down hard into my back. Nails dig into my skin. I press {b}harder.{/b}"
    "A little part of me wants to live alone. If I didn’t have a roommate, I would stay lying here. Honestly, rotting here sounds better than waking up for classes tomorrow...{w=1}"
    "I press down even harder. I can’t think this way. This is the only chance I have to change my life for the better."
    window hide dissolve
    pause 3.0
    window show dissolve
#add sfx
    "I almost did lie in bed forever. Only until my phone alarm went off. I totally forgot about my estrogen shot. Shoot."
    "Today was such a drag, I should’ve done this hours ago."
    "As I unbox the syringe and sanitizing wipes, I notice that I left the blood stained handkerchief on my side table. "
    "I use it as a mat to set down some of the injection supplies."
    "The weekly ritual somewhere other than home feels off."
    "I inject {nw}"
    window show
    #hahahaha got it
    show red screen onlayer master with {"master": Dissolve(0.1)}:
        alpha  0.25
    window show
    extend "the needle into the sanitized sight."
    "Everything about this place feels off.  No loud TV drowning out the oppressive silence, no loud sighing from my mother, interrupted by her growling to herself about some chore I forgot to do."
    "Even my brain felt...{w=0.5} quiet."
    "I take it out.{nw}"
    hide red screen
    #hide red screen onlayer master with {"master": Dissolve(0.1)} doesnt work :(
    extend " I have to cherish this peace and quiet while I still have it- it's only a matter of time until Samyaza brings over her friends."
    "Instead of my mother’s sighs, I’ll be terrorized by piercing laughter. "
    "The thought of it made me scream into my pillow. I don’t want to go through that feeling again. "
    "My head is flat on the pillow. But I felt my hand guide itself over to the handkerchief."
    "I looked at the small splotch of dried blood against the pristine white fabric. A small golden eye was embroidered on the side. "
    "Slowly, I bring the handkerchief off the bedside drawer,{cps=*.5} {w=.5}then lead it up my leg,{w=.5} then right to my face. {w=.5} {i}I take a whiff.{/i} {w=.5}My free hand makes its way down,{w=.5} from my chest,{w=.5} to my stomach,{w=.5} to my crotch.{w=1}{nw}{/cps}"
    "{cps=*.5}My hand reaches for the zipper.{/cps}{nw}"

    window hide dissolve
    pause 1.0
    window show vpunch
    "I throw the handkerchief to the other side of the room."
    "{shader=jitter:u__jitter=1.0, 3.0}What the fuck am I doing?{/shader}{nw}"
    "What the fuck am I doing?{fast}"
    "Something in me, a divine presence, picks me up, and I walk over to pick the handkerchief up."
    "I lay it down next to me again. And drift to sleep."

    window auto

    scene yuri_living_room with  Dissolve(4.0)
    show angel idle at scene_right with dissolve

    "Samyaza is up bright and early. She eats a strange resinous bread, and gives me a relaxed grin. I rub my eyes while I grab a cup of yogurt."

    s "Good morning, I was worried that you were going to miss class."
    show daisy blush at scene_left with dissolve
    d "Thanks.. But you really didn’t have to wait for me."
    show daisy idle
    s "It’s no biggie."
#sprite
    "She leans back on her chair and smiles, eating a piece of bread into her mouth. "
    show daisy anxious
    "I can’t respond. I shove the yogurt into my mouth, the thick texture and sour taste stay stuck in my throat as I try to avoid her. Her eyes are so bright, almost like a blinding car headlight."

    "Once I finish with the yogurt, she quickly takes the bowl and spoon and puts it in the sink, and cleans it immediately."

    "Uh.. {w=0.5}you really didn’t have to do that, I’m ok with washing it."

    #SAMYAZA (happy/genuine) sprite
    s "Really, it’s no big deal. Just wanted to help."
    "Her smile shines on my face. It kind of hurts, it feels like I’m looking directly at the sun in the middle of a hot summer day."

    "We take our bags and begin to walk over to our class."
    window auto
    scene yuri_classroom_01 with dissolve
    #INT - CLASSROOM - DAY
    #(sfx of people shuffling out/talking)

    "As our class got out, I get up and yawn."

    show daisy happy  at scene_right_far with dissolve
    d "Man, that was boring."
    show angel idle at scene_left with dissolve
    "Samyaza stares at me for a second, like the cogs in her brain are shifting.{p}She.. seems to be genuinely thinking about.. something? It’s kind of hard to read her expression right now."
    show daisy anxious
    "I’m going to go with the safest bet that I said something that annoyed her, and she’s just trying to be nice because she knows she has to deal with me for the next year."
    show daisy nervous
    "My face heats up. I quickly sit back down, and began to pack my stuff. I need to run to my next class and act like she didn’t just ignore me."

    d "…Or maybe it was interesting.."

    "It doesn’t matter how much I try to steer my mind away from her lack of response, my hands are clammy and slippery. {w=.5}A couple loose pencils ricochet against my fingers and fall straight to the ground as I quickly try to pack. I freeze."

    d "Oh…{w=.5} wow… "

    "The familiar pang of anxiety and shame wells up inside of me, my face must be bright as a tomato right now.."
    d "Guess I just can't do {i}anything{/i} today, huh!"
#sprite
    "Samyaza smirks at me, creasing her eyes and showing her teeth."

    s "Nah, it wasn’t boring."
    show angel idle at scene_center with moveinright
    "She gets up, and helps me put the stuff into my bag."

    s "It was SUPER boring."
    show daisy anxious
    d "You really didn’t ha-{w=1}{nw}"
    show angel desire
    s "{b}I want to.{/b}"
    show daisy sappy
    "My eyes widen as if they are going to burst out of my skull."

    show daisy blush
    s "That’s what roomies are for..{w=0.5} Right?"
    #sprite
    "She nonchalantly grins." #cut this line?
    show daisy at unflip,  scene_right_far
    show angel at flip, scene_center_offright with moveinright
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
    "Samyaza slyly hands me over notes from the upcoming lecture. She must be a good student if she’s already this far ahead. Way better than me."

    "Sheepishly, I grab the notes and begin to copy them down."
    show daisy surprised
    "I notice a cute little drawing on the corner. Poorly drawn versions of me and her diligently studying."
    show daisy happy
    "I rip it out to add to my scrapbook."


    scene yuri_park_01 
    show daisy idle at scene_right_far
    show anya idle at scene_center, flip
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    show mob_dress at scene_center_offleft
    show mob_walk at scene_left_far
    show black screen
    hide black screen with Dissolve(0.5)

    "I try to hang out with Anya and her friends. They howl with laughter at Anya’s joke."

    "I lounge a bit further away from them,"
    show anya idle at scene_center_offright,unflip with {'master': moveinright}

    extend "Anya sympathetically looks my way and scoots closer to me."

    "She tries to include me in the conversation,{nw}"
    show daisy idle smile
    extend "but all I can do is weakly laugh."
    show daisy anxious 
    "I tense a bit, staring at the leaves of the same tree I did all those weeks ago when I first transferred."

    "In the middle of her conversation, I hear Anya spontaneously jump up, and grab something from that tree."

    "She hands me a little flower. I gingerly reach out to it."
    
    show daisy surprised
    d "Is this for.. My scrapbook?"

        #ANYA (smile sprite)
    a "Duhh!"
    show daisy blush
    d "You remembered?"
    show daisy happy
    "Anya noogies me."

    a "Who do you think I am?"

    

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

    camera:
        perspective True

        zpos 0
        xpos 0
        ypos 0
        linear 2.0 zpos -600 xpos 450 ypos -250

    pause 2.0
    "Samyaza and I sit down and eat sandwiches she made."
    show black alpha behind daisy
    show angel behind black
    extend " I feel like a sore thumb."
    show daisy nervous
    "Could I really live a normal college life? I stare at the sandwich. I shouldn't eat this, I don’t belong here."
#sprite
    "Samyaza brings the sandwich to my mouth, but it just falls against my cheek."
    show angel sad
    "I’m such an alien, and aliens don’t eat human food. "
    show daisy upset
    "The physical weight of my body takes up the space, suffocating everyone else enjoying their day outside."
    hide black
    show angel desire
    "Samyaza opens my mouth{nw} "
    show daisy surprised
    extend "like she’s opening a trash chute and puts the sandwich in it."
    
    
    show daisy happy at unflip, scene_right_far
    "I start to cackle."

    scene room daisy night with fade
    camera:
        perspective False
        zpos 0
        xpos 0
        ypos 0
    show angel idle at scene_right
    "Samyaza helps string up some fairy lights, she’s tall enough to do so. I sit on my bed and watch her. The fabric of her vest stretches across her back, it traces the lines of her muscles with every movement. "

    show daisy anxious at scene_left with dissolve
    d "I’m really sorry for being unable to help…"
#sprite
    s "No worries, sit your pretty little self down. Ladies shouldn’t do this work."
    show daisy blush
    "I bite my nails and enjoy the view."

    scene yuri_living_room_night with Fade(1.0,1.0,1.0)
    show daisy anxious at scene_left_far
    "I’m typing away at my computer with urgency. The first big project of the semester is coming up. My brain feels like it's filled with fog as the document just can’t seem to fill up."
    "In 30 minutes, I have to meet up with my group members for this class. I want to make sure the presentation is done by then. I’m hoping I can just make the presentation, and write the content."
    "...I’d rather {i}die{/i} than present and be under the microscope of the entire class."

    "I can’t afford to do poorly, my groupmates already think I'm irritating. They’re always asking if I have any questions after our meetings."
    "I can’t ever look them in the eye when I do have questions, though. I feel the awkward glances they give each other as I try to talk."
    show black screen behind daisy with dissolve:
        alpha 0.8
    "If I do poorly, I’ll disappoint Anya. I already hear the scolding I’d receive if I failed."
    "After that, it'll only be a matter of time until she realizes that everyone was right, and that she ought to cut me off instead of using me like some charity case."
    "She’ll be sick of me even more than before."
    #sfx
    
    "My stomach rumbles, but I continue to furiously type. I’m never able to get work done, so I ignore it. I catch a whiff of myself too… I guess the shower will wait."
    show angel idle at scene_right behind black with dissolve
    "Samyaza comes into the apartment, her last class today ends rather late."

    s "Daisy, how was your day?"

    "I don’t deserve to talk to her until I finish. I focus in on my laptop screen."
    show angel confused
    s "Daisy?"
    show daisy angry
    d "Sorry, I’m busy."

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
        linear 1.0 zpos -600 xpos -450  ypos -250
    "Samyaza sits down in front of me."
    
     
    s "Come on, tell me about your day."
    hide black with dissolve
#sprite
    show angel idle
    "She softly grins, leans forward and holds her face in anticipation."
    show daisy anxious
    "I take my hands off of the keyboard, and rub my fingers together. I am completely blank, how {i}was{/i} my day?"
    show black alpha behind daisy
    show angel behind black
    "It's like I'm watching someone else go through my days. What’s the right way to answer her, I want to give her an answer that will make her happy.."
    hide black
    s "Sooo? "

    d "Uh.. sorry! Uhm, it was okay… I guess."
#sprite
    "Her lips flatline, as she tilts her head. She gets a little closer to me."

    s "{cps=*.25}Andd…?{/cps}"

    d "I…{p=1} I really need to get back to work."
    show angel frown
    "Samyaza slowly closes my laptop until it’s halfway open."
    show daisy surprised
    d "Hey!"

    s "I’ll open it up again… once you tell me about your day!"

    d "I mean, I studied then I scrapbooked."
#sprite
    show angel idle
    s "…Scrapbooked? Do tell."
    show daisy anxious
    "I sink into my feet, and rub my hands with more intensity, I want  to feel any sort of friction. In the back of my mind, the project feels like an unbearable itch that I can’t scratch."

    d "{cps=*2}The other day I was hanging out with my friend- Anya, and she knows I like scrapbooking… so uhm she drew a little cat on a receipt. We went to a coffee shop.{/cps}"

    s "And? How was the coffee?"

    d "It was okay. Nothing to write home about."
#sprite
    s "What did you get?"
    
    d "Just an iced vanilla latte. I  really wanted to try this place cause I know they have specialty beans."
    d "Back at home we don’t have anything cool like this. Honestly, there’s nothing cool at home. The interior was really cute too, and also the…"

    s "The?"

    show daisy angry
    d "Samyaza. I really need to do this assignment. It's due {b}soon.{/b}"
    show angel sad
    s "Make sure to talk to me after, okay? It’s so lonely here."

    "I hesitate to open up my laptop."

    d "Yeah..{w=0.5} it really can be."
    
    "I open up my laptop. I don’t know how but thirty minutes have passed."
    "I checked my phone, for some reason the ringer didn’t go off at all."
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
    "Ugh… it’s because of you! They {b}hate{/b} me because of you!"

    s "Huh- What do you mean?! I don’t understand! I can’t help you if I don’t know what’s going on!!"

    show daisy at offscreenleft with moveinright
    "I turn my laptop off and run into my room. I shut the door behind me. "


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

    "The slamming is deafening. I curl up into bed and cover my ears with the pillow."

    s "Daisy! Open up, please!"

    "{b}Go away!{/b} My entire face hurts with the intensity of how hard I’m squeezing my eyes shut."

    d "You’re only making it worse!!!"

    "Samyaza’s voice quivers more and more. The knocking increases in intensity. "

    #[DOOR KNOB OPEN BUT ITS LOCKED SFX]

    "My pillow is becoming damp with my tears."

    "Why am I lashing out? She’s not going to like me if I keep this up."

    "I guess I'm saving myself. At least I’ll know {i}exactly{/i} why she hates me. I’m ripping the bandaid clean off."

    scene black screen with dissolve 
    #INT - APARTMENT - NIGHT

#[BLACK SCREEN + SOMBER MUSIC]

    "My hand is stuck on the apartment doorknob. Something deep inside my soul is working against me. Do I {i}have{/i} to open the door? I don’t know if I can face Samyaza. "

    "I really am the worst of the worst. Ignoring Samyaza for the past day? I don’t think I deserved to talk to her after yesterday."

    "But, as horrible as it sounds, I like that I can finally say she really cares about me. She was miserable the entire day today. Cartoonishly so- like she learned how to look sad through sitting down and watching Saturday morning cartoons."
    "She looked like an abandoned puppy."

    "Standing still like a statue, not knowing whether to open the door and accept the punishment I deserve, or run away and prolong it. Samyaza deserves better than me."

    "Regardless, I opened the door, not because I was brave- but because I was a coward who wanted the comfort of my own bed after a terribly long day."

#[MUSIC STOPS]
#[DOOR OPENING SFX]
    #INT. APARTMENT LIVING ROOM - WHITE SCREEN
    scene yuri_living_room
    show white screen:
        alpha 0.8
    show black screen
    hide black screen with dissolve
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

    s "Glglg..daisylglgl"


    d "Samyaza, what’s going on????"


    d "My heart is beating so fast and my eyelids trembling in fear."
    scene white screen
    show red screen:
        alpha 0.8
    "My body glues them shut. And even if I want to, I’m too afraid to open my eyes."
    "It’s sweltering here and it's hard to breathe."
    "My entire body clenches up."

    "Samyaza grabs my wrist, her gurgling continues. She guides me to some sort of tubed object."
    "Her hand sears my skin."
    "Her fingers, like a branding iron."
    "I bite my lip to hold in my whimpers of pain."
    "The pain helps ground me-{p=1.0} it helps me realize that whatever is happening is real. "

    "She opens the cap to the object, and guides my hand to draw a circle."


    d "Mmph…!"

    "My nails are digging into my hand, as my other hand is drawing a series of shapes I can’t figure out."

    #[MUSIC STOPS]
    #[FADE TO BLACK]
    scene black screen with dissolve
    "The light instantly goes out, Samyaza coughs and wheezes, like something big is coming out of her.."

    scene yuri_bathroom_01
    show daisy anxious at scene_left, flip
    show angel pain at scene_right


    "I tentatively open my eyes- her eyes are red, with a less vibrant light seeping out of her orifices. Her veins are pulsating and golden."

    camera:
        perspective True
        linear 1.0 zpos -500 xpos 300  ypos -175
    show daisy nervous at scene_center with moveinleft
    "I gently kneel down by her side, rubbing her back with my other hand. The other one stings too much, I left it limp beside me. My hand blisters as if it is stuck into a nuclear reactor."

    "Timidly, my head makes its way to the mirror.. Some sort of… sigil like drawing. A large circle with strange lettering was drawn with lipstick."

    "Samyaza weakly clenches onto my hand, she gently pets my burn mark. Still feeling the residual heat, I bite my lip to hold in the pain."
    show angel sad
    s "…We should do something about this…"

    show daisy nervous
    "I sigh, exhaustion catches up to me.{nw} "
    show daisy blush at scene_center_offright with moveinleft
    extend "Maybe that sigil has some sort of effect on me too, because I sheepishly lay  my head on her shoulder."

    "I’m so selfish, but I don’t care.{w=1} She lights a fire within me.{w=.5} I want the heat to melt us into each other at this moment."

#INT. APARTMENT LIVING ROOM - NIGHT
    scene black screen with dissolve

    camera:
        perspective True
        zpos -600 xpos -450  ypos -250
    scene yuri_living_room_night 
    show daisy anxious at flip, scene_left_far
    show angel sad at scene_center_offleft, flip
    show black screen
    hide black screen with dissolve
    "Samyaza sits, she’s hunched over, still catching her breath. Her exhaustion is palpable"

    "I walk over, handing her a warm cup of tea. I’m so useless, I can never really help people. I want to do more for her, but I’m still frazzled from whatever the hell just happened. I dig my nails into my legs."


    s "Hey, Daisy..{w=1} Don’t worry about it."

    d "…."

    s "Really, it’s not your fault."

    #DAISY (sad gay puppy eye etc sprite)
    show daisy anxious
    "Well… maybe If I didn’t ignore you all day… this wouldn’t have happened.."

    s "No, it’s not that…{w=1} It's fine. "

    "I can’t bear to look at her."
    camera:
        perspective True
        linear 2.0 zpos 0 xpos 0  ypos 0
    show daisy at scene_right,unflip with MoveTransition(2.0, leave=offscreenleft, leave_time_warp=_warper.easeout) #tbd define this
    "I uncomfortably scooch away. I still feel the heat emitting from her, but I’m far enough to be edged by it."
    show angel at flip
    s "I should tell you about something."
    show daisy nervous at unflip
    "My head is hung down. I peep in her direction."

    s "I’m not… really what I say I am. {nw}"
    #[happy/genuine sprite]
    extend "Hah. that must be obvious by now."


    "My expression is unchanged. Trust me Samyaza,{i} whatever it is {/i}, it can’t be any worse than me."

    show angel idle
    s "I’m not from here, like from Earth. "
    show daisy surprised
    "Huh?"

    d "..An Alien..?"
#sprite here
    "Samyaza weakly laughs."

    s "You’re so cute.. No, like...{w=1.0} well, why don’t I show you."
    show angel at unflip

    "After that, she takes off her vest. Two painful bumps, almost like large hard cysts infested themselves on her back. Her sweat glistens under the light of the cheap ikea lamp."

    s "Feel them."
    show daisy at scene_center with moveinleft
    show white screen with dissolve:
        alpha 0.25
    show daisy sappy
    "I slowly bring my hand over, it’s softer than I expected. But extremely hot, a bright light peeks through one orifice."
    "My hand stings, but I won’t dare pull away, the thought of it weighs down my heart."

    show daisy surprised
    d "This looks really painful…"

    s "It’s not that bad. What must be really painful is your wrist. I’m sorry about that."
    d "No, it’s okay…{w=1} as long as you’re alright."

    show daisy nervous
    show angel behind daisy

    show black behind daisy with dissolve:
        alpha 0.8
    "I caress the cysts, hoping it’d soothe her pain. After how much misery I’ve caused her, it’s the least I could do."

    "What even is she? What’s even fucking happening? I don’t want to bother her anymore than I already had either, so I suck it up."
    show black behind daisy with dissolve:
        alpha 0.95
    "My body feels compelled to get on the ground, and beg for her forgiveness."
    "Humiliating myself with tears, and repeating myself so much that my mouth shrivels up."
    "The only thing I can do is withstand the pain of her searing skin as I pat her wounds."
    hide black with dissolve
    show angel sad
    s "I’m scared to tell you the truth..{w=1} But just now, I really want to go back home. It seems like I’m not reacting well to this new body.."

    show daisy surprised
    "I tilt my head."
    show angel sad
    s "Sorry. I don’t mean to worry you."

    d "No..{w=.5} I’m just..{w=.5} Confused."

    #SAMYAZA (frown sprite)
    show angel frown
    s "Don’t worry about it…"

    "I gather up all my strength, I spit out the words, stuck like phlegm, in my throat."

    show daisy anxious
    "No, Samyaza.. I want to help you, please tell me what it is."
    #sprite time
    #show angel frown
    "Her face twists into a mix of satisfaction, and concern."

    s "Can I tell you a story?"

    "I bob my head."
    hide white
    show black screen behind daisy, angel with dissolve:
        alpha 1
    
    s "Lets say, heaven is real. Would that drive you mad?"

    show daisy happy
    "That’s a question..!"
    show daisy idle
    s "Well..?"
    show daisy anxious
    d "I don’t know… I never had the best relationship with that stuff. I guess it depends?"
    show angel sad
    s "Would you want to die?"
    
    show daisy surprised
    "I raise my eyebrows at her."
    show angel confused
    d "What??"

    show daisy nervous
    "She’s so intense and sweltering. I shrink into myself."

    d "…Sorry…"
    show daisy surprised
    show angel frown at flip
    "Samyaza grabs my burnt wrist. It hurts less now after she bandaged it."

    s "Don't apologize."

    "She doesn’t blink." 

    d "I don’t know…{w=1.0} I mean, I guess I’ve thought about dying before…"
    show daisy anxious
    "I grit my teeth through the lie, hoping beyond hope that she wouldn’t dig further."
    show angel sad
    s "Daisy…"
    show daisy idle smile
    d "No! Don’t worry! That’s all in the past…{w=1.0} things have been fun lately."

    show black alpha as ba behind daisy with dissolve
    show angel behind ba
    show daisy anxious at flip
    "I look away, hoping she doesn’t read me for what I am."
    "I mean, who knows what she can do."
    "I should be scared, shouldn’t I?"
    "I’m stepping too close to a flame that I know nothing about."
    pause 1.0
    show daisy blush
    hide ba with dissolve
    "But I can’t resist its warmth."

    show daisy at unflip
    show angel frown
    s "I will always, always be here for you. You are my first real human friend. You don’t know how much you mean to me."

    show daisy idle
    "Her grip is tight. I hold in my confusion at her passion."

    d "Do you want to go back to the story?"


    s "Oh.{p=1}Right."
    show angel sad
    s "Well, let’s say there {i}is{/i} a heaven. And amongst its denizens, guardian angels exist. Their sole purpose is to protect humans with their brethren."

    s "Now…{w=0.5} let’s say that one particular guardian angel failed. Her love for humans is far too strong for her to handle."

    s "The angels send her away. She now lives her days with a maddening silence. An emptiness that’s impossible to fill."

    hide black with dissolve
    #(FADE BACK TO INT - LIVING ROOM)

    show daisy idle
    d "What will the angel do now?"

    s "After a while..{w=2} {nw}"
    #sprite
    show angel frown
    extend "After a while of living aimlessly, with her days blending in together, she remembers something she heard a long time ago; about a human who tried to reach the angel’s level…{w=1.0} Maybe, this could help her return home.."

    show daisy anxious
    d "So...{w=1} you’ll leave?"

    #SAMYAZA (sighs)
    show angel sad
    s "I’m unsure, I’ll have to see. "
    show daisy nervous
    d "I don’t know if I like this story."

    show daisy crying at flip, scene_right_far with moveinright
    "I tear up, facing away."
    show angel confused
    s "You don’t want to help me?"
    show angel pain
    d "{b}{shader=jitter:u__jitter=1.0, 3.0}No, that’s not what I meant!{/b}{/shader}{nw}"
    d "{b}No, that’s not what I meant!{/b}{nw}{fast}"
    show angel sad
    s "I need a human to help me with this ritual. The only person I want to help me is you."

    show angel at scene_center_offright with moveinright
    "She scoots closer to me, but I feel like I'm sinking.{p=1.0}Some stupid girl like me would probably just mess it up. "

    s "You’re the most beautiful human I’ve met. You have the brains to do this."
    show daisy blush
    "I blush. She’s probably just trying to fool me. I won’t fail for these tricks. Something as ethereal as her could never love me."

    d "...{w=1}I’ll help."


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

    
