label chapter11:

    # [Scene: Tideward Waterline | Dusk]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves battering, a metallic beep from a failing sensor, a generator clunking irregularly]
    # play music "music_placeholder"  # [Music: Fractured strings—urgent, staccato; a bass drum undercurrent like a heartbeat]
    "You stand at the edge of everything: wet clothes clinging to your skin, hair plastered to your neck, compass cold and slick against your sternum. Salt tastes like old promises. Around you the town looks smaller"
    "and sharper—faces cut out of the dusk, lit by phones and the harsh white of a spotlight someone has brought for better pictures."
    "You can feel every bruise the night has made. Rope burns, a bruise starting under your ribs from where you grabbed the snapped line; the ache that will not stop at muscle because it reaches into"
    "the place your father's absence lives. He is a memory you still measure against the horizon. You wonder, with the sting of seawater in your throat, whether that measure has ruined you or kept you honest."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of the crowd; a single child's sob cut off by a held hand]
    # play music "music_placeholder"  # [Music: Strings rise, skittering into a tension that will not let you breathe easy]
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "Mara—' (he steps forward, voice thin with cold and something like blame) 'We can still pull what's left. We can—"
    show mara_linh_alvarez at right:
        zoom 0.7

    mara_linh_alvarez "We were supposed to test the lines at slack. The anchors—' (You stop because speaking aloud will make decisions into accusations. Your voice comes out small, bruised.) 'Something failed, Kai. Something failed when people trusted us with ropes and boats and time."

    kai_navarro "I know. I know, okay?' (He runs a hand through his braid until it flops down, wet and dark.) 'I—look. I kept the tension lower than the logs said. We—' He searches your face, looking for a line to take you back from the edge. 'We can salvage the kelp frames. We can show people we learn."

    mara_linh_alvarez "Salvage.' The word tastes like an ultimatum. 'Or spin it. Or hide it until it's polished."

    "Nita (arriving breathless from the promenade)" "Spin? Hide? Mara, people saw anchors tearing out. Kids saw panels drift. If we wait to tidy it—if someone from the paper shows up before we say something—' She spits the last words like stones. 'You know the mayor will twist silence into consent."

    "Reverend Sol (leaning on his carved cane)" "Silence won't keep anyone safe. But neither will rushing the water's edge like a dare. We must think clearly—' He looks at you, then at Kai, then back. 'The town is asking who will lead."

    "Dr. Leila (pulling a dripping sensor from a satchel)" "Sensors fried on impact. A few of the data logs are corrupted. I can't confirm load patterns yet, but the anchors show asymmetry—something struck at the anchoring node.' She meets your eyes like a surgeon. 'We can raise the pieces for analysis. Or we can let tides wash them out and lose the raw evidence."
    "The air narrows to a thin wire of sound. You can hear your own pulse like a distant alarm. The decision you make will not be erased by tides. It will be lived in headlines, in"
    "the way Nita glares when she hands you a hot pack, in the way Juno watches you from the fringe—alarmed and not yet convinced you can keep them safe."

    menu:
        "Grip the compass and still yourself":
            "You close your fingers around the brass, feeling the cold bite. The motion steadies a tremor in your hands, like a small anchor of your own."
        "Step toward the kelp platform and shout instructions":
            "Your voice cuts across the water—sharp, ordering. Volunteers turn; two begin hauling a stray line while someone waves for a boat. The crowd blurs to purpose."

    # --- merge ---
    "Continue"

    kai_navarro "If we wait for the paper to spin this into a horror piece, people will lose faith in the living-route approach altogether. They'll take Evelyn Black's offer just to stop the noise."

    mara_linh_alvarez "And if we go out now—' (your throat tightens) '—we risk more than a headline. We risk people."

    "Juno (stepping closer, voice small but hard)" "You're letting them decide, Mara. I can't watch another thing we built be used to put a fence around our choices. My friends—' He stops and swallows. 'We need you to choose."
    "Everything accelerates. The tide pulls at the pilings like a hungry hand. Someone's flashlight sweeps across Evelyn Black's development site across the channel—an island of clinical light in the wet dark—and for a second you think"
    "you see her silhouette at the edge, head tilted, unmoving. The image is unreadable; your mind supplies everything from triumph to worry and then is forced back to the task at hand."
    show dr_leila_osei at center:
        zoom 0.7

    dr_leila_osei "Technically, the sooner we secure whatever we can, the better for data and safety. But salvage in tonight's swell is dangerous. If you lead it, we get the clearest picture. If we broadcast—public transparency might be humiliating, but it builds trust. If we conceal—"

    "Reverend Sol" "You are not the town's only voice, Mara. But you're its center right now. Do not let guilt alone steer you."
    # [Scene: Kelp Platform | Night]
    hide kai_navarro
    hide mara_linh_alvarez
    hide dr_leila_osei

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of waves against the platform; a distant foghorn; a volunteer's cough]
    # play music "music_placeholder"  # [Music: Percussion tightens—ticking rhythms; wind instruments shrill with urgency]
    "You step onto the kelp platform because standing still feels worse than the cold. The wood bobs underfoot, untrustworthy. Breathe—one inhale, one exhale. Reassess. You run fingers along the broken seam of a frame. The algae is slick like a smear of green night-ink."
    show anita_nita_ramirez at left:
        zoom 0.7

    anita_nita_ramirez "We can rig a temporary brace to keep the rest together. We can hold the line until morning and bring a crane. Or—' She glances toward the promenade where the town is starting to gather, '—we can call it and take the optics now."
    show mara_linh_alvarez at right:
        zoom 0.7

    mara_linh_alvarez "Optics won't fix anchors,' you say. 'They'll only make the lawyer's narrative easier."
    show kai_navarro at center:
        zoom 0.7

    kai_navarro "We can do both—secure the pieces we can now, pull the rest for analysis, and stream the process. Transparency and salvage."

    mara_linh_alvarez "And if streaming is all people see—clips of wet hands and failed knots—if that is what cements the fear? What then? Who pays when people choose a wall over the work?"
    hide anita_nita_ramirez
    show dr_leila_osei at left:
        zoom 0.7

    dr_leila_osei "We won't know the 'what then' unless we preserve the data. Without it, Evelyn Black and her contractors will say 'unreliable' and the court will nod. The political power tilts toward certainty—and manufactured certainty is their currency."
    "Your hands smell of kelp and diesel. Juno presses a bandana into your palm—his fingers rough from bike chains and repair. There is so little theatrics left in you. You are counting consequences in small increments: trust lost, danger accepted, time bought."

    menu:
        "Order the volunteers to hold the platform and prepare for immediate salvage":
            "Your command snaps the group into motion. Ropes are secured tighter, hands finding knots. Two volunteers exchange a look that says 'we'll die if you want' and keep working."
        "Call a quick town broadcast—tell the honest story and invite helpers":
            "You grab a soaked phone, press record. Your voice breaks once, but you say the facts: failure, injured pride, request for aid. Voices from the promenade begin to filter into the feed."

    # --- merge ---
    "Continue"
    hide mara_linh_alvarez
    show anita_nita_ramirez at right:
        zoom 0.7

    anita_nita_ramirez "If you go live, Mara, people will come—good and bad.' She spits the truth plainly. 'That's a flood of volunteers, of rescuers, of those who want to make names out of tragedies."

    "Reverend Sol" "A flood is not only water. A flood can be a tide of care if guided well."

    "Kai Navarro (lowering his voice so only you can hear)" "We can't be perfect. We can be honest. Or we can be effective. Maybe honest helps us be effective in the long run. I—' He swallows. 'I know you're scared of being the person who gave the town a false bet. But you're not the only one wearing their mistakes. Let people decide on truth."
    hide kai_navarro
    show mara_linh_alvarez at center:
        zoom 0.7

    mara_linh_alvarez "And if the truth ends us? If the town chooses the concrete because they are more afraid of a second headline than of the slow drown?"
    hide dr_leila_osei
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "Then we fight on other fronts. But we'll do it with our faces up, not pretending we didn't scald the kettle."
    "Kai Navarro's words are both offer and challenge. They sit between you like a rope stretched taut. Behind him, a teenager pulls at a frayed strap and curses where it snaps. The swell makes everyone smaller. Your pulse thrums like an engine on the brink of stall or surge."
    # [Scene: Promenade | Late Night]
    hide anita_nita_ramirez
    hide mara_linh_alvarez
    hide kai_navarro

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur has sharpened into voices: questions, accusations, someone clipping a microphone into place for a livestream]
    # play music "music_placeholder"  # [Music: All instruments converge—rhythms frantic, a short, high violin note cutting like an intake of breath]
    "You walk back up onto the promenade and find the crowd has arranged itself into judgment and support. Faces you know—Nita's hands clenched, Juno's jaw set, Reverend Sol's eyes luminous with expectation. You see Dr. Leila tapping notes into her phone, an island of data in a storm of feeling."

    "A volunteer pushes a recorder toward you. Radio Host" "Mara, will you speak?"
    "You look at Kai Navarro. His jaw is a calm line. He gives you a small nod that is more an offering than an instruction. In the end, this is your decision."
    "It all condenses into a single hot point of pressure behind your eyes. You think of your father's boat list—things he'd mark off hurriedly when a storm came: check lines, secure hatches, pray. You think of"
    "the kids who trust you to act like the adults aren't perpetually wrong. You think of the lawyer who once told you that silence is a strategy when damage is contained. You think of Evelyn Black's"
    "clean drawings of straight walls and the way her smile doesn't reach her eyes."
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "No matter what you choose, I'll stand with you.' (He says it with a soft ferocity that feels like a prophecy.) 'I just—' He stops, searching for the truth he can live with. 'I hate the idea of you carrying this alone."
    show mara_linh_alvarez at right:
        zoom 0.7

    mara_linh_alvarez "I have carried things alone before, Kai. That didn't make them lighter."
    "Kai Navarro: (a beat; then) 'Then don't this time.'"
    "The air feels like it is about to break. People are watching. Recorders are on. The town's faith is a fragile vessel on the waves. You can feel the gravity of each path under your feet:"
    "the immediate danger of salvage; the humiliation and possible renewal of public transparency; the quiet rot of concealment."
    "Your hands flex around the compass, feeling the worn dent where you once held it during worse storms. You can steer this moment into peril or into a sacrificial truth. Either one will hurt. Neither option lets you hide."
    "You inhale the cold, brine-thick air and exhale into the crowd. The moment opens."
    "You must choose how to handle the failed demonstration in public."
    "You consider the options and the faces around you—the volunteers who will follow, the lawyers who are already drafting words, the children who will inherit whatever you leave."

    menu:
        "Lead an immediate salvage operation":
            jump chapter12
        "Broadcast transparency—show failure and invite repair":
            jump chapter12
        "Conceal the full extent and rebuild quietly":
            jump chapter14
    return
