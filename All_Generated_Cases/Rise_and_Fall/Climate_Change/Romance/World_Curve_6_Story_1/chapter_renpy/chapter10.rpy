label chapter10:

    # [Scene: City Hall Promenade | Early Evening, Steady Rain]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm piano motif, a single note of cautious optimism]
    # play sound "sfx_placeholder"  # [Sound: Rain tapping in soft, steady percussion; distant gulls]
    "You step onto the promenade with your jacket clinging to your shoulders, leather journal damp at your side. The petitions are folded inside the journal like quiet evidence—names in ink that smell faintly of salt and"
    "late-night photocopy toner. The city lights smear on wet stone; every reflected screen is a promise, every reflection a ledger."
    "Your pulse hammers warm and bright under the ribs where guilt lives. You taste coffee and metal in the air, and beneath that the brine that has been home to half your life. You breathe slow"
    "and let the braid of hope you’ve been nursing loosen into something louder: you came here because the neighborhood could not be ignored."

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps—one measured set approaching; Ilan’s smartwatch soft chime in the distance]
    "Evelyn looks at you as though she is calibrating a machine: a quick tilt, an internal running of variables. Her eyes are steel-gray and direct; she wears decisiveness like armor and, for a moment, you feel small and essential at once."
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "Ms. Marin. Thank you for coming. I read your submission. The archive—it's thorough."
    "You can hear surprise in her voice, a thin note that complicates the clean lines of her public persona. It makes your throat soften."
    show ava_marin at right:
        zoom 0.7

    ava_marin "I came because numbers are only meaningful when someone remembers what they measure. These names—these stories—are the ground people stand on."

    evelyn_harrow "I understand the cultural value. I do. I also understand what insolvency looks like. Bond markets are already pricing the coastal districts as extreme risk. If we don't act at scale, insurers will withdraw, and the city will have fewer levers to protect anyone."
    "Her words are crisp, almost surgical—risk matrices and timelines like predictable waves. Still, there is no sneer. There is the economy of a pragmatist who has watched failure once and is allergic to repetition."
    "You feel the old image—your uncle's shop dark and empty—fold into the present and make your chest tighten. But alongside that clench, a current of something else runs: the tiniest ember of possibility. If she is"
    "offering a seat at the table, then maybe you can move more than a line item."

    menu:
        "Open the journal, show the map with the milkman route":
            "You slide the journal open to the folded map; Evelyn's frown eases as she traces a path with a finger—human routes become data in her hands."
        "Hold the journal closed, let the petitions speak":
            "You keep the journal clasped, and slide the petitions forward. Names press against the glass between you and her, weight enough to tug at policy language."

    menu:
        "Propose a cultural covenant tied to property deeds":
            "You outline the covenant, your voice steadying as you picture Tomas stamping a deed. Evelyn nods, scribbling a notation—small, but real."
        "Suggest a publicly funded cultural trust managed by neighbors":
            "You sketch the trust model with gestures; Ilan adds pragmatic supply-chain notes. Evelyn pauses, considering community oversight as an accountability lever."

    menu:
        "Accept her offer to formalize Tideward’s plan under city oversight.":
            jump chapter12
        "Refuse to work with Evelyn and organize a citywide populist coalition instead.":
            jump chapter14
        "Negotiate a hybrid: accept oversight but secure contractual guarantees for residents and cultural preservation.":
            jump chapter17
    return
