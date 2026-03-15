label chapter12:

    # [Scene: City Hall Glass Atrium | Afternoon]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, mournful strings; careful, patient percussion]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversation, camera shutters, the distant clack of a news van door]
    "You leave the podium with your throat raw from the questions you chose to ask aloud. The council chamber feels like a bell with a crack in it — sound spilling, not contained. Reporters cluster at"
    "the doors like cormorants; their microphones catch every pause and toss it back louder. Jun stands where he always stands in public life — precise, composed — but the tightness around his mouth is new and"
    "human. Behind him, the council votes to open audits. Funding for the municipal construction is frozen pending review."
    "You can taste copper and salt on your tongue; the atrium smells of wet coats and old coffee. People turn toward you with faces you recognize and faces you don't. Some are hopeful—eyes bright with the"
    "satisfaction of seeing a wrong named. Others are already braced, calculating the next ledger entry that might cost them a roof. You press your palm against your journal in your pocket as if you can steady"
    "the damp spine inside; the compass pendant brushes your sternum like a second heartbeat."
    show jun_park at left:
        zoom 0.7

    jun_park "We should examine this thoroughly. Oversight will be granted. We will cooperate with the auditors."
    "You watch his hands, the way he folds compassion into procedural language. There is a relief in the room when he says oversight, and a recoil too—the auditors arrive like a tide that could pull everything from the sand."
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "You did as we taught, ledger and salt,' she says, voice steady as a tide-line. 'You named the shape of the fear. People will follow when something is named."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "We named it, but naming it doesn't rebuild what was taken from us."

    rosa_alvarez "No. But it makes the taking visible."

    menu:
        "Answer the reporter's question about the freezing of funds":
            "You step up, your voice even. 'We requested accountability — because secrecy costs lives.' The microphone picks up the sentence and it becomes a small blade in the air."
        "Turn away and find Elias in the crowd":
            "You move through the cluster of bodies and find Elias by the back exit. He looks at you as if worried the data will stop being a buffer between you and the world. He reaches for your hand; his thumb lifts the skin, steadying you."

    # --- merge ---
    "Continue with subsequent narration."
    "The audit announcement does what audits always do: it reveals flaws, slows momentum. Contractors hesitate. Shipment manifests are re-opened. Supply lines are re-inspected. The hybrid plan you helped propose — the living reefs that would absorb"
    "wave energy and feed habitat — sits in a gray bureaucratic limbo. Some of the community's volunteer labor continues, quietly, while municipal crews step back."
    hide jun_park
    show elias_navin at left:
        zoom 0.7

    elias_navin "Mara—' (he falters at your name, as if that small syllable is an instrument that could fracture) 'We ran more models this morning. The scaffolding on the westward break is underbuilt for the torque we projected with the updated cyclone routing. If—if the funding holds, we could shore up the anchoring within days."

    mara_kestrel "If the funding holds,' you repeat, but the words already carry the new, bureaucratic cadence. 'We pushed for public transparency because we couldn't watch the supply manifests walk away. We couldn't let volunteers shoulder blame if things failed."

    elias_navin "I know. I—I'm with you. But I'm thinking of those anchors. The sensors show a shift in the Gulf's eddy. It's worse than the forecast said this morning."

    mara_kestrel "Then we need to push people to move. Evacuations. Prioritize the elder houses along Meridian and the Basin's low end."

    elias_navin "You'll take Meridian. I'll coordinate the sensors and the volunteers on the north moor. Rosa and Ivy will handle the Basin's sheltering plan."
    "The plan is a litany of small actions — a map folded into a fist. The atrium seems to compress around it."
    # [Scene: Partially Built Barriers | Coastline — Two Weeks Later | Late Afternoon]
    hide rosa_alvarez
    hide mara_kestrel
    hide elias_navin

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind gusting through empty pylons; the distant clatter of half-built panels]
    # play music "music_placeholder"  # [Music: Low brass; a slow, ominous refrain]
    # play sound "sfx_placeholder"  # [Sound: An emergency radio crackles with municipal updates]
    "Weeks of audit hearings have yielded invoices and subpoenas, but they are also time. Time that the tide will take in its own rhythm. The city bureaucracy moves with the measured certainty of a ship in fog: slow enough to avoid ripples, too slow to outrun a storm."
    "You walk the line of the partially built barriers with a group of volunteers. Salt collects in the stitches of your jacket and on the rubber boots of the people who spend their days between sea"
    "and land. The breakwater's living modules are stacked but not anchored. Mussel cages sit boxed, waiting for technicians who cannot sign off under the auditor's scrutiny. The empty rigging sighs."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "We made sandwiches, organizer! You want coffee or tea? We can cart out the gardeners' supply too."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Tea. And the tarp. Get the elderly from the corner flats on the shelter roster now. We can't wait for another forecast."

    "Volunteer Leader" "Evacuation routes are packed, but the north ferry—it's been held up by last week's embargo. We might have fewer boats."

    mara_kestrel "Work with what we have. Churches, school vans, the Basin's intake pumps. Prioritize mobility-limited residents first."
    show elias_navin at center:
        zoom 0.7

    elias_navin "The unmoored modules will change the current direction if we don't anchor them at the seaward seam."

    mara_kestrel "How long to secure them with volunteers?"

    elias_navin "Not long — three crews, bustling, but we need a certified dive team for the deeper anchors. I'm trying to call in floats from the university. But the auditors have frozen certs access from municipal teams — it's a chain, and the chain keeps taut."

    mara_kestrel "So we get creative."

    elias_navin "We can attempt temporary anchoring. It's risky, but the calculations show it's better than nothing."

    mara_kestrel "Do it."

    elias_navin "We do it together. Your call."

    menu:
        "Assign the volunteers to temporary anchoring despite inspector risk":
            "You beat your palm once against the module. 'We have to keep people safe. If the certified teams can't get here, we'll learn the temporary method. Rosa will sign off on community oversight.' Volunteers exchange looks — fear braided with resolve."
        "Delay anchoring and focus on evacuation routes only":
            "You swallow. 'We focus on getting everyone off the low lines first.' Elias's jaw tightens. 'If the barriers fail, the currents could turn the north channels into funnels. We might not be fast enough.' He doesn't say it aloud, but his hands tighten around the wrench."

    # --- merge ---
    "Continue with subsequent narration."
    "You choose, and the city responds with a choked mixture of courage and bureaucratic reprisal. Letters from the auditor's office arrive like rain; one volunteer group receives a cease-and-desist, another gets a fine. The hybrid plan"
    "is now not only a policy conversation but a moral ledger that people keep in the margins of their wallets."
    # [Scene: The Beacon & Coastline | Cyclone Night]
    hide ivy_kestrel
    hide mara_kestrel
    hide elias_navin

    scene bg ch12_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Rapid strings, distant percussion; then sudden silence as wind swallows sound]
    # play sound "sfx_placeholder"  # [Sound: Howling wind, the roar of water, splintering wood, and distant, fractured cries]
    "The cyclone doesn't ask permission of audits or of council votes. It comes as a law of physics, a grammar that refuses to be mediated. The partially built defenses hold in pieces — a module here,"
    "a tied-off net there. But the gaps are spaces for water to remember old routes."
    "You stand at the edge of the serving road with a radio against your ear. Your hands are numb. The rain drums at the collar of your jacket like a heartbeat trying to communicate. Evacuation lanes"
    "are clogged. The ferries that once carried children to dry land are stalled by broken mooring lines and bureaucratic red tape."

    "Radio Voice" "Meridian block reporting—flooding at the first floor. Medical triage requested. Old Beacon's south face compromised. South entrance closed."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Send the backup convoy through Gable's way. Route firefighters to Meridian north entrance. Keep the Basin shelter open—do not let people—"
    show elias_navin at right:
        zoom 0.7

    elias_navin "The current's changing. The cyclone is shearing off the outer modules. It's carving a channel. The water is heading straight—"
    # play sound "sfx_placeholder"  # [Sound: A deep, catastrophic cracking. The Old Beacon groans. Stone that has stood for a century gives up a memory and falls into the surf with a sound like a great bell being struck and then muted forever.]
    "The partially built barriers, the half-signed manifests, the auditors' frozen pens—none of it can keep the water from its terrible, particular course. The cyclone funnels currents through neighborhoods that had thought themselves above such violence. Houses"
    "flood. The shelter at the Basin overflows. People are swept from stairways; belongings streamed like small, soggy bodies down newly formed canals."
    "You run. Every motion is grit and salt and the sick sense that you are too slow. Volunteers you rallied are caught mid-task. Some you drag free. Others you cannot reach. The radio carries names you know, addresses you know, and then silence where there once was a voice."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "They called me—no. The Basin—"

    mara_kestrel "Where—where is Ivy?"

    rosa_alvarez "She is with the children at the school. They were moving them. She—' Her hand goes to the braided reeds in her hair and squeezes them as if to keep memory from unravelling. 'We don't know."
    "In the hours that follow, the tally comes in the hush between rescue teams. It is smaller than your worst private reckonings and larger than any ledger you keep. Some bodies are recovered. Some are not."
    "Families sit in the wet, holding each other like small boats. The news cycles through footage of the Beacon's fall on repeat — the image becomes a symbol that is both true and inadequate."
    # [Scene: Makeshift Memorial at the Strand | Two Weeks After]
    hide mara_kestrel
    hide elias_navin
    hide rosa_alvarez

    scene bg ch12_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Solo piano, slow and resonant]
    # play sound "sfx_placeholder"  # [Sound: The low susurrus of the tide; muffled conversation; a distant gull]
    "The city has rearranged itself around loss. The audits continue, and a public inquiry is convened that culminates in a painfully honest set of findings. The exposure you forced can't be undone. Contracts are amended, leaders"
    "are sanctioned, and a new oversight board is created with teeth and community seats. Jun appears at the memorial, his coat still buttoned against the salt air, his jaw fissured with the work of apology."
    show jun_park at left:
        zoom 0.7

    jun_park "I thought the numbers could be trusted alone,' he says. 'I thought I could make the hard choices without asking if they were right. I failed to see what you warned me of, and for that —' He stops, and the stop is a confession that the city cannot put on an auditor's ledger. 'I will not ask forgiveness yet. I will make reparations, and I will stand accountable for what was lost."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "We needed transparency because secrecy costs lives,' you say. 'We needed the community at the center because we are the ones who live with these choices."

    jun_park "You were right about the names. The rest — the costs — are mine to bear. I will resign my seat on the committee. I will help rebuild the process with Rosa and with the community board."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "Words and resignation are a start. What we need is repair—safe corridors, equitable compensation, a mandated hybrid plan that can't be frozen by a single vote."
    hide jun_park
    show elias_navin at left:
        zoom 0.7

    elias_navin "We will rebuild,' he says. 'Not just structures. Systems. We'll make the models that survived talk to the people who rebuild them. And we'll build in redundancies — social ones, too."

    mara_kestrel "Do you think this—' (the question splinters) 'Do you think what we did mattered enough to justify it?"

    elias_navin "I don't know,' he replies. 'Some lives were saved because a route was opened earlier. Others were lost because the chain didn't hold. But hiding what happened would only make more deaths inevitable. We made a public choice; now we have to live with the consequences."

    mara_kestrel "I keep counting blame like beads. Could I have done something else? Could I have kept the meeting closed and fixed the anchors myself?"

    elias_navin "If you'd done that, the manifests might have been altered and the staff diverted. People who rely on public records would have had their recourse taken away. The audits hurt the momentum, but they also made things visible. The visibility is what will prevent future denial."

    mara_kestrel "Visibility doesn't stop the sea. It only makes us responsible."

    elias_navin "Responsibility is what binds us. It hurts, but it also keeps us from trying the same mistake,"
    "The memorial does not make the dead return. It rearranges the living. The hybrid model you pushed for is enacted in a new, cautious form with layered oversight and guaranteed community management. Funding is redirected into"
    "rapid-response anchoring teams, and grassroots training programs are created to teach temporary anchoring techniques that had not been certified before. Rosa chairs a cultural committee that ensures relocations—where necessary—are handled with cultural sensitivity and compensation."
    "Jun keeps his word to step down from the decisive committees and to participate in oversight and reparative measures. He does not appear cleansed; he appears altered, younger in his face where judgment has cracked open into accountability."
    "Mara Kestrel and Elias Navin stand at the Strand one evening, the lamp glow painting your skin the color of bruised pear. His hand finds yours as if there were no other place it could rest."

    mara_kestrel "Will you stay?"

    elias_navin "Where?"

    mara_kestrel "Here. With me. Not just the projects. The rebuilding. The meetings that don't end at a ledger."

    elias_navin "I thought I'd be running models and leaving cities in better shape. This is harder and better and more human. I didn't plan to fall in love with the project lead.' (He meets your eyes.) 'But I am here. If you let me be."

    mara_kestrel "Then stay."
    "Staying does not mean the ache is gone. It means each morning you wake to a city that remembers both its pride and its losses. You keep a list now, in the margin of your journal,"
    "of things to repair: social scaffolds, flood-slowing marshes, guaranteed seats on boards for elders and fishermen, trained rapid-anchor teams, and memorial funds for those whose names were taken. The list is long. It is lit by"
    "small decisions you can manage."
    "The sea keeps making its arguments in waves. The Beacon will not forget the night it fell, nor will the city. The moral victory of exposure is a lamp that illuminates cold truths — truths that"
    "in the short term sharpen the dangers we could not prevent. In the longer term, they make it harder for secrecy to grow back like mold."
    hide mara_kestrel
    hide rosa_alvarez
    hide elias_navin

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Low, understated strings; a single sustained cello note]
    "You stand at the Strand with Elias at your side and Rosa across from you, and you all look toward the horizon where work remains. You think of the people you could not carry, of the"
    "decisions that cost them their homes and their breath. You also see hands — many hands — building something else where ruin had been planned."

    "You are tired. The journal in your pocket is damp with salt and grief, but you open it and write" "We are responsible."

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Fades to a melancholic but steady chord]

    scene bg ch12_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
