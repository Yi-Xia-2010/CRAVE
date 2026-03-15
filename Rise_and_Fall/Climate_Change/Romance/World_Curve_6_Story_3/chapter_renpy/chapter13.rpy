label chapter13:

    # [Scene: Council Hall / Community Forum | Evening]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, tremulous strings; a distant roll of thunder underpins speech]
    # play sound "sfx_placeholder"  # [Sound: Murmur of conversations, the crisp rustle of paper, a chair scraping on tile]
    "You stand by the lectern, satchel heavy at your hip, the sea-glass pendant cool against your sternum. The prints inside smell faintly of ink and rain; the graphs snap at the edges where you've handled them a thousand times."
    show maya_ibarra at left:
        zoom 0.7

    maya_ibarra "We need a codified oversight council. Funding can't move until ecological thresholds are written into the contracts, and apprenticeships are guaranteed for the crew that will build and maintain the work."
    show aria_sol_representative_of_veridian_holdings at right:
        zoom 0.7

    aria_sol_representative_of_veridian_holdings "Maya, I understand your dedication, but timelines matter. Delays cost lives; they cost the company money — and the faster we act, the more damage we can prevent."
    "You hear the inside edge of her argument — the currency of speed, the language of leverage. Her team sits behind her, tablets open, contracts already being redlined. The halogen lights over her table make her cuff glint like a promise."

    "Mayor Cortez" "We can't afford paralysis. But we also can't sign away oversight and hope for the best. Maya, what legal language are you proposing? Walk me through it."
    "You inhale. The room tastes of coffee and salt; a damp coolness slides in through a cracked window. You place the prints on the lectern, letting the town's mapped points be your authority."
    "If Veridian moves first, they write the rules. You can see their pilings in your mind's eye — concrete where marsh should be, a straightened shoreline that would choke the nurseries. You will not let that be the town's future without agreement."
    show dr_kira_ansel at center:
        zoom 0.7

    dr_kira_ansel "Audits are reasonable, but they add time. If we run rolling audits — short, focused, with clear pass/fail metrics — we can preserve some pace and ensure ecological baselines are respected."
    hide maya_ibarra
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "Kira's right. We can design phased milestones tied to measurable indicators. That way, work can proceed in segments that protect critical habitats."

    aria_sol_representative_of_veridian_holdings "If you make each milestone contingent on outside audits, you risk stopping work between phases. Mobilizing crews twice is inefficient and costly. Veridian could pull back if the economics don't hold."
    "You feel the word 'pull' like a knife. Funding leverage is a blunt instrument; you've watched companies tighten their grip before."

    aria_sol_representative_of_veridian_holdings "Let's be frank. Our investors expect deliverables on a timetable. Either we find a way to reconcile speed with assurance, or I can't guarantee the same financial offer."
    "The room hushes. Mayor Cortez looks between you and Aria, the balance of politics on her face."

    menu:
        "Name the non-negotiables now":
            "You place your hands flat on the table and list the four thresholds you will not budge on: no marsh dredging, mandatory local hires for labor, ecological stop-clauses, and an apprenticeship fund. The list lands in the room like a thrown stone; Aria's smile thins."
        "Propose a fast-track audit compromise":
            "You take a breath and offer a compromise: a fast-track, third-party audit panel with weekly check-ins for the first sixty days. It's an olive branch — risky, but it might keep crews moving. Aria studies the note, fingers drumming the edge of the table."

    # --- merge ---
    "Aria's team exchanges a look that is both businesslike and impatient. Mayor Cortez takes a paper from the Mayor's aide, eyes flicking across the clauses."

    "Mayor Cortez" "If we can codify oversight and keep funding flowing, I can support a motion at the council. But we have to be precise about who sits on that council."
    "You feel the weight of a thousand small hands on your shoulders — Clara the grocer who will need markets that don't flood, Tomas who remembers when the dike failed, Rosa's camera capturing every bruise to the town."
    hide aria_sol_representative_of_veridian_holdings
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We have to be careful with the definitions. 'Ecological stop-clause' can't be vague. The community needs teeth. Not a suggestion."

    elliot_chen "I know. And I think we can write standards that are testable. But you pushed hard tonight. Be prepared — Veridian won't be pleased."
    "Aria Sol's last words before she leaves the hall hang like a warning. 'You can make conditions, Maya. But remember: people are watching the water.'"
    # [Scene: Construction Site | Morning]
    hide dr_kira_ansel
    hide elliot_chen
    hide maya_ibarra

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The metallic ping of tools, distant calls of site foremen, muffled engines in standby]
    # [Smell: Diesel and damp earth; the electric tang of machinery]
    "You come to the site before dawn, hoping presence will feel like work. The machines idle like resting beasts. A handful of workers stand in clumps, coffee cups warming hands. Yellow tape flutters on temporary fences."
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "This whole charade's been stretching on for weeks. Guys are on the books but not getting steady hours. The crews need to fish, Maya. Kids need rent. You pushed for this oversight council —now we're waiting for lawyers and auditors."
    "His voice is blunt, not angry for the sake of it but raw with worry. You can see the tendons in his neck, the knuckles callused from rope."
    "Noah's fear isn't abstract. His nets live or die with a season. You wanted to protect the marshes because they're the lifeblood of the fisheries. But the pause costs real wages."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "Noah, I hear you. The goal is to protect both the marsh and your work. The oversight is meant to prevent short-term fixes that kill the nurseries."

    noah_rhee "People on the docks don't want a lab's promises when their families are hungry. We need the work now, Maya. Not a promise of 'later' stitched in legalese."
    show dr_kira_ansel at center:
        zoom 0.7

    dr_kira_ansel "We can set emergency pay buffers, temporary work on soft protections that don't violate ecological limits. But we can't write checks to all damage after the fact. That's not a solution."
    "Noah's expression softens for a beat, then hardens. 'Tell that to the vendor at the fish market who can't cover the ice for their catch.'"

    menu:
        "Offer immediate temporary work details":
            "You pull out a quick roster and mark a list of tasks — sandbag teams, temporary boardwalk repair. It's imperfect, but it buys time. Noah nods, a flash of relief in his eyes."
        "Insist on holding for legal assurances":
            "You stand firm. 'I can't authorize work that damages the marsh,' you say. Noah's jaw tightens; he spits a word you know meant love and accusation. The gap between you seems to widen."

    # --- merge ---
    "You leave the site with dust in your nostrils and the taste of metal at the back of your tongue. The legal drafts are going to town attorneys now; each clause feels like a hinge on the future."
    # [Scene: Tidewatch Laboratory | Late Afternoon]
    hide noah_rhee
    hide maya_ibarra
    hide dr_kira_ansel

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low fan whirr, the pinging of incoming sensor data, the quiet clicking of a keyboard]
    # [Smell: Brine and wet paper; the musk of damp wood]
    "The lab is a shelter of small certainties. You set the red-lined contract copies on the bench and watch the tide data scroll in Elliot Chen's tablet. The numbers are a flat line with a small, worrying uptick."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "There's a surge forming offshore. Not a full storm, but a pressure band pushing more water than the last few tides. If mobilization is delayed another week, the old market's shoreline stands to take a direct hit."
    "You feel the blood in your ears. The legal team had promised to be quick. Papers move fast on some days and slower on others."
    show dr_kira_ansel at right:
        zoom 0.7

    dr_kira_ansel "We can put out temporary barriers. But sandbags and quick berms are a stopgap — and they require manpower. The contracts don't allow unilateral deployment on Veridian's site without breaching clauses. That's the legal bind."
    "The clauses you fought for to protect the marsh are the same clauses that are hemming in emergency action. The law is a ladder and a trap at once."

    elliot_chen "We could push for an emergency variance from the Mayor. It's a long shot, but it might let crews shore up the most vulnerable structures."

    "Mayoral aide via phone" "Mayor's in a closed meeting. She's aware but cautious — Veridian's counsel is threatening to pause entirely if we move without contractual clarity."
    "You touch the pendant at your throat. It feels very small."
    # [Scene: Old Fish Market | Night]
    hide elliot_chen
    hide dr_kira_ansel

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Howling wind, water slapping wood, someone shouting a name, an engine straining to start]
    # [Smell: A raw, metallic tang of salt and upturned fish; the damp cloth of nets]
    "The surge hits harder than the forecast. Water finds the market's weakest seams and folds them open. You run with a group of volunteers, boots sinking, hands slick with muck, trying to salvage what can be saved."
    "Vendors shout over one another — curses that have names, bargaining and grief mixed together. You wrench at a soaked plywood panel and it splinters in your hands."
    "Noah Rhee is there, sleeves rolled, younger men following him. He barks orders to divert water from a narrow alley; his voice is all work and no blame."
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "Help pull that freezer out. It'll mean the difference between a week's loss and a month's."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We'll try to save the ice chests. Keep the accounts — we'll get you emergency funds."

    "Vendor" "Promises. Like before. We need cash now."
    show rosa_ibarra at center:
        zoom 0.7

    rosa_ibarra "Maya, they're calling you out in the feed. People want names."
    "You can feel the heat of public judgment like a second sun. A woman you grew up with — Mariela, who used to give you spare sardines when you were a kid — points at you across the waterlogged boards."

    "Mariela" "You told us you'd keep our nets and our marsh. Now look. My freezer's ruined. Who fixed the rest of it while you argued with the suits?"
    "Elliot Chen appears at your elbow, handed you a sopping tarp. His trench coat is saturated; his hair is plastered to his forehead. There's fatigue on his face that wasn't there before."
    hide noah_rhee
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "I'm sorry. I tried to push legal to authorize temporary measures. They wouldn't sign off."
    "Guilt presses so hard your ribs ache. The oversight council you fought for is still only ink on paper. The fish market smells of loss and cold fish and the particular, crushing betrayal of slow action."
    "Mayor Cortez arrives with municipal workers trailing behind, their faces pulled taut. She speaks into a recorder, promises aid, but her eyes seek you and then slide away to the crowd."

    "Mayor Cortez" "We'll get emergency relief to vendors. We'll convene emergency funds. Maya — I know why you demanded oversight. But people are hurt."
    "Aria Sol does not step into the wet. Her team watches from the edge of the fenced-off development site; their reaction is careful, businesslike, complex — unreadable in the bright convenience of corporate posture."
    "You stand in the ruined market, hands raw, salt drying on your knuckles. People shove blame like driftwood toward whatever will float it."

    "Vendor" "You tied Veridian's hands. You made them sign checks for the marsh while our nets are full of seawater!"
    hide maya_ibarra
    show noah_rhee at right:
        zoom 0.7

    noah_rhee "I used to work with you, Maya. We pulled nets side by side. Now my aunt calls my name when the ice melts and I have nothing. How is that protection?"
    hide rosa_ibarra
    show maya_ibarra at center:
        zoom 0.7

    maya_ibarra "I wanted to save what feeds us in the future. If we let them concrete over the marsh now, there will be less fish every year. The oversight was meant to keep both alive."

    noah_rhee "Words don't patch a freezer. They don't pay rent."
    "The crowd's murmurs swell into something like a tide of its own, and you are a small, exposed rock in the current."
    hide elliot_chen
    show dr_kira_ansel at left:
        zoom 0.7

    dr_kira_ansel "This fracture was a risk. Political safeguards always have that cost. We need emergency relief mechanisms built into the oversight so delays don't become harm."
    hide noah_rhee
    show elliot_chen at right:
        zoom 0.7

    elliot_chen "We could build a rapid-response payroll, temporary hires to cover things like salvaging stalls. It's feasible if we push the council now."
    "There is an ache where certainty used to sit. The pendulum between urgency and care has struck someone, and the hurt is loud and human."
    "You walk home with wet boots and the taste of metal in your mouth. Legal notices and revised contracts pile into your inbox like small indictments. Each email is a reminder: governance slows the machine; governance"
    "also prevents a different set of losses. The town fractures along those exact lines — who wants immediate stability, who trusts the long view."
    # [Scene: Tidewatch Laboratory | Midnight]
    hide maya_ibarra
    hide dr_kira_ansel
    hide elliot_chen

    scene bg ch11_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, a single low note repeating like a toll]
    # play sound "sfx_placeholder"  # [Sound: Distant siren now fading; the hush of people sleeping uneasily]
    "You sit alone with the red-lined statutes and the images Rosa took at the market. The photos are sharp: faces, water, broken boards. Your pendant feels heavy and small."
    "You asked for guarantees because you didn't want the marsh to die. You wanted apprenticeships and oversight because you wanted the town to survive more than this season. And yet here, tonight, the market lies in ruins and people are cold. The law is both shelter and shutter."
    "A notification pings — a new draft from Veridian's lawyers. Another drone of meetings for next week. The cycle continues: hearings, audits, reparations or not. Each paper is an armature built around a choice you already made."
    "You imagine the living dike again — the one you sketch when you can still breathe — the woven coir, the young plantings, Rosa photographing people mending nets side by side. The image feels fragile, like something you could lose by gripping too tightly or by letting it slip."
    "You stand, go to the window, and look out over the dark water. The lighthouse pulses, amber and patient. Behind it, the town breathes unevenly."
    "People are cold now. You chose oversight because you thought it would protect them forever. Now you've learned the other lesson: sometimes protecting the future inflicts wounds on the present."
    "A quiet resolve gathers alongside remorse. The paperwork will not stop piling up tomorrow. The council schedules, audits, and redlines will take time. You know what must be done — the laws to write, the mechanisms"
    "to enact — but that knowledge is no cure for the grief settling in the market stalls."
    "You run your thumb along the edge of a contract, the ink smudging slightly. Outside, the rain eases, but the town is raw and talking. You hold a map of the creek in one hand and"
    "a photo of the ruined fish market in the other. You think of Noah's hands on a net, of Elliot's quiet urgency, of Aria's precise smile. The living dike you imagined seems both further away and"
    "more necessary than ever. If governance fragments the town now, what will bind it tomorrow? You fold the contract, leave it on the lab bench, and step back out into a Port Veridian that feels smaller,"
    "colder, and yet still stubbornly here."

    scene bg ch11_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter15
    return
