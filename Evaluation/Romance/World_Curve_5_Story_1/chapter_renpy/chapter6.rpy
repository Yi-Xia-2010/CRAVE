label chapter6:

    # [Scene: Boardwalk → Festival Grounds | Late Morning — Overcast with shifting sun]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Light acoustic guitar with warm strings; gentle percussion like footsteps]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation, soft splashes from tidal pools, occasional cries of gulls]
    "You arrive at the festival in a way that makes you notice how people arrive—slow, purposeful, carrying buckets and gloves rather than slogans and placards. The air tastes of salt and wet wood; someone is frying"
    "something sweet in a cart, and the smell threads through the brine. Your satchel hangs against your hip, heavy with a folded map and the compass that has felt like a totem and a trial in"
    "equal measure."
    "You think of the routes that led here—how the town argued until its voice was hoarse—but you don't catalogue whose slogans were louder or whose calls were sharpest. What matters now is this: hands in mud,"
    "small shoots trembling in plastic pots, and the way people bend to listen when Dr. Linh speaks. The past has been a long tide; today, the tide is carrying lots of things away and bringing new"
    "ones in."

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Seedlings being pressed into soil, low hum of conversation]
    "You taste the damp of peat on your tongue as you kneel to hand over a bundle of shoots. Your fingers are rough from the morning's work; the fabric of your navy jacket is darkened with"
    "mud. When you fold a shoot's roots into the sand, the motion is small and rote, and also holy. You feel the compass at your throat, cool against skin, a small weight that now steadies rather"
    "than binds."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Salt-tolerant beds slow waves, bind sediments, and create living barriers. They're not a single fix, but they're part of a network of protections. Think of them as gardens that fight back against the sea."
    show aria_marin at right:
        zoom 0.7

    aria_marin "And they'll keep the water from taking the boardwalk where our shops and homes meet the marsh?"

    dr_linh_pham "They won't stop everything. They work with tides, not against them. But combined with thoughtful raised walkways and community-managed berms, they can spare the places that matter most."
    "You watch as a child—Maya's mural-streaked raincoat bobbing—presses a shoot into the mud with two deliberate thumbs. The child's grin is contagious; Kai watches her for a long beat and doesn't speak. There's a slant of sunlight for a moment, and in Kai's amber eyes you see something unguarded."
    show kai_solano at center:
        zoom 0.7

    kai_solano "You always manage to make a planning meeting feel like a party."

    aria_marin "You mean you never planned a party around a policy brief?"

    kai_solano "No. Parties tend not to have fine print."
    "His laugh opens something between you. He reaches for a shoot, kneels beside you, and for a second you work in companionable silence—two sets of hands tending the same fragile thing."

    menu:
        "Lend your compass-streaked gloves to the child":
            "You pull off your gloves and hand them over; the child looks up at you as if you've handed her a treasure, and the way she cradles the shoots makes your chest unclench."
        "Keep your gloves; show the child how to hold the eelgrass gently":
            "You keep your gloves and guide the child's hands with your own; her small fingers fit inside yours, and she presses the roots in with concentration, proud and solemn."

    # --- merge ---
    "Return to the main scene."
    hide dr_linh_pham
    hide aria_marin
    hide kai_solano

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Quiet piano motif; a hopeful swell]
    "Noah's presence is a small weather. He doesn't stride into the center; he moves, instead, along the edges, talking to volunteers who were skeptical of his firm a season ago. When he approaches you, his smile"
    "is rehearsed but genuine, and his hands are free of corporate neatness—there's mud under his nails from helping repair a raised walkway overnight."
    show noah_vega at left:
        zoom 0.7

    noah_vega "You look like you could use a cup of bad coffee and a smile."
    show aria_marin at right:
        zoom 0.7

    aria_marin "You brought coffee?"

    noah_vega "The firm has decent catering. I figured if I'm going to be part of the pivot, I should at least bring the bad coffee personally."
    "You let out a short laugh. It’s the sort of laugh that loosens a seam you didn't know was taut. You can't pretend everything is unscarred—there are still whispered doubts and old grievances carved into the"
    "boardwalk planks—but there's a practicality now that feels like work rather than negotiation: he helped fund the tenant protections you insisted upon. That fact grips you as both compromise and small victory."

    aria_marin "We didn't win everything. But the cultural block—it's open. People can keep shops. The berm held in the models Linh ran."

    noah_vega "And when PR made the firm rethink the rollout, it gave us time. Time is a resource we didn't have until attention made it costly to ignore the people on the map."
    "You study his face. There's real contrition in the set of his jaw, and the way his shoulders have begun to drop. You think of his niece, and the raw human reason that pushed him from policy memos toward late-night calls with your team."

    menu:
        "Offer Noah a brush-off handshake":
            "You offer a brief, formal handshake; it's polite and efficient. Noah accepts it with a professional nod, and the air between you cools into respectful distance."
        "Let your hand linger in his, acknowledging the cost":
            "You let your palm rest a moment longer than necessary. Noah's fingers curl slightly, surprised, and you both seem to agree—without words—that this is not the end of blame but the start of repair."

    # --- merge ---
    "Return to the main scene."
    hide noah_vega
    hide aria_marin

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Old wood creak, Tomas's voice thick with remembered salt]
    # play music "music_placeholder"  # [Music: Low, resonant cello underlines his story]
    "Elder Tomas clears his throat, the sound of someone shifting a lifetime of stories into the present."
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "I remember when the sea used to take less and give more. We used to dream of fish that filled nets like silver coins. But we also learned how to repair things—fasten the boards with hands that knew one another. Those hands are still here."
    "A hush spreads. The seeds in your pockets feel like small promises. He looks at you—not searching, not judging, but noting."

    elder_tomas_quay "You promised the town you wouldn't sell its bones. Maybe you didn't promise you'll fix every break. That wasn't the kind of promise we ever had. We promise to try."
    show aria_marin at right:
        zoom 0.7

    aria_marin "Trying is better with company."

    elder_tomas_quay "We both know that. Good spirits and stubbornness, girl. That's how this town lasts."
    "Maya, your sister, finds you between shifts handing out biodegradable pots. Her hair is shorter since the last storm; paint still clings to the collar of her raincoat. She touches your forearm with a quick, fierce affection."
    show maya_marin at center:
        zoom 0.7

    maya_marin "You look like you slept on the map."

    aria_marin "I might have. Worth it?"

    maya_marin "It looks worth it. Just...don't start keeping all the best seeds to yourself."
    "You both laugh. Her eyes search yours, then rest on Kai nearby. There's an unspoken tally in her look—what was broken and what has been mended—and when Kai catches her gaze he gives a small, sheepish wave."
    hide elder_tomas_quay
    show kai_solano at left:
        zoom 0.7

    kai_solano "I misread things before. I let anger make the scale tip too far. I thought urgency meant bulldozing the middle ground."

    aria_marin "And I thought process would protect everyone. I forgot that sometimes process can get lonely."

    kai_solano "You were trying to hold everything at once. I didn't see how heavy that was for you."
    "You let his fingers close around yours. His hand is warm, callused, the map of years of labor across it. It's not a declaration—no swept vows—but in this gentle touch there is repair. The world around"
    "you continues: kids plant, volunteers laugh, Elder Tomas begins another tale. Love feels like a steady flame, small but enough to heat two people through a cold night."

    menu:
        "Press your thumb under Kai's knuckles":
            "You press a thank-you into his palm—a quiet concession and a quiet acceptance. Kai's jaw eases; he breathes out, and for the first time in a long while you see him decide to be patient."
        "Squeeze his hand, then let it go and get back to work":
            "You squeeze his hand quickly, a promise that work comes first—and love, steady as the tide, will be patient. Kai nods, understanding that repair is both private and public."

    # --- merge ---
    "Return to the main scene."
    hide aria_marin
    hide maya_marin
    hide kai_solano

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell into a warm, sustained chord]
    "The festival moves like a slow, faithful tide. People wander into the cultural block, pausing at a bakery that smells of warm salt and sugar, at a small bookshop with a hand-painted sign, at a workshop"
    "where an elderly carpenter teaches teenagers to plane wood the old way. You stand at the edge of it and feel the town settle around what you now call preservation—not static museum pieces but living places"
    "with new scaffolding."
    "You remember the models Dr. Linh ran earlier in the year, the long nights of meetings with Noah's firm where you pressed for tenant safeguards until the contract smelled of ink and concessions. You remember the"
    "occupation's noise and how it made quiet things—listening, accountability—exposed and necessary. The victory is messy; it tastes like sand and metal and the sweetness of a pastry someone hands you as thanks."
    "You walk to the edge of the inlet. Wind fingers through your hair. A small wave pushes in and then pulls, and the eelgrass you planted holds a crumb of silt where it was loosened. You"
    "touch the compass against your throat. It feels lighter now—less a shackle and more a wayfinder."
    show aria_marin at left:
        zoom 0.7

    aria_marin "We didn't make it perfect. We made it repairable."
    "A reporter you know from a community newsletter wanders up, microphone replaced with a paper and pen."

    "Reporter" "How does it feel, Aria? To see it here—this festival, this living shoreline?"

    aria_marin "It feels like starting. Not the end we wanted, maybe, but it’s a continuing that includes more voices. We built protections with people at the center, and we kept our shops. We kept our stories."
    "Noah stands a bit away, watching a young woman hammer a board into a raised walkway. Kai watches children plant eelgrass. Maya has paint on her fingers and the stubborn, furious grin of someone convinced of"
    "the rightness of their work. Elder Tomas tells a new twist to an old story and throws in a line that makes the children shriek with laughter."
    "You breathe in. The salt is thick; the sky has the sheen of an ocean held back by cloud. Later that fall, when a storm runs farther up the inlet than anyone expected, the living shorelines"
    "will take the first battering and dull the worst of the surge; the raised boardwalk will lift and flex rather than snap; a row of houses will stand where models had once said they might not."
    "These things do not erase loss or the slow ache of change. They do, however, keep people in place—hands together where they can rebuild."
    "You look at Kai again. He squeezes your hand, not loudly, but with a steady pressure that says: I misjudged how you carry hope. I will try to carry part of it with you."

    aria_marin "This is enough. Not perfect. Not complete. But enough to keep going."
    "You tuck the compass back into the satchel, the silver band warming against your palm. Your jacket is smeared; your hands are raw from digging; your face has a thin line of salt where you blinked"
    "too fast. A child presses a little flag into your hand—one marked with a painted eelgrass and your town's name."
    "You fold the flag into your satchel beside the map. You sit on a low step and watch the festival breathe—an event that will be spoken of in small, grateful ways for years to come. People"
    "will point to this day and say, 'We planted that,' and some will remember the nights of shouting and the nights of agreeing, and they'll teach the next generation to listen to both."

    aria_marin "Come on. Help me plant another bed."
    show kai_solano at right:
        zoom 0.7

    kai_solano "Lead the way."
    "You stand together and go back down to the water, hands finding each other on the walk back like a rope thrown across a small, uncertain divide. The town keeps working. The town keeps loving in small, stubborn increments."
    hide aria_marin
    hide kai_solano

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Full, hopeful swell; choir-like overtones mixed with strings]
    "In the end, the festival is quieter than the first rallies, but steadier—a cadence that speaks of habit and tending rather than flash and fury. The living shorelines are a beginning you can plant your hands"
    "in; the protected block is a place your sister can paint in; the tenant protections are a promise inked imperfectly but enforced; Noah has a new set of messy hands; Kai has a new patience."
    "You press your thumb against the compass inside the satchel—a gesture that feels ceremonial and practical all at once. You let the sound of laughter and the slap of small waves be the last thing you memorize from the day."
    # [Scene: Festival Grounds | Late Afternoon — Sun slanting low]
    # play music "music_placeholder"  # [Music: Gentle diminuendo into soft, sustained notes]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, low laughter, the faint trowel scrape as volunteers finish planting]
    "You close your eyes for a second. The town hums like a thing healed enough to keep going. Love flickers, steady and private: a weathered hand finding yours beneath a drape of salt air. You do not promise forever; you promise to keep showing up."
    "You open your eyes and step forward."

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, final chord lingers]

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
