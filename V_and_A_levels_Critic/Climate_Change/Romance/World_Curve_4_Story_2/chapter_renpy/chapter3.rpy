label chapter3:

    # [Scene: Glass Pier | Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady cello; a mid-tempo pulse beneath the murmurs]
    # play sound "sfx_placeholder"  # [Sound: Boardwalk planks creak; the tide sighs against pilings]
    "The benches are packed so close you can feel the breath of the person behind you press through the weave of your jacket. Salt and smoke and the sharp citrus of someone’s thermos hang in the"
    "air. People lean forward on knees callused by years of patchwork fixes; a child's small rubber boot taps impatiently against a step. You hold your field notebook on your lap like a small, steady thing—its cover"
    "familiar under your palm."
    "You remember the Tide Garden light that morning—the solar sails folding into gull-wings—and Ori Navarro's seaglass charm tapped once against the page. The echo of that tap lives behind your ribs now, something warm and almost"
    "unwarrantedly hopeful. There is a rope you can climb together; the ropes are frayed, but they're there."
    "From the pier's edge a hush falls as Calder Voss walks under the work-lamps. His suit eats the lamp light; his movement is economical, the way of someone who measures words before they leave the mouth."
    "The signet ring at his finger catches and throws a pinprick of LED-blue across a nearby poster. He smiles—small, practiced—and then begins."
    show calder_voss at left:
        zoom 0.7

    calder_voss "Good evening. Harborlight is at a crossroads. We can retreat—scatter lives—or we can build something that allows people to stay. VossArc is that answer: controlled floodgates, integrated housing, guaranteed tenure for residents who relocate to the pilot. Safe courtyards for children. Jobs during construction. Stability."
    "His voice is precise, not without warmth. He shows rendered images on a crisp screen: a glass pier folding into a crystalline tower, terraces lined with trees, children laughing in a courtyard sheltered from the water."
    "The images are pretty and arranged to cradle fear. A murmur moves through the crowd—hope tightening into curious, fragile attention."
    "You taste the sea and something metallic at the back of your tongue, like coin rubbed by salt. Jun, sitting at your shoulder with his recorder almost hidden, slides a damp packet across to you—papers mottled"
    "at the edges from the spray he took on the way over. You peel the top sheet back with your free thumb and your eyes skim legal language that reads like kindness folded into caveats. Words"
    "like 'contingent,' 'relocation agreement,' and 'performance clause' sit in neat, corporate rows. The paper smells faintly of fish and printer ink."
    show jun_park at right:
        zoom 0.7

    jun_park "Look. The guarantees are there, but there are footnotes. There are trigger clauses connected to 'unviable occupancy' and 'force majeure' that could mean—' His voice tightens. '—that tenure isn’t as ironclad as he says."
    "You feel the room's temperature change in small increments: one neighbor's hand pressed to her mouth, another's jaw unclenching a fraction. Old Mara sits a few rows up, hands curled around her fishing-hook beads. She watches"
    "Calder with the same unreadable look she gives the ocean: patient, knowing, and unafraid of naming storms when they come."

    menu:
        "Read the transcript now":
            "You lean forward, the damp paper between your fingers. Each clause becomes a pebble you turn over, sharp edges and legal grain; you memorize the places where a promise might thin into a loophole."
        "Fold it away for the moment":
            "You tuck the transcript into your notebook's back pocket. For now, you stay with the room—faces, breath, the way Calder's images land on people. Strategy can wait a minute. Hearts cannot."

    # --- merge ---
    "The discussion continues; Calder shifts from technical to narrative and addresses photographs and the crowd."

    calder_voss "I know there is fear—I've seen it. My own family learned what loss tastes like. This isn't corporate abstraction; it's an answer we've engineered so parents can sleep. Let us pilot VossArc with your community co-designing certain elements—let us prove it works."
    show maya_lin at center:
        zoom 0.7

    maya_lin "Promise him checks the paperwork. Promise him Jun reads it line-for-line in public. Promise him we keep community oversight or we don't sign."
    "Her voice carries the precise, practical heat of someone who keeps lists and people in the same head. Across from her, a woman you recognize from the laundry-bridge whispers, 'They say 'guaranteed'—do they mean guaranteed?' and the crowd shifts."
    "Ori Navarro, beside you, fingers worrying at a frayed strap of his satchel, says quietly—just for you—'Show them what we can build. People need to feel it. Silhouettes and plants and a place that smells like the garden, not like antiseptic glass.'"
    "Ori Navarro's tone is all pull—creative insistence wrapped in that mischievous, steady grin he uses to close a spark in your chest. You look at the small models Ori Navarro has left at the edge of"
    "the pier earlier: a hand-carved section of living seawall, a tiny terrace with halophytes sprouting in a cracked shell of resin. They caught the light this morning like proof that ecosystems can be engineered with tenderness."
    "Calder watches these exchanges, his fingers steepling. He replies to Maya's demand with the practiced calm of someone used to negotiations."

    calder_voss "Public oversight is part of the pilot. We will include community representatives in the design review board. We will fund legal assistance for residents to review contracts. We will—' He hesitates the faintest moment, then adds, '—and we will commit to performance metrics that include resident retention."
    "Jun raises his voice, not accusatory but deliberate."

    jun_park "Metrics are only as good as enforcement. There are clauses in the corporate playbook that allow for de-facto displacement through 'efficiency' arguments. If those clauses are in your draft, we need an independent oversight mechanism, not one appointed by you."
    "Calder tilts his head, acknowledging Jun with a slow nod that reads as both concession and counterweight."

    calder_voss "Fair. Independent oversight can be negotiated. But understand—time is part of the calculus. If we wait for every mechanism to be perfect, people will be moved anyway by policy delays.' His gaze softens for a second. 'We are offering funds now, labor contracts for locals, and the infrastructure to protect the shore."
    "The room hums with conflicting impulses—relief at resources offered now; caution over strings hidden in velvet; anger at the history of promises unkept. Your pulse rises, steady as a tide. The arousal is not panic. It's"
    "alert, attentive: mid-range energy that sharpens your senses without fraying them. You can make arguments here; you can marshal trust. This is the climb you promised the neighborhood when you returned."
    "Old Mara clears her throat once—a small, dry sound—but does not speak. Her hands tighten on the beads. Her look is not simple approval or condemnation; it is complex. You read that complexity like a weather map: the pressure's changing; choose your course wisely."
    hide calder_voss
    show ava_maren at left:
        zoom 0.7

    ava_maren "We want safety. We want to keep Saltway together. Those images—' You let your thumb trace the edge of your notebook as if counting the possibility. '—but we can't trade tenure for frontage. If there's independent oversight, what's the mechanism? Who appoints it? What are the triggers, and how are they adjudicated?"
    hide jun_park
    show calder_voss at right:
        zoom 0.7

    calder_voss "We can structure the oversight through a civic trust—board members jointly appointed, with rotating seats for community representatives. Triggers would be tied to quantifiable metrics—storm resistance, occupancy rates—evaluated by independent engineers."

    maya_lin "And who chooses the 'independent' engineer? VossCorp's vendors, or someone who actually knows the neighborhood—knows the gutters that always clog, the way the current runs?"
    "Calder's jaw moves, thoughtful."

    calder_voss "We can open the vendor shortlist to public nomination. We can agree on community-vetted names."
    "Jun leans closer, offering you the faint heat of his conviction."
    hide maya_lin
    show jun_park at center:
        zoom 0.7

    jun_park "We put those names in writing tonight. We publish a copy. Transparency is not a favor; it's the work."
    "Ori Navarro squeezes your hand beneath the bench, a small, silent anchor. His eyes—warm, earnest—ask you for a choice that isn't only logistics but intimacy: can you accept a conversation with the man whose cranes shadow your shore if it means a chance to hold the neighborhood intact?"
    "You feel the weight of residents' faces on you—Old Mara's unreadable seam, Maya's curtled resolve, Jun's recorder skimming the edge of scandal, Ori Navarro's hopeful hands. The decision sits on the scrawl in your notebook, the place where you draft promises and margins where consequences run."
    "For a moment the pier is quiet enough to hear the distant city engines like a second tide. You consider three paths: invite Calder into a co-managed pilot and hope the oversight holds; refuse and let"
    "Jun and protests take the heat of public exposure; or retreat with Ori Navarro to build a proof that asks for no corporate signature and hope the neighborhood will believe once it sees."
    "You look up at Calder, whose face is the shape of professional confidence and a real, quiet ache you recognize from someone who has lost things to storms. You are not blind to the possibility that"
    "partnership could deliver resources—materials, jobs, protections—that grassroots alone will struggle to raise. You are also not blind to the ledger on Jun's damp transcript: contingencies are where promises erode."
    "Maya Lin's whisper is urgent now."
    hide ava_maren
    show maya_lin at left:
        zoom 0.7

    maya_lin "We can negotiate. We can demand names, guarantees, and a clause to rescind. Or we can make noise. Or we can build—slow but clean."
    hide calder_voss
    show ori_navarro at right:
        zoom 0.7

    ori_navarro "Whatever you choose, I build with you. I don't want to rush you."
    "The crowd leans in. You feel the community's collective breath shift, waiting on the single movement you are about to make. The arousal folds upward—still measured, still thoughtful—but it is unmistakably higher than when Calder first spoke. Hope has crested into imperative."
    hide jun_park
    hide maya_lin
    hide ori_navarro

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull's call rolls across the pier; a distant hammer punctuates the air]
    "You touch your pen. This is not about you alone. It is about tenure and about whether Saltway remains on the map of living neighborhoods or becomes a curated exhibit of what once was. It is"
    "about whether your relationship with Ori Navarro—delicate as it is, woven of shared work and small confidences—bends to the same pressures that press at the whole community. You lift your chin and breathe."
    "Calder waits, palms open in the practiced pose of an offer. Maya watches with her ledger-face on. Jun's eyes glitter with the recorder's red light under his collar. Old Mara's beads rest like a small reef in her hands."
    "The room wants a course of action. Your pen hovers. The choice will set the next tide."

    menu:
        "Negotiate a hybrid pilot—work with VossCorp on a co-managed prototype.":
            jump chapter4
        "Refuse; escalate a public campaign with Jun's reporting and protests.":
            jump chapter7
        "Prototype quietly with Ori and delay publicizing—build proof first.":
            jump chapter10
    return
