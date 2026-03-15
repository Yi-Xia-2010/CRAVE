label chapter8:

    # [Scene: City Hall Plaza | Morning — the day after Tamiko's drop]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The plaza hums—phones buzzing, distant chants; a newsroom crawl beeps under it all]
    # play music "music_placeholder"  # [Music: Tense BGM, staccato strings and a low synth pulse]
    "The feeds woke you before your eyes did."
    "Your phone vibrates in the pocket of your jacket—an insistent, small animal. Notifications stack: shares, DMs, a clip from Tamiko titled “Unmasked: Vale Procurement,” a dozen hashtags wound around it like barbs. You thumb it open"
    "and the footage hits: wide-shot glamour of Cassian at a podium, then brutal close-ups of stamped, routed contracts and a ledger of shell companies. Tamiko's camera lingers on the ink, on signatures half-hidden behind corporate stamps."
    "You taste iron—wet fear—but there's also a raw, uncanny exhilaration. The plaza outside your apartment windows is already a nation of faces and placards; your chest tightens with the recognition that this is bigger than a meeting room now. It is noise and consequence and momentum."
    "You tighten your coral scarf and step into the street."

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A rising swell of voices in the distance; the crowd is assembling]
    # play music "music_placeholder"  # [Music: Percussive rhythm increases]

    menu:
        "Call Elias immediately":
            "You hit dial; his voicemail picks up. You leave it brief—'We need to talk. Now.' The screen shows him tagged in hundreds of replies; you see his name under a photo of him at your side during last night’s greenhouse meeting."
        "Text Tamiko for raw files":
            "You send a terse message asking for the uncompressed footage and timestamps. A single read-receipt blinks back—Tamiko's reply: 'On my way to plaza. Bring Lina. Wear boots.'"

    # --- merge ---
    "Continue to City Hall Plaza | Late Morning"
    # [Scene: City Hall Plaza | Late Morning — crowd growing, press tents popping up like dark mushrooms]

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chanting, the squeal of bicycle wheels, camera shutters; a journalist shouts a question]
    # play music "music_placeholder"  # [Music: Tense BGM persists, strings layering into higher intervals]
    "Lina finds you before you find her—paint on her palms, rain boots slapping the plaza tiles, grin missing but voice steady. Tamiko is already live, framing her shots like a vendetta: close-ups of cheques, slow pans of contract numbers, a headline superimposed in Tamiko's trademark font."
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "Everyone—this is not a rumor. This is paper. Follow the links. Share the names."
    "You move through the crowd, your notebook damp against your ribs. Dr. Arun arrives with a stack of charts and a portable projector, breath fogging the morning air. He sets up with the efficient clumsiness of"
    "someone used to teaching people how to read data, not how to argue against power."
    show dr_arun_patel at right:
        zoom 0.7

    dr_arun_patel "What Tamiko found correlates with procurement timelines—fast-tracked awards without the red flags we use to catch conflicts. If they proceed, we’ll see maladaptive structures cemented in place. Buildings that don't account for sediment flux, seawalls that redirect flooding to lower-income stretches—"
    show mira_santos at center:
        zoom 0.7

    mira_santos "—and that’s exactly what we can't let them do. Not here."

    dr_arun_patel "The science supports the injunction proceedings. But science doesn't win headlines—people do."

    tamiko_sato "Then let's give the people a story they can't ignore."

    "The feeds crackle; your name is being said on air. Somewhere, a reporter leans into a mic and asks the question that will run through the day" "Ms. Santos, so the city halts construction—what is your plan now?"
    "You can feel a dozen narratives waiting for you to pick one. The viral footage is an accusation that sparked this temporary freeze; the freeze is a fragile thing, paper-thin and reactive. Cassian's rebuttal—slick, rehearsed—arrives on the municipal screens like a counter-tide."
    hide tamiko_sato
    hide dr_arun_patel
    hide mira_santos

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cassian's voice, smooth and controlled, amplifies; the crowd murmurs]
    # play music "music_placeholder"  # [Music: A single low chord underlines his words, then a sharper, dissonant motif]
    show cassian_vale at left:
        zoom 0.7

    cassian_vale "The Vale Consortium has always acted in Verdante's best interest. Any claims tying us to shell entities are politically motivated. We have announced donations to community resilience funds; our intent is to help. We welcome oversight and transparency."
    "A ripple of applause comes from somewhere in the crowd—an audience planted in his PR feed, you suspect. The donated funds headlineizens peace, but your chest clenches as Tamiko's footage showed contracts routed through accounts that don't speak of philanthropy; they speak of profit funnels."
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "He buys optics faster than we can breathe."
    show mira_santos at center:
        zoom 0.7

    mira_santos "He buys them to slow our breath."
    "Elias Moreno appears at the edge of the crowd. He is in a municipal vest now—public, visible. The cameras find him and tack his face with yours, two individuals in a sea of many. For a"
    "moment, his sea-gray eyes find you; there is something like urgency there, and a vulnerability that is usually masked by policymaker composure."
    hide cassian_vale
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "I support the freeze. Transparency should happen. People deserve to know who is writing the checks—and why."

    mira_santos "Are you sure you want to be out here?"

    elias_moreno "I'm sure of the facts. I'm not sure of Cassian's next move."
    "You can hear the subtext: his loyalty to policy, his need to be seen as competent and on the right side of history, the fear of being complicit. His presence steadies the crowd; his words make"
    "headlines. But Cassian's machine is already moving—donations, denials, and a slow drip of counter-accusations designed to muddle public attention."

    menu:
        "Step up to the podium and speak now":
            "You climb the steps, breath caught and then disciplined into words. The crowd leans in; you hand Tamiko a marked timestamp. Your voice cuts through static: 'This is about our homes.' The applause is raw, but you feel every eye like a weighing scale."
        "Let Elias take the microphone first":
            "You stay planted as Elias steps forward. He speaks with measured cadence, a planner's logic braided with moral commitment. The crowd listens—and you notice some nods shift to him as if searching for an anchor. Afterwards, he squeezes your hand briefly, an electric, private touch before returning to the press."

    # --- merge ---
    "Continue to Emergency Oversight Hearing"
    # [Scene: City Hall Plaza — Afternoon | Emergency Oversight Hearing announced]
    hide lina_cortez
    hide mira_santos
    hide elias_moreno

    scene bg ch7_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Legal language—gavel knock sampled into live video—murmurs of 'injunction,' 'procurement irregularities']
    # play music "music_placeholder"  # [Music: Tense BGM intensifies into a driving rhythm]
    "The city's emergency oversight hearing feels like a theater of law: measured statements, counsel in navy suits, and the low mechanical whir of livestream drones. The judge grants a temporary injunction—the construction is frozen. For a"
    "breath, the plaza erupts like a body rediscovering its lungs: cheers, ululating whistles, Tamiko laughing into her camera like it's a victory bell."
    "But the chest-tightening returns quick. Dr. Arun points out, with a heavy hand on your shoulder, that the freeze reroutes municipal cash: pool funds are diverted to legal contingencies and the oversight process. The small, neighborhood-scale"
    "projects you fought for—elevating the community pier, subsidized home retrofits, storm-drain pumps—are now threatened in the budget shuffle."
    show dr_arun_patel at left:
        zoom 0.7

    dr_arun_patel "Litigation buys scrutiny, which is necessary. But scrutiny costs money and time. The interim is where communities get hollowed out."
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "They're already calling families with relocation packages. 'Safety first,' they say. But safety as a one-way street—out of here. Half of Mali's block took the offer yesterday. They couldn't sleep."
    show mira_santos at center:
        zoom 0.7

    mira_santos "Fear is an engine. We set it racing when we pulled on the thread."

    lina_cortez "We pulled it because it was tied to a liar."
    hide dr_arun_patel
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "This is the right push. But right now… right now people are hungry and anxious."
    "Your stomach drops—images colliding: Tamiko's footage going viral, then the same screens running glossy campaign shots of Cassian giving a ribbon to a playground in a different district. Your victory feels both enormous and painfully partial; the legal pause that smells like justice also tastes like collateral."
    hide lina_cortez
    hide mira_santos
    hide tamiko_sato

    scene bg ch7_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversations, the occasional staccato sob]
    # play music "music_placeholder"  # [Music: Strings fray into unresolved intervals]
    "You walk among them, listening. A woman you know from the Row presses a folded eviction notice into your hand—it's a relocation offer disguised as care. Her eyes are raw, and her voice is a brittle whisper."

    "Resident" "They say they'll cover moving costs. They call it 'temporary relocation.' They say it's for our safety. What do I do, Mira? My arthritis—my son—"
    show mira_santos at left:
        zoom 0.7

    mira_santos "We fight for you to stay. We push for protections. But I need time and—"
    # [Scene: Behind the podium, a quiet corridor | Late Afternoon]
    hide mira_santos

    scene bg ch7_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant chorus of the crowd; the sound of a camera shutter—Tamiko, always watching]
    # play music "music_placeholder"  # [Music: Tense BGM softens into a taut, intimate motif]
    "Elias Moreno looks tired in a way that reaches past his curated public face. Up-close, the mapping of practical concern is visible in the way he rubs his temple, in the slight catch to his breath. He steps closer; the proximity is both a solace and an accusation."
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "I didn't plan this. I thought oversight would buy time to build right. I didn't expect the money to be pulled like this."
    show mira_santos at right:
        zoom 0.7

    mira_santos "You didn't expect a man like Cassian to play chess with people's homes as pawns."

    elias_moreno "Maybe I expected systems to hold. I'm starting to see how naive that was."

    mira_santos "So what do we do? Because the people who can leave are leaving. The people who can be silenced are getting offers at their doors."

    elias_moreno "We can do several things. We can push for immediate protections—temporary seawalls, emergency grants, the works. Or we can double down and try to dismantle every contract—drag them through the courts until the consortium collapses. Or we can negotiate—try to build oversight into whatever settlement they offer. None of them are clean."
    "His voice drops at the last word—'clean'—and you feel its weight: no solution here is pure. Each path is a calculus of sacrifice."

    mira_santos "If we push for protections now, we buy people time. But then the legal case might weaken. If we go full legal, we risk losing the interim safety. If we negotiate, we risk a velvet compromise that looks like progress but leaves holes."

    elias_moreno "And there's politics. Cabinet members whisper about reputations; contractors already scuttle to hide ledgers. The moment we choose a lane, the city will bend to it."
    "You look past him at the crowd: Tamiko on a small rise, livestreaming, her expression feral with adrenaline; Lina rallying a group into a planning circle; Dr. Arun speaking to a reporter with a flat, exhausted clarity. Your movement has moved mountains and scattered pebbles."
    # [Dialogue continues—multi-turn, voices frayed and intimate]

    mira_santos "I feel the ledger my grandmother left me. The sandbags she sewed at midnight. This isn't abstract."

    elias_moreno "I know. I grew up with engineers who believed in fixable problems. I thought that was enough. I'm realizing now that fixing the problem isn't only about structures—it's about people having seats at the table."

    mira_santos "Do you think Cassian will ever willingly give seats to people who will slow his timeline?"

    elias_moreno "He'll give what looks like concession if it keeps the project moving. That's the difficulty. We need vigilance and leverage."

    mira_santos "Leverage."

    elias_moreno "I want to help you. I don't want to be the city planner who stands on the right side of a moral argument but on the wrong side of the people."
    "You study his face—there is truth in it, and there is also the structural force of his training, impatient with messy delay. For a moment, the two of you are simply two people on a municipal"
    "ledge—lungs heaving with the city's air, not knowing whether the next breath will be relief or rival."
    # play sound "sfx_placeholder"  # [Sound: A sudden cheer from the plaza snaps you both back; Tamiko's feed just posted new documents, and the comments flood]
    # play music "music_placeholder"  # [Music: Tense BGM swells toward a climax]
    "The strain in your shoulders is a physical thing now. The viral drop bought a freeze, but it also tore open a thousand small fissures: funds redirected, families uprooted, the slow erosion of coalition trust. You"
    "are at a narrow, exposed decision-point—the kind that will define who you are to the people you love and to the community that birthed you."
    "You think of the ledger again, your grandmother's hands sewing at the edge of the tide. You think of Elias's tentative commitment and Cassian's practiced smile. You think of Lina's bright boots, of Tamiko's camera lens juddering with righteous urgency, of Dr. Arun's charts that insist on long-term thinking."
    "The city waits like a held breath."
    # play music "music_placeholder"  # [Music: Tense BGM reaches its most intense, refusing resolution]
    hide elias_moreno
    hide mira_santos

    scene bg ch7_453e40_8 at full_bg
    "You know there are three clear pathways ahead. Each is dangerous in its own way."

    menu:
        "Push for immediate neighborhood protections while litigation proceeds.":
            jump chapter9
        "Double down on the legal case to dismantle Vale’s contracts entirely.":
            jump chapter11
        "Negotiate a public settlement with built-in oversight and community seats on project boards.":
            jump chapter11
    return
