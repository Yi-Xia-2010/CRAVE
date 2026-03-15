label chapter6:

    # [Scene: Coves | Dawn — After the Surge]
    # play music "music_placeholder"  # [Music: Low, brittle strings; distant thunder like a fist against a drum]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water sluicing through new channels; the metallic rasp of machinery left to idle; gulls crying thinly]
    "You arrive to the coves with salt in your mouth and the taste of copper at the back of your teeth. The air is cold and clean in the technical way of rain-scrubbed mornings, but the scene before you is not clean—it's raw with things undone."
    "In some versions of what happened, machines came like a tide of their own—armored diggers biting into the curves Tomas has mapped in his hands for fifty years. The earth smells of upturned roots and diesel; the fjord's edge looks amputated, neat as a surgical cut."
    "In other versions, Lux delayed the gates to bargain for a clause, and the sea answered the delay. A sudden surge pushed farther than the models had last winter, and a low street near the diner"
    "took on a shallow, oily water that ate at foundations and a tenant's life-supply of clothes and keepsakes."
    "In yet another version, the contract you leaked frightened investors into silence. Cash dried at the wrong hour; walls waited for money that never arrived; a spring high tide found a weakened jetty and collapsed it into black foam."
    "You do not know which exact timeline is yours—not in the literal ledger sense—and you do not need to. The meaning is the same: the town has a new line in its skin where things split, and you can read grief there."
    "Tomas Bianchi stands on a ragged knoll, coat zipped to his chin, and watches the water as though it might say its name if he stares hard enough. His beard is flecked with salt; his eyes are a closed, small mourning. He does not look at you when you approach."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "You can see what it did,' he says finally, voice a stone rolled half into the surf. 'It found the seam, like you said it would if—"
    "You want to answer. You want to say that you did what you thought would save people, but that line will slope into excuses. Instead you press your thumb against the face of your brother’s dive"
    "watch and feel the cool metal—its cracked crystal, a frozen minute—anchor you to the particularity of loss. The watch is small, dense with the weight of promises you made and cannot undo."
    "Hana Kim comes up the path, apron dark with water, eyes red at the corners. She keeps her hands busy—folding a tarp, checking tied lines—as though movement can keep grief at bay."
    show hana_kim at right:
        zoom 0.7

    hana_kim "They called the protestors fools this morning. Some took banners to the promenade. Some went to the docks to try and stop the machines. And then—' She swallows, breath sharp. 'Then Mara's unit flooded. Her kids... the couch they inherited from her father is ruined. We moved what we could, but—"
    "Kaito Sato arrives with his satchel half unzipped, sensor pendant blinking a slow, hurtful blue. He moves through the scene like someone who has been trying to measure ruin with instruments, only to find that instruments do not soothe like hands do."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "We logged the wave crest,' he says, more to the pendant than to anyone. 'We thought the buffer would hold until construction finished. The models—Maya, the models said one thing. The sea said another.' He looks up at you. His hands tremble just enough to betray him. 'You signed, or you bargained, or you leaked—whatever you did, I trusted it would buy time. This is—"

    kaito_sato "If you thought this would spare people, tell me. Tell me what you weighed."
    "There is a long beat where the sound is just the water and the light metallic cough of a stranded hydraulics pump. The world is a list of small betrayals: salt on the soles of boots,"
    "a child's shoe sticking out of muck, the iron tang of a broken gas line that no one can fix yet."
    "You could answer with logistics, with data, with the language you have trained yourself to, the ledger of pros and cons that once helped you sleep. You could tell Kaito he is right to be afraid"
    "of partial measures, that Lux's machines cleaved coves that were homes to the little fish Tomas relied on, or that Hana's tenant lost everything because the gates weren't done, or that the leak froze funding and"
    "that the jetty gave. Each sentence will be true in some version and false in another."
    "You choose a smaller truth."
    hide tomas_bianchi
    show maya_inoue at left:
        zoom 0.7

    maya_inoue "We tried to hold them all at once.' Your voice cracks a bit at the edge and you feel it like a small shiver down your spine. 'We tried to buy time and keep control and not hand our town off like a receipt. It wasn't enough."
    "Kaito's laugh is a short, pained thing. He steps closer and his fingers find your arm with the awkward familiarity of someone holding onto a colleague more than a lover in public."

    kaito_sato "Not enough,' he repeats. 'Not enough for them. Not enough for Tomas' nets or Hana's tenant. Not enough for—' He looks away, jaw clenched. 'You thought you were choosing between bad and worse, Maya. But people need someone to point at when the worse happens. You're the one they can point at."

    menu:
        "Kneel and inspect the jetty":
            "You crouch, fingers tracing the line where treated timber met sea. Salt flakes on your knuckles. The wood is softer than it should be; your stomach rolls as you imagine the town's boats without a safe berth."
        "Stand and keep Tomas company":
            "You stand beside Tomas, letting the silence do what speech cannot. He grunts once, a small acknowledgement, and together you watch the gulls pick at something the tide left behind."

    # --- merge ---
    "Both outcomes reconverge to continue the scene."
    # [Scene: Promenade / Forum Back Rooms | Morning]
    # play music "music_placeholder"  # [Music: Low brass; a single violin holds a minor note]
    hide hana_kim
    hide kaito_sato
    hide maya_inoue

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled arguing from the forum; someone banging a table off-screen; the slap of wet nylon banners]
    "The forum is not a debate anymore; it is an inquest. People crowd the room with faces pasteline with anger and exhaustion. They lean like a tide against one another. The mayor, paper-thin behind her resolve,"
    "presses a hand to the podium and looks at you like a ledger that has been forced to present the math the town needs."
    "Hana Kim stands at the edge of the room, hands clenched around a thermos, watching each speaker with a rawness that makes her younger, more exposed. Tomas is on the second row, a granite silhouette. Kaito"
    "sits slightly apart, staring at the table, as though measuring the room's temperature with his eyes."
    "Lux arrives as if entering any room where money and control are contending. Her coat is unruffled; the rain won't touch her shoes. She chooses her words like seals unrolled by practice."
    show lucia_lux_moreno at left:
        zoom 0.7

    lucia_lux_moreno "We proposed a defense. It would have been fast and effective. Regret that floods came before construction—' She gestures, precise. '—is not an argument against action, Maya. Systems need deployment. Delays cost lives."
    show hana_kim at right:
        zoom 0.7

    hana_kim "Delays cost lives, too! When you delayed your gates, my tenant lost their home. Do you own that?"

    lucia_lux_moreno "Responsibility is a shared thing. Governments, contractors, and citizens all carry it. Blame doesn't protect anyone."
    "Tomas Bianchi speaks then, and the room stills—the kind of still you notice because it weighs on the bones."
    show tomas_bianchi at center:
        zoom 0.7

    tomas_bianchi "When you cut the cove, the little fish stopped coming. When you left the gate half-finished, the water kept finding weak spots. When money left the table, we were asked to stand by without tools. Whoever you are, whoever you claimed—this place matters."
    "Somewhere in the room a child cries, and the sound lances through the adult arguments, making them smaller and more careful for a breath."
    "Kaito Sato stands suddenly, anger replacing the calculation you have grown to expect from him. His hands are open, a human pleading."
    hide lucia_lux_moreno
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "You were my measure of care,' he says directly to you, voice raw. 'I thought we were building things together. I thought there was a way to thread the needle. I poured data into trust. I trusted you.' He looks at Lux, then back at you. 'But people are hurting. You picked a path. We all have to live with what it did, Maya."

    "There are shouts. Someone in the back calls you a "sellout." Another voice defends choice" "We had to do something!"
    "You try to speak—explain the calculus, the moral arithmetic, the ways you tried to avoid choosing anyone but the town. Your words fall against the room like rain on a tarp. They bead, then slide away."
    hide hana_kim
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "I—I tried to hold us together. I thought if we negotiated we could keep the local clauses. I thought if we signed we could save people fast. If I leaked it, I thought the town deserved to know. None of that—' Your sentence breaks. 'None of that saved everything."
    hide tomas_bianchi
    show lucia_lux_moreno at center:
        zoom 0.7

    lucia_lux_moreno "Regret isn't a policy."
    "Kaito's laugh again, the sound more helpless than angry now."

    kaito_sato "You think policies will hold when people are angry and cold? You think contracts can stitch the hole in a life? We were trying to build scaffolds, Maya, and maybe you set the wrong nails."
    "You feel each accusation like small rocks thrown into a shallow bay—they splash, they stain, and the ripples find you."

    menu:
        "Walk out to the promenade and speak to protestors":
            "You push through the side door into drizzle and the mob's heat. Voices rise, words fly; some call your name, some spit at your choices. You try to answer, but every sentence gets caught on the barbed wire of what people have lost."
        "Stay and confront Lux privately":
            "You stay. In the quiet hallway outside the forum, you find Lux folding her gloves. The conversation is small and sharp; she doesn't soften, but she doesn't gloat either. You feel the old intimacy in the edges of her voice, and it hurts."

    # --- merge ---
    "Both outcomes reconverge to continue the scene."
    # [Scene: Storm-broken Lighthouse | Late Afternoon — Aftermath]
    # play music "music_placeholder"  # [Music: Single piano note repeated, slowly descending]
    hide kaito_sato
    hide maya_inoue
    hide lucia_lux_moreno

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant, steady roar of the ocean; wind threading through loosened planks]
    "The town feels smaller now, compressed by loss. You walk the cracked flagstones toward the lighthouse because you need a place that remembers storms and keeps speaking. The lamp is dimmed; its scaffolding creaks. It feels like a good place for all the metaphors to land."
    "Kaito Sato comes up behind you, uninvited, and for a moment neither of you speak. He hands you a small vial—tide samples he'd been saving for modeling. The water inside sloshes sullenly."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "I thought I could fix this with tech,' he says. 'But tech isn't compassion. It doesn't patch the things that matter—the long, slow work of trust. Maybe I thought if I was useful, you'd see me differently. That's not what this is about, but—"
    "You look down at your hands. The dive watch is heavy like a decision you can never truly pay off."
    "Maya Inoue [inside]: You promised him you would choose them—your town, the people who raised you—over the promise of tidy solutions. You promised Tomas that you would respect the sea's memory. You promised yourself that you'd"
    "be the one to keep things together. You keep thinking promises are currency; they're not. They are things you keep against other people's losses, and sometimes the bank is empty."
    "Kaito Sato places a tentative hand on your shoulder, a bridge you do not know how to cross or burn."

    kaito_sato "I don't know if staying here with you now is the same as standing with the town. But I know I can't pretend nothing happened. I can't pretend I didn't hope you would choose me somehow. You—' He searches for the right word and makes do with a small laugh that shivers. 'You chose a path, Maya. We all have to live with it."
    "You imagine the town in a year: patched berms where cove lines used to be, a diner with new windows patched more carefully, Tomas teaching a different generation how to read tides that changed. The horizon is not a promise; it is work."
    "You think of leaving. You think of staying. You think of the watch, warm now against your palm, and you feel the pressure of a life shaped by an absence. You are tired of being the"
    "hinge on which blame turns. You are tired of the private calculation that always makes you the last line of defense."
    "Tomas Bianchi's voice comes across the harbor on the radio—short, brittle—as he coordinates a volunteer effort to salvage nets and boats. Hana Kim's laugh, when you catch it, is small and not quite whole, but it"
    "is there: a live wire. Lux's logo still gleams on a near-distant plaza, indifferent like a lighthouse that refuses to warn. Kaito stands close, a human instrument trying to measure things that are not only numbers."
    "There is no neat reconciliation here. The town is wounded, and wounds teach in ways that feel unfair."
    "You fold the dive watch into your palm and rub the worn bezel. The second hand is a stubborn, pointless arc. You make a sound that is half-sob and half-laugh."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We broke it. We fixed what we could. We will have to live with the rest."
    "Kaito's hand finds yours and holds it in a way that is neither assurance nor surrender. Tomas lights a pipe in the distance; Hana waves at you from where she's stacking wet blankets. Lux passes by"
    "with her placid stride, and for a fraction she looks at you like a ghost of something you once shared."
    "You think of the forum the next day—how it will be less about options and more about assigning responsibility. You think of the faces in the crowd, the names on your list in that little waterproof"
    "notebook, the places you have promised to save. The work ahead is messy, and the ending you imagined—tidy, just, compensated—is gone."
    hide kaito_sato
    hide maya_inoue

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings fold into minor chords; the single piano drops out]
    # play sound "sfx_placeholder"  # [Sound: Sea rolling, a low, continuous presence]
    "You tuck the watch back against your chest and feel the ache of being known and found faulty. You will answer at the forum. You will listen to the blame and the pleading. You will be"
    "a target because you were the one who had to call time and place. You will not be absolved, and you are learning that absolution is not the point anymore."
    "You stand at the edge of the lighthouse path and breathe in the salt and the diesel and the thin, stubborn green of life that will not stop trying."
    "You imagine rebuilding—not just engineered defenses or press releases, but the slow, threaded work of trust: dinners to bring people together, community labor days to mend nets and jetties, meetings where Lux's team and Tomas's knowledge"
    "try to find a way to be less false to one another. You imagine sleepless nights, apologies that never land right, and quiet mornings like this one, where the only honest thing is the work."
    "Maya Inoue [inside]: You cannot promise to fix everything. You can promise to keep the town in the ledger of your life. That will have to be enough."

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, unresolved cello note; then silence]

    scene bg ch6_601bcb_6 at full_bg
    "THE END"
    # [GAME END]
    return
