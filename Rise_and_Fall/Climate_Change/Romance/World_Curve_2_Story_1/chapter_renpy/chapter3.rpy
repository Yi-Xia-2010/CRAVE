label chapter3:

    # [Scene: Old Lighthouse Ruins | Dusk — Storm Approaching]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through ruined brick, distant gulls cut off by the weather; rain tapping a slow staccato on exposed stones]
    # play music "music_placeholder"  # [Music: Low, mournful strings; a cold undertow]
    "You leave Harborfront with the taste of salt and neon in your mouth, the memory of the model under its shroud pressing at the back of your teeth. The boardwalk thins into rutted earth and then"
    "into the marsh, where the spartina leans and the mud is the color of old coins. The lighthouse waits at the edge of the world — crumbled, stubborn, a place you've always come when you need"
    "to remember that the sea does not yield to plans."
    "Your jacket is damp. The bronze pendant hangs heavy against your sternum, a familiar, private weight. Your notebook is tucked into your side like a talisman; the pages are full of margins and small handwriting that has felt, lately, too timid."
    "You sit on a low, moss-softened step and let the wind take the rest of you. The rain drums harder; salt and wet brick rise to your face as if to make you taste the decision"
    "on the air. The guilt you carry — the misforecast that still rounds the inside of your skull like a small, unfinished sentence — hums under everything. In the quiet before Cass speaks, you imagine what"
    "would happen if you are wrong again: who would get displaced, what nets would be lost, which memories would be buried under new concrete."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Fabric whispering; the faint electronic ping of a watch against their wrist]
    # play music "music_placeholder"  # [Music: A thin piano line, patient and contained]
    show cass_adler at left:
        zoom 0.7

    cass_adler "You found the lighthouse,"
    show maya_rios at right:
        zoom 0.7

    maya_rios "It's where plans go to be reminded they're not everything."
    "You answer (soft, but firm). You close your notebook a little harder than necessary."
    "Cass steps closer; up close their face has the same edges you remember from university—too precise, too practiced—but weather softens the lines. Rain paints their hair darker at the temple. Around their mouth, something unreadable moves."

    cass_adler "I didn't come out here to argue in the open. Not tonight."
    "(They glance at the water.)"

    cass_adler "Listen — let me be blunt. Aquila needs someone with credibility to sign off on the shoreline elements. They'll buy the optics of 'community oversight' if it's framed right. If you help me from the inside, I can put living-shoreline features into the proposal and lock in a structure for local governance. We can get protection and keep the community voice from being performative."
    "You hold that like the phrase it is: both a promise and a marketable product. You can see, as plainly as the slick model they pulled from the crate, the schematic in their head — steel and marsh stitched together by language that sells."

    maya_rios "And why would you want that?"
    "You ask. 'You've made your life offering scale. Why trade control for...for compromise?'"
    "Cass lets out a small, bitter laugh that is almost a wind gust."

    cass_adler "Because scale without legitimacy is fragile. Because I made calls that worked on paper and failed in places that mattered. Because I don't want to be someone who only builds monuments. And because —"
    "(their eyes flick to you, and for a second there's a softness)"

    cass_adler "— because you were the best person I trusted at uni. You know how to make something defensible that still smells like place. Help me frame it so it's not Aquila's plan but the town's future."
    "You feel the pull of old collaboration — late nights with coffee gone cold, the thrill of solving a problem on a whiteboard — and the current of betrayal that lives in promises from corporate lips."
    "Cass's proposal is a bridge thrown between two cliffs. It's tempting. It is also a place you could fall."

    cass_adler "We'd be inside. We could fight from within. You wouldn't have to risk arrests or dangerous midnight work. You'd have data, clout, and leverage."

    maya_rios "Leverage that comes with strings,' you reply. 'And what if those strings are cut in the meeting room and left dangling while the seawall gets poured?"
    "Cass gives you a level look — inscrutable, the way tide charts hide the riptide until you're caught."

    cass_adler "You help me write the clauses that mandate community oversight, that keep maintenance and decision-making local. I can put pressure in the right rooms. But I can't do it without you."
    "Silence settles like a wet cloth between the three of you: the lighthouse, the water, and the words that could reroute lives."

    menu:
        "Ask Cass to explain exactly how oversight would be enforced":
            "Cass taps their watch, then speaks in a slower, more technical cadence. They outline a tiered trust model, mentions escrowed funds and a community board with veto power — dense words that sound like protection until you notice the clause about 'market-rate partners.' You file each phrase against your memory and your doubts."
        "Tell Cass you need to sleep on it and won't be used as a prop":
            "Cass's expression thins; their voice goes quiet. 'I know this asks a lot,' they say. 'But if you don't move, someone else will fill the slot.' The sentence hangs like a warning and a plea."

    # --- merge ---
    "The conversation continues."
    "The night breaks around the edges of your choices like the sea breaks against the rocks: loud, insistent, and inevitable."
    # play sound "sfx_placeholder"  # [Sound: Boots on wet stone; a voice, closer, edged with anger]
    hide cass_adler
    hide maya_rios

    scene bg ch3_98c6f2_3 at full_bg
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You're not seriously considering this?"
    "His hurt is raw enough to be a physical thing. He moves as if to shore you with his body, to pull the question back into the harbor where the people are."
    show maya_rios at right:
        zoom 0.7

    maya_rios "Eli—"
    "You try to keep your tone even; your mouth tastes of salt and the remainder of untaken promises. 'I haven't decided anything.'"

    eli_navarro "You haven't decided — or you're deciding for us? For the people who will lose their moorings if Aquila 'refines' them away with a prettier model?"
    "He steps closer, and thunder underlines his words. 'We don't hand them the town because they have a glossy plan and a bank balance.'"
    show cass_adler at center:
        zoom 0.7

    cass_adler "Eli, it's not—"
    "(They raise a hand in placation that only makes matters worse.)"

    cass_adler "This isn't about handing anything away. It's about integrating proven protections with local stewardship so people can stay. We can avert displacement."

    "Eli lashes back, voice thick with something that could tip into fury" "You speak about averting displacement like it's a checkbox. You weren't here when the nets gave out. You weren't here when people had to choose between paying the dock fees or keeping the lights on."
    "Cass's jaw tightens; they look older in the rain, the sheen of public polish clinging to them like water."

    cass_adler "And you think small gestures and barricades will hold? The sea doesn't negotiate with blockades. We can get the resources to build protections that last. If you sabotage that, what then? Arrests and no wall."
    "Ivy's voice cuts through like a bell."
    hide eli_navarro
    hide maya_rios
    hide cass_adler

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A dry laugh undercut by determination]
    show ivy_okoye at left:
        zoom 0.7

    ivy_okoye "If Aquila gets in, they will pave over our rights and call it resilience. Civil disobedience works. It gets headlines. It makes the cost of eviction political. It makes it harder for them to steamroll us."
    "She steps closer to Eli and locks eyes with you. 'Maya, we can stand in the way. We can expose the model for what it is. We can show people there are alternatives that don't involve corporate boards.'"
    "You feel the marsh under your boots as literal and metaphorical ground. Ivy's words carry the clack of a thousand leaflets and a hundred phone calls. They also carry legal peril, the possibility of arrests, and worse: the memory of that misforecast whispering that taking bold action could end poorly."
    show maya_rios at right:
        zoom 0.7

    maya_rios "So the options are — sit inside and try to change language, mobilize and risk escalation, or go rogue and do unpermitted restoration?"
    "You don't say the last part aloud, but it hangs between you like a low cloud."
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "If you take them in, Maya, you make a deal with people who will put their logo over our graves. They will call it a gift while erasing the people who remember us. You can't build trust back after that."
    hide ivy_okoye
    show cass_adler at left:
        zoom 0.7

    cass_adler "Trust can be institutionalized. We can require local control, audits, community trustees. We can make this a model other towns use. You could be the one who makes that possible."
    hide maya_rios
    show ivy_okoye at right:
        zoom 0.7

    ivy_okoye "Or you could let them in and watch us get priced out."
    "She points, rain making the gesture theatrical. 'That's not a model; it's colonization with better lighting.'"
    "The wind tugs your hair, the ocean speaks in layered voices. Your chest feels raw, as if you've been rinsed by cold water and left to shiver. The three arguments — inside change, mass resistance, and"
    "unpermitted immediate restoration — are each attractive and terrifying. Each contains a promise and a poison."

    menu:
        "Tell Ivy you'll support a rapid, visible demonstration instead of illegal restoration":
            "Ivy narrows her eyes, measuring you. Relief and suspicion flicker across her face. 'Good,' she says slowly. 'If we mobilize fast, we can pressure the council and make Aquila sweat. But you'll have to show up in public—not just talk from the inside.' The rain seems to listen."
        "Admit you're tempted by working inside Aquila to shape their plan":
            "Eli's expression fractures between betrayal and a pleading hope. 'If you go in,' he says quietly, 'be honest. Don't let them use your name to polish a lie.' You feel his hands—unoffered—reach for you, a steadiness you are suddenly aware you've been leaning toward for months."

    # --- merge ---
    "The decision tightens; the scene moves toward a major choice."
    "You stand on the slippery stones of the lighthouse, rain blurring the edges of faces and the town's map. Each possible path is a current pulling at different parts of you: the scientist who craves robust"
    "data and leverage, the community member who can't bear to see elders priced out, the woman who lives in a place that remembers the sea more powerfully than any law."
    "Your misforecast hums like an undertow. You imagine making the wrong call and watching the marsh—your life's work, and the community's heartbeat—bend or break. The wind carries the faint, impossible thought that every path will cost something essential."
    "Cass steps back a few paces, rain forming thin rivers down their collar. Their look at you is complex — respect braided with ambition, old affection and the hard edge of an operator."
    "Eli stands with the full weight of the harbor and its people behind his words; his anger is a shield and a spear. Ivy's stance is all motion and immediate consequence, future headlines and the courage of bodies in the face of bulldozers."
    "You find your thumb worrying the corner of your notebook, the way you used to when you needed to choose a variable in a model. The lighthouse hums with electricity from the storm, and for the"
    "first time you realize how tired you are of the idea that a single decision should hold the burden of everyone's future."
    "A gust of wind flings rain across all of you. The sea answers with a distant, thunderous swell."
    "You inhale. The choice is sharp and immediate."

    menu:
        "Work with Cass inside Aquila to try to steer the plan toward a hybrid, community-led model.":
            jump chapter4
        "Organize public resistance with Ivy and Eli—blockades, petitions, and direct negotiation pressure.":
            jump chapter9
        "Lead an unauthorized marsh restoration at night—earthworks and oyster re-siting—hoping to show a viable alternative.":
            jump chapter12
    return
