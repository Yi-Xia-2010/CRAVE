label chapter13:

    # [Scene: Tide Lab | Pre-dawn]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low, constant hum of desalination pumps; the occasional squeal of a gull in the distance.]
    # play music "music_placeholder"  # [Music: A single piano line, patient and steady]
    "You are up before the harbor. The city above you is only a ribbon of sodium lamps and fogged windows; everywhere else the tide keeps its slow appointments. Your notebook is open to a page of"
    "dense notes, but your fingers keep returning to the metadata sheet: timestamps, sensor calibrations, chain-of-custody notes. You can taste the salt under your tongue and the metallic tang of fear-coffee at the back of your throat."
    "There is no glamour in this hour—only the long work that makes a case impossible to ignore."
    "Professor Asha stands across the bench, sleeves rolled, braid looped against her shoulder like a question mark. Her hands are steady; her voice is the sort that gathers clarity out of bustle."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We've reconciled the turbidity anomalies with the buoy drift logs. The error bands close when we include community spot-sampling. That alone will neutralize the main counter-arguments."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "And the provenance is airtight? Chain-of-custody on the sensors? The timestamp servers are cross-checked with the lab NTP?"

    professor_asha_rao "Redundant checks. Independent checksum copies. We seeded the repository with archived logs from the city—immutable snapshots. Legal teams like certainty; regulators like replicability. We give them both."
    "You run your thumb along the tide-lines etched into your brass watch. You remember canvassing the Drowned District, watching people point to the algae lines on doorframes and say, 'It was here. It was here.' You"
    "remember the way those markers can be shrugged away by men with slick presentations and PR gloss. This dataset is your answer to being shrugged away."
    "Jonah Reyes slips down the lab ladder, damp jacket clinging to his shoulders, camera bag at his side. He carries coffee in one hand and a printed timeline in the other, each fold worn from use."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You look like someone who's about to change a map."

    mara_ellis "Maps get changed. The hard part is making sure the new lines keep neighborhoods on them."

    jonah_reyes "Then let's make them so stubborn no one can erase them."

    professor_asha_rao "We publish the code, the calibrations, everything. Open-source, peer-reviewed, and packaged for legal audits. We push in a single release with the coalition endorsements. Federal attention follows hard on good evidence and public pressure."

    mara_ellis "And NovaSeis?"

    professor_asha_rao "We document the trade-offs that their models obscure. We don't need to name every executive to make the contracts untenable."
    "You let the sentence sink. You and Asha have talked through the moral arithmetic a dozen ways—how transparency can break monopolies yet also destabilize livelihoods tied to rapid contracts. You think of Jonah's compromises; of the"
    "volunteers who will cheer the headlines and the families whose roofs will go unbuilt if the city freezes funding in the scramble."

    mara_ellis "We make it impossible for them to sell harm as certainty. We make the harm visible."

    professor_asha_rao "Exactly. Evidence that can't be spun is a lever. But levers change weight distribution across the city. Be ready—success will be messy."
    "You feel the truth of that like a cold wind: success as an instrument that cuts as much as it lifts."

    menu:
        "Run one last sensor audit yourself":
            "You crouch to the console and run through the calibration script, fingers moving with the familiar ritual. Each successful checksum is a small, fierce reassurance."
        "Call Jonah and confirm the rollout sequence":
            "You use the lab's satellite link to call Jonah. His voice is low with the fatigue of vigilance, and you both read the rollout checklist aloud like a prayer."

    # --- merge ---
    "Both outcomes converge; continue to the Promenade scene."
    # [Scene: Promenade | Late morning]
    hide professor_asha_rao
    hide mara_ellis
    hide jonah_reyes

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of small waves against pylons; murmured conversations; a volunteer's laughter clipped by nervousness.]
    # [Smell: Frying oil from a nearby food cart, the briny smell of seaweed, the earthy scent of wet soil from seedling trays.]
    # play music "music_placeholder"  # [Music: A swelling string arrangement threaded with low brass]
    "You stand at a small makeshift podium, your notes clipped but largely unnecessary—the numbers are in your bones now, the story etched into the scars of the neighborhoods you love. People look at you: students with"
    "damp hair, elders with faces like maps of the coast, city volunteers who once doubted but now listen. Jonah waits at the edge of the crowd, camera in hand, his gaze a steady presence."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They're with us. Old Mate is here. Maya's handing out timelines. We have calls from three civic groups upstate."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We published the full dataset this morning. Every sensor, every sample, every method—available to anyone who wants to verify, replicate, or build on it. The point is simple: when the science is open, the choices the city makes are public."
    "A murmur of approval ripples through the crowd. A woman near the front raises a fist; a child presses their nose to the projector screen like it's glass."

    "Volunteer" "What does this mean for the pilot projects?"

    mara_ellis "It means pilots will have to meet standards that protect ecology and people. It means contracts that reward short-term fixes will be legally and politically risky. It means federal regulators can—will—act on hard, replicable evidence."
    "From the promenade steps, a reporter pushes through, voice clipped with practiced urgency."

    "Reporter" "Mara—(you)—does this mean NovaSeis's contracts are now in jeopardy?"
    "You keep your voice even. You are a scientist speaking through a heart that keeps making choices in the language of people."

    mara_ellis "Our work shows where those contracts produce unaccounted harm. We are not proposing chaos; we are proposing accountability. Cities can do both: build defenses and ensure they're ecologically sound and socially just."
    "Asha steps forward, tablet in hand, and displays a live feed of the repository. The screen is a dense, honest thing—graphs that refuse simplification, time-series that show erosion rates and ecological signal."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "We invited independent reviewers to the release. Their preliminary reads are clear: some widely-touted interventions shift sediment budgets in ways that increase long-term exposure for adjacent neighborhoods. The models used by private contractors rely on closed assumptions; those assumptions are now public."
    "The applause is immediate and relief-sweet. Jonah's camera catches your face from the side; you are smiling, but there is a tightening behind your ribs."

    menu:
        "Invite Old Mate to speak next":
            "You step aside and gesture for Mateo to come up. His voice, rough with salt and story, grounds the science in memory and consequences, and the crowd leans forward as if tethered."
        "Keep the floor and read a technical summary":
            "You walk them through the core findings—simpler than you'd rehearsed, sharper for clarity. The crowd takes in the mechanics of harm and begins to translate that into pressure."

    # --- merge ---
    "Both outcomes converge; continue to the Federal Agencies scene."
    # [Scene: Federal Agencies | Midday, One Week Later]
    hide jonah_reyes
    hide mara_ellis
    hide professor_asha_rao

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The neutrally amplified murmurs of officials; the distant drone of city maintenance outside.]
    # play music "music_placeholder"  # [Music: Low, taut strings that suggest consequence]
    "You and Jonah sit opposite a panel of federal regulators—stern faces, competent voices—joined by legal advisors who flip between terminologies like cards. The air here is filtered and cool; your hair smells less of sea and more of sterile carpeting and bureaucracy."

    "Senior Regulator" "Your data is rigorous and replicable. We've had petitions, complaints, and—now—open-source evidence that shows model failures with proprietary implementations. This changes the regulatory calculus."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "We didn't want the city to be handcuffed. We wanted policy that would force better contracts—transparency clauses, ecological impact bonds, monitoring requirements."

    "Regulator's Advisor" "We've drafted emergency guidance that will require public disclosure of long-term sediment and ecological modeling assumptions in any federally funded coastal defense contract. Non-disclosure will be a disqualifier."
    "A subdued cheer ripples through you. Federal action—something that had felt like a horizon until now—has moved into the present. You picture seedlings arriving, grant checks being cut, community liaisons hired."
    "But the panel's counsel is not without sharp edges."

    "Legal Counsel" "We expect litigation. NovaSeis has already filed for interim injunctive relief claiming proprietary rights. This will be messy. We can protect the open data, but courts will be busy, and politicians will be vulnerable."

    mara_ellis "We expected that. The point is not immediate quiet; it's durable standards."

    "Senior Regulator" "Durable standards mean reallocating funds. That means some short-term projects will be paused. Some neighborhoods will be prioritized for relocation funds because their geophysical position and economic exposure mean adaptation here is not viable."
    "The words land like a different tide—slow, inexorable. You had argued for community-centered approaches, for trying everything to keep people in place. But now federal triage will formalize what you feared: some places cannot be saved."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We did the right thing."

    mara_ellis "We did what could be proven. But proof becomes policy, and policy makes winners and losers. Be honest with them—be honest with us."
    "Across the city, the release has already cascaded into action. NovaSeis's stock drops; board members make terse statements; news cycles spin narratives of accountability, victory, and righteous exposure. Public comment forums overflow with citizens who feel heard for the first time—and with angry contractors and displaced workers demanding protection."
    # [Scene Transition: Montage — Press conferences, hearings, volunteers distributing relocation pamphlets, legal filings, community meetings where fists and tears appear in equal measure. The city is alive with the feeling of tectonic change.]
    # play music "music_placeholder"  # [Music: A fuller arrangement starts bright, then folds into dissonant undertones]
    "You and Jonah are invited to testify before a national committee. You ride an elevator that smells faintly of lemon cleaner and nerves; reporters cluster at the doors. The applause when you exit feels thin compared"
    "to the images that return to haunt you—flood-streaked doorframes; old neighbors with packed suitcases and faces like closed doors."

    "Professor Asha [weary but resolved] (on a conference call)" "This is systemic change. NovaSeis will litigate. The federal rules will reshape bidding, but the legal processes and bureaucratic reallocations will mean pain for some. We must pour resources into relocation ethics and reparations frameworks now, not later."

    mara_ellis "We will. We have templates. But the city will need to own the heavy conversations—compassionate timelines, community-led site selection, guaranteed housing."

    "Jonathan (a federal liaison)" "There's funding for that. Priority channels are open. But political churn is inevitable. Officials pushed too far too fast will be exposed."
    "You imagine the mayor's face, the councilors in suits who once offered bland assurances. A city that changes its rules in public will spawn enemies and allies in complicated measures. You are not naive; you are"
    "not unprepared. Still, as the applause dies down and the tape recorders are turned off, you feel the first real ache of the costs."

    menu:
        "Attend the community relocation meeting tonight":
            "You show up at the community center with a stack of pamphlets and your measured empathy. People press concerns and memories into your hands—you answer, you listen; sometimes, the two don't reconcile."
        "Debrief with Jonah and Asha privately":
            "You close the lab door and let the three of you speak plainly—strategy, legal shadows, what has been sacrificed. The conversation is harder for being honest, but it steels you."

    # --- merge ---
    "Both outcomes converge; continue to the Drowned District edge scene."
    # [Scene: Drowned District edge | Dusk]
    hide mara_ellis
    hide jonah_reyes

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow lap of water, a radio playing a children's song, the distant murmur of a protest across the bridge.]
    # [Smell: Old wood, mildew, the sharpness of wet paper.]
    "You stand at the boundary where the city has drawn a new line. Some houses will be fortified; others will be marked for relocation with neat, bureaucratic stickers that feel like erasures. A child presses a"
    "damp rock into your hand—a gift, she says, for 'keeping the water honest.' You accept it like taking a small and complicated truth."
    "Old Mate sits nearby, toes in brackish shallow water, face unreadable."

    "Mateo "Old Mate" Alvarez" "You did a thing, niña. You made loud what was being whispered. But loud makes people move faster than they can pack."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "We couldn't let them build certainty on someone's loss."

    "Mateo "Old Mate" Alvarez" "No. But letting certainty go is also costly. There'll be lawsuits. There'll be money that doesn't arrive fast enough. There'll be councilors fired and new ones who don't know the old stories."
    "You close your eyes for a second and think of your childhood house—its last winter roof sagging, the smell of your mother's soup, the mattress pulled up on blocks during a flood. You think of how"
    "you promised to keep other neighborhoods from the same slow erasing. That promise is a living thing now, and it will demand choices that scar."
    "Jonah Reyes steps to your side and sets a small potted marsh grass between you. He kneels and presses it into the soil of a raised planter already marked with community names."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We plant here, and we plant elsewhere. We make new ground and remember what this cost."
    "You both lean in, hands covered in damp earth and salt, and plant."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "The regulations are passing. Federal funds are committed to relocation where necessary. NovaSeis's suits will drag; we must be ready for protracted legal defense for the open data. Prepare community legal aid. Prepare the memorial events. Prepare the training programs."
    "You breathe in the marsh smells and the human noise around you. There is pride—sharp, bright—and grief threaded through it."

    mara_ellis "Is this enough?"

    professor_asha_rao "Enough isn't the right question. This is what we can do now. It alters what comes next."

    "Mateo "Old Mate" Alvarez" "You will need stories later, niña. Not for the papers—for the ones who stayed and the ones who couldn't. Tell them true."
    "You promise with the kind of vow that is tacit and heavy. The city shifts under your promise—laws, lawyers, funds, and uprooted roots all rearranging the skyline."
    # [Scene: Rooftop Garden at the PolySilo | Night]
    hide mara_ellis
    hide jonah_reyes
    hide professor_asha_rao

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through succulents, a distant siren, the soft click of Jonah's camera shutter capturing a moment you both know will be edited into history.]
    # play music "music_placeholder"  # [Music: A bittersweet cello line under a warming piano]
    "You and Jonah sit with your feet against a low wall, sharing a thermos. Your hands find each other without looking, fingers tracing the familiar maps of knuckles and tides. The city's new rules hum like a background engine—good, necessary, disruptive."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "People are saying you're a hero. I'm saying you made the hard call."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Heroes get statues. I get spreadsheets and court notices."

    jonah_reyes "Which sounds worse?"

    mara_ellis "Both. But look—' (you sweep the skyline) '—they're listening now. Cities will change because the data wouldn't let them pretend. That is real. That matters."

    jonah_reyes "And we will lose some things. People won't like how fast or slow it goes. There will be anger. There will be poems and lawsuits."

    mara_ellis "And we'll answer. We'll keep the records. We'll keep the ethics committees on them. We'll push for reparations where we can. It isn't a clean victory."

    jonah_reyes "It isn't supposed to be. It's the sort of victory that asks you to carry the weight deliberately."
    "You feel that weight settle onto your shoulders—not crushing, but honest. You think of Professor Asha's steady hands, of the volunteers standing in the rain, of the families who have already had to move. You think"
    "of Elias Crowe—of his fall from polished podiums to obscure litigation, of boardrooms that no longer mirror his voice as loudly. His loss is political and surgical and small compared to human displacement, but it is"
    "a part of the reckoning."
    "You reach into your pocket and pull out the damp, curling print Jonah once gave you long ago—the one you pressed your thumb into as if to hold that earlier certainty. You place it between your palms and let the harbor light paint it."

    mara_ellis "We changed the rules. We made a place for the kind of adaptation we believe in. The system shifted under everyone's feet."

    jonah_reyes "And you shifted too."
    "You look at him. The softness there is real and unperforming. The future is not a promise but a series of commitments, some joyous, some bitter."

    mara_ellis "We keep going. We keep the data open. We keep telling the stories of those who can't stay. We keep planting."
    "Jonah Reyes squeezes your hand; the gesture is small and complete."
    "You look out at New Maris: the harbor lights, the half-submerged boardwalk, the small green patches that are becoming something like a network. The city will never be what it was. You will never be what you were. Change has the shape of losses and lessons."
    "You place your palm over the small plaque in the soil—fingers pressing into wet dirt. The act feels like an offering and an account."

    mara_ellis "We gave the city its chance to do better. That is true. It cost us what we must carry."
    hide jonah_reyes
    hide mara_ellis

    scene bg ch13_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: The cello resolves into a haunting major chord, then softens]

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch13_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
