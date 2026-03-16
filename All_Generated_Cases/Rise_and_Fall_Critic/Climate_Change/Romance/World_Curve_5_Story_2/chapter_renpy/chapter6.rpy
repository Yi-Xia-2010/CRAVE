label chapter6:

    # [Scene: Restored Check Dams | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft rasp of rope, distant gulls, low conversation—work and relief braided together]
    # play music "music_placeholder"  # [Music: Warm strings swell beneath a steady, hopeful piano motif]
    "You step onto the softened ground where the living shore meets the boardwalk, the soil giving under your boots with a familiar, bracing dampness. The morning smells of peat and hot coffee; salt hangs in the"
    "air in a way that tastes like a promise instead of a threat. Your notebook—edges softened by rain and by the many hands that have turned it—sits heavy in your jacket pocket. The pressed marsh grass"
    "inside feels like a heartbeat against the paper."
    "People are already at work. Hands you know—callused, ink-stained, freckled—pass sandbags, tie rebar, nurse seedlings. Faces are tight with exhaustion and bright with something that looks like faith. You remember the night when everything narrowed to"
    "a single unresolved note. Now there are chords: a council's approval whispered through a liaison's sleeve, an emergency fund wired in muted triumph, a midnight salvage of sewn packs that held long enough. Which of those"
    "threads led here is not needed; what matters is that the corridor holds, and that the town—shaken but not broken—has gathered itself into action."
    "Jun Park approaches, sleeves rolled, tablet dangling with new models. His grin is wry but unguarded."
    show jun_park at left:
        zoom 0.7

    jun_park "Data looks better than we dared to hope. The check-dam pressure is within safe thresholds this morning—biological recruitment is already visible in the upper pools."
    "You let out a breath you didn't know you'd been holding. 'Visible recruitment' feels like a small miracle, and you say it aloud because saying the words makes them more real."
    show aria_solen at right:
        zoom 0.7

    aria_solen "How long until we can call this stretch 'stabilized' on reports?"

    jun_park "Conservatively? A season. Politically? Depends on the council narrative. Practically? We can call it stable enough to start moving market goods back onto the boardwalk today."
    "You can see Marta across the shallow channel, her hands stained and her grin wide enough to split the morning."
    show marta_quin at center:
        zoom 0.7

    marta_quin "Aria! Bring that face over here. The vendors are already asking if we'll do the seed program next market."
    "You move toward her, feeling the boardwalk hum underfoot—the same hum that used to be worry. Marta squeezes your shoulder in a way that says she knows the nights you spent worrying into the grain of wood."

    marta_quin "We didn't lose everything. Not this time."
    "Her voice is both fact and benediction. You let it settle."

    menu:
        "Help Jun check the upstream packs":
            "You crouch with Jun, fingers finding the knots. The cold soil presses into your palms; you tune into the system's tiny oscillations and feel a quiet, technical joy."
        "Walk the boardwalk and greet the vendors":
            "You cut across the planks toward the market. A vendor hands you a warm, salt-sweet pastry and a child presses a seed packet into your palm. Community returns like tidewater—insistent, generous."

    # --- merge ---
    "The scene continues."
    hide jun_park
    hide aria_solen
    hide marta_quin

    scene bg ch6_601bcb_2 at full_bg
    # [Scene: The Helix | Mid-Morning]

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping softly at the hull; distant chatter from the market; the Helix's machinery sighing a steady beat]
    # play music "music_placeholder"  # [Music: Acoustic guitar phrases weave under the piano—the air contains warmth and steadiness]
    "The Helix feels like a home coming: the single familiar smell of compost and leaf mold, the soft leaf-scratch against glass. Eli is there before you, sleeves rolled, a smudge of soil on his cheek. He"
    "moves with the easy improvisation that always made you trust that, somehow, a plan could be made from scraps."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Look at this—our little swamp babies are already sending roots into the mesh. You should see the way the kids from the market point at them like they're constellations."
    "You can't help the small, vulnerable laugh that escapes. It is relief translating into sound."
    show aria_solen at right:
        zoom 0.7

    aria_solen "We kept a lot of constellations frayed tonight."

    eli_navarro "We almost lost it. You almost—' (he stops, searching your face) '—you almost carried that alone."
    "The words fall in the warm light like an offering. You feel your old reflex tighten—the one that wants to shoulder everything quietly so others don't have to. But the day has rearranged something in you;"
    "standing at the Helix you remember your mentor's ring warming against your finger and the way your sibling laughed when mud splattered their boots. Guilt has taught you resolve, but trust has to be learned."

    aria_solen "I thought I had to. For a while, it felt like the only way to keep from losing more."
    "Eli reaches for your hand with no theatricality—his fingers find your palm and stay."

    eli_navarro "You don't have to do it by yourself. I know you're built for it, Aria, but I'm here. We—' (he glances at the seedlings) '—we get to be the kind of people who rebuild together, not just rebuild for."
    "You blink. The words are small, but true. You swallow the tightness in your throat and let warmth spread through your chest instead."

    aria_solen "Okay. Together."
    "The sentence feels like a new type of work—deliberate, fragile, and fully worth the effort. Eli smiles then, the way he does when he's both relieved and proud, and the Helix hums a little brighter."

    menu:
        "Lean into Eli's hand":
            "You let your fingers curl around his. It's not a grand promise—just a present, grounding—to share the next shift, the next sleepless night."
        "Pull your hands back, focus on the seedlings":
            "You take a step toward the seed racks, returning to the task. The warmth between your palms lingers, a slow ember you can tend later."

    # --- merge ---
    "The scene continues."
    # [Scene: Boardwalk & Old Pier Market | Afternoon]
    hide eli_navarro
    hide aria_solen

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Vendors call prices; a pot of soup bubbles; someone laughs, voice bright as a bell]
    # play music "music_placeholder"  # [Music: The piano returns—brighter now—layered with a community chorus of percussion; the track moves forward with confident steps]
    "The market is full—full of life and small economies that smell of smoked fish and new bread. You walk through, receiving offers of thanks in the form of wrapped parcels, earnest nods, and the steady, practical kindness of people who know how to hold one another."
    "Lina Voss approaches, her coat still neat despite the march of the morning. She's holding a slim envelope. The expression on her face is careful but not closed; something in her posture says she has been moved by what she has seen and heard."
    show lina_voss at left:
        zoom 0.7

    lina_voss "The council issued conditional approvals for the corridor's governance model. We have to meet a few more reporting milestones, but the permits are in—conditional on community oversight and continued monitoring."
    "You look at the envelope like it's a talisman. It's not all the victory you imagined in quiet fantasies, but it's real and it's breathable: permission to continue, to scale with constraints that keep stewardship tied to those who live here."
    show aria_solen at right:
        zoom 0.7

    aria_solen "Conditional oversight—transparent checkpoints. That was important."

    lina_voss "Jun's data, and the way people turned up at the hearing—you made it a civic moment. The council listened."
    "The vendors around you murmur, a tide of gratitude and pragmatic questions—who will deliver the logs, who will monitor the next storm, which stalls can set up permanently on the newly raised planks. Marta steers the flow, practical and fierce."
    show marta_quin at center:
        zoom 0.7

    marta_quin "We'll make a rota. Jun will do the modeling. Lina, can we get a liaison line so we don't get blindsided by the next capital push?"

    lina_voss "Yes. And I'll advocate for more funding to support the community-led maintenance plan."
    "You close your eyes briefly. The sound of the market—the immediate, practical bustle—works its way into the nook of your chest and settles. It confirms something you could not know in the rawness of crisis: resilience is a hundred small agreements, many hands, and the stubborn insistence to keep trying."
    "Vendors lift a makeshift toast with paper cups. Someone cracks a joke about the council finally being useful; someone else offers you a hand-stitched paddle as a mock ceremonial award. Laughter threads through the exchanges like gold wire."

    menu:
        "Accept the paddle and make a short speech":
            "You hold up the paddle, clear your throat, and talk about the corridor as a living promise. You speak of loss and of labor, and people listen. It feels ceremonial and true."
        "Decline and continue helping vendors":
            "You wrap the paddle back in your hands and walk the stalls, trading plans and names. The work you do in the small middle spaces feels like a speech, enacted rather than declaimed."

    # --- merge ---
    "The scene continues."
    hide lina_voss
    hide aria_solen
    hide marta_quin

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: The instruments swell and then settle into a warm, steady cadence—the music of a community that has been through ordeal and is now, deliberately, choosing to rebuild its joys as well as its defenses]
    "You find a moment with Eli away from the busiest row, leaning against the railing of the boardwalk. Sea-spray beads the wood; your palms feel warm with the day’s labor. He looks at you with an expression that contains question and answer both."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You were scared there for a bit. I was, too. But watching everyone pull together—seeing you make the hard calls—I'm proud of you."
    "You tilt your head. Pride from someone you love is not a simple thing; it carries relief, and a reflective warmth."
    show aria_solen at right:
        zoom 0.7

    aria_solen "I was afraid I'd let everyone down. That old reflex—thinking the only way to keep people safe is to do it myself."

    eli_navarro "We don't need solitary heroes. We need people who can ask for help. Who can accept it. You're doing both—and it makes this better, not weaker."
    "You inhale. The ring at your finger catches the light, and for a beat your late mentor is in the space with you—their voice in memory saying that stewardship is always collective."

    aria_solen "I don't know if I can stop trying to fix everything. But I can try to let other hands be part of the fixing."

    eli_navarro "That's all anyone can ask."
    "He leans in and kisses you—not as a grand rescue, but as something steady and human, the small miracle of two people choosing proximity after damage. It is messy and imperfect and entirely right for the afternoon."
    # [Scene: Evening — Boardwalk Overlook | Sunset]
    hide eli_navarro
    hide aria_solen

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant tide, laughter, a chorus of low conversation]
    # play music "music_placeholder"  # [Music: The piano motif returns, rounder now, with voices layered like harmonies—complete and hopeful]
    "Night settles like a soft blanket. The corridor has been re-staked, the Helix humming its quiet life, the market packed down into satisfied stillness. Jun sends a last message: preliminary recruitment rates look promising. Lina emails"
    "the final conditional paperwork. Marta organizes the volunteer list with an efficiency that would make a bureaucrat weep."
    "You sit with Eli on the edge of the boardwalk, legs dangling over the water. The ring on your finger feels like a small compass against your skin; your battered notebook lies open beside you, marsh grass pressed between pages as if to preserve a promise."
    "You think of the sibling you lost—how the promise you made then set you on this track. You think too of every person who tied a knot at two in the morning, who fed seedlings with"
    "careful hands, who argued in council rooms until voices were hoarse. You feel the shape of your life soften around the steady presence of other people—faults and all."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "So—what now? More grants? More ceremonies? More coffee at ridiculous hours?"
    "You laugh, the sound elevated by the salt-air cool. 'All of that. And tending. Every day is tending. We'll make a plan that includes rest, too. I want to learn how to accept help without guilt.'"

    eli_navarro "We'll figure it out together."
    "You rest your head against his shoulder for a moment. The tide contracts and expands; the corridor breathes with the world. It will still be work—hard and ongoing. There will be storms and disagreements and the"
    "slow, patient labor of ecosystems. But right now, the shore is held, and with it your place in the town and a love that has shifted from improvisation to intention."
    hide eli_navarro

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: The music resolves into a warm, sustained chord]
    "You trace a finger over the pressed grass and close the notebook. The city—the people—move around you, a living lattice of care that you helped breathe into being. The corridor is not perfected. It is, instead,"
    "reclaimed: stitched by many hands, anchored in community trust, and warmed by the steady refusal to surrender to fear."
    "You stand. Together, you walk back along the boardwalk toward the market's sleeping stalls. Conversation follows—a plan for the next morning, a joke about the council's new-found humility, an exchange about who will take the first"
    "watch when another swell rises. Plans are made with laughter, because laughter helps stitch muscle to mind."
    "You feel the tide within you settle into something like peace. It is a work-formed peace, not a naive calm, and it holds both grief and gladness. The Helix hums; the check dams flex and flex"
    "again like patient lungs. You feel, at last, less alone in the promise you made to the island—and the promise begins to feel possible."
    # play music "music_placeholder"  # [Music: Fade to a single, hopeful piano line; strings linger like a warm afterglow]

    scene bg ch6_601bcb_8 at full_bg

    scene bg ch6_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
