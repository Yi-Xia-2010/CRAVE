label chapter16:

    # [Scene: Promenade | Early Evening]

    scene bg ch11_ac0435_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent strings; a staccato electronic pulse underlies the air]
    # play sound "sfx_placeholder"  # [Sound: Phone buzzes in the background, gulls cut through wind]
    "You press the compass harder against your throat because it feels like the only honest weight you still own. The cord bites a shallow line in the skin. Behind the glass of the Beacon, words you"
    "signed for—phrases you let sit in legal soil because you needed time—are surfacing in the wrong light."
    "Your phone vibrates again. The screen blooms with a thread: a leaked clause flagged, bolded, quoted—'investor claims under unforeseen exigency.' The headline is a cold pulse on the town's sleep. Comments tumble in; someone posts annotated"
    "screenshots of the contract. Somewhere, a property group's logo appears, tagging waterfront titles for review. Insurance companies send terse notices: premiums recalculated, rates subject to immediate reassessment."
    "The world tilts. Not literally—just the map you were holding. You taste metal, panic thin and bright at the back of your tongue."
    "Noah Reyes is at your shoulder before you realize you've looked for him. His hand finds the small of your back, then steadies on your shoulder—warm, solid against the damp of your jacket. The gesture is simple but precise: a human brace against a machine-cold night."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "They're amplifying the worst line. They'll spin fear into a firewall between neighbors.' (He rubs his thumb in a small, deliberate circle on your shoulder.) 'We can do two things right now: hold the facts up where everyone can see them, or let rumors do the shaping."
    "You want to say the thing you usually keep in the ledger—how legalese can become a weapon if left alone—but the storm is already unspooling overhead and your voice is a thread against thunder."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "If people panic about titles, they'll sell, or they'll take mortgages they can't afford. They won't wait for audits. They won't wait for lawyers. They will move to survive the present.' (You let anger and exhaustion lace the words.) 'We have to stop the panic before it eats the town."
    "Noah Reyes: (breath close to yours) 'Then we anchor them. Transparency, now. A public thread with the exact clause, line by line, and our—' (he catches himself) '—and our explanation. And a meeting tonight. Mayor Rosa needs to speak.'"
    "You nod, but your fingers tighten on the compass until the brass is warm. The Beacon's feed lights up your face with a cold, indifferent white. Even that light feels like it belongs to someone else."

    menu:
        "Open the thread loudly—call attention to the leak":
            "You hit reply and type with a tremor. Your words are careful but unflinching; you paste the clause, annotate it, and send it to the community list. Within minutes, the thread explodes with questions and angry hearts."
        "Hold the line—focus on the storm first":
            "You tuck the phone away. The noise will have to be handled, but the wall failing is immediate. You tell Noah: 'Storm first. People first.' He nods and already looks toward the boardwalk where the first alarms blink."

    menu:
        "Help Eli with the ferry—take the helm":
            "You leap onto the skiff, cold water spitting at your knees. Eli curses under his breath and hands you the oars. The current fights every stroke but you get the first elder to shore. Her fingers find yours like a prayer; you feel the town's history lean into your hands."
        "Stay at the marsh and coordinate volunteers":
            "You stay ankle-deep in mud, shouting at lines of people moving sandbags into place. Your voice rasps but the marsh responds: soil packed, cordage tied, a living buffer forming under your palms."

    menu:
        "Work with Lila to mobilize corporate resources to shore the town immediately.":
            jump chapter19
        "Expose the leaked clauses and pursue legal action with Mayor Rosa to renegotiate terms publicly.":
            jump chapter28
        "Mobilize the community for an accelerated natural restoration—risky, resource-heavy, but autonomous.":
            jump chapter19
    return
