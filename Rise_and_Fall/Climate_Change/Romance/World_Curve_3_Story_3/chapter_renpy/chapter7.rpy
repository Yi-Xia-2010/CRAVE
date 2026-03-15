label chapter7:

    # [Scene: Municipal Office | Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, unresolved cello]
    # play sound "sfx_placeholder"  # [Sound: Printer whirring in the corner; soft tap of Ayla’s pen on the desk]
    "You walked in with the taste of last night's meeting still on your tongue—coffee and salt, and the memory of faces lined behind you. You chose negotiation. The choice sits in your chest like a bruise you haven't learned to press yet."
    "The room smells of hot paper and polished leather, an antiseptic confidence you know all too well. Dr. Ayla Voss stands by a floor-to-ceiling map, her platinum bob a stark edge against the soft rain beyond"
    "the glass. Her wristband emits a quiet, clinical glow as data scrolls across it: sensor thresholds, compliance timelines, conditional funding cliffs. The numbers are tidy in the way danger sometimes can be—organized, legible, terrifying."
    "You set your tablet on the table and open the proposal draft you and Ayla have been sketching. The hybrid plan unfurls: engineered tidal barriers along the harbor mouth, targeted buyouts along the lowest blocks, and"
    "a funded co-management program that funnels resources into community-led mangrove restoration and modular housing prototypes. The layout looks like a compromise you can print on letterhead and sign without trembling."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "The hybrid model balances engineering certainty with local stewardship. With phased buyouts, we concentrate structural defenses and reduce long-term maintenance costs. Sensors will trigger escalations—if X exceeds threshold Y, relocation funding activates."
    "You read the lines the way you read tide charts: with a clinical eye and a private panic. Each metric is a lever; each lever pulls people somewhere else."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And the buyouts—how are we framing compensation and support? If we mark households for relocation, we have to offer more than a check. There's cultural loss there, not just economic cost."

    dr_ayla_voss "We include relocation counseling, priority access to new housing stock, and enhanced community transition grants. The goal is to minimize disruption while maximizing survivability."
    "Mayor Tomas Nkem, hands folded across his chest, shifts in the chair—his tropical shirt a small rebellion against the room's stiffness."
    show mayor_tomas_nkem at center:
        zoom 0.7

    mayor_tomas_nkem "Partial solutions attract money, sure, but they also attract political heat. Donors will demand metrics and quick results. If some blocks are left—permanently—exposed, we'll have angry families and angry funders. It's a narrow path, Maya."
    "You glance down at your tide-watch; the brass is warm from where it rests against your palm. The watch's small, steady tick grounds you, a private metronome against the rush of policy language. You feel the"
    "weight of both Tomas's worry and Ayla's precision pressing inward. The town's future is being drawn in vectors you can calculate—yet every vector intersects with someone's kitchen table, someone's photographs on the wall."
    "Elias Jun pushes back from the window with the easy force of someone who builds to solve things. Salt and sawdust cling to his cuffs; a smear of paint drags up his knuckle. Bare feet on the municipal rug, as if the floor were an extension of the dock."
    hide dr_ayla_voss
    show elias_jun at left:
        zoom 0.7

    elias_jun "So we protect the center and ship families out of the parts we don't like? That's not a hybrid—it's triage with a prettier font."

    maya_reyes "It's not 'shipping out.' It's targeted support so people don't lose everything when the next surge hits."

    elias_jun "Support. Right. You and Ayla put it in a spreadsheet and call it compassion."
    hide maya_reyes
    show dr_ayla_voss at right:
        zoom 0.7

    dr_ayla_voss "Compassion without viability leaves people exposed. This model is survivable."
    "You feel the sharp friction between them like a frayed rope. Elias's insistence on hands-on action collides with Ayla's insistence on systemic certainty. You are stuck between them—an interpretive hinge neither fully trusts."
    "Your internal voice says: We can be both. But another part, older and quieter, knows how easily good intentions are co-opted by deadlines and donors."

    menu:
        "Ask Ayla to run a social-impact scenario on the spot":
            "You tap your tablet and ask for a simulation that includes cultural metrics—school disruption, community rituals lost, elderly mobility. Ayla's fingers hover, a microfrown breaking her composure as the wristband recalibrates. The model spits out numbers you hadn't seen before—emotional cost as a set of variables—and you flinch at how small compassion looks in columns."
        "Call Elias out on his rhetoric, demand practical alternatives":
            "You set the tablet down and face Elias. Your voice tightens: ask him to show tradeable models, concrete costs for his proposed builds. Elias's jaw tightens; he lists manpower and materials in a rush, then falters at the parts he can't quantify. The air between you thins—charged and necessary."

    # --- merge ---
    "The scene continues with Ayla watching your reaction."
    "Ayla watches you react to the choices you make—your fingers hover, and for a moment she lets something like curiosity cross her usually imperious face."

    dr_ayla_voss "I can run social-impact scenarios. But we need measurable proxies to satisfy funding conditions. If we frame ceremonial spaces as infrastructure, we appease donors—and possibly preserve them."

    elias_jun "So now we sell our grandma's kitchen to donors under a line item called 'cultural preservation.'"
    "You close your eyes, picturing your grandmother's stoop, the clay pot stained with last summer’s tomato juice. The map on the wall begins to feel less like geography and more like a ledger."
    "There is a rhythm to negotiations: propose, clarify, bracket what you cannot accept, repeat. You push, gentle and deliberate."
    hide mayor_tomas_nkem
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "If we include community co-management, we keep a say in how barriers are placed and how transitions happen. We can bind funding to participatory oversight. People must retain agency—even if their addresses change."

    dr_ayla_voss "Conditional co-management is feasible. It reduces social friction and, more importantly, it improves maintenance outcomes for the engineered systems."
    hide elias_jun
    show mayor_tomas_nkem at left:
        zoom 0.7

    mayor_tomas_nkem "And the legal language? How do we guarantee priorities without opening a legal morass? Court fights will eat budgets."

    maya_reyes "We use tiers—priority for displaced residents, community seats on the oversight board, legal aid provisions included in the buyout package. We write the contract to favor the community where possible."
    "There's a long pause. Outside, rain intensifies into a steady drum against the glass. The printer spits out a single page—your proposal's first tidy summary, a neat title across the top. You read the headline and your throat constricts."
    "Elias leans forward; his bare feet find a scuffed chair leg. You can see the urge in him to stand up, to go build a model with his hands and prove the math wrong."
    hide dr_ayla_voss
    show elias_jun at right:
        zoom 0.7

    elias_jun "Maya—are you with us, or with this...this bureaucratic smoothing of our losses? Because you can be a bridge, but a bridge that sells out its path isn't a bridge at all."
    "You feel the word 'sell' like cold water on your skin. It stings because there are truths on both sides. You chose negotiation because you believed a middle path could save the town and keep the"
    "harbor's angle intact. But the idea of deciding which houses stay and which go makes your stomach drop."

    maya_reyes "I'm trying to keep as much of Marisora intact as possible. That means some hard trade-offs. I'm not selling our soul, Elias. I'm trying to make sure we survive in form and memory."

    elias_jun "Memory won't save people from a surge."
    "The exchange continues—longer, sharper, the kind of conversation that chews at you and leaves no easy balm."

    mayor_tomas_nkem "Politics will force the hand of whichever plan wins public opinion. If people see neighbors leaving because of your maps, Maya, petitions will form. You have to be prepared for the social fallout."
    "You nod, but your brain has already begun to catalog the fallout: who protests, who accepts, who will be furious with you. You can hear the distant, inevitable rumble of social machinery—petitions printed at Rita's, heated posts, neighbors gathering on stoops."
    # [Scene: Rooftop Watch | Dusk]
    hide maya_reyes
    hide mayor_tomas_nkem
    hide elias_jun

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind soughing the string lights; gulls distant; the town below begins to murmur as people arrive at the municipal hall.]
    # play music "music_placeholder"  # [Music: Sparse piano, descending motif]
    "You climb the low ladder carrying the printed map, the paper dampened at the corners by your fingers. The rooftop smells of wet soil and rosemary, and the green scarf your grandmother knitted scrapes against your neck like a memory."
    "You spread the map on the rooftop bench. The buyout zones are shaded in a soft gray band—clinical and inevitable. One blotch sits where your childhood home still stands, the house that taught you how to"
    "bait a hook and how to patch a net. You didn't expect the sight to feel like a physical blow."
    "Your internal voice is louder here, unmediated: This is the line. This is the place where policy meets flesh—the house with the porch swing, the aunt who refuses to leave, the neighbor whose family has lived there for generations."
    "You run your thumb along the gray band, tracking streets you remember as a child. You imagine sending an official letter offering relocation funds and a priority spot in a modular housing complex. The image pins to your chest like a splinter."

    menu:
        "Walk to the childhood home now to gauge reaction":
            "You gather the map and head down the stairs, boots muddy, intent pressing against your ribs. The porch light is on; an older neighbor's silhouette moves inside. You feel the words already forming in your mouth—careful, rehearsed—only to catch in your throat when you see the tacked-up children's drawing locked to the window. The house is a person, not a line on a map."
        "Call Elias and ask him to meet you at the breakwater":
            "You pull out your cracked tablet and tap Elias's number. His reply is instant—'Be there.' Minutes later the distant clatter of his truck arrives over the clanging of the harbor, and when he appears, he's quieter than you expected. He doesn't ask for numbers—only for the map, which he handles like a relic. He points out places he'd rather shore up than abandon, but the list is thin against the gray band."

    # --- merge ---
    "The scene continues from here as the town's murmurs rise."
    "The breeze tugs at the scarf and at your hair. The rooftop feels both intimate and alarmingly exposed, a perfect vantage and a terrible place to be alone with a map that tells you who will go."
    "You think of Rita organizing petitions, of older neighbors muttering about fairness, of Tomas warning about angry donors. You think of Ayla's wristband, of its cold certainty, and of Elias's varnished hands."
    "Your head is a ledger of moral arithmetic: preserve the harbor core and risk fracturing families; preserve all families and risk losing the town to flooding. There is no clean calculus that eases the moral weight."
    "Below, as the municipal hall doors open and people spill into the evening, you hear the first thin sound—someone shouting across the square, a voice testing the ground. The murmur swells, a tide forming. You feel it in your bones: tonight will not end with signatures and polite handshakes."
    "You fold the map with hands that tremble just enough to matter and tuck it into your jacket. The wind picks up, and the string lights above you sway like little flags of an uncertain truce."
    "You close your eyes and let the sounds of the town rise—the low thrum of conversation, an oath whispered in anger, a child's laugh like a slap of sunlight against a bruise. You are poised at the center of a decision whose consequences have already begun to ripple outward."
    "A chant begins somewhere below, thin as a wire and then widening. Papers rustle. Someone starts a rhythm with their feet. You realize that the petition and the protest will arrive together, a dual front of plea and fury."
    "You draw the green scarf closer. The rooftop is suddenly too high, too exposed. You are not sure if you are bracing to hold the line or making space to watch it break."
    "Page-turn thought: If you negotiate and the town fractures, did you avert disaster—or only defer blame? If you refuse to negotiate, how many will lose more than roofs? Either way, the next morning will ask for"
    "names on petitions, for placards, for voices that decide who will be counted as 'at risk' and who will be left behind."

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
