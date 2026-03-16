label chapter14:

    # [Scene: Subbasement Data Lab | Night]

    scene bg ch14_9d8ae5_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — restless strings, a driving high-tempo beat]
    # play sound "sfx_placeholder"  # [Sound: Distant sirens; the building creaks as distant waves push at foundations; a steady, mechanical hum of servers undercut by sudden alarm chirps]
    "You are still riding the echo from the Beacon—its lamp a stubborn dot in your mind—but now that light is a thin filament against this room's cold, buzzing heart. The air tastes metallic and oily, like"
    "a kitchen over a storm. Condensation beads on the underside of the cable trays and drips with an insistent, ridiculous rhythm onto the concrete below."
    "Rafi crouches beside a rack, fingers moving with practiced impatience over a recorder and a slate of emergency logs. He spits a curse you feel more than hear: the sound bites of panic compressed into a syllable."
    show rafi_alvarez at left:
        zoom 0.7

    rafi_alvarez "The control node's actuation feed is misaligned. It's routing to the wrong pressure manifold—look at this telemetry, Aiko, it's cascading to the lower conduit."
    "You lean closer to the screen. Neon models flicker: lines turn red, then blink into frantic orange. You want data to be a steady thing—numbers you can interrogate, systems you can translate into steps. The models aren't obedient tonight. They twitch and collapse."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "Show me the valve map. Which manifold is being pressurized?"

    rafi_alvarez "Lower B—no wait—the bypass clamp's stuck in a half-loop. Helio's remote lock tried to reroute and it failed. Water's heading down the service shaft, not out."
    "The hum grows teeth. Somewhere above you, someone shouts into a comm—Elias's voice slices through with the rawness of someone on the surface being shoved by boots, but present enough to steady you."
    show elias_chen at center:
        zoom 0.7

    elias_chen "Aiko! The barrier's breached at Promenade West. Officers—crowd's being pushed back. We need that node off now—before they hit manual override and lock it again."
    "You taste salt and guilt. You hear Mina's steps, softer, clutching a med pack that suddenly seems like a child's toy. Sora's voice, moved like an old tide memory, murmurs from the doorway where she lingers with a hand on the stone."
    hide rafi_alvarez
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "Machines remember what we forget. Make your choice quick—water doesn't wait."
    hide aiko_mori
    hide elias_chen
    hide sora_watanabe

    scene bg ch14_9d8ae5_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A hatch clangs open above; a far-off megaphone cracks]
    "Your hands—your hands remember ledger margins and tide maps, not soaked circuitry. Still, you move. You are the practical center your neighbors look to when the city frays."
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "Rafi, lock the network readouts to manual. Elias, can you pirate the actuator's handshake? Mina, keep the med corridor clear. Sora—watch the shaft, call any movement. I can try a manual recalibration at the panel, but I need clear access."
    show elias_chen at right:
        zoom 0.7

    elias_chen "No—Aiko, don't—"
    "His protest is not a whisper; it's the sound of someone trying to pull a friend back from an edge. You know the inflection—he's already imagining the hurt in his hands. You almost answer with dry humor, but the humor drowns in the alarms."

    menu:
        "Focus on the servers — triage data to prevent long-term loss":
            "You slow your breath and push the servers' cooling priorities up one notch, fingers leaving faint steam prints on the glass. The logs stammer but hold a moment longer."
        "Head straight for the valve controls — water first, data second":
            "You pivot toward the valve bank, boots hitting a puddle. A metallic tang fills your mouth; the valve wheel is warmer than you expect, already slick."

    menu:
        "Override the automated seal and trust the manual failsafe":
            "You flip the override switch with a fingernail that shakes. The panel clicks and hums as relays reroute; for a half-breath everything seems aligned."
        "Insist on a buddy team — two people at the panel, one to watch the shaft":
            "You call for a partner; Elias reaches, but Mina blocks him with a hard look. Sora lifts her chin, age and experience mapped in the way she breathes."

    jump chapter15
    return
