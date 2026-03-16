label chapter27:

    # [Scene: Marabel Promenade | Dusk]

    scene bg ch14_612518_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady cello motif]
    # play sound "sfx_placeholder"  # [Sound: Gull calls folded into the whisper of tide against pilings]
    "You arrive where you left off months ago — same boards, same gulls, a different tally. The compass hangs against your chest, its brass scuffed from constant handling. It still finds north, but you know now"
    "that bearings in this town are moral as well as geographical: the needle trembles when you think of what you had to sell and what you kept."
    "The promenade smells of brine and frying oil from a vendor packing up for the night. Children’s laughter, muffled through wind, comes from somewhere raised and green. The Beacon no longer reads like pure promise. Its"
    "lights pulse methodically now, a machine folded into the horizon. For some it has become instrument; for others it is a scar."
    "You breathe the dusk into your lungs. The air carries a thin metallic tang — old storms in memory, insurance in small print. You count what’s visible: patched roofs, raised planters, a new plaque at the"
    "foot of the promenade with modest fonts and corporate logos. You count what’s not: a shuttered stall, a gap between two houses where a family once hung laundry."

    scene bg ch14_612518_2 at full_bg
    # play music "music_placeholder"  # [Music: Cello continues, slightly pressing]
    "You let your ledger sit, closed but present, a weight at your hip. Tonight you promised yourself a walk that is not work, but promises bend easily in a town where weather and contracts make demands."
    # [Scene: The Old Boatyard | Early Evening]

    scene bg ch14_612518_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant laughter, a hammer’s measured tapping]
    "You settle on an upturned crate and open a folded letter with hands that still know how to be precise. The first is from a family who took the buyout: careful cursive, polite sorrow. They write"
    "of a distant sister’s spare room, of clearer nights without the Beacon’s glow, of guilt that the offer felt like survival. The ink blurs where salt caught the edge of the paper."
    "A second note, scrawled on a busier scrap, is from someone who stayed. It’s shorter, almost defiant: seed-swap next week, bring cuttings. The page is bent where a finger has made it into a tattered bookmark."
    "You press your thumb to both and feel the pulse of the town in miniature: departures and tenacity stitched together."

    menu:
        "Read the letter aloud to the boatyard":
            "You clear your throat and read the family’s words into the damp air. Eli pauses his hammering; his jaw tightens. He says little, but the way he sets the mallet down makes the sentence 'We did what we could' feel like a verdict."
        "Fold them quietly and keep them to yourself":
            "You fold the letters into the ledger and tuck them away. Eli watches the movement and asks, softly, 'You alright?' You give a small, tired smile and say, 'I will be.'"

    # --- merge ---
    "Eli finds his way over with his shirt rolled to the elbow, sawdust speckling his forearms like calloused constellations."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "You carry letters like stones, Ash. Do you want to keep them all?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Everyone writes differently about leaving."

    eli_duarte "Some leave with a suitcase. Some leave with an account statement. Both smell like salt."

    asha_moreno "And some of us stay up late counting both."

    eli_duarte "Then count with your hands dirty. It’s how we know the numbers aren't neat."
    "You both stand for a long moment, the hammer’s rhythm a distant heartbeat. The boatyard feels honest in its mess: what’s real here has weight and grain you can trace with a hand."
    # [Scene: Raised Gardens | Twilight]
    hide eli_duarte
    hide asha_moreno

    scene bg ch14_612518_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Children’s chatter, Marta’s quick directions, the smell of wet earth and seaweed compost]
    "Down the path, Marta is kneeling among cordgrass and seedlings, teaching a ring of children how to bend a heel into the soil and tuck roots in like secrets. Her gloves are stained a cheerful brown; her voice is a bright, practical thing."
    show marta_chen at left:
        zoom 0.7

    marta_chen "Not too deep. Let the tide do the work of reaching roots, not your shovel. Pass it slow."
    "A child looks up at you with soil under her fingernails and big earnest eyes. You find yourself showing her how to plant, your fingers small and patient around the fragile stems."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Press gently. Feel for the space between breath and root."

    "Child" "Do these plants stop the water?"

    asha_moreno "They help. They slow the water and teach the mud to stay."

    marta_chen "You teach at Tidewatch now, huh? Those tidelines need your lecture voice."

    asha_moreno "They need to know what the instruments mean in a language that smells like soil."

    marta_chen "Then teach them. But come back for the town meeting next week — your voice matters at night, too."

    asha_moreno "I will be there."

    menu:
        "Stay and help Marta tonight":
            "You crouch and work the soil until your knees ache. The children laugh when you make a false solemn face and promise the plants secrets. Marta claps when you finish the row; the light tastes like small victories."
        "Walk back toward the lab to prepare notes for tomorrow":
            "You rise, palms dusty, and walk with the ledger under your arm. The raised beds blur behind you like a memory you will return to, but not tonight. You rehearse sentences in your head, legalese and soil-side phrasing rotating like tide cycles."

    # --- merge ---
    "You enter the lab with a thermos and a stack of handouts. The room smells of ozone and toner and the wet cardboard of field kits."
    # [Scene: Tidewatch Lab | Night (late)]
    hide marta_chen
    hide asha_moreno

    scene bg ch14_612518_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low hum of servers, the faint drip of a drying chart]
    "You enter the lab with a thermos and a stack of handouts. The room smells of ozone and toner and the wet cardboard of field kits. Students — volunteers and neighborhood interns — work at benches, parsing data that now must sit beside the stories you've been collecting."
    "Noah Reyes is there before you, looking up from a tangle of sample reports. He straightens as you approach; his face is warmer for the lab’s cool light, but there’s that distant, fragile set to his mouth."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You teach tonight?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Basics. Sensors, sure, but mostly what to ask of the data."

    noah_reyes "Good. The more people who can read the ledger, the fewer surprises."

    asha_moreno "Sometimes the ledger hides what matters in footnotes."

    noah_reyes "Then we teach them to read the footnotes."
    "You exchange a look that says both of you know 'we' is conditional and heavy with history. The lab feels like a small vessel you both are trying to steer."

    asha_moreno "How did the meeting with Mayor Rosa go? Did she sign off on the new clause you drafted?"

    noah_reyes "She did. With handshakes and a look like she was holding the town's breath. She emphasized transparency. Lila sent a message of—' (he searches) '—cooperation, almost warmth. But the clause still has slippage."

    asha_moreno "Slippage is where the water gets under wood."

    noah_reyes "We can put nails in it. We can make audits public, embed community vetoes on certain projects."

    asha_moreno "We already have words for that. The question is enforcement."

    noah_reyes "Enforcement is the long walk. I'm not saying we can finish it tonight, but we can map the steps."

    asha_moreno "A map doesn't stop a storm."

    noah_reyes "No. But a map helps us find each other in what passes for one."
    "You both fall quiet; the lab's monitors scroll predictive models like slow snow. The conversation stokes in you a restless, steady energy: this is work that will not end, and the urgency of it is a daily metronome rather than a shouted alarm."

    noah_reyes "Do you ever regret... not walking away when it got easier?"

    asha_moreno "Every morning I wake and test the compass. Regret is like tide; it returns. But it's not the tide I answer to. I answer to the people who don't get to move."

    noah_reyes "And to the ones who did move? Do you—"

    asha_moreno "I read their letters. I don't have a right to their choices, but I hold the pages so their voices don't blow away."

    noah_reyes "Do you feel lighter, sometimes, to let the ledger be ledger and not heart?"

    asha_moreno "If it were that simple, we wouldn't need a town hall for nights."

    noah_reyes "I'm not asking for simple. I'm asking if you let yourself rest in the small mercies."

    asha_moreno "I count them, Noah. But counting is not resting."
    "Noah Reyes reaches for your hand across the bench. His fingers find yours with the same familiarity as always, and the touch is both reassurance and a fragile truce."

    noah_reyes "Then let me help you count."
    "You stare at your joined hands, at the scuff on the compass, at the small curl of a corner where the letter from the family who left sits in your ledger. The ledger's pages are full of numbers, but these hands press reality into the margins."
    hide noah_reyes
    hide asha_moreno

    scene bg ch14_612518_6 at full_bg
    # play music "music_placeholder"  # [Music: Cello motif widens slightly, tension building but contained]
    "You feel the arousal in your chest — not panic, but an upward pressure, an insistence. Months of working, litigating, teaching, planting have accumulated into this quiet, insistent ache: the town is safer on paper and"
    "scarred in memory. People moved, others stayed. The Beacon's halo is now an ordinary light in your nights, and yet in its ordinary shine you keep finding new reasons to fight the fine print."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "What do you want to do next?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We keep the ledger open. We make the audits public. We teach people to read sensors and soil the same way. We keep pushing back when clauses creep."

    noah_reyes "And on a smaller scale?"

    asha_moreno "We keep planting cordgrass. We keep teaching the kids they can put something in the ground and watch it hold."

    noah_reyes "You always make it both large and small."

    asha_moreno "Because both scales sink or float the same town."
    hide noah_reyes
    hide asha_moreno

    scene bg ch14_612518_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull cries once; the lab’s hum deepens]
    "You let the ledger sit between you, its pages fluttering slightly in an air that has always smelled like rain. The crescendo of the night is not a single event but a swell: letters, litigation, seedlings, audits, hands held — all building into something that demands decision and endurance."
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "Will you come with me to the hearing next week? Not as a negotiator, but as —"
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "As someone who remembers the names on the list. Always."
    "You feel that familiar ache again — a negative, tender thing. The work is continuous. The ledger will not be neat. Some nights will be mercies; some will be tallies that sting."
    "Page-turning thought: You tape another page into the binder labeled 'Community Governance.' It is small and stubborn and will matter when someone reads the ledger and tries to make it mean profit instead of protection. You"
    "close the binder, inhale the mixed smell of toner and salt, and brace for tomorrow — for meetings, for court filings, for seed deliveries, for the long, mid-intensity march that is keeping a town alive in"
    "changing tides."
    hide asha_moreno
    hide noah_reyes

    scene bg ch14_612518_8 at full_bg
    # play music "music_placeholder"  # [Music: Cello resolves into a held minor chord, leaving space]
    # play sound "sfx_placeholder"  # [Sound: Tide breathing, distant and patient]

    scene bg ch14_612518_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter33
    return
