label chapter5:

    # [Scene: Collapsed Pier | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls cut through chants; water lapping against splintered pilings]
    # play music "music_placeholder"  # [Music: Low, insistent strings; a slow, sinking heartbeat]
    "You chose to come. It is a decision you can still feel like a bruise: deliberate, present, and impossible to hide. Your boots squelch salt and sand onto the rotten boards; the fabric of Elias Novak's"
    "scarf — looped once around his neck, flecked with tide — brushes the back of your wrist when he leans close. The scarf smells faintly of detergent and seaweed and the sharp, burned sugar of coffee"
    "from too-quick dawns. Elias Novak's hand, warm and steady, rests for a breath on the small of your back. It is an anchor you didn't realize you needed until now."
    show elias_novak at left:
        zoom 0.7

    elias_novak "We sit. We won't move until they notice we won't let them push this through without us."
    "You hear the conviction in his voice, and beneath it the tremor you'd felt at the dunes: the thrill of a crowd that thinks it can bend a policy like metal. Around you, neighbors press together."
    "Someone drums calluses on a reclaimed crate. Signs flap like tired birds: HANDS OFF THE HARBOR / SALTBRIDGE LIVES HERE / COMMUNITY NOT CONCRETE."
    "The police form a kettle — a slow tightening circle. Their boots on the wooden slats sound too precise for a place that has fallen apart; it is a sound that says containment, not conversation. Cameras"
    "angle from the fringe, lenses like hungry eyes. A man with a broadcaster's jacket stands just beyond the line, microphone held out as if anything you say will be a line in a script he already"
    "wrote."
    # play sound "sfx_placeholder"  # [Sound: The sharp crack of breaking glass]
    hide elias_novak

    scene bg ch5_4001e7_2 at full_bg
    # play music "music_placeholder"  # [Music: A sudden staccato hit; a collective intake of breath]
    "Someone—an older woman with weather-lined hands—throws a bottle and the bottle meets a lens. The crowd surges, noise rising until it feels like a physical thing. Within minutes, the press will tell it as headline fodder: the movement turned violent. They will lean into the frame they prefer."
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "Maya—move!"
    "You look up and see Finn sliding across the pier, the board under his foot splintering with a sound like a broken promise. He grabs for the crossbeam and hits the edge of exposed metal. A"
    "shallow piece of rebar catches him under the shoulder. The world narrows to the color of his shirt, to the red blooming across the denim."
    "You lurch forward and your knee catches on wet wood. Saltwater sprays your face. The taste of metal roars in your mouth. People shout—instructions, prayers, names. A uniformed officer pushes through the press, shouting for hands"
    "to be raised. A line of officers forms, then reforms as more bodies press against the perimeter."

    menu:
        "Call out for medics":
            "You shout until your throat cracks, pushing against the tide of people to get to Finn. Someone hands you a bandage; a neighbor's breath smells of eucalyptus as they hold his head. The medics find him, but you notice the hollow in his statement: he used to be younger than this injury makes him sound."
        "Stay seated and document":
            "You keep your place on the plank, fingers already pulling your notebook from your jacket. Your pen finds the edge of the event in quick, furious lines. You register Finn's fall as an index of risk—vital evidence—while a piece of you prays someone else will save him."

    # --- merge ---
    "Both outcomes resume the main narrative."
    "Elias Novak reaches you as the officers begin to separate bodies. His hands are on your shoulders and his amber eyes are furious and wet."
    show elias_novak at right:
        zoom 0.7

    elias_novak "You didn't—' [he swallows] '—you shouldn't have been where that board gave way. I told you—"
    show maya_serrano at center:
        zoom 0.7

    maya_serrano "I know.' (your voice is thin; you taste salt and the iron of Finn's blood in the air) 'I couldn't stand there and watch them pretend we didn't exist."

    elias_novak "We can hold the line without getting people hurt. We can—"

    maya_serrano "We can't wait for perfect plans when people are losing homes."
    "There is no clean motion. Hands clamp on wrists. A uniform grips Finn's arm and tries to help and then wince because the wound is worse than it looks. Someone is on their phone, a low,"
    "accusatory voice telling a dispatcher there were rocks thrown. A protester kneels, fingernails digging into wood, trying to hold a splintered board in place."

    "A surge and then the world shifts into the mechanical rhythm of arrests. Voices reduce into odd, clinical phrases" "You are under arrest,' 'Step back,' 'Stay seated."
    "Rosa Alvarez's voice comes through a chorus of static—snapped words passed along by a volunteer on the perimeter. 'Maya—there's a message at the café. Spray-painted on the door. Said 'KEEP QUIET OR ELSE.' No one's inside. People are scared to come down.'"
    hide finn_serrano
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "I locked the ovens. I put out a note on the chalkboard. No one wants trouble, Maya. But when those cameras show people smashing things—"

    maya_serrano "They didn't see the boards that were already gone. They don't see the people who can't afford to move."

    rosa_alvarez "I know what you're trying to do. I just—' (her voice nearly breaks) 'I need the café to be safe. It's where Finn learned to tie knots with the fishing rope. It's where old Mr. Del Rio takes his tea at noon. People live through that doorway."

    maya_serrano "We'll get through this. I'll—"
    "There is no easy reconciliation between the urgency of now and the habit you have of accounting for everyone's thin margins. The kettle tightens like a noose around your plans."
    # play sound "sfx_placeholder"  # [Sound: Handcuffs snapping; a fluorescent buzz beginning like a distant thunder]
    hide elias_novak
    hide maya_serrano
    hide rosa_alvarez

    scene bg ch5_4001e7_3 at full_bg
    "The arrest process is sloppier than the calm, practiced choreography you imagined. Names are shouted; wrists are stamped with an ink that stings and then settles into a bruise-colored ring. An inked bracelet — a plastic"
    "band stamped with a docket number — is fastened around your wrist. Cold plastic cools your skin; the band feels like a small circlet of failure."
    "They herd you onto a transport van. Bodies press against you from all sides; you taste diesel and the sharp lemon of disinfectant. A woman two rows down sobs silently into a sodden sleeve. Through the"
    "slatted windows, Elias Novak stands outside the kettle, not moving to follow. He is outside the legal line, his face lit by duty and something that looks like apology."
    show elias_novak at left:
        zoom 0.7

    elias_novak "Maya! They'll spin it. They'll make it look like we wanted violence. Hold the line in whatever way you can—hold them to the truth."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Hold them to the truth."

    elias_novak "I'm going to get everyone legal help. I'm—' (his voice breaks, and the break is a new thing; it is intimacy carved into urgency) 'I'm so sorry, Maya."

    maya_serrano "Don't be.' (you speak because you have to, because the protest has given you the words to fight but not the words to console) 'Just—come."

    elias_novak "I will."
    "The van doors clang shut. For a moment, you press your forehead to the window, trying to catch the smell of his scarf, to anchor yourself to an image of him whole. He plants his hand"
    "on the wood and looks at you levelly; one corner of his mouth tries to smile and fails. There is no easy comfort in that look — only the kind of raw, urgent love that obeys"
    "a higher law: the law of standing beside someone even when standing breaks you both."
    # [Scene: Boardwalk Holding Cell | Night]
    hide elias_novak
    hide maya_serrano

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of ventilation; distant footsteps and the thud of a cell door]
    # play music "music_placeholder"  # [Music: Sparse piano notes, cold and slow]
    "You ride the intake process like a dream you don't remember leaving. Names are taken and misspelled. Fingers press into the ink pad and then onto your wrist beneath the plastic band; the mark is a"
    "small, indelible cross. An officer takes your photograph — your hair flattening from the damp — and slides the paper into a file that will later be scanned by people who do not know Finn's name."
    "They put you in a holding cell that smells like wet coats and bleach. The fluorescent light stutters in a rhythm that makes everything look brittle, like old glass. You sit on a metal bench and"
    "the inked bracelet is a pulse of humiliation and humiliation is also, strangely, a small teacher."
    "You pull your Moleskine from inside your jacket. The leather is warm where your body heat has kept it. Your pen is a familiar instrument in a place that otherwise feels foreign. You open to a blank page and the hand that moves is your own, refusing to be erased."
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "List of what went wrong: logistics, scaffolding, rotten planks, inadequate medics on-site, communications drop, press narrative."
    "You write and write until the words loop and start to look like language someone else has used. You catalog failures as if inventory can make them smaller. Each note is a small stone placed in a line. The line holds, for a moment."
    "You think of the neighbor who died in the storm long ago — an image that returns to you like tide-worn driftwood. He was someone who counted his days in nets and slow coffee. You promised"
    "his porch light would never go dark on watch of your doing. Tonight that promise feels thinner than the band on your wrist. You catalog it in the book because naming a shame is how you"
    "keep it from becoming a ghost that eats everything."

    menu:
        "Write until the page is full":
            "Your pen skids over paper, small furious loops. Names. Times. Injuries. The act of listing steadies you. You map the cracks so you know where to hammer nails when morning comes. It is work and it is a prayer."
        "Close the book and stare at the light":
            "You slide the notebook back into the jacket and stare at the fluorescent bulb until the buzzing seems to echo a heartbeat. The silence lets images move through you with no barrier—Finn's face as he hit the beam, Elias's hand on the barricade. It is emptiness and it is full of accusation."

    # --- merge ---
    "Both outcomes resume the main narrative."
    "A guard slides a tray of plastic-wrapped food through the slot. The sandwich inside tastes like cardboard and salt. You pick at it. The fluorescent light makes your eyes look pale. Sleep does not come easily;"
    "exhaustion and adrenaline tango until one wins a moment's peace. You trace the red thread tied to your wrist with your thumb—an old knot of a promise you tied yourself—and feel the frayed fibers bite the"
    "pad of your skin."
    "Across the room, a man you recognize from the dunes — someone who had been filming the boards— coughs and laughs bitterly. 'They'll call us vandals tomorrow,' he says. 'They'll call us something that makes it easy to ignore the underlying math.'"
    "Finn is brought in hours later. He limps, favoring the left; his arm is in a sling and there's a dark bruise along his ribs. He does not make much of it. He presses his lips thin and sits beside you, not touching but present."
    show finn_serrano at right:
        zoom 0.7

    finn_serrano "I didn't want to stop anyone. I thought I could—' (he swallows and looks at the ink band on your wrist) '—I thought I could help hold the water out of the house myself."
    "Maya Serrano: (you reach for his hand and your fingers find the warmth of his palm; it is small and solid) 'You helped more than you know. You saved a kid who fell into the gaps. Don't—' (you can't finish)"

    finn_serrano "It keeps happening, doesn't it? The town keeps getting pushed into corners and then we run together and it's messy and proud and also—' (fear undercutting the pride) '—people get hurt."

    maya_serrano "I know.' (you think of all the nights you worked on donation lists and the dozens of spreadsheets where hope wore the cheap coat of statistics) 'I will fix this."

    finn_serrano "Not alone, Maya. Don't do it alone."
    "You close your eyes. The fluorescent light stares back. The ink bracelet around your wrist is a small, cold circle that tells you what you already know: moral clarity does not equal capacity. You can be"
    "right and still be unprepared. You can be brave and still let people get hurt."
    "There is a rustle at the cell's bars. A policeman slides a phone through and Elias Novak's face fills the small square, jittery and close. He has been battered at the edges — a smear of grit on his cheek, his scarf twisted — but his eyes are all fire."
    show elias_novak at center:
        zoom 0.7

    elias_novak "They're spinning it. The channel says there was 'chaos'—like that's the story that absolves them. I'm getting a lawyer. Rosa's okay—she's boarded up and texting me lists. Finn—' (he pauses) '—Finn's okay?"
    "Finn Serrano: (grunts) 'I'll live.'"

    elias_novak "Good. Listen—' (he leans forward, voice suddenly small) 'I thought I could hold a line without people breaking. I was wrong. I'm sorry I pulled you into the center of that."

    maya_serrano "You didn't pull me. I walked there."

    elias_novak "You shouldn't have been where you got hurt.' (anger, then softness) 'I can't make it go back. I can try to make it forward without the same mistakes. Let me help get people out of this."
    "Maya Serrano: (your voice thins) 'Help doesn't feel the same when it's a plan on a page. Help should feel like someone keeping watch.'"

    elias_novak "Then let me keep watch.' (and now there is a bristle of plea under the command) 'Let me be on the side where I can do that."
    "You look at the camera; you look at the ink on your wrist; you look at Finn. You remember the neighbor whose porch light went dark and the promise you tied to your skin with a"
    "red thread. The cost has been paid in bruises and broken boards and a night's worth of cold shivers."
    "You feel smaller than the person who stood on the dunes with a ledger of hope. The bottom presses in; the movement has moral clarity and diminished capacity. You catalog each misstep in your notebook because"
    "naming them is how you avoid repeating them—how you hope to make a different future possible—but the ledger itself feels like a poor substitute for a paramedic on time or a plank that doesn't give way."
    "The night drags thin. At some point, sleep threads through you and you dream of water in the kitchen; you wake and the light is the same, unrepentant. Elias Novak's call log stays on the phone,"
    "a bright square you tap and then put away. You run your thumb over the red thread on your wrist until the frayed fibers catch on the skin. The world outside still moves, indifferent and relentless."
    "A thought creeps in like tide over a dock: momentum without scaffolding becomes spectacle. Spectacle becomes story. Story becomes law in the court of public opinion. The calculus of choices is cruel."
    "You close your notebook and press the red thread to the dented compass at your throat, feeling the cold metal and the frayed fiber. You are not sure what the next move looks like. You only"
    "know this: tonight marked a trough you did not mean to find, and morning will demand planning that remembers every cost."
    hide maya_serrano
    hide finn_serrano
    hide elias_novak

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter7
    return
