label chapter6:

    # [Scene: Field Lab & Greenhouse | Late Morning]

    scene bg ch6_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent strings; a single staccato piano begins to tick like a counting heart]
    "You set the final page into the binder with hands that still tremble from last night's final run of the models. From Chapter 4, Option B — you chose the slow, earnest path. The choice hums under your skin like a ritual you both welcomed and feared."
    "Dr. Henrik Sato sits across from you, spectacles perched, leafing through the executive summary as if tasting the sentences. His breath smells faintly of tea and the harbor—brine and paper. Elias Voss leans in beside him"
    "with your laptop open, smoothing a slide about projected job retraining rates like a seamstress pressing a fold flat."
    show dr_henrik_sato at left:
        zoom 0.7

    dr_henrik_sato "Maya, these assumptions—your sediment accretion rates—are conservative but not pessimistic. You built room for error."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Margin's thin. We can't promise certainty we don't have. We can promise transparency and staged commitment—a phased living seawall, tidal gardens, retraining."
    show elias_voss at center:
        zoom 0.7

    elias_voss "And the economic slides? If we soften the rhetoric—translate 'community stewardship' into employment numbers and stepwise financing—we're talking language funders understand."

    dr_henrik_sato "You translate values into schedules and people listen. That's the trick."
    "You breathe in, the greenhouse humid and warm against the cold outside. Your compass pendant rests between your sternum and shirt; you touch it without thinking, like seeking a familiar coastline."
    "You tighten the binder's rings. The report smells of ink and salt and something older—like the town itself, bound up in pages."

    menu:
        "Add a personal preface — make it human":
            "You write two short paragraphs, a memory of the storm that took your streetlamp. It reads like a promise. Elias looks at you and blinks; the slide deck just became harder to dismiss."
        "Keep it clinical — let the data speak":
            "You delete the preface and replace it with a tighter methodology section. The document becomes an arrow. Elias exhales; this will survive political scrutiny."

    # --- merge ---
    "..."
    # [Scene: Municipal Hall / Council Chambers | Afternoon]
    hide dr_henrik_sato
    hide maya_ortega
    hide elias_voss

    scene bg ch6_4001e7_2 at full_bg
    # play music "music_placeholder"  # [Music: Cello line pulled taut; percussion enters as a heartbeat speedens]
    # play sound "sfx_placeholder"  # [Sound: Murmur of the crowd, microphone feedback baseline]
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "We present a phased plan that prioritizes livelihoods and the town's character. Phase one: reinforced tidal gardens and modular living seawall sections at critical nodes. Phase two: public works training and microloans for local businesses. Phase three: monitoring and iterative expansion tied to measurable outcomes."
    show councilwoman_tamsin_hale at right:
        zoom 0.7

    councilwoman_tamsin_hale "You ask for time when money is on the table. Time has a cost, Ms. Ortega."

    maya_ortega "Time's not an absence of action. It's staged mitigation informed by site-specific data. We can build in weeks—testbeds—while securing larger funding."
    show mira_chen at center:
        zoom 0.7

    mira_chen "Our funders are willing to move at scale if we can commit to a single, fast-build path. They purchase certainty."
    "Dr. Henrik Sato steps up to the projector, pointer in hand. He walks the council through sediment maps, tide projections, employment forecasts—point by patient point. Elias Voss slides in economic charts translated into blunt numbers: job-years"
    "created, percentage of local hiring, projected revenues for small businesses helping to staff green infrastructure. The room leans into the math because numbers are less messy than grief."
    hide maya_ortega
    show dr_henrik_sato at left:
        zoom 0.7

    dr_henrik_sato "This isn't sentimental. It's pragmatic. These measures lower risk and build capacity. They buy resilience and keep wealth in the community. They also require phased funding and oversight—"

    councilwoman_tamsin_hale "Phased funding is a political unicorn. Grants come with deadlines. If we can't prove immediate results, those funds move to neighboring counties that can deliver faster."
    hide councilwoman_tamsin_hale
    show elias_voss at right:
        zoom 0.7

    elias_voss "We can pilot within funding windows. Show metrics at ninety days, six months. The pilots are replicable. The model scales if it's successful."
    hide mira_chen
    show councilwoman_tamsin_hale at center:
        zoom 0.7

    councilwoman_tamsin_hale "Replication isn't cash. It's a promise. Promises don't pay salaries this quarter."
    "Her voice is a blade. The room's temperature drops. You sense bifurcation: procedural argument on one side, immediate human need on the other."
    # play music "music_placeholder"  # [Music: Percussion accelerates, high strings creep upward]
    # play sound "sfx_placeholder"  # [Sound: Emergency alert chime—sharp, metallic; a notification tone from the town's emergency system]
    "A council aide's tablet flutters to life. The projection screen blinks red: STORM WARNING — RAPID INTENSIFICATION FORECAST. The emergency system routes a live feed to the room. On the video, clouds churn low, an angry bruise on the horizon."
    hide dr_henrik_sato
    show mira_chen at left:
        zoom 0.7

    mira_chen "Weather does not care for your pilot schedule."

    councilwoman_tamsin_hale "If we delay, the money evaporates. If we commit to slow, we risk losing capital—and with it, any chance to secure the town's borders quickly enough."
    hide elias_voss
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Money that ignores the land will change it. A concrete wall may stop a wave—temporarily. It will change our shoreline ecology and livelihoods. It will push fishermen farther out."

    councilwoman_tamsin_hale "Sometimes the choice is between preserving a coastline and preserving lives now."
    hide councilwoman_tamsin_hale
    show elias_voss at center:
        zoom 0.7

    elias_voss "We're not against saving people. We're asking for solutions that don't make survivors soulless."
    "Council members exchange glances veterans know as the 'vote-of-avoidance' look. The microphone crackles. Outside, the rain steps up into drumbeats. The model on Henrik's slide flickers as network packets slip; the feeds stutter."
    hide mira_chen
    show dr_henrik_sato at left:
        zoom 0.7

    dr_henrik_sato "We showed competence. We showed the road. But competence doesn't keep a roof on tonight if a wall goes up tomorrow."

    maya_ortega "Then tell me what keeps the warehouse on the dock. Tell me what keeps the boats from being lost before our pilot proves itself."

    "Councilwoman Tamsin Hale leans forward, voice low and decisive" "Our regional partners have offered immediate funding contingent on fast deployment. Mira's group can meet those timelines. If we reject that now, the fund shifts. I am not willing to gamble the town's paycheck on a pilot that takes months."
    "The storm siren outside swells into the room's margins. People begin to call out names—Luca—neighbors—warehouse numbers. The room condenses into points: fear, calculation, urgent need."

    menu:
        "Call Luca and ask for a status on the warehouse":
            "You hit call and hold. Static, then Luca's voice: 'Door's holding but water's creeping under the rafters. We're trying to sandbag.' You end the call with a hollow, 'Be careful.' The sound of his breath is a geography of threat."
        "Stay in the room—push the presentation through":
            "You close your phone and drive forward with the slides. The council needs data. The room needs a plan. You can hear the ocean in the pause between sentences."

    # --- merge ---
    "..."
    # [Scene: Harbor — Night into Dawn]
    hide maya_ortega
    hide elias_voss
    hide dr_henrik_sato

    scene bg ch6_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: High, discordant strings; wind instruments shriek intermittently]
    # play sound "sfx_placeholder"  # [Sound: Creaking wood, dull thuds as waves lap and pry at structures; a distant, terrible grinding noise]
    "You did not get to be everywhere. You could not. By dawn the low-lying warehouse has surrendered—its roof ripped off like a page from a book; crates and pallets are strewn in a greasy, floating morass."
    "The smell is diesel and brine and something burned—paper from invoices and a poster of a summer festival curling in the salt."

    "Mira Chen stands at the dockphone, composed in a way that makes your stomach tighten. Her funders' voices echo in her ear; she repeats them almost mechanically" "Immediate action... rapid deployment... we need commitment."
    show mira_chen at left:
        zoom 0.7

    mira_chen "We can fund a rapid-build seawall tonight. We can have crews mobilized within forty-eight hours. We can—"
    show councilwoman_tamsin_hale at right:
        zoom 0.7

    councilwoman_tamsin_hale "We will need a commitment tonight. The warehouse loss makes the argument unanimous. The insurers will push; the public will demand action."
    show maya_ortega at center:
        zoom 0.7

    maya_ortega "That warehouse held people's livelihoods. We didn't stop that. We showed a path and time ran out."
    hide mira_chen
    show elias_voss at left:
        zoom 0.7

    elias_voss "You did what you could in the time you had. You made the plan that kept people in mind."
    "But the council isn't a single heart; it's a tangle of veins. A cluster of neighboring councils text their conditional support—emails you've already scrolled through—pledging political backing if you can show near-term metrics. They like the science. They do not like the wait. Mira's funders smell leverage."
    hide councilwoman_tamsin_hale
    show dr_henrik_sato at right:
        zoom 0.7

    dr_henrik_sato "The science is a ledger that records what happened. Right now the ledger says: unspent pilot funds and a warehouse gone."

    maya_ortega "It's not just numbers. It's—"
    "Your words don't finish because there is nothing to finish them with. The day folds around you like a palm closing. People shout into phones, chain-link fences clang, someone starts clearing floating debris by hand with a shovel because some tasks cannot wait for meetings."
    "Elias Voss squeezes your hand so hard it hurts—an anchor in the dragging current. You can feel the heat of his palm through your glove."

    elias_voss "We make this mean something. We don't let a lost warehouse be the end of what we started."

    maya_ortega "Make it mean—how? We don't have the funds Tamsin talks about. We don't have the political majority. We don't have the time the sea dictates."
    "He looks at you, and for a moment the noise falls away: the wind, the crack of splintering wood, the reporters' cameras clicking in the distance. There is only that pressure between your fingers and his—small, human. A promise that is not a solution."
    # play music "music_placeholder"  # [Music: A single low string note that sustains and frays into nothing]
    # play sound "sfx_placeholder"  # [Sound: The low, distant groan of a hull settling; gulls return like witnesses]
    "You walk away from the immediate wreckage and down the living seawall path toward the stretch of shore where the tide gardens are supposed to take root. The marsh shoots lie flattened in places, bruised. Your hands, still smelling of salt and diesel, close around your compass again."
    "You think of every meeting, every night in the lab, every time you chose a slower path because you believed people deserved agency. You think of the warehouse—of Luca and the crew who lost inventory, of Rosa's nets tangled with plastic and timber."
    "You lay the binder on a driftwood bench and watch the water take a faded logo from a business card. The technical report—bound, peer-reviewed, and persuasive—feels like a small, heavy stone. It proves competence. It proves care. It does not buy the town another season."
    "Councilwoman Tamsin Hale presents the motion to accept Mira Chen's rapid-build proposal with conditions that she promises to negotiate—timelines, oversight, limited local hiring clauses. The council votes. You can see the arithmetic in the hands raised: fear, practical need, pressure from unseen funders. The motion carries."
    hide maya_ortega
    show councilwoman_tamsin_hale at center:
        zoom 0.7

    councilwoman_tamsin_hale "We will work to include local labor where possible."
    hide elias_voss
    show mira_chen at left:
        zoom 0.7

    mira_chen "We will mobilize immediately. We'll collaborate with local subcontractors."
    "Your report will be archived. Your models cited by neighboring councils. Your name will be in emails praising the pilot's clarity. The town will change. The seawall will go up. It will look like protection—vast and unyielding—and parts of the living shoreline you imagined will be altered beyond quick repair."
    "Maya Ortega closes the binder and slides it into your messenger bag. Elias Voss walks beside you without speaking. The town's sirens fade into a wet silence. Neighbor by neighbor, people appear—wringing out blankets, salvaging crates,"
    "taking stock of loss. Rosa Delgado yells instructions in her practical, hoarse voice—concrete next steps: distribution lines, temporary storage, volunteer signups."
    hide dr_henrik_sato
    show rosa_delgado at right:
        zoom 0.7

    rosa_delgado "We don't have time for pity. We have time for work. Hands—everybody—now."
    "You shoulder the weight of the binder and the weight of complicity. You wanted a path that kept the town's shape intact. Weather and capital chose differently."
    hide councilwoman_tamsin_hale
    hide mira_chen
    hide rosa_delgado

    scene bg ch6_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: A slow, mournful piano; the tempo decays into a soft, hollow space]
    "You stand on the boardwalk with Elias Voss at your side and listen to the town rearrange itself around the new reality. Councilwoman Tamsin Hale shakes hands with Mira under the municipal lights. Dr. Henrik Sato"
    "folds his notes with a care that looks like resignation and pride at once. Luca arrives with mud on his boots and a small, stubborn smile that tries to promise that they'll rebuild, even if they"
    "must do it over someone else's schedule."
    show elias_voss at left:
        zoom 0.7

    elias_voss "What you tried to do matters. We'll keep that going, even if it's behind bigger machines."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "It matters, yes. But it also—didn't stop tonight."
    "You press your thumb against the compass pendant until it aches. Salt stings at the corner of your eyes. The town will be repaired in ways both protective and indifferent. The report sits inside your bag, evidence of a way chosen and argued for—true, careful work that was not enough."
    # [Direction: Close on Maya's face; wind threads hair across your cheek. The camera lingers until the sound of the tide fills the frame.]
    "You let the grief sink in because it is real and immediate, and because naming it is the only honest thing left to do. The narrative of saving the town grows more complicated and less heroic"
    "than you envisioned. You did not fail in process; you failed in timing. You did not abandon care, but care does not always equal survival."
    "Elias Voss squeezes your hand again, gentler this time. For a breath, it is a small human truth in a large, indifferent storm."

    elias_voss "We keep the work alive. We keep showing the alternatives. People will remember what's been proposed here."

    maya_ortega "They may remember the plan or they may remember the loss. Either way, we keep doing the next right thing we can see."
    # play music "music_placeholder"  # [Music: A single piano chord dissolves; distant gull calls return faintly]
    hide elias_voss
    hide maya_ortega

    scene bg ch6_4001e7_5 at full_bg
    "You breathe and, for the first time since this started, name the ache: a long, low grief that will not be smoothed over by a single meeting or a single wall. The route you took produced"
    "clarity and dignity and a document that will outlast the immediate scramble—but clarity does not equal victory."
    "You fold your hands around the compass. It is small and cold and it keeps no promises you cannot make. You tuck the binder deeper in your bag and stand with the town that is yours and not yours now—with its losses, its bargaining, its stubborn, compromised survival."
    # [Direction Cue: Fade out on the harbor—broken lines of light across a wind-rippled, tired sea]
    # play music "music_placeholder"  # [Music: Fade to a distant, unresolved string tone]

    scene bg ch6_4001e7_6 at full_bg
    "THE END"
    # [GAME END]
    return
