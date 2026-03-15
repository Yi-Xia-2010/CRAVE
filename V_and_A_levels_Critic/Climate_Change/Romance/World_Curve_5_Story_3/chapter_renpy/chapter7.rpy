label chapter7:

    # [Scene: Verdant Terrace | Morning — Busy, sun through pollen haze]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Fast, rhythmic percussion with bright strings — a marching, hopeful pulse]
    # play sound "sfx_placeholder"  # [Sound: Sawing timber, calls across beds, the click of Elias's camera, distant gulls]
    "You come up the fire stair and the Terrace greets you like a living thing—soil warmed by yesterday's sun, a row of newly cut planks leaning like a promise against a trellis, the faint metallic tang"
    "of rainwater barrels. Hands are everywhere: transplanting, stitching, hammering. The air smells of wet earth and sawdust and the citrus oil Mina uses to keep the tools from rusting. Your notebook tucks against your ribs; the"
    "pages there are a map you've already chosen to follow."
    show elias_chen at left:
        zoom 0.7

    elias_chen "You're up early. Thought you'd be in the subbasement ignoring sunlight."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "I have models that need sunlight to behave,' you say, and there's a smile tucked behind the sentence. 'Also—people need me looking like I belong here."

    elias_chen "You belong like this. Eyes glowing with schematics."
    "He angles the camera toward you; you pretend to glare, but your shoulder loosens. He hands the camera back and wipes a smear of mud from the lens with a corner of his bandana, fingers smudged"
    "with soil. He moves quick, his energy infectious, catching moments and making work look like celebration."
    "You step into the workline where volunteers lift the first barricade frame. Your hands know the rhythm: measure, mark, saw, brace. You set the angles, calling out lengths. Your tattered notebook is open on a crate—diagrams,"
    "sensor pinouts, the sorts of sketches that turn a ragged plan into something that will stand in wind and salt. You listen as conversations unspool around you—someone talking about a neighbor's flooded stoop; another person quoting"
    "a slogan for the banners—and fold that human data into the shapes you build."
    hide elias_chen
    hide aiko_mori

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rasp of a saw; a hammer landing in time with the percussion in the music]
    "Elias Chen leans over the crate and reads a line in your notes."
    show elias_chen at left:
        zoom 0.7

    elias_chen "Citizen-run sensor grid. Low-cost nodes. Open data. You really did plan for us to read the tide like a language."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "We need eyes on the water that anyone can understand,' you answer, voice low but firm. 'If HelioCorp won't give us transparent tools, we build our own. The sensors will map pressure, salinity, flow—simple things. Community owns the feed."

    elias_chen "And you lead it."

    aiko_mori "I lead the math. You lead the people.' You pause. 'We make sure they stay together."
    "There's a moment—short, bright—where the Terrace seems to hold its breath with you. Then Mina calls out, laughing, and the work resumes. You feel the lift of it: practical, communal, immediate."

    menu:
        "Attach the banner that reads 'OUR SHORE, OUR RULES'":
            "You pin the banner above the barricade; it snaps in the wind like a vow. People pause and clap, some wiping eyes. A kid runs under the banner grinning as if she owns the sky."
        "Use the gentler slogan: 'Neighbors First, Science Together'":
            "You secure the softer banner. A few neighboring organizers exchange approving nods—it's measured, hard to attack. Elias takes a photo, framing the banner with hands at work beneath it."

    # --- merge ---
    "The community reaction folds back into the day's work and planning; the Terrace continues its preparations."
    # [Scene: Verdant Terrace | Midday — Assembly and Sensors]
    hide elias_chen
    hide aiko_mori

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussion rises; brass enters for a bright, urgent lift]
    # play sound "sfx_placeholder"  # [Sound: Murmured coordination; the high chirp of a freshly programmed sensor booting]
    "You climb the scaffold with a spool of cable and a weight on your shoulder. The Terrace is a hive; Rafi is there too, recorder tucked against his chest, asking quick questions between running off to"
    "fetch printouts. You strap a weatherproof node beneath a trellis—its casing plain and home-made, its guts an elegant bricolage of sensors purchased with pooled funds. You plug it into the little solar puck that will keep"
    "it alive through cloudy weeks."
    "Internal math ticked through your head: power budgets, transmission windows, redundancy maps. You trace the code (written in your neat block script) into the notebook margin and explain it aloud so volunteers understand why the node"
    "must face the bay, why the antenna tilt matters. Teaching is an extension of building; every person who knows the node's name is a person the shoreline can trust."
    "Rafi returns, cheeks flushed with wind and news."
    show rafi_alvarez at left:
        zoom 0.7

    rafi_alvarez "You need to hear this. HelioCorp's contracts—there's language in their staging agreements that could let them claim infrastructure as proprietary if it's within X meters of their sites. It's subtle. It's predatory."
    "The air thins for a beat. People pause; a tray of seedlings is forgotten in someone's hands."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "Read it."
    "Rafi unfolds printed pages, pointing to underlined clauses on brittle paper. You read the legalese—clauses that would turn public data into private property through ownership-by-proximity, clauses that would let a corporation veto community sensors within declared"
    "operational perimeters. Your chest tightens—not from fear, but because the facts turn your plan into fuel."
    show elias_chen at center:
        zoom 0.7

    elias_chen "So they come in and set up 'temporary' staging, and overnight our cooperative tools could be swallowed by their legal fog."
    hide rafi_alvarez
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "Then they don't get a foot over our threshold."
    "Sora, sitting on a low crate with her walking stick across her knees, speaks without rush."
    hide aiko_mori
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "Words on paper are branches that bend the wind if you let them. We are wind too."
    "The conversation branches and loops—legal strategy, public messaging, possible escalation. You moderate, bringing attention back to practical safeguards: timestamped data logs, distributed backups, physical marker buoys that declare community-maintained zones, the plan for a public archive."
    "You write an action list on a reclaimed signboard. People volunteer for night rotations, for legal liaisons, for sound systems at the blockade. The energy grows, tight and taut like a bowstring ready to release."

    menu:
        "Make the clause your opening line at tonight's rally":
            "You nod toward Rafi. He feels the weight of the words you choose, then grins a little and says, 'We'll give them rope and show them the knot.' The crowd responds with a low, focused murmur—rising, ready."
        "Hold the clause for the legal packet; focus the rally on the human story":
            "You decide to lead with Mina's story of the fishing nets. Rafi tucks the pages back into his jacket—quietly satisfied. The rally becomes a chorus of memory and loss that draws people closer."

    # --- merge ---
    "Regardless of framing, the rally galvanizes volunteers and resources; plans continue toward the blockade."
    # [Scene: Old Beacon | Night — Planning Circle]
    hide elias_chen
    hide mina_kuroda
    hide sora_watanabe

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: A steady drumbeat under warm strings — intimate but driving]
    # play sound "sfx_placeholder"  # [Sound: Low voices, cups clinking, the distant rumble of a city that hasn't slept]
    "The Beacon holds your circle like an ember. Mina ladles stew into bowls and everyone eats standing, elbows touching. Sora moves through the rotation chart—names, times, backup pairs. The Beacon is not a building tonight; it's a human machine: nodes set to watch, hands set to act."
    "Elias Chen sits close, camera temporarily idle. He speaks softly, but his words carry."
    show elias_chen at left:
        zoom 0.7

    elias_chen "We block the staging area at first light. No violence—just bodies, banners, cameras. We hold space. We make it visible."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "We also need a technical perimeter. I'll deploy quick nodes on bikes and pumps. If they try to claim the sensors, we have photos, time stamps, and off-site backups."
    show rafi_alvarez at center:
        zoom 0.7

    rafi_alvarez "I've got the HelioCorp lawyers' names. I can feed the phrasing to a sympathetic reporter. Public pressure will make it harder for them to smother us."
    hide elias_chen
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "We'll feed anyone who shows up. If you stand in the rain with an empty stomach and someone hands you a bowl, you'll stay."
    hide aiko_mori
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "And remember why we're here. The sea keeps taking if we don't stand. We are not just fortifying bricks and boards; we are keeping stories alive."
    "You make a list in the margin of your notebook—who will handle the node backups, which valves to test on the pumps, who will film, who will keep the legal packet within reach. Each item is"
    "a small contract, given and accepted. The mood hums; it's urgent, but joyful in the way that solidarity often is: people making each other stronger because they can."
    "Dialogue stretches, overlapping as plans refine. The Beacon's lamp sways; your hand traces the names on the rotation chart like a promise."
    hide rafi_alvarez
    hide mina_kuroda
    hide sora_watanabe

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Rapid strings swell — a building, thrilling rise]
    # [Scene: HelioCorp Staging Area | Pre-dawn — The Blockade]

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: High, urgent percussion; brass hits accentuated by sharp string stabs]
    # play sound "sfx_placeholder"  # [Sound: Wind along concrete, distant engines idling, the murmuring crescendo of a crowd that is becoming a single organism]
    "Dawn is a bruise-pink edge along the skyline when you arrive at the staging area. The corporation's floodlights throw everyone's shadows long and hungry across the pavement. Volunteers form chains; Mina and Sora check first-aid kits;"
    "Elias Chen moves through the ranks like a bright node, taking photographs that capture hands, faces, the way banners fold like flags. You move methodically, attaching a final sensor node to the hood of a community"
    "van—cheap, duct-taped, brilliant. It faces the staging area and begins to whisper telemetry into the network. Your chest is a drum."
    "People chant in low, structured bursts—lines taught and practiced so no one has to think at the moment when fear would otherwise sharpen. The sound is a living thing: rhythm and insistence."
    "Rafi stands near the front, voice up, handing copies of the clause he found to press volunteers and to anyone who asks. He gestures to the page and then to the crowd as if translating law into narrative."
    show rafi_alvarez at left:
        zoom 0.7

    rafi_alvarez "They promised to protect us. Their contracts say they'll do it on their terms. We say: not on our soil."
    "A cluster of security personnel appears at the perimeter—sleek, corporate, calm in a way that tries to be intimidating. The trucks sit, engines idling, swollen with crates labeled in geometric fonts. Someone on your side—young, hands trembling—starts singing, and others pick up the melody. The song stitches courage into bodies."
    "You feel the arousal in your nerves now: high, sharp, a focused energy that runs through every volunteer. Your mind sorts: monitor feeds, legal standby, med teams, media positioning. You think of past storms, of Sora's"
    "patient history, of Mina's food, of Elias Chen's buoyant belief that people will move like tides when led. You think of your notebook, of the code that pulses life into a sensor, of the ledger you're"
    "writing with your hands and with the city's feet."
    show elias_chen at right:
        zoom 0.7

    elias_chen "This is it."
    show aiko_mori at center:
        zoom 0.7

    aiko_mori "This is ours."
    "You hear the crunch of gravel under boots as someone at the staging gate fidgets with a clipboard. The security team straightens, the corporation's representative steps forward with an expression that is too polite. Cameras tilt; drones hum in the far distance like bored wasps."
    "You scan the crowd—Mina with a thermos, Sora murmuring a blessing, Rafi counting breaths before he speaks, volunteers linking arms. Everything narrows to the line in front of you: bodies, banners, the gap between the trucks and your people. The moment is electric, full of forward motion and unspoken stakes."
    "Your breath is a metronome. You can feel the community's pulse matching it. There is a decision in the immediate air—a pivot that will mark the ledger many different ways. You are poised at the fulcrum. The sound of a chant rises and fills your ears."
    "Page-turn thought: The whole Terrace and Beacon and every small act that led here compress into the seconds before you. You do not know the outcome. You know only the truth of the present: that a"
    "thousand small preparations have aligned into one action, and that whatever happens next will be the story you write together."
    hide rafi_alvarez
    hide elias_chen
    hide aiko_mori

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
