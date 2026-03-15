label chapter7:

    # [Scene: Saltline Harbor | High Noon — Ceremony Day]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Brass and percussion swell into an urgent, celebratory march — fast, bright, insistent]
    # play sound "sfx_placeholder"  # [Sound: Waves clap against newly placed slabs. Hammers, conversation, a distant gull. A megaphone crackles intermittently.]
    "You are standing with your back to the tide, toes dug into splintered wood, salt on your lips. The model you once sketched in a fogged lab window has been grown, hammered, bolted, and seeded here"
    "— a strange, human-made reef that looks half-sculpture, half-ecosystem. Engineered slabs flex like ribs; beneath them, kelp and coral frames sway in tethered arrays, turning storm force into life."
    "Your heart is a drum under your ribs. The air tastes of wet wood, tar, and something green — kelp bruised in hands. Around you are faces you have argued with, pleaded to, worked beside: Luka's"
    "lined profile turned toward the sea, Maya perched on a crate with her camera, Rin waving a handkerchief that used to be a poster. Kaito Sakamura stands a step to your left, sleeves rolled, paint and"
    "salt at his nails. There is a nervy, joyful electricity between you that the wind cannot swallow."
    "You breathe in, and the inhale catches a memory — the last time the tide took too much, the way the marsh screamed in a language you once thought you could translate with blueprints alone. That"
    "guilt flares; then something steadier takes root: the people here, the living scaffolds, the charter folded into folders like a promise. Today is the wager made visible."

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings surge into a hopeful, fast-tempo motif]
    # play sound "sfx_placeholder"  # [Sound: A boat horn calls twice — long, affirmative]
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "You remember the old binders I kept? My hand can barely lift them, but I've kept each petition, each torn map. Today you'll add one that says we decided together."
    "Luka's voice is slow but not tired. His eyes are wet in the corner; his smile is small and fierce."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "We decided together,"
    show kaito_sakamura at center:
        zoom 0.7

    kaito_sakamura "No half-measures.' He reaches out, fingers brushing the shell at your throat. 'Only the work that actually holds up when the water comes."
    "You laugh; the sound is raw and full. He squeezes your hand and then releases it, the kind of steady contact that has always steadied you in meetings and in the shop. His presence steadies the spike of adrenaline in your chest."
    hide luka_sorensen
    hide marin_alvarez
    hide kaito_sakamura

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: A single held horn note — a question that will be answered]
    # play sound "sfx_placeholder"  # [Sound: Murmurs hush as Elena Moro steps forward]
    show elena_moro at left:
        zoom 0.7

    elena_moro "This hybrid system — the slabs where needed, the living frames woven in — it keeps the district safe while protecting marsh plots we agreed must remain untouched. It is not my usual style, but… it is effective."
    "Her words are crisp; there is a steeliness there, but her eyes—when they flick to the kelp frames—are unreadable and somehow less cold than the last time you argued."
    show ishaan_rao at right:
        zoom 0.7

    ishaan_rao "Agency funding remains attached, conditional on oversight. But the governance clause gives the council co-signatory authority. That's unprecedented."
    "He looks at you and then at Elena Moro, an almost-boyish smile trying to break through his bureaucratic polish."
    "You feel the heat behind your eyes — not anger anymore, relief. The numbers on Ishaan's printouts are less abstract today; they're a scaffold that will stand under people's feet, not over their heads."
    show maya_chen at center:
        zoom 0.7

    maya_chen "You did it, Marin.' She jumps down, camera hanging forgotten. 'You actually did it— the nursery frames are already showing recruits. Look!' She thrusts a tablet toward you, the camera feed alive with neon-green tendrils clinging and young coral polyps etching themselves to armatures. 'They took."
    "Your chest expands in a rush of triumph. For months you have been saying 'maybe' and 'if', and now the proof is a twitching, living thing. The crowd's applause rises like surf."

    menu:
        "Adjust the kelp tethering on the nearest frame":
            "You crouch and reach for the line, fingers nimble despite the day's nerves. Your hands find the knot Kaito taught you; it answers with a soft give. He leans close, murmuring a corrective tip, and you both grin at the small private victory."
        "Step up to the crate and speak to the crowd":
            "You climb up, barrel of your voice meeting the assembly. The sound washes over you: the faces, the sky, the water. You say the words that have been practicing themselves inside you — short, honest, and full of thanks — and the applause thunders like a rising tide."

    # --- merge ---
    "You take neither long alone nor frivolous. You do both — the small practical touch, then the larger public word. Kaito Sakamura's hand finds the small of your back as you step up, and the contact is an anchor."
    hide elena_moro
    show marin_alvarez at left:
        zoom 0.7

    marin_alvarez "This isn't a trophy,' you tell them, voice clear. 'It's a tool and a story. We built it because the marsh is not just habitat — it's our memory, our food, our shelter. This charter puts the money where people can see it, the slab where engineers say it must be, and the kelp where the marsh can keep being itself."
    "A woman from the floating farm calls out, 'And the coral nursery?' Her tone is sharp with hope. 'Will fisheries benefit?'"
    hide ishaan_rao
    show elena_moro at right:
        zoom 0.7

    elena_moro "We projected yield increases. Where we place slabs we've modeled flow redirection so nursery frames actually get nutrient pulses. It's a system. It needs tending."
    "There is a murmur — skepticism braided with possibility. You see Luka's jaw loosen, Maya's grin widening until it hurts. People begin to shout out logistical questions; the air vibrates with engaged, messy democracy."
    "Ishaan steps forward with a folder and a pen. He looks at Elena Moro, and then at you. For a second the world narrows to the tremble of that small instrument."
    hide maya_chen
    show ishaan_rao at center:
        zoom 0.7

    ishaan_rao "We can sign today, if the co-signatory clause stands as drafted. The funding releases will follow. It will fund the retrofit work, the nursery expansion, the cooperative's workshop upgrades. It will pay for monitoring so you can refuse bad projects more easily."
    "Elena Moro watches you. Her expression is complex — there is a shadow of the old engineer who believed in big systems, and something else, a grudging admiration for how the town made the system bend. She lifts the pen, hesitates."

    elena_moro "I lost a city before I learned to listen to it. Maybe that's why I build so loud now. But what you've made here — it's loud in a softer way. It matters."
    "Her voice is a step across a floorboard you'd sworn would never creak. The crowd exhales; even the gulls seem to pause."

    marin_alvarez "We did this so we wouldn't have to choose between protection and memory,' you say, and your fingers close around the pen as if on a rope. 'We did it so the marsh, the nursery, the people — everyone who has a stake — has a say."
    hide marin_alvarez
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "Whatever comes next, we do it together. No one does it alone in Saltline."
    "Those words are a small cathedral. Your throat thickens. You sign."
    hide elena_moro
    hide ishaan_rao
    hide kaito_sakamura

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: The tempo accelerates into a full, driving ensemble — strings, brass, percussion — triumphant and breathless]
    # play sound "sfx_placeholder"  # [Sound: A cheer erupts; clapping, a few whoops. Hammers resume, but now their rhythm feels like construction, not panic.]
    show ishaan_rao at left:
        zoom 0.7

    ishaan_rao "Funds released. First tranche disbursed. Community liaison positions approved. The retrofit works begin next week."
    "He grins — controlled, relieved. 'Accountability protocols are written; audits will be collaborative. We expect transparency reporting.'"
    show luka_sorensen at right:
        zoom 0.7

    luka_sorensen "Transparency is only good if you look through it. We'll be watching — and teaching. No quiet deals."
    "He bumps your shoulder and then, to everyone's surprise, pulls you close and plants a quick, grandfatherly kiss on your temple. The crowd laughs and claps; you laugh with them in a clean, relieved burst."
    show maya_chen at center:
        zoom 0.7

    maya_chen "Now— celebration. Then work. Then more celebration when the nursery is thriving. Photographs, songs, lists of who hauled what wood."
    hide ishaan_rao
    show rin_okubo at left:
        zoom 0.7

    rin_okubo "And the bulletin will call for volunteers at dawn. Kaito Sakamura, you're bringing the saw team. Marin, you'll come too. No more ghost projects."
    hide luka_sorensen
    show kaito_sakamura at right:
        zoom 0.7

    kaito_sakamura "Always,' he says, eyes on you. 'Always."
    "The high tide edges closer to the slabs, and the first engineered wave is absorbed with the hiss of kelp and the thunk of secure padlocks. You feel the structure breathe, not like metal and concrete alone, but like a system with muscle."

    menu:
        "Take Kaito's hand and lead a volunteer wave to the nursery":
            "You fold your fingers into his and step down off the crate together. People move with you like a current; you pass buckets, sling frames, laugh when someone drops a spade. The work is hot and wet and immediate, and your shoulder presses against his in a seamless rhythm."
        "Walk the perimeter and check the anchorage readings":
            "You move with the engineers, hands running over bolts, eyes on gauges. The numbers line up with your internal criteria; the confirmation is clinical, but your chest still blooms. You give a thumbs-up to a nearby volunteer, and that small approval is enough to feel whole."

    # --- merge ---
    "You pick both again — you are greedy for everything: to be useful and seen. You kneel by a coral frame as Kaito Sakamura steadies the line; your fingers are inked with salt and sap, and"
    "the world narrows to the small work and the soft pressure of someone at your side."
    "For a moment, Elena Moro stands back and watches the two of you. Her face is unreadable and humane, a map of vulnerabilities you have not abandoned. She moves closer and offers a hand — a"
    "formal, almost awkward gesture that carries an apology you did not ask for and perhaps did not expect."
    hide maya_chen
    show elena_moro at center:
        zoom 0.7

    elena_moro "Thank you for pushing me to think smaller where it helps. And bigger where it's needed."
    "She looks at Kaito Sakamura and you; the corners of her mouth tilt not quite into a smile. 'Saltline is stubborn and beautiful. Keep it that way.'"
    "Kaito Sakamura accepts her hand with a carpenter's nod; you accept her gaze with one of your own. There is a realignment here: not a surrender, not a capitulation, but a pooling of wills to match the magnitude of the sea."
    hide rin_okubo
    hide kaito_sakamura
    hide elena_moro

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A warm, swelling chorus — the climax now receding into a gentle, sustained glow]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the clink of cups, the rustle of kelp]
    "You stand with Kaito Sakamura as food is passed — fish wrapped in kelp, bread, bowls of stew — and you taste the salt of a day that demanded everything and returned more. The charter slips"
    "into the town archives with a ribbon; Luka hums an old boat-song; Maya captures it all with a grin that could split the sky."
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "We built something that can learn. We built something that can be loved."
    "You lean into him, to that steadiness you have come to need. Your past guilt — for the marsh you once failed — loosens. It will never be gone, but it becomes the reason you do"
    "the work rather than the thing that binds you to shame. This is repair in the largest sense: the environment, the town, and the soft, complicated place in your chest where personal and professional meet."
    "You take one last look at the harbor: the slabs flex, the kelp breathes, the nursery frames flicker with small neon recruits. The contract is signed, the funds secured, the governance charter written to give voice"
    "and veto, the work shared. The tide will still come, storms will still test these measures, but today Saltline chose a way forward that honors both protection and memory."
    hide kaito_sakamura

    scene bg ch6_601bcb_6 at full_bg
    "You exhale, and it is not relief alone — it is a chorus of small triumphs. The harbor hums with life. Around you, people argue about paint colors for the nursery frames; Luka tells a story"
    "the children crowd around to hear; Elena Moro and Ishaan sketch a monitoring schedule with a technician; Maya plans a celebration exhibit; Rin writes the headline that will be in every window."
    "This is not the end. It is something better: a beginning braided with resolve and shared risks. You let yourself believe, for a wildly unscientific second, that the future will be kind enough to match this effort."
    # play music "music_placeholder"  # [Music: Swells once more, then settles into a warm, lingering chord]
    # play sound "sfx_placeholder"  # [Sound: The harbor's night chorus — the distant surf, voices, soft laughter — grows comfortable, human, alive]
    "You look at Kaito Sakamura and feel the truth of what has always been waiting beneath the plans and tremors: love and work are not separate here. They are scaffolds for the same life. You reach"
    "for his hand and, without dramatics, kiss him on the forehead. He laughs, the sound a small, bright thing that nearly drowns out the gulls."
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "Come on. There's still paint to mix and frames to truss. And Luka insists the first post-signing stew needs more pepper."
    "He grins. His warmth leaks into you like sunlight."
    "You stand, shoulder to shoulder, as the harbor party folds into routine — song, dishes, the methodical clink of tools — and you know you will not be alone at dawn. The governance meetings will be"
    "long; the storms will test the design. But the charter is inked; the community's hands are in the work; the kelp and coral are already doing what kelp and coral do best: hold on."
    hide kaito_sakamura

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Ends on a sustained, hopeful note — a final chord that rings like a promise]
    # play sound "sfx_placeholder"  # [Sound: The tide, steady; a single gull; distant laughter]
    "You have won something fragile and durable at once: a cooperative covenant that keeps funding and honors the marsh, a repaired trust with those you once clashed with, and a partnership with Kaito Sakamura that is"
    "finally spoken and sealed by everyday acts. The future is not resolved, but it is chosen — messily, lovingly, with hands that will keep working."
    # [Scene Transition: Fade Out]
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
