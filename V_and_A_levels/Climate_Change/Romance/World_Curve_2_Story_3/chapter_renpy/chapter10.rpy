label chapter10:

    # [Scene: Reclaimed Wetlands Festival | Twilight]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tinny festival accordion undercurrent with a rising string ostinato]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a low generator hum, the hiss of smokers at food stalls]
    "You walk through the festival like someone walking a tightrope — careful where you put your feet, every step set to the rhythm of other people's expectations. The dusk makes everything soft-edged and urgent: faces come"
    "and go in pools of light, laughter braided with the metallic tang of smoked fish. Someone rings a bell by the market stall and the sound knocks into the hollow under your ribs."
    "Amalia spots you first, clipboard half tucked under her arm, a scarf bright as a protest flag at her throat. She waves you over with one hand and with the other gestures at a string of"
    "volunteer schedules pinned to a board. Her breath puffs out in the cooling air; the smell of frying kelp follows her like a small, domestic halo."
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "Marina — okay, walk me through the order. Where do we put the demo platform? Old Tom wants his circle close, kids need a safe channel, and Kai's pilot can't anchor too near the shallows."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "We center the floating pilot in the larger channel — visibility for everyone, but anchored to the deeper piling near the old boat ramp. Old Tom can set up just behind the crowd so his stories can feed into it. Mika's got the comms — she'll run the livestream and the sensor feed."

    amalia_reyes "If the council shows up, we need a clear, simple line. No jargon. People here are tired — give them what they can do tomorrow, not a lecture about wave spectra."

    marina_reyes "You always know how to make it into something people can take home. Thanks. Keep the kids' zone staffed; if the wind picks up, we fold the lanterns quick."
    "Amalia hesitates, then pins the schedule with an extra thumbtack. Her hands are steady, but there's a tremor in her jaw that you know means she is scared for the same things you are: livelihoods, houses, the thin line between ceremony and panic."
    hide amalia_reyes
    hide marina_reyes

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clank of hardware, excited chatter from a small crew]
    "Kaori 'Kai' Matsuda moves like a storm in miniature, all motion and insistence. She slings a long, improvised skiff across a shallow channel — the pilot — and plugs thin solar strips into junction boxes like"
    "a jazz musician hitting riffs. Mika bobs at her elbow, tool-belt flashing, passing wrenches and a tablet with schematics that look hand-annotated in every color."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "Okay, this is our showpiece. Modular solar, buoyant frames, and the kelp lines will damp wave energy and feed the pilot with nutrients. If we make it pretty, people will touch it and understand."
    show mika_tran at right:
        zoom 0.7

    mika_tran "Comms green. Sensors calibrated for salinity and flow. If we kick power, we'll have live data overlays sent to the big screen."
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "Make sure the tethers are redundant. We can't have a drift mid-demo. Old Tom's circle will hold the crowd if you need to pull the plug."

    kaori_kai_matsuda "Redundant, redundant — I live for redundancy. Also we're making it lantern-pretty. People love lanterns."
    "Your chest tightens at Kai's cheer. It's infectious, reckless, and exactly what this moment needs — and exactly what could blow it apart. You feel the old pattern rising: you want to stitch everything together yourself,"
    "to keep each thread safe. But the pilot is fragile and the weather is impatient."
    hide kaori_kai_matsuda
    hide mika_tran
    hide marina_reyes

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low, patient voice of Old Tom beginning a tale; his words curl in the air]
    show thomas_old_tom_bellamy at left:
        zoom 0.7

    thomas_old_tom_bellamy "I remember a tide that ate the road in ’79. We tied boats to trees and sang staves until dawn. Folks think the sea is only taking — it also remembers."
    "You step closer. His voice is a map: memory, warning, and a slow, aching affection for the town. The crowd listens. Their faces tilt toward the light like flowers to a last sun. You feel a"
    "fresh pinprick of responsibility—every story he keeps alive is another reason you can't afford to fail."
    hide thomas_old_tom_bellamy

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The festival fades around his figure; nearby, the wind picks up]
    "Elias Kato is there, folded into the crowd like an instrument you once knew how to play. He doesn't step forward; he watches. When your eyes meet, something passes — not a confession, not necessarily an"
    "invitation, but an assessed weight. His face is unreadable in the lantern glow, the faint silver strand at his temple catching light like a punctuation mark."
    show elias_kato at left:
        zoom 0.7

    elias_kato "How public is this going to be? We risk scaring people. We risk people seeing the worst-case stuff and making snap decisions. We risk the council pulling permits."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "We risk silence too. People already make snap decisions about leaving. If they can feel the kelp line hold the water, that's different than another chart on a wall."

    elias_kato "Feelings are not enough to secure funding, Marina. You know that."

    marina_reyes "Feelings are enough to get people to stand in the water with you. And sometimes standing matters more than funding."
    "He shifts, searching for an edge to land on. His skepticism isn't just political; it's a thing that keeps him steady. You remember the way he used to plan roadmaps on napkins, precise and calm —"
    "and you remember that distance between the two of you when policy and place pulled taut."
    # play sound "sfx_placeholder"  # [Sound: A sharp, officious voice cutting across the clatter; footsteps on packed earth]
    "A municipal aide appears, clipboard in hand — pressed fabric, a lamplight reflection. Their expression is paper-thin professionalism; the voice carries the faint scent of bureaucracy warmed by the festival heat."

    "Aide" "I'm sorry — this is an unsanctioned demonstration. We have a safety inspector on duty and—"

    "Kaori "Kai" Matsuda (cutting in, hands raised)" "We're registered. We're in the community showcase. We have safety protocols and redundancy."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "We're registered. We're in the community showcase. We have safety protocols and redundancy."
    "Aide: (checking a phone) 'The permit on record does not authorize active prototypes in the main channel. For liability reasons, I'm going to have to ask you to contain any experiments to the back dock.'"
    "Mika: (fuming) 'Back dock? The back dock is a shoal with three houses and two kids' channels. That's not safe.'"
    "You feel the blood rush to your face. The aide's words are not just a bureaucratic hindrance; they are the thin edge of the town's political machinery — a pressure that can fold the festival into safe, forgettable gestures."

    menu:
        "Stand your ground and argue immediate public demonstration":
            "You plant your feet and feel every pair of eyes slide toward you. You explain the community protocols, cite the sensors Mika read off, and call for volunteers to attest to safety. The aide's jaw tightens; the crowd murmurs, split between applause and wary whispers."
        "Offer to move the demo to a safer, restricted area":
            "You bite the corner of your lip and suggest a compromise: the pilot will be anchored at the back dock under supervision, with live cameras projected to the main square. Kai scowls but nods; the aide relaxes slightly, jotting in the clipboard. The crowd exhales — relief and disappointment in a single breath."

    menu:
        "Give the go-ahead for an immediate tethered pilot, trusting Kai":
            "You lock eyes with Kai and nod. She howls with a grin and the team moves like lightning, tethers slamming into place. The crowd leans in; hands reach out. The pilot's lights blink on like a small promise. Your heart gallops — exhilarated and terrified."
        "Insist on full safety checks and data-first presentation":
            "You hold up your hand and call for sensors to be sequenced through the comms. Mika reads out the telemetry; Elias's face tightens with approval at the numbers. The crowd shifts, some bored, some reassured; the pilot remains still, lights dimmed, like a hope waiting in the dark."

    menu:
        "Show raw, unedited data and demo hardware openly.":
            jump chapter12
        "Focus on spectacle and story — make it emotionally convincing.":
            jump chapter14
        "Invite Elias to co-present for political cover and data legitimacy.":
            jump chapter15
    return
