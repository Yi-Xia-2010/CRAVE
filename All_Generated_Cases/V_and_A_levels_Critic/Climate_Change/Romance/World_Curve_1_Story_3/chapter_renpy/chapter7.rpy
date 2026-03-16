label chapter7:

    # [Scene: Glass Harbor Development Site | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant thrum of idling machinery; gulls cry; an undercurrent of chanting like a held breath]
    # play music "music_placeholder"  # [Music: Urgent percussion loop; strings building]
    "You arrived by the boardwalk, salt drying on your sleeves, the satchel against your hip heavy with seed tags and folded flyers. The decision you made in the atrium has a shape now — not a"
    "speech, not minutes and figures, but bodies, work gloves, and a fence that refuses to be only an advertisement for concrete."
    "Tala paces like a radiant metronome, corralling volunteers into neon-recycled vests that catch the harsh sunlight like little flags. She hands out clipboards with a grin that's all teeth and stubbornness."
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "Okay, okay — picket lines here, seed beds there. Reyes, you on story duty. Maya, can you run point at the rendering wall? Keep people focused on the memory pieces."
    "You nod and find that your voice is steadier than your stomach. Everything feels simultaneously lighter and more dangerous: the bright vests, the smell of fresh timber from the plywood boards, the metallic tang of exposed rebar, the hot glare of cameras already framing angles."
    hide tala_ruiz

    scene bg ch7_453e40_2 at full_bg
    "You move through the crowd in your boots, trading fist-bumps and anxious looks. Hands rough with rope meet your palms; a teenager whose hands smell of paint laughs briefly and then folds in when a developer's"
    "assistant passes a glossy envelope near the edge of the line. You see the shadow of uncertainty cross faces you know — taxes due, rent to pay, children to feed. The town’s practicalities whisper like tidewater"
    "at their heels."
    "A man in a developer jacket leans close to a volunteer and murmurs about 'expedited payouts' and 'relocation bonuses.' The volunteer glances at the envelope, then back at you. Your chest tightens."

    menu:
        "Step in and remind them what we're fighting for":
            "You crouch to their level and remind them of Captain Reyes' stories — of porches that used to look over reeds, not parking lots. Their jaw hardens and they tuck the envelope away."
        "Let Tala handle it; you have bigger tasks":
            "You pull back and let Tala smile her fierce smile. The volunteer looks to Tala and then nods; you feel guilt and relief braid together."

    # --- merge ---
    "Scene continues."
    "Tala notices the wavering and crosses to intercept the developer's assistant with a practiced smile that does not soften."
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "If you're buying folks out, you're buying silence, not solutions. We will hold this line; we will show the town a different way."

    "Assistant" "It's not personal. We're offering an option."

    tala_ruiz "We have options that don't erase half the marsh."
    "The assistant steps back. Tala winks at you — a private salute that says: keep going."
    hide tala_ruiz

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, attentive hush falls around him]
    "Captain Reyes shuffles forward, his voice a rough string tightened by memory."
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "You remember the old inlet? They used to tie nets on stones. The moon would lift the water and you'd swear the marsh breathed with you. We didn't ask permission then. We listened."
    "People lean in. Older neighbors wipe their eyes; the microphone picks up the cotton of breaths and the shuffle of feet on gravel."
    "His testimony is a lever. It isn't science on a graph; it's salt in the mouth, it's the ache of porches that sagged after a fever summer. It makes the renderings on plywood read like lies."
    "A police line holds a short distance away — more officers than you'd expected, caps bristling under the sun, a cold tape running like a second shoreline. Mayor Lionel threads between them, tie loosened, face flushed with the strain of compromise."
    show mayor_lionel_park at right:
        zoom 0.7

    mayor_lionel_park "Maya—please. The last thing we need is a headline about arrests. We've got offers on the table. Talk to me — we can get mitigation packages, job guarantees. We have to think of immediate needs."
    show maya_alvarez at center:
        zoom 0.7

    maya_alvarez "Immediate needs matter. So do memory and marsh. We can do both if we lead with repair and labor that rebuilds, not erases. Let us lay the pilot habitats and the seed beds. Show how lives stay put and livelihoods adapt."

    mayor_lionel_park "How many people will that employ, Maya? How fast? They want metrics. They want numbers before funding is cut."

    maya_alvarez "Then we will give them numbers. We will put these hands to work and make the proof right here.' (you glance at Evan's toolbox set near the denim bundles) 'But we need to stand together to get that proof."
    "Mayor Lionel hesitates — you can see the political calculus in his blink. He nods once, tiny, not surrendering, but not pulling police forward either."
    # play music "music_placeholder"  # [Music: Drums swell; tempo quickens]
    # play sound "sfx_placeholder"  # [Sound: Murmurs ripple into a rising chant]
    "Evan Kaito arrives like a contained storm: his jacket dusted with grit, hands already smeared with adhesive from transport, his face a study in quiet calculation. For a moment he stands at the edge — watching,"
    "measuring the crowd — and you feel the old memory of him at your shoulder in the atrium, the compass at his neck catching a sliver of light."
    hide captain_reyes
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "I shouldn't be here. They might use it against me... my old contacts—"

    maya_alvarez "You being here is what I need more than anything. Show them alternatives. Build with us, not around us."
    "He bites the inside of his cheek, hesitation cutting a line across his face, then he sets down salvaged panes of glass and rolls out coils of denim strapping. His hands move sure and fast, a small, steady engine making something out of discards."
    hide mayor_lionel_park
    hide maya_alvarez
    hide evan_kaito

    scene bg ch7_453e40_4 at full_bg
    "The pilot habitat goes up under a chorus of practical voices — a tongue-and-groove of reclaimed glass panes, denim holding joints taut, rope netting for plants to climb. Each snap of a clip, each hardened scrap"
    "of metal fitted in place, translates into a kind of promise: that adaptation can be beautiful, dignified, and local."
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "It needs to anchor deeper on storm side. If we can show this survives a surge, that's something they can't ignore."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Then we show them. Help me plant the cordgrass in the first tier."
    "He hands you a clump, eyes finding yours in a long, electric look that says more than the carefully neutral reports ever will. There's fear there — the kind that comes from the possible costs of standing firm — and something close to hope."

    menu:
        "Reach for his hand and steady the planting":
            "Your fingers lace with his for a second, muddy and warm. The contact steadies you both; the clump goes into the soil with less tremor than before."
        "Give him a quick, practical nod and get back to organizing":
            "You pat his shoulder and move on. The small distance between you is filled with work; the habitat gains form and the possibility of later words."

    # --- merge ---
    "Scene continues."
    # play sound "sfx_placeholder"  # [Sound: The crackle of a bullhorn; a legal envelope slapped against the fence]
    hide evan_kaito
    hide maya_alvarez

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Tension string plucks under the steady drumbeat]
    "A woman in Irene's team strides forward with the clinical calm of someone used to winning rooms. The legal notice reads like a paper tide: cease and desist, trespass warning, the developer's name sharp as a brand."

    "Irene's Aide" "We have served notice. You are obstructing a legally permitted site. Leave now and avoid further action."
    "Irene Vale stands behind her, immaculate against the dust — the too-exact line of her blazer a counterpoint to your frayed cuffs. She watches, expression unreadable but not unkind. The fence between you is only plywood, but it's a line drawn in ink and money."
    show irene_vale at left:
        zoom 0.7

    irene_vale "We can work with the town, Maya. There is room for mitigation. But there must be process."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Process has been going for years while the marsh drowned. These people are offering their labor and their homes to prove another way. They are not obstruction; they're stewardship."

    irene_vale "And if stewardship costs jobs? People will vote with their paychecks."

    maya_alvarez "Then we'll show a way to create paychecks that don't sell the marsh. Build livelihoods on restoration, not replacement."
    "Dialogue continues in overlapping, multi-turn exchange; Mayor Lionel interjects."
    show mayor_lionel_park at center:
        zoom 0.7

    mayor_lionel_park "Irene—both of you. This makes headlines. Arrests will bury plans. Maya, can you guarantee no arrests? Irene, can you delay enforcement? We need space to negotiate."

    irene_vale "I can ask for a pause. But the developers are within their rights to secure the perimeter."

    maya_alvarez "Pause, yes. But not at the cost of the marsh. Let us finish the habitat demonstration. Let Dr. Sora and the team measure the resilience. Put the enforcement on hold for 48 hours."
    "Irene's eyes flick to the reporters, to the cameras that make any concession into a headline. For a breath, everything feels like a coin wobbling on a ledge."
    # play sound "sfx_placeholder"  # [Sound: A reporter's microphone pushes through, urgent]

    "Reporter" "Mayor Park, are you asking police to stand down? Will this set a precedent?"

    mayor_lionel_park "We're seeking a peaceful resolution. People have reasons to be here."
    "The cameras sharpen. Phones lift like a field of white moths. The air tastes suddenly of ozone and salt. Volunteers tighten hands around picket signs. Tala starts a rhythm with a wooden mallet on a drum"
    "barrel; others pick it up, and a chant forms — imperfect, raw, gaining volume like surf growing toward shore."

    "Crowd" "For the marsh! For the marsh! For the marsh!"

    "You feel the chant enter your bones and rearrange them. The chain of seed tags is a frayed ribbon now; names written in marker, short notes pinned to the fence" "My father's inlet,' 'Our oyster beds,' 'Don't erase us."
    "Captain Reyes steps up and lays his own tag, his hand steady though his voice cracks."
    hide irene_vale
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "We remember. We will not sell our remembering."
    # play music "music_placeholder"  # [Music: Full swell; drums and strings in crescendo]
    # play sound "sfx_placeholder"  # [Sound: Police boots shuffle; a distant siren begins to give a single long note]
    "Your stomach twists with the old, animal worry of being taken from the place that has your bones. Fear edges every nerve — fear of arrest, fear of retribution, fear of failing the people who trusted"
    "you. Under that fear sits a firmer thing: a moral clarity that hums like a well-tuned wire. If you let this fence be only a billboard, the marsh will be gone. If you hold, even for"
    "a day, you create evidence of another path."
    "You step to the front, the first notes of the chant falling away as you lift the microphone Tala pressed into your hand. Cameras pivot; someone screams 'Maya!' and it folds into the chant."

    maya_alvarez "We are not a problem to be cleared. We are a community to be engaged. We will demonstrate repair. We will give you data and dignity both. This is our home. Stay here with us."
    hide maya_alvarez
    hide mayor_lionel_park
    hide captain_reyes

    scene bg ch7_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The siren resolves into two short, urgent blasts; police begin to form a closer line]
    "The officers step forward another ten paces. A uniform officer raises a hand and repeats the legal warning in the same flat voice as the paper."

    "Officer" "This is your final warning. Disperse, or you will be subject to arrest."
    "The crowd tightens as one organism. People lock arms, a chain human and practical, seed tags braided like beads between them. The media noise becomes a white static of anticipation. Your palms sweat where you're gripping"
    "the mic. If arrests come, the story will be bigger than this fence — it will be about a town choosing a future. If you step back, the developers may claim victory and the marsh will"
    "become a footnote."
    # [Music drops to a single sustained note; heartbeat tempo rises]
    "For a second, everything narrows to the sound of your own breath and Captain Reyes' low, steady humming of an old fishing tune. The chant rises again, louder, not angry but full of insistence."

    "Crowd" "For the marsh! For the marsh! For the marsh!"
    "You feel the tide of people beneath you — not just bodies, but history, labor, hunger, stubborn love. You can imagine the headline, the meetings, the slow work of proof that will come if you can"
    "hold this hour. You can also feel the scraping weight of legal papers and police lists pressing down."
    "You think of Evan's hands on the frame, Tala's grin, Captain Reyes' carved pillar. You think of your barometer necklace against your chest — a small, cold promise of measured weather and steady time."
    "A single officer moves forward, clipboard out, and the first name is called."
    "You realize that this moment will define the next months — whether the town keeps its marsh memory or trades it for quick, bright promises. Your throat tightens; you set your jaw and prepare to choose the action that will carry everyone forward."

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
