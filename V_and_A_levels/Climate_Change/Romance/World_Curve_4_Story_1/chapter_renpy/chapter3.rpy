label chapter3:

    # [Scene: Municipal Hall | Early Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Rising, bright strings under a driving percussion]
    # play sound "sfx_placeholder"  # [Sound: Murmurs ripple like wind through reeds; a single chair scrapes, then quiet.]
    "You step into the room with the weight of the rooftop behind you: the volunteers, the projector slide that read PILOT APPROVAL — COMMUNITY-LED MONITORING, the small surge of applause. Your palms are slightly damp from"
    "gripping the stack of handouts; your Moleskine bobs in the pocket of your jacket like ballast."
    "You breathe the room in. Coffee, wet wool, the metallic tang of optimism—people hoping for something steadier than the tide. The air is electric, but not frantic; it's a sharp, focused charge that makes your pulse quicken only enough to remind you you're alive."
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "Good evening. Thank you all for coming. Tonight we hear two proposals. We'll keep order—one speaker at a time."
    # play sound "sfx_placeholder"  # [Sound: Sound swells as heads turn. Arin Kai stands near the front under the projector's glow, cap tilted back, hands folded but not closed. The sight of him is an anchor; his amber eyes find yours in a way that loosens something timid in your chest. He gives the tiniest incline—no words, but an offer of steadiness.]
    "You move to the podium. The microphone is warm and a little sticky; the slide behind you fills with the flattened, honest colors of marshland: channels like veins, bands of planted cordgrass, a small map annotated with pilot plots. Your voice, when it comes, is steadier than you expected."
    show maya_soler at right:
        zoom 0.7

    maya_soler "Thank you, Mayor Greer. Lira Bay is not only a place people work from—it's what holds us when storms come. The pilot we're proposing is small, replicable, and—most importantly—designed to grow with us. It uses native planting, living shorelines where possible, measurable sediment capture, and community monitoring so decisions keep coming from the people who live here."
    hide mayor_tomas_greer
    hide maya_soler

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A few approving murmurs. Someone sniffles; someone else coughs support.]
    "You outline the data—simplified, human-scaled: expected reduction in surge heights for the harbor mouth, projected increase in juvenile fish habitat, volunteer shifts scheduled to monitor success. You talk about cost-sharing, about Lina and the local NGOs"
    "ready to manage volunteer training, about the pilot's ability to be scaled if it performs."
    show lina_park at left:
        zoom 0.7

    lina_park "We already have volunteer lists. We've got students lined up, retired crews, and a partnership with the community college for sediment analysis. This plan moves fast with the resources we have."

    "A fisherman near the aisle" "So how long 'til it actually helps? I need to know if my nets stand a chance next season."
    show maya_soler at right:
        zoom 0.7

    maya_soler "It's not an overnight fix—no ecological fix like this is—but modeled results are promising: pockets of restored marsh can reduce the worst of surge effects at key choke points. And because the community runs it, we won't be cut out of the decisions about our water and livelihoods."
    show rita_soler at center:
        zoom 0.7

    rita_soler "We raised our children on this bay with softer hands than fear—give them some place to learn that, not just a wall to hide behind."
    "Evelyn Hart rises with the calm, crisp authority she always wears like tailored armor. Her coat clicks as she crosses to the lectern; she holds a sealed packet—slick, official, and heavy with implication."
    hide lina_park
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "What Maya described is admirable—community spirit is vital. But we face immediate hazards. My office has secured a comprehensive seawall proposal that protects our critical infrastructure, our harbor basin, and—yes—investment we need to keep this town solvent. The packet I'm presenting contains engineered blueprints, an implementation timeline, and committed funding. It's decisive."
    hide maya_soler
    hide rita_soler
    hide evelyn_hart

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain begins against the high windows—a soft, urgent tapping.]
    "Her numbers are clinical, precise. She lays out a timeline that sounds like certainty: bids, contractors, flood-risk models that prioritize roads and harbor arteries. Her voice is persuasive because it removes doubt—it offers a single promise: security, quickly."
    "Arin Kai stands, then sits again. You watch his jaw work; he doesn't clap, but his presence says more than applause could. There’s a tension between his fisherman’s practicality and the long slog of ecological work you propose. The room feels split along that seam."
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "Both plans have merits. People worry about immediate property loss and jobs. People also worry about being sidelined.' He raises his hand. 'We'll hear a few more voices before calling the vote."
    "Voices rise. A lender—slick tie, anxious smile—voices concern about investor confidence, while a young volunteer tries to make an impassioned case for long-term biodiversity. The fishermen ask blunt questions about the season; elders quote storms from decades ago. The hall becomes a chorus of lived stakes and urgent, small mercies."
    "You move back to the lectern when the murmurs die. This is the point where conviction feels like a physical thing pressing against your sternum. High arousal—the room's emotional temperature rising—makes your speech rhythm snap to urgency, but it's a clean urgency, charged with hope rather than panic."
    show maya_soler at right:
        zoom 0.7

    maya_soler "We don't have to choose bravery against prudence. We can bind them together. A hybrid—start with pilot tidal marsh restoration at critical nodes, pair it with targeted hardening where infrastructure is most at risk, and tie funding to transparency and community oversight. We build resilience that holds people's livelihoods and the bay's life together."
    "Someone in the back laughs—a short, incredulous sound that dies as people consider the possibility. Evelyn Hart's expression shifts—mildly contemptuous, then narrowly respectful. This is a contest she can respect because it doesn't rely on fear, it relies on optimism with a plan."
    show evelyn_hart at center:
        zoom 0.7

    evelyn_hart "You propose splitting resources into smaller experiments. Good will won't keep a road from washing out. If we fragment funding, we risk neither plan being sufficient."

    maya_soler "And standing on a single wall isn't enough if the ecosystems that absorb storms are gone. You can't invest your way back into a bay that has been simplified out of existence."
    "The back-and-forth grows textured: data versus immediate protection; community control versus centralized speed. Each line feels like a pebble thrown into water, sending ripples across faces that have to live with the results."

    menu:
        "Invite Arin up to speak for the fishers’ perspective":
            "You gesture subtly toward Arin Kai. He hesitates, nods, and steps forward. His voice is rougher than a podium speech—short words, clear concerns. He speaks of nets, tides, and neighborly trust; his honesty lands, steadying nervous faces."
        "Call Lina to show volunteer readiness and community schedules":
            "You tap the next slide and motion to Lina Park. She strides to the front with a tablet and a roll of volunteer rosters. Her energy is bright and organized—timelines, training plans, and a list of partners. The room murmurs at the practicality of it."

    # --- merge ---
    "Both reactions resolve quickly; neither choice shifts the fundamental debate, but both deepen the texture: Arin Kai's grounded testimony brings faces of fishermen into the room; Lina Park's organization shows that optimism can act on deadlines."

    mayor_tomas_greer "We'll take two final comments."

    "A young science student stands, cheeks flushed" "We ran sediment tests—where we work, capture is happening already. We can scale; we just need to be financed to do it properly."
    "An older fisherman—the same man you heard at the rooftop—shifts his hat in his hands. 'I want my boy to come back, not be pushed out because some plan forgot how to ask us first.' The room leans into that plea; it's simple and heavy."
    "You feel the temperature of the hall spike. Cheers ripple when your pilot is mentioned, low applause for Evelyn's promise. The vote, when it comes, is heavy with people's lives—houses, boats, small businesses, children."

    menu:
        "Step down and clasp Arin’s hand before the vote":
            "You step down, your fingers find his. The contact is brief but fortifying—the kind of human proof that plans are for people, not paper. He squeezes back; together you return to face the room."
        "Stand alone and meet each gaze in the room":
            "You straighten, letting eye contact be your quiet argument; you don't need a touch. Faces flicker—some with anger, some with hope—but as you look, a few more hands stay open in the air, waiting."

    # --- merge ---
    "Both choices heighten the communal feeling—a tangible unity either physical or through shared sight. The arousal peaks; everyone's held breath is a tide."

    mayor_tomas_greer "All right. It's time to make a decision that will shape the bay for a generation. We will vote. I'll take the official count by raised hands. Those in favor of Evelyn Hart's seawall proposal—raise your hands."

    "The clack of palms and the creak of chairs answer. The room splits, but not evenly—a wash of raised arms and other hands clenched at sides. Mayor Tomas Greer notes, voice steady" "Those in favor of Maya Soler's community-led hybrid pilot—raise your hands."
    "Your breath catches as hands go up in waves—students, Lina's volunteers, Rita's small but fierce cluster, and pockets of fishermen. The energy is almost physical—hope moving across the room like a quick wind."

    "Mayor Tomas Greer (pauses, looks out over the faces)" "And finally, those who want more information, a transparency review into the seawall's funding before we commit—raise your hands."
    "You watch fingers twitch. The choice that was once theoretical fractures into three real paths, each with faces attached: people who need quick rescue from risk, people who want stewardship and long-term resilience, people who mistrust promises and want the truth laid bare."
    "A drum-roll hum—that's the room; it's the shuffling of coats, the low collective inhalation before a storm breaks. Your heart thuds in your ears, a steady, proud beat. You are certain of what you want, and yet the hall's chorus reminds you there are urgencies you must honor."

    mayor_tomas_greer "This is the town's moment. We will call the vote on the floor. Make your positions known."
    "You feel the future poised on the tip of the next words you speak. The air tastes of salt and coffee and the bright metallic edge of possibility."
    # play music "music_placeholder"  # [Music: Crescendoing strings, brass hints—hope sharpened into urgency]
    hide mayor_tomas_greer
    hide maya_soler
    hide evelyn_hart

    scene bg ch3_98c6f2_4 at full_bg
    "You open your mouth to answer the call—a single sentence that will anchor the town toward one road or another. The chamber leans in. The moment is, impossibly, full of triumph."

    menu:
        "Lead the community-led hybrid pilot with Arin and Lina":
            jump chapter4
        "Back Evelyn's seawall proposal for quicker protection":
            jump chapter7
        "Investigate the seawall's funding and demand transparency":
            jump chapter10
    return
