label chapter11:

    # [Scene: Tidelab Greenhouse | Late Afternoon]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, slow cello undercurrent; distant wind through the vents.]
    # play sound "sfx_placeholder"  # [Sound: A phone vibrates sharply against metal; somewhere outside a truck backfires and a gull calls.]
    "You had just written the word 'fragility' twice and closed the notebook like a promise. The lamps are down to a softer pulse; volunteers have already drifted away in pairs, their laughter thinning into the boardwalk's"
    "late light. You let the air settle in your lungs and savor the hush—until the screen of Asha's tablet flashes with a headline that tastes of battery acid."
    "The headline is small, then enormous: leaked model, 'acceptable displacement' memo. A truncated forecast, a line out of context, a sentence boiled into a banner. The Tidelab's warm air turns thin, like someone opened a door to a cold stairwell."
    "Your mouth goes dry. For a moment you only listen—count the beats of your heart against the hum of pumps, the slow drip from a clogged gutter. Then you move."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Asha's breath, shallow; distant, muffled shouts from the boardwalk.]
    "Asha looks up at you, cheeks flushed, fingers white where they've gripped the tablet."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "Mira—someone clipped Jonah's model and sent it to the paper. They ran the memo about 'acceptable displacement' as if it's policy. The parameters were partial—only a sensitivity test—and they cut the notes. People are... they're reading it like a plan."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Partial how?"
    "Her hand finds yours; you feel the small, familiar tremor."

    asha_mehta "Truncated. The version released skipped the mitigation scenarios. It shows worst-case relocations as if those were the targets, not thresholds we were testing. Cassian's group saw it—before we'd even called for a town meeting. They think we're delaying because we're 'analyzing.' They think delay is displacement."
    "You taste iron and salt as your chest tightens. Your mind fans through a hundred little failures that could let a file slip: an unsecured drive, an offhand email, a borrowed laptop left logged in. None"
    "of it is tidy. None of it gives meaning to the particular betrayal you feel."

    menu:
        "Call Jonah directly and demand answers":
            "You snatch up your phone and scroll for Jonah's contact, thumb hovering. In the cold ring of the call you try to keep your voice steady, to ask for facts before fury."
        "Gather Asha and head to City Hall":
            "You close the tablet with a hard press and shove it into your jacket. The motion says 'we fix this together.' Asha nods, wiping her hands on her vest as you both step into the damp light, moving fast toward the Mayor's office."

    menu:
        "Step forward and mediate between Jonah and Cassian":
            "You position yourself between their voices, palms open. Your voice is low, trying to stitch the room back together: 'We have to speak plainly.' Cassian's jaw keeps working, but he lets you speak. Jonah's hands fold around an invisible pen, listening."
        "Let Cassian speak and take notes for the later public forum":
            "You stay back and let Cassian's fury have its space, fingers moving over your notebook as if the act will preserve the truth. His words cut through the room; your notes will later become structure."

    menu:
        "Prepare a limited release—annotated files with context, framed as clarification":
            "You start drafting a concise, annotated packet that explains the truncated outputs. It feels like building a bridge—careful, contextual, and possibly toothless. Asha nods, relief and fear braided together."
        "Begin preparing a full forensic report for publication—no redactions":
            "You set your jaw and start compiling everything: raw models, emails, memos. It's honest, brutal, and risky. Asha's eyes widen, then harden; she reaches for the files, hands steadying."

    menu:
        "Push an organized, supported relocation paired with strict community protections.":
            jump chapter13
        "Allow a hard infrastructure push to move forward under protest, hoping political pressure limits displacement.":
            jump chapter14
        "Expose the consortium’s flawed modeling publicly, risking the pilot and funding but potentially stopping harmful construction.":
            jump chapter16
    return
