label chapter10:

    # [Scene: Harbor Promenade | Late Afternoon — Days After the Vote]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Distant, fragile strings — hopeful modes splintering into dissonance]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of a crowd, the slap of water against cracked concrete, an ambulance siren far off]
    "You arrive carrying the same Moleskine that carried the invitation months ago. The paper in it has turned to a ragged evidence of the campaign: scrawled names, tide sketches, a pressed leaflet announcing the referendum win."
    "The air tastes like salt and the cheap beer someone passed around earlier; sunlight glares off puddles and glassy plastic tarps that volunteers used to keep materials dry during the march."
    "Rosa Marin is at the edge of a cluster of people, her hands still dirty from greenhouse soil, a knitted scarf trying and failing to keep out the damp. Niko laughs at something to her right,"
    "quick and bright, but there's a thinness to it — the kind of laugh that exists to hold the edges of a fraying thing together."
    "Tomas Herrera stands a few paces away, tablet closed against his ribs like a small, inadequate shield. He looks toward you with that conciliatory patience that used to feel like an anchor and now feels like a map whose edges are already smudging."
    show mara_voss at left:
        zoom 0.7

    mara_voss "You won the vote. That word still feels strange in your mouth: won. You held a tide of people together and put a living solution on a paper the law had to respect."
    "You move through the crowd like a current that remembers every rock and shoal. People come up to you with brief, earnest thanks. A kid presses a tide-sticker into your palm with milked-out excitement; an elder"
    "grips your shoulder and doesn't say anything — only nods as if the weight of memory finally found a place to rest."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "They signed. It carried. We did what we set out to do."

    mara_voss "We did. But the letter of the law isn't the sea. It doesn't hold back a storm or a bulldozer."

    tomas_herrera "I know. But it gives us leverage. It gives Mayor Anton a mandate he can use to resist—"

    "Before he can finish, Lena’s voice cuts across the crowd, clipped, urgent" "Broadcasting live — Elys Reed announces emergency development measures. Says it's to 'stabilize economic security' after storm threats. Investors pledging immediate funding."
    "The word 'immediate' lands like a stone. You feel it ricochet off something deep and held."
    hide mara_voss
    hide tomas_herrera

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crowd's murmur falters; a dozen conversations become a dozen small alarms]
    "Mayor Anton arrives suffused with the bland sheen of municipal protocol: a press dossier in hand, a smile that attempts steadiness and finds fatigue instead."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "The referendum matters. It matters very much. But in light of Elys' mobilization, we must be pragmatic. There will be negotiations."
    "Rosa Marin steps forward before you can. Her voice is soft but carries the slow, inexorable authority of someone who has tended soil through droughts and tides."
    show rosa_marin at right:
        zoom 0.7

    rosa_marin "Negotiations with what are you balancing? Cemented walls? Money that doesn't remember our names? We planted a shoreline, Mayor. We watched it breathe."
    show mayor_anton_chi at center:
        zoom 0.7

    mayor_anton_chi "We balance what keeps people in their homes and what ensures the city can pay for services. I don't—"
    "Elys Reed appears on the fringe like a photograph come to life: composed, her platinum hair immaculate despite the damp, AR-frames reflecting the crowd and the glint of funders' logos. She speaks with the clarity of someone who knows exactly which syllables make the cameras settle."
    hide mayor_anton_chi
    show elys_reed at left:
        zoom 0.7

    elys_reed "My position is simple. Economic security and infrastructure must be prioritized. Emergency measures allow us to accelerate protective development. Investors have responded. We will act quickly."
    "Your stomach tightens. 'Protective development' is a phrase that tastes of poured concrete and promises."
    hide rosa_marin
    show mara_voss at right:
        zoom 0.7

    mara_voss "She frames it as rescue. The grammar of rescue has always been good for investment."
    "Tomas Herrera steps in, placing a hand at the small of your back—a touch meant to steady you. He turns back to Mayor Anton."
    hide mayor_anton_chi
    show tomas_herrera at center:
        zoom 0.7

    tomas_herrera "Is there a way to include the community plan within those measures? To ensure living shoreline components are part of any accelerated build?"
    "Anton glances to Elys Reed; Elys Reed's mouth forms a thin line. The exchange is a ledger of power."

    elys_reed "We can negotiate components. But speed is essential. Delays cost lives and livelihoods — and investors."
    "You cannot tell if the 'we' she's invoking includes you or erases you."

    menu:
        "Push the crowd to protest Elys' measures now":
            "You scan the group: Rosa Marin's gaze is steady but tired, Niko's fingers twitch with readiness. You step to a makeshift crate, lift your voice, and the crowd answers — a ripple of shouts, of 'No' and 'Our shoreline' — immediate, defiant, messy."
        "Pull Tomas aside and demand a private negotiation":
            "You take Tomas Herrera' arm and pull him back to a quieter patch of promenade. Your words spill out raw: 'If you can get that ordinance into the emergency measures, we can limit damage.' He listens, fingers absently tracing the silver band on his wrist, weighing policy against the ache in your voice."
        "Call Lena and push for a live exposure piece":
            "You find Lena, spectra of camera light in her eyes. You hand her a list of questions and a recording of the shoreline restoration's early successes. Her jaw tightens; she nods and raises her recorder with a new angle to cut."

    # --- merge ---
    "Visual: The crowd rouses and recedes, actions and words splintering into separate futures"
    # play music "music_placeholder"  # [Music: A low, unresolved chord; the strings hang like kelp in cold water]
    "You choose more than one strategy in the end because you are not a single tactic. Volunteers swarm sidewalk corners; a small group marches toward Elys Reed. Lena files a live segment that evening about investors'"
    "rapid commitments and the risks of top-down construction. Tomas Herrera spends the night drafting amendments that could tether emergency measures to living components — clauses that might not hold against a judge or a leaseholder, but"
    "which might slow a bulldozer."
    # [Scene: Stormfront Beach | Night — Several Weeks Later]
    hide elys_reed
    hide mara_voss
    hide tomas_herrera

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea is a low, monstrous hiss. Wind rakes like fingers over sand. A siren's tail flees into the distance.]
    # play music "music_placeholder"  # [Music: A single, aching cello line; distant timpani mimic the impact of waves]
    "The referendum's legal victory feels like a memory from another life. Paper doesn't hold in the same way as earth does. Elys Reed's emergency funding moved fast. Permits were signed. Contractors came with machines that chewed at the shoreline under the rationale of 'stabilization' — and then the surge came."
    "You were at the edge of the newly stabilized strip when the first wall collapsed. You remember the sound: not like the crashing of a single wave but like metal tearing open, like the gasp of"
    "a held thing being loosed. The water did not blink. It took the new dune, the transplanted cordgrass, the protective berms you and neighbors had coaxed into life."
    show mara_voss at left:
        zoom 0.7

    mara_voss "You stand ankle-deep in what should have been a new beginning and instead count what's been taken."
    "Someone screams; a child's voice. Niko is wading in, hands full of buckets and rope. Rosa Marin stands at the crest of the high tide line, mouth pressed into a thin, unreadable seam. You move with them because you always move with them."
    "You work through night that smells of salt and fuel and something worse: the metallic reek of failure. You shout directions into the storm, your voice tearing, your hands raw from knotting rope around drifting posts. Volunteers are cold and furious and exhausted."
    "When the sea finally releases its hold, it leaves gaps that a law cannot stitch. Basements are full of wet detritus, a community garden is a smear of mud; a row of children’s bike frames juts from the sand like sad fossils."
    "Tomas Herrera finds you under a streetlamp that flickers on and off like a tired pulse. His jacket is streaked with water and mud; he looks smaller in it than he ever did before."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "We did what we could in the ordinance. I fought for the clauses to be binding."
    "You look at him, and the line between 'could' and 'did' is a chasm you can feel in your teeth."

    mara_voss "They bulldozed before the plants took root. They promised anchoring and poured concrete. Investors took the 'stability' Elys sold them and left the living parts as decoration. Your clauses didn't stop concrete."

    tomas_herrera "If I'd pushed harder —"

    mara_voss "Would you have? Would you have risked everything on a municipal vote that could be overturned by litigation? Or would you have been the planner who tells us to wait for a 'sounder' solution while the sea keeps coming?"
    "He flinches, not at your words but at the truth they carry."

    tomas_herrera "I tried to bridge it. I thought I could do both. Keep the political floor under you and the practical tools in your hands."
    "You feel a hot, bitter flare at his attempt to straddle both worlds. For months, that very thing felt like safety; now it feels like the place where your trust slipped out through a crack."

    mara_voss "Bridging is not the same as choosing. When investors think 'stability' is a new boardwalk and a shopping strip, you 'bridging' becomes their permit."

    tomas_herrera "I'm with you on the goal. I—"

    mara_voss "Are you? Because when they started breaking ground, you called for incremental approval. Elys Reed called it 'necessary phasing.' The first beds we planted were removed for 'access.'"
    "Tomas Herrera searches for a foothold in the conversation and finds only the jagged edge of regret."

    tomas_herrera "I didn't want to be the person who lost us the room at the table. I thought holding the center would let us later push the edges."
    "You taste bitter salt as the rain begins again, soft and precise."

    menu:
        "Tell Tomas you can't work that middle ground anymore":
            "You say it plainly, each word a small hammer: 'I can't ask people to trust me while I split myself in two.' Tomas Herrera' face crumples; he reaches for you as if to repair the break, but his hands tremble, uncertain whether to pull you back or let go."
        "Ask Tomas to show you the ordinance — one last look":
            "You ask for the ordinance pages, for the exact clause language. He fishes it from his bag and spreads legalese between both of you. You trace where living shoreline requirements became 'recommendations' and feel the betrayal in bureaucratic parentheses."

    # --- merge ---
    "You take the ordinance and read. The living components that once were bold paragraphs are now appendices; the emergency language is broad. Where there were teeth, there are only molars, round and ineffectual against the real bite of capital."
    "Rosa Marin approaches, hands tucked into her apron, eyes like weathered stone."
    show rosa_marin at center:
        zoom 0.7

    rosa_marin "We will plant again. We will teach the children how to knot cordgrass, how to remember the tide. Paper cannot hold everything, child. It is people who hold it when the law cannot."
    "Her words are a balm and a rebuke: steady, unwavering, and not sentimental."
    "Niko, hands raw, collapses on a bench and laughs in a way that is half sob. 'We did good,' he says. 'We did what we could. It's just — it's a tide too fast.'"
    "The phrase lodges."
    # [Scene: Harbor Promenade | Dawn — The Morning After]
    hide mara_voss
    hide tomas_herrera
    hide rosa_marin

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano; a descending motif that resolves into silence]
    # play sound "sfx_placeholder"  # [Sound: The gulls are loud, brazen. Somewhere, a jackhammer begins work where it shouldn't.]
    "You move through the aftermath like someone cataloguing a map of losses. Each name you read on a sign is a family, a child, a memory. The referendum is still law; the legal victory exists as a formal shell that protects nothing from the immediate force of capital and weather."
    "Tomas Herrera finds you near the waterline where a sapling you planted months ago lies half-buried in mud. He does not reach for your hand this time. He simply stands in the rain, the shape of his silhouette a question."
    show tomas_herrera at left:
        zoom 0.7

    tomas_herrera "They offered me a position in the regional office. More reach. More leverage. I can do more from there."
    "The words are polite, but their intent is sharp. Leave? Stay? The choice is his, not yours — and that makes it harder."
    show mara_voss at right:
        zoom 0.7

    mara_voss "So you leave when the shore surrenders?"

    tomas_herrera "If staying where I am means helping create half-measures, maybe I should step back and push for broader policy elsewhere. I—"

    mara_voss "Or you leave because it's the pragmatic thing that keeps you clean enough to sleep."
    "He does not answer that accusation. Instead he studies the sapling, then looks at you."

    tomas_herrera "I don't want to leave you. I want to change the conditions that make choices like this necessary."

    mara_voss "Change takes time. People need hands tonight."
    "You realize, in the rain and the mud, that 'together' has shifted from a place you both stood to a territory that might no longer overlap."
    "You cross your arms to keep out the chill. The sound of a jackhammer reverberates in your chest. Behind you, people are already organizing neighborhood shifts to shore up what remains. They work because they always have: because there is no other option."

    tomas_herrera "Whatever you decide, I'm not against you."
    "You look at him, and the words land like a boat beached on its side: intended to hold, too small for the weight."

    mara_voss "Against me or with the system that erases what I've tried to save? Those are not the same."
    "Tomas Herrera's mouth trembles. He reaches forward, then stops — as if the rain itself were a line he cannot cross."

    tomas_herrera "I thought I could be the person who kept both doors open. Maybe I was mistaken."

    mara_voss "You have loved a bridge-builder. Bridges collapse if both ends don't hold."
    "You think of Rosa Marin's greenhouse, the hands that planted cordgrass, Niko's laugh. You think of the kids who left tide-stickers on your pocket. You think of the taste of victory that dissolved in the salt of structural compromise."
    "You let out a breath that is more like a small surrender."

    mara_voss "Go, Tomas. If you must go where you believe you can change more, go. But don't tell me you'll come back to carry this for me. We don't get to keep the same promises and call them both true."
    "He nods, the motion small and grave. He steps back, then turns and walks away down the promenade. You watch him until he is a shape among other shapes."
    hide tomas_herrera
    hide mara_voss

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, low note that fades into the sound of tide and wind]
    # play sound "sfx_placeholder"  # [Sound: The distant thud of construction, the chatter of volunteers refocused on immediate repair]
    "You kneel and find your hands again in the mud, fingers learning the weight of replanting. You place a cutting into the mud, press it down, and hold it there with everything you've got. It will"
    "not stop the next storm. It will not unpick the legal maneuvers or rethread contracts. But it will be a small, honest thing to tend."
    "Rosa Marin comes to your side and begins to work with you without fanfare. Her hand, warm and rough, finds yours for a moment in the soil and squeezes."
    show rosa_marin at left:
        zoom 0.7

    rosa_marin "This is how we keep living. Piece by piece. Plant by plant. You will have days that feel like cut waves. You will also have hands."
    "You look up at the horizon, at the cranes moving like distant skeletons. The town hums with both grief and stubborn motion."
    show mara_voss at right:
        zoom 0.7

    mara_voss "This is not the ending you wished for. It is a map of what remains. You will carry the law of the referendum, and you will carry the scar the surge gave to your shore and to the people you love. You will carry the decision to stay."
    "You rise, fingers cupped in mud. You do not know what will come after this season of loss — whether this will be the seed of a comeback or a quiet persevering that never reaches the"
    "headlines. But you know the work you will do tomorrow: meetings with neighbors, late-night plantings, legal follow-ups with Lena pushing stories that hold people accountable, counsel for families left with wet furniture and damp grief."
    hide rosa_marin
    hide mara_voss

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A slow, mournful cello; then a faint, persistent pluck that suggests continuation rather than resolution]
    "You walk away from the shoreline with Rosa Marin and Niko, each step heavy but deliberate. Your chest is raw, and grief mixes with stubbornness — a difficult, necessary twin."
    "You find a small spot on the promenade where volunteers are distributing warm drinks. You take one, feel heat spread through your palms, and with it a brittle, enduring resolve."
    "You will grieve. You will organize. You will plant. You will keep showing up."

    scene bg ch9_3be532_7 at full_bg
    "THE END"
    # [GAME END]
    return
