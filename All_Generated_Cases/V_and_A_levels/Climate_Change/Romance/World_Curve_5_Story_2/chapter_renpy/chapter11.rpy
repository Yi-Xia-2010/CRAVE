label chapter11:

    # [Scene: Rooftop Community Garden & Storm Shelter | Night]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind pushing against the shelter tarps; a distant, steady roar of the tide beneath it all.]
    # play music "music_placeholder"  # [Music: Low, urgent strings — a heartbeat under everything]
    "You stare at the rectangle of light in your hand until the edges blur. The subject line is the same as the ping you felt earlier: audit_upload_... You open it because that is what you do: you follow the numbers, the evidence, the possible harms."
    "The file blooms across your screen — tables, highlighted passages, a leaked internal email threaded beneath. The words read like a hinge about to snap: TideLine’s prototype would reduce immediate exposure but the contract clauses give"
    "the company priority control over shoreline access and operational decisions. 'Operational control' repeats in a sterile font until it feels like a verdict."
    "Your wire-frames slide down the slick of rain on your nose. You push them back, clumsy, and realize your hands are shaking. A wet smear of ink from your notebook darkens the webbed paper between your fingers; the tide's roar pushes a cold comment through the city, mocking and enormous."
    "You think of the greenhouse, of Lian's patient explanations, of Rosa's blunt maps. You think of Old Tomas bending to the net that once held a fish you never met. Guilt flares hot under your ribs"
    "— not strategic, not useful — and then the practical part of your brain catalogues the consequences with the unkind clarity of a scientist under fire: the contract could privatize piers, fence off traditional paths, subcontract"
    "enforcement, and bind the town into nondisclosure around risk assessments. The email beneath the audit reads like a map of how that might be sold as efficiency."
    "You stand. The rooftop lantern bobbles in the wind. Rosa finds you, hands steady on your shoulders."
    show rosa_sol at left:
        zoom 0.7

    rosa_sol "We warned them we'd look. We asked for space. We gave them time. You did the right thing bringing this up."
    "You want to believe her voice. You want it to be a tether. But the urgency that follows is not comfort — it's demand. The leak will not sit quiet. It will move."
    hide rosa_sol

    scene bg ch11_e67f19_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings snap into higher tempo — a climb]
    # [Scene: Town Hall — Special Meeting | Late Afternoon, Storm Outside]

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs turn to a low wash; a camera flash snaps like a starting gun. The tide's roar threads through an open vent.]
    # play music "music_placeholder"  # [Music: Percussive, frantic—high-tempo with metallic edges]
    "You take the lectern with your notebook clutched to your chest. Dr. Lian stands behind you with a tablet that glows like a second heartbeat. Mayor Ana sits to your right, composed but exhausted; Aria Chen"
    "sits across the dais, the TideLine cuff a small flash of silver when she gestures. Jun Park is tucked near the back, face pinched; he keeps checking his hands the way someone checks a wound."
    "You breathe and tell them what the audit says, and your voice is a precise instrument at first — numbers, confidence intervals, modeled exposure. You call out the clear, immediate benefit: the prototype's engineering would lower"
    "short-term flood exposure metrics along several sections of the bay. You do not sugarcoat it."
    "Then you hold up the clauses."
    show marin_sol at left:
        zoom 0.7

    marin_sol "But the contract language gives operational priority to TideLine. Access control, enforcement rights, and unilateral maintenance windows are all written in. That means—' (your voice tightens) '—the co-op piers we use, the winter haul-outs, seasonal traps—those could be restricted under company discretion."
    "A hand raps the table; the room splits into a scatter of reactions. Half of the faces have fear carved into them. The other half have the quick, hungry math of relief: protection now."
    # play sound "sfx_placeholder"  # [Sound: A voice breaks the room — sharp, accusatory]

    "Crowd Member" "So you're telling us to choose culture over safety?"
    "You pivot, but before you can answer, Jun stands. He looks smaller than the last time you saw him. Rain beads on the collar of his jacket where someone stepped in through the back—people have been moving between the meeting and the street to watch the news feeds."
    show jun_park at right:
        zoom 0.7

    jun_park "I—' (he swallows; his words come in ragged breaths) 'They asked me to sign nondisclosure pages. I refused the first time. Then they said it would be 'standard practice' and they'd handle communications. They told me not to worry about 'day-to-day' access language. But—' (his hands fumble) '—they kept saying legal teams would 'have final say' on ambiguity."
    "A low, collective intake. You feel the room tilt."
    "Aria Chen's smile is measured but thin."
    show aria_chen at center:
        zoom 0.7

    aria_chen "Jun—there are standard clauses in many contracts. TideLine's goal has always been to provide quick, reliable protection. Operational language does not mean privatization. It means efficiency—coordination during emergency protocols."
    "Jun's expression fractures."

    jun_park "You told us to trust you. You told us this was about safety. Then they showed me a template with enforcement language and penalties for 'unauthorized access.' It—' (he breaks) '—it reads like a lock."

    "Aria Chen moves forward, almost smooth" "No one wants to lock anyone out. We have plans for community liaison and shared access periods. We're open to oversight."
    "Old Tomas, who has been listening in a corner, leverages the old cadence of story-telling — the kind that slows a room down."
    hide marin_sol
    show old_tomas at left:
        zoom 0.7

    old_tomas "When I was a boy there was a path the gulls knew like a prayer. We walked it to the inlet, to the nets, two or three of us balancing on a board. If you put a fence there, you don't just stop a person. You stop a memory. You stop the way the sea feeds us and we feed back."
    "The room hums with that image. Someone begins to cry. A shout cuts through it."

    "Townsperson" "They're selling us a wall for a price!"

    menu:
        "Answer firmly, explain the data and the clauses line-by-line":
            "You lean into the microphone. Your words are sharp and slow, each clause parsed, each sentence anchored to a slide. People listen — some nod, some scowl. You earn comprehension but also deepen the fear; the room's temperature rises."
        "Hold silence and let others speak":
            "You close your notebook and let the air fill. Others fill the space with stories and outrage; you feel the pressure move outward and away from you for a heartbeat, but the silence feels like an unspoken admission. The murmurs grow louder, and a reporter edges closer."

    # --- merge ---
    "The meeting fractures into smaller arguments, and the leak—pairing the audit with the internal email where a TideLine manager wrote 'operational dominance will prevent politicized interference'—changes the rhythm entirely. The phrase 'politicized interference' flashes on screens in the hands of people who haven't slept."
    "Mayor Ana rises, palms flattened on the table. She speaks with the political calculus of someone who has learned to weigh votes like tide tables."
    hide jun_park
    show mayor_ana_beltran at right:
        zoom 0.7

    mayor_ana_beltran "We need options that do not gut our safety. We also cannot sign away our people's rights. Marin, what would your legal team recommend first? What gives us leverage without leaving us without protection while storms come?"
    "You think of timelines. You think of grants expiring, storms scheduled in the modeling, the calendar of herring runs that cannot be postponed. The room seems to fold in on itself — like a lung failing to take air."
    hide aria_chen
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "Technically, an injunction could expose the clauses to public scrutiny fast. But it's costly and adversarial. It could slow implementation but not guarantee that external funding stays. A negotiated clause with binding community co-ownership could be inserted, but TideLine will push back hard."
    "Aria Chen's jaw tightens. She steps in, voice a cool, dangerous clarity."
    hide old_tomas
    show aria_chen at left:
        zoom 0.7

    aria_chen "We can redline. We can accept oversight language. But you must understand: every delay increases risk exposure. We are prepared to activate the prototype on a schedule. If you create legal obstacles, TideLine cannot guarantee timelines."
    "Jun moves closer to you, voice small and urgent."
    hide mayor_ana_beltran
    show jun_park at right:
        zoom 0.7

    jun_park "I didn't want to lie. They asked me to keep certain emails internal. I—' (he looks at you, as if you might steady him) '—I thought I could keep them honest from the inside, but now—"
    "You reach for him; your fingers touch his sleeve. He flinches, not from your touch but from the exposure."

    menu:
        "Press Jun for the full extent of what he knows now":
            "You press with the kind of gentle insistence that betrays no malice. Jun tells more—dates, names, times he was instructed to withhold emails. Each detail is a small fissure in the company's narrative. The room leans in."
        "Protect Jun and steer the conversation back to technical options":
            "You put a hand on Jun's shoulder and deflect to the next slide, talking models and oversight frameworks. Jun breathes out; he looks relieved, but a sliver of distrust cuts the room—some think you're shielding a corporate actor. The crowd's anger sharpens."

    # --- merge ---

    "Outside, a hullabaloo builds. Rosa's voice on a livestream is a bright spark" "Meet us at the prototype. Don't let them build fences in our names."
    # [Scene: TideLine Prototype Site | Early Evening, Downpour]
    hide dr_lian_obasi
    hide aria_chen
    hide jun_park

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chanting, the howl of amplified wind pushed through cheap PA speakers, a police radio chirps in the distance.]
    # play music "music_placeholder"  # [Music: Rapid, metallic percussion; the emotional tempo peaks]
    "Old Tomas stands on a low crate. He repeats the path story, hands at his sides, voice raw with memory. People join his cadence. Someone holds up a wet photograph of the old nets, another waves a weathered buoy."
    show old_tomas at left:
        zoom 0.7

    old_tomas "When they put cages where the path used to be, they will tell you it is for 'safety.' But you'll remember which gates open for checks, and which stay shut. You'll remember who can bring tractors and who gets a permit. The sea doesn't forget how you choose to keep it."
    "Aria Chen arrives, the TideLine team in a line behind her. She meets Rosa halfway, the two of them the spines of two different futures."
    show aria_chen at right:
        zoom 0.7

    aria_chen "Rosa—this doesn't have to be a showdown. We can frame shared use in maintenance windows. We can—"
    "Rosa: (cutting) 'You put a clause in that says 'priority.' You tell us it's for coordination. When my uncle needs to pull his net, I don't need TideLine's 'coordinator' to tell him when he can touch his life. We are not a policy variable.'"

    aria_chen "I'm not proposing life be assigned a number—"
    show rosa_sol at center:
        zoom 0.7

    rosa_sol "Then don't write us into one."
    "The crowd noise swells into something like a single, pulsing animal. You stand between them, rain running down your neck, notebook soaked. Your hands feel too full of consequences you cannot somehow arrange into a shape that keeps everyone."
    "Jun is there too, thin and pale. He looks at you as if asking permission and apology at once. He has become the human hinge of a corporate machine and your neighborhood's trust."
    "A news van flashes; the email text scrolls across a battered screen: operational dominance; enforceable penalties. Someone in the crowd shouts that the company is 'taking our shoreline.'"
    "Your chest tightens until it is a physical thing. The tide's deep voice thrums under your feet like a drumroll you did not order. The political pressure becomes a tidal bore: hotels call, the mayor's office pings your line, the town's legal counsel asks for a meeting."
    "Back at Town Hall, after the prototype gathering, the mayor's office forms an island of whispered counsel. The options lay out before you like salted knives:"
    "- Press the mayor to flatly reject any TideLine contract and mobilize a legal challenge. (Immediate political collision; possible loss of short-term protection.)"
    "- Take the leaked clauses to court and file an injunction right now. (Legal clarity at the cost of confrontation and expense.)"
    "- Negotiate a binding community clause with Mayor Ana and trusted counsel, demanding co-ownership. (A hard compromise that could secure long-term protections — if TideLine agrees.)"
    "Your breath catches at the practical realities: storm windows, grant timelines, volunteer rescue crews who cannot wait for lawyers to untangle lines. Your emotional reality — your guilt and the memory of the friend you once lost to a sudden storm — turns the choices into moral knives."
    "Aria Chen watches you, inscrutable but alert. Jun stands to one side, a small man under a big machine. Rosa is incandescent with righteous anger, ready to march on whatever decision you make. Old Tomas looks like he might fold in half from the strain."
    "You remember the greenhouse light, the slow promise to build differently. You remind yourself of Dr. Lian's charts and the models that whisper 'delay increases risk,' and you also remember how a fence does not care whose hands make it."
    "The rain intensifies outside like a metronome for panic. The crowd noise threads into a single high pitch. Your pulse matches it. You feel every eye on you, every expectation and reproach."
    "You have to choose."

    menu:
        "Step forward, call for immediate rejection of the TideLine contract and mobilize political action":
            "Your voice is raw but steady as you tell the mayor you will make the refusal public, to mobilize legal counsel and town votes. The room explodes — some cheer, others panic. Rosa clamps your hand and begins to organize a march. But you also hear the murmur of 'who will fund the barriers if not them?' and the worry cuts deep."
        "File for an injunction in court right away, exposing the clauses formally":
            "You outline the legal route, telling Ana you want to take the clauses into court. Dr. Lian nods affirmatively at the scrutiny this will bring, but you feel the immediate recoil—cameras sharpen their focus and Aria's face steels. Jun looks both relieved and terrified; the town readies for a courtroom battle."

    menu:
        "Convince Mayor Ana to flatly reject any TideLine contract and mobilize a legal challenge.":
            jump chapter12
        "Go to court immediately with the leaked clauses and file an injunction.":
            jump chapter12
        "Negotiate a legally binding community clause with Mayor Ana and trusted counsel, demanding co-ownership.":
            jump chapter13
    return
