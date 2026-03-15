label chapter13:

    # [Scene: Pilot Bay | Late Afternoon]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Distant, uneasy strings under a slow percussion; beats that feel like a counted breath]
    # play sound "sfx_placeholder"  # [Sound: Wind tearing at tarps; gulls muffled by fog; the soft slap of water against sand-and-silt]
    "Narration"
    "You are handing out gloves when the first camera shows up — not the theatrical kind, but one of those compact vans with the telescoped microphone and the polite, rehearsed urgency. The van's engine coughs and"
    "idles; its logo is a blank rectangle you don't care to read. You thumb the elastic on a pair of nitrile gloves, feeling grit under your fingernail, and the damp smell of earth and salt climbs"
    "into your throat."
    "Your hazel eyes catch flecks of salt as if the sea itself has been thrown in your face. Dr. Linh stands nearby with a handheld meter outstretched, its screen blinking an indifferent green that promises numbers"
    "you half-trust. Volunteers joke with each other — too loud, too sharp — because humor is a way of making something enormous feel like a small, manageable thing."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "The salinity is edging higher than our preliminary sweep suggested. If this surge carries that level inland, transplant survivorship drops significantly."
    show aria_marin at right:
        zoom 0.7

    aria_marin "How high are we talking? A margin we can mitigate tonight?"

    dr_linh_pham "It's a few practical points. We can flush, we can shield, but those require pumps and constant oversight. The model's sensitivity to repeated inundation… it's non-linear."
    "Narration"
    "Her words hang. You know what 'non-linear' means in practice: small, repeated insults to the system compound into collapse. You hand a volunteer a map with a finger you can feel tremble slightly, even though your face is blank for everyone watching."

    "Maya (elbows propped on the berm, paint-splattered cuff catching a fleck of rain)" "We can work faster. We have to. That little memorial garden — if those seedlings go, it's not just plants. It's them."

    aria_marin "We protect what we can. We triage. Linh, start with the flats near the garden."

    dr_linh_pham "If the salinity spikes after the next high tide, the flats will be more vulnerable. We need pumps at two points."

    menu:
        "Smile and joke back":
            "You throw your shoulders into a grin, make a ridiculous, sunlit joke about gardening under moonlight. The volunteers laugh; for a moment the air lightens and a trembling of relief passes through the group."
        "Be blunt about the risks":
            "You cut through the small levity with the blunt edge of what you know. Silence falls. Faces shift from easy to hard; the jokes stop. The mood tightens, but the work accelerates with a clearer purpose."

    # --- merge ---
    "Continue"
    "Narration"
    "The news van parks too close. Someone taps the glass and asks for a soundbite about hope. You answer in measured sentences, the cadence of someone who has given a hundred interviews: careful, key points, community-first"
    "rhetoric. The camera takes your measured hope and will later frame it however the headline wants."
    "Kai Solano arrives with a pack slung across one shoulder, breath sharp from running; his hair is damp, and his eyes are a hot, impatient amber. He doesn't wait for an invitation."
    show kai_solano at center:
        zoom 0.7

    kai_solano "They're going to turn this into a headline and a footnote unless we make it undeniable. Double the scope — more volunteers, push the media, make it impossible for them to ignore the outcome."

    aria_marin "If we mobilize more people, we risk confrontation. Developers don't like being shown up."

    kai_solano "Good. Maybe they should feel uncomfortable. Let them earn public trust the way we earn it — in the muck."
    "Narration"
    "There is a righteousness in him that has always felt like wind to you: propulsive, cleansing, but sometimes able to knock someone over if they stand too close. You see the way he scans the camera now, like he's choosing a target to redeem."
    hide dr_linh_pham
    show noah_vega at left:
        zoom 0.7

    noah_vega "Aria, we have limited runway on funding. Headquarters is pushing for an accelerated partial build — a modular seawall that we can bolt in stages. It reduces uncertainty for residents tonight."

    aria_marin "Modular in the sense of cutting corners?"

    noah_vega "Not corners. Priorities. We focus on the most exposed lots first. We put covenants in place to protect cultural sites where possible. There's a middle ground."
    "Narration"
    "His language is always neat, the edges sanded by risk assessments and stakeholder presentations. You can hear the pressure behind the politeness; it's like a tide you can feel in the soles of your boots."

    "Dr. Linh (to you, softly)" "If they accelerate construction, we might get a temporary drop in immediate risk, but the living systems we're testing could be cut off before they establish resilience. Engineering without ecology can save roofs while leaving soil dead."

    "Maya (angry, small)" "My mural is on the seawall they'll build. If that wall goes up, they paint over our work with corporate logos. They make our history into display cases."
    "Narration"
    "The volunteers set up pumps, shovels sink, and you begin to coordinate movement like a conductor who has to keep the orchestra playing while a storm is changing the sheet music. The berm is built to"
    "be a learning instrument — a living shoreline experiment — and every tweak you make is a tiny hypothesis. The pilot is a crucible and a classroom; each spilled handful of sand is a lesson."

    menu:
        "Ask Linh to run a rapid salinity test now":
            "You step closer to Linh, voice firm. 'Run it. Now.' She nods, thumbs a sequence on the meter, and the group edges toward methodical panic: clear tasks, cleaner hands. The data will give you a sliver more of agency."
        "Trust the model and continue the plan":
            "You choose faith in the plan. You hand out more gloves instead of asking for more data, and the volunteers pull harder. Your choice distributes responsibility; you cope by making the work communal."

    # --- merge ---
    "Continue"
    "Narration"
    "The sky darkens in a way that feels impatient, as though it has been holding its breath and finally decides to exhale. The tide comes in with a noise like something being unzipped. What was cautious practice becomes an emergency of water and memory."
    # play sound "sfx_placeholder"  # [Sound: A rising, rolling thunder; the slap of water booming against the berm; the abrupt crack of wind-bent wood]
    hide aria_marin
    hide kai_solano
    hide noah_vega

    scene bg ch11_e67f19_2 at full_bg
    "Narration"
    "The surge is meaner than the models showed. A low row of small homes surrenders; water slips like a thief under doors and lifts rugs and knits grief into the air. The memorial garden — the"
    "photos under plastic, the tiny bottles, the salt-stiff flowers — is ripped open; soil swims away and the pictures bob like small, sad corks."

    "Volunteer (voice breaking)" "The Johnson house—"
    show aria_marin at left:
        zoom 0.7

    aria_marin "Get the Johnsons to the high point. Move the kids. Take the blankets from the van."
    show kai_solano at right:
        zoom 0.7

    kai_solano "Hold the line! If we can keep the berm intact, we buy time!"

    "Dr. Linh (shouting over the storm)" "The flats need immediate protection! Pump now or the transplants are gone!"
    "Narration"
    "You move as if your body is obeying old, practiced motions: direct a pair of hands here, brace a stake there. But every time your fingers close around the brass compass at your throat — the"
    "cool, familiar weight — your perfectionism claws at you: we didn't model this. We didn't predict this intensity. You taste culpability like metal."
    # play sound "sfx_placeholder"  # [Sound: A blaring alert from your tablet — an automatic funding notification that reads like a countdown]
    # play music "music_placeholder"  # [Music: A low, relentless percussion under a thin violin lament]
    "Narration"
    "The alert tells you the deadline for a crucial tranche of funding is shorter than you knew. A boardroom clock somewhere else is dictating minutes on your shore. The pilot now has to show results before it has fully had a chance to prove itself."
    "Your phone rings again. It's Noah. You hesitate, mud on your palm."
    show noah_vega at center:
        zoom 0.7

    noah_vega "Aria, we need a decision you can stand behind. Headquarters wants speed. If you back the modular acceleration, we can get crews in within forty-eight hours. We'll include covenants for cultural preservation. It's not everything, but it keeps people out of the water."

    aria_marin "Covenants are paper. They don't stop a cultural erasure that happens slowly, during construction and the economics that follow."

    noah_vega "I know what you care about. I also know what's at stake if another neighborhood floods tonight. Protecting lives is not a betrayal."
    "Narration"
    "He speaks as someone trained to resolve discomfort with solutions. His voice is steady and contains a plea smuggled inside a spreadsheet."
    "Kai Solano's call is next; his tone is rawer, less measured, like someone holding a live wire."

    kai_solano "They push a wall, we push back — physically if we have to. We take the construction site. We make it impossible for them to start. The pilot becomes a rallying point. If you want the town, Aria—if you want people to actually feel like they have a say—this is where we stand."

    aria_marin "Mass mobilization risks arrests, legal action, perhaps violent clearing. It could also dismantle what trust we have in institutions."

    kai_solano "Then let institutions feel what it means to be accountable. Either we build together, or they build over us."
    "Narration"
    "The words fall between you like a storm-front: urgent, boundary-setting, uncompromising. Behind both calls, a pressure chamber hums: Noah with deadlines and corporate breathing down his neck; Kai with a moral heat that can burn alliances if you step too close without planning."
    "Dr. Linh, hands still damp with soil, looks to you with a scientist's exhaustion and something like sorrow."
    hide aria_marin
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Any path chosen now will change the experiment irrevocably. If you scale the pilot quickly with media, we risk it being framed as demonstration theater — failure could delegitimize future funding. If you accept accelerated build, we save structures but likely lose living-system integrities. If you organize a blockade, we may get negotiating power, but your legal exposure will spike and my data collection stops."

    "Maya (small, fierce)" "Whatever you choose, remember what you're choosing for. Not just buildings. People who wake up and remember this place by name."
    "Narration"
    "Your fingers close on the brass compass until the metal bites. Memories spool behind your eyes: the storm when you were a teen, the town left with a seam of loss, the map in your satchel"
    "with thin, hopeful annotations. Your flaw — the voice that demands perfect outcomes — whispers that every compromise is a debt."
    "You can hear the future in the swell of conversation and the hollow, patient moving of water: a choice that is not symbolic but material. The pilot can be doubled into a public demonstration that either"
    "exalts or ruins your approach; Noah's accelerated partial build offers immediate shelter with cultural sacrifice; Kai's blockade can force negotiation at the cost of legal peril."
    "Narration — Internal"
    "You catalog the costs the way you know how: a ledger of what will be lost if you pick wrong. Lives versus heritage; speed versus process; spectacle versus quiet work. Your chest is tight. The town leans on your shoulders like a tide. You have one more decision to make."
    hide kai_solano
    hide noah_vega
    hide dr_linh_pham

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: A single, cold cello note sustains and then cuts]
    # play sound "sfx_placeholder"  # [Sound: The sea exhaling; the distant, small noises of people moving—clamorous, human]

    menu:
        "Double the pilot’s scope — mobilize volunteers and media to prove efficacy.":
            jump chapter15
        "Accept Noah’s accelerated partial build with strict community covenants.":
            jump chapter7
        "Coordinate a targeted blockade to buy time and force a truly negotiated compromise.":
            jump chapter21
    return
