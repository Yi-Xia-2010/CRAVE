label chapter12:

    # [Scene: Saltwren Commons | Dawn]

    scene bg ch9_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant jackhammers and the low thrum of diesel generators; gulls call once, twice]
    # play music "music_placeholder"  # [Music: Percussive strings; a frantic undercurrent]
    "You wake to the taste of metal and cold coffee in your mouth, a name—someone’s voice—vibrating through the messages on your phone. The Commons is not quiet anymore. Where yesterday there were seedlings and soft steps, there are trucks idling and surveyors' tape flapping like flags."
    "Your satchel is heavy with flyers you'd printed the night before and with a fatigue that does not belong to this hour. You pull your jacket tighter against the wind; the air smells of brine and fresh-cut plywood, of wet soil overturned and the diesel that comes with promises."
    "You move across the raised beds. A few volunteers are already at work: Rae has her teal hair buried under a hood, hands stained with paint and mud; Tommy presses his forehead into the curve of"
    "his palm, the lines at his eyes deeper. They look up when you approach, and for a moment the place remembers how to breathe."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "Mara. They started the perimeter down at the old promenade by night. Bulldozers. People saying they were told to be ready to move."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Was anyone given notice? Formal relocation terms?"
    "Tommy spits a curse like a line carved into the air. 'Some signed. Others—no. Old Mrs. Chen? She only had—' He looks at you, and the sentence hangs unfinished with salt air."
    show rae_carter at center:
        zoom 0.7

    rae_carter "The feed's blowing up. Footage from the westside—lawyers, placards, people being served papers. They're calling it a 'relocation contract' but the clauses are—"
    "You cannot look at the contract now and not see the red underlining Celeste Park made with that same practiced calm. You feel the memory of the coffee's warmth in the meeting room, of Elias Navarro's hand hovering—so close to the page. The Commons smells like compost and loss."
    hide tomas_tommy_reyes
    hide mara_lin
    hide rae_carter

    scene bg ch9_6b08b4_2 at full_bg
    # [Narration]
    "Your first tasks split like tides: respond to immediate needs—shelter, food, temporary repairs—and carry the stories outward, to the cameras, to the lawyers, to anyone who will listen. There is not enough of you to be everywhere."

    menu:
        "Triage the displaced—get them to shelter now":
            "You drop your flyer and run for the makeshift registry, barking names into a phone and assigning blankets. The Commons fills with a practical, urgent choreography—soup boiled, tarps secured, a crib reassembled out of driftwood."
        "Document and record—collect testimony for legal threads":
            "You pick up a battered notebook and a phone, and you sit with Mrs. Chen as she talks, voice small and trembling. Rae films with a steady hand; each story becomes a pinch of memory to hold against the lawyers at Town Hall."

    # --- merge ---
    "The Commons continues its urgent work; both immediate care and documentation proceed as the day unfolds."
    # [Scene: Various Neighborhoods | Late Morning]

    scene bg ch9_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Shouts rising and receding; a child wailing somewhere; engines idling]
    # play music "music_placeholder"  # [Music: High, nervous violin strokes]
    "You go where the calls are loudest. In some houses, furniture sits stacked irreverently near doorways; in others, there are nothing but boxes and the scent of boiled lemons. You move from doorstep to doorstep—listening, advising,"
    "stitching together a network that was always part of the town but is now stretched thin like a pulley bearing too much."

    "Mrs. Chen" "They told us the trucks were to 'assist with logistical transition.' I thought—"
    show mara_lin at left:
        zoom 0.7

    mara_lin "They promised relocation funds, but the legal language—"
    show tomas_tommy_reyes at right:
        zoom 0.7

    tomas_tommy_reyes "We were supposed to be protected. Fishing permits, landing access—now the promenade has locked gates and signs. They say it's 'stabilization.' Stabilize for who?"

    mara_lin "For investors who don't know how to fish, apparently."
    show rae_carter at center:
        zoom 0.7

    rae_carter "If we don't get these testimonies on record, their lawyers will bury everything in clauses. People are scared to sign anything without counsel."
    "You realize there are dozens of small choices in front of you: which neighborhood to prioritize, who to put on the bus to the temporary housing, which stories to elevate to the cameras. Each choice feels like a vote in a tribunal you don't control."
    # play music "music_placeholder"  # [Music: Crescendo—percussion driving faster]
    # [Scene: Town Hall | Afternoon]
    hide mara_lin
    hide tomas_tommy_reyes
    hide rae_carter

    scene bg ch9_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, a microphone squeal, camera shutters; someone attempting to shout orders]
    # play music "music_placeholder"  # [Music: A chaotic tangle of brass and strings—urgent, unforgiving]
    "When you step into Town Hall the air is thick with expectations. There are banners—some hand-painted, some corporate—swaying on either side of the chamber like two different languages that used to mean the same thing."
    "Celeste Park stands near the dais, immaculate as a lighthouse. She takes in the room with that half-smile that has always made people lean in. Around her, lawyers whisper in clipped cadence. Across from her, Elias Navarro stands with a tablet turned off; his jacket is precise, shoulders taut."
    show celeste_park at left:
        zoom 0.7

    celeste_park "We did what we said. The promenade is secured, funds disbursed. We offered relocation and—"
    show rae_carter at right:
        zoom 0.7

    rae_carter "Relocation under what terms? Under language you vetted with your counsel?"
    "Celeste Park's smile doesn't crack. The cameras love the calm."

    celeste_park "We accompanied every participant through their options. All protocols were observed."
    "You feel the chamber contract around you; trust becomes something you must demonstrate with evidence, with witnesses, with legalese. People shout. A stack of letters slam onto the clerk's desk—grievances, signed and trembling."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "Mara, don't—"
    hide celeste_park
    show mara_lin at left:
        zoom 0.7

    mara_lin "Don't what, Elias? Watch it happen? Help draft the clauses that allowed waivers? You sat in rooms where these words were written."

    elias_navarro "I—' He looks at Celeste Park, at the counsel, then back at you. 'We negotiated restraints, Mara. We built monitoring into the clauses. We have commitments to get people out of immediate harm."

    mara_lin "Commitments that require people to sign away legal agency until 'monitoring' is complete? They can't live on promises."

    elias_navarro "You can't just—' He swallows. 'You can't just refuse funding and expect people to sleep through another winter with roofs full of holes."

    mara_lin "And you think this was the only way? That there wasn't time for binding protections? For enforceable guarantees?"

    elias_navarro "We attempted that. You know we pushed. But Celeste Park had leverage—"
    hide rae_carter
    show celeste_park at right:
        zoom 0.7

    celeste_park "—And we secured what will prevent further loss. We made choices under pressure. You can pick apart the language, Mara, or you can help implement the protections that are already on the table."
    "The room roars and your chest is a drum. People are yelling their own versions of the truth. Someone in the crowd calls out a name—Elias Navarro's name—and the sound is like a thrown stone."
    hide elias_navarro
    show dr_amina_bhatt at center:
        zoom 0.7

    dr_amina_bhatt "From a monitoring perspective, the hybrid approach—' Her words are measured, scientific; they land in a different register. 'We will collect data on Erosion, salinity shifts, displacement impacts. There is rigor to the program."
    "You want to thank her for the rigor and then shake her until she remembers children on stoops. She is caught in the same web: scientist, witness, small shelter for evidence."
    # play music "music_placeholder"  # [Music: Rapid, dissonant chords; heartbeat-thudding rhythm]
    "You step down from the dais and into the press. Reporters push microphones like fishing nets. A camera is shoved inches from your face."

    "Reporter" "Mara Lin—are you calling for legal action?"

    mara_lin "I'm calling for accountability. For temporary housing that doesn't force signatures, for legal aid, for transparency."
    "A group from the westside—people you have been working with—move to the front with folders bulging with papers. A lawyer from the city unfurls a thick binder and places it on the clerk's desk—sued. There are names that will not be erased easily now."

    menu:
        "Name Elias in public as complicit":
            "You take a breath and say his name into the lights. Cameras find his face. For a suspended second, the hope you held about shared work collapses into a single, brittle shard of accusation."
        "Keep accusations to private confrontation":
            "You hold your tongue and frame it as systemic failure. The cameras take the story as an institutional struggle, not as a personal betrayal—Elias remains a figure in the cage of process."

    # --- merge ---
    "The hearing proceeds, and tensions between personal accountability and systemic critique continue to shape public perception."
    # [Scene: Backstage / Hallway Outside Town Hall | Late Afternoon]
    hide mara_lin
    hide celeste_park
    hide dr_amina_bhatt

    scene bg ch9_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muffled roar of the hearing through closed doors; your own breath loud]
    # play music "music_placeholder"  # [Music: A single violin note held until it cracks]
    "You find Elias Navarro in a doorway, his shoulders curved, his jaw working like he's chewing on the taste of coal."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "Mara. I didn't come here to hurt people. I came back because I thought I could help."
    show mara_lin at right:
        zoom 0.7

    mara_lin "You helped build the pathway that pushed them out of their homes and into lawyers' offices."

    elias_navarro "We tried to build a safety net. There's funding now—there's actual money for people who'll be moved. This prevents future deaths."

    mara_lin "At what cost? The people you saved a month from now are the ones who signed their rights away today."

    elias_navarro "You think I like being on that side? I am on both sides, Mara. I can't un-hear what the data says; I can't ignore the models that show more people drown if we do nothing."

    mara_lin "You can choose which models to trust and which voices to center. You've chosen budgets and binding legal language over someone's attic full of photographs."
    "He reaches for you, fingers trembling. There is so much he wants to fix with diagrams and protocols. You are a tangle that he cannot translate into a blueprint."

    elias_navarro "We can still build protections into the project that enforce relocation support. Celeste—"

    mara_lin "Celeste Park has always known how to write the right sentence and the right headline. You had other options, Elias. You could have walked away from clauses that were—' Your voice breaks and you have to steady it against the corridor wall. '—that were designed to be loopholes."

    elias_navarro "If I walked away, those funds might not exist at all. People might've faced winter with no cash, no trucks—no solutions. I'm trying to save people."

    mara_lin "And in saving them, you made them vulnerable to something else."

    elias_navarro "I am trying. I'm so tired of us—' He searches your face as if for a map back to a room where both of you believed the other could be trusted. 'Please. Help me make the protections enforceable. Help me make sure no one is coerced."
    "You want to believe him. You want the relief of reaching across and finding familiar ground. But the corridor is full of echoes—of Mrs. Chen and of single mothers who signed papers under the fluorescent glare—and you can feel the rupture like a draft."

    mara_lin "Help me do that from outside his machine, Elias. Not inside it, where it will be reshaped into what Celeste Park needs it to be."
    "He looks at you—an unreadable blend of shame and calculation—and for a beat you think he will step away from the table. He doesn't."
    # play sound "sfx_placeholder"  # [Sound: A sharp, collective intake of breath from the hearing room like a bell toll]
    # play music "music_placeholder"  # [Music: Climactic brass; tempers and emotions peak]
    # [Scene: Press Venue Outside Town Hall | Early Evening]
    hide elias_navarro
    hide mara_lin

    scene bg ch9_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chants, speakers, a siren wailing in the distance]
    # play music "music_placeholder"  # [Music: A brutal overlay—drums, low brass, a keening violin]
    "Celeste Park gives an interview to a polished anchor. Her words are smooth; the rendering of a sparkling promenade rolls behind her. The camera crops the water to look neat and cooperative."
    show celeste_park at left:
        zoom 0.7

    celeste_park "We have done what the town needed. Stabilization, economic opportunity, and an honest program for relocation and workforce transition."
    "Rae stands across the pavement, paint-splattered and furious, holding up a stencil that reads COMMUNITY, in block letters, thick with paint. People hand out leaflets; lawyers hand out clinic times. The Commons has transformed into a triage hub that is both a war room and a refuge."
    show dr_amina_bhatt at right:
        zoom 0.7

    dr_amina_bhatt "We will publish all monitoring data. We will audit the displacement impacts quarterly. Transparency is necessary."
    "Tommy finds you in the press crush, and for the first time in days his face has that old wind-scorched humor replaced by something hard and set."
    show tomas_tommy_reyes at center:
        zoom 0.7

    tomas_tommy_reyes "They'll put in a promenade and call it resilience. They'll hire outsiders and call it jobs. But who owns the harbor? Who owns the way we come home?"
    hide celeste_park
    show mara_lin at left:
        zoom 0.7

    mara_lin "Nobody owns the harbor, Tommy. The harbor owns us all."
    "A man in a suit with a glossy paper badge—one of Celeste Park's PR—tries to steer a camera away from a grieving father who is holding photos of a home now in the path of the new road."

    "PR Man" "We encourage everyone to speak with our community liaison for assistance."
    "Grief and slogans mingle. Your throat is raw from speaking. The town you know has been translated into terms and clauses and renders; people have been translated into bullet points."
    # play music "music_placeholder"  # [Music: A shrill rise and then a snap—the moment of breakdown]
    # [Scene: Saltwren Commons | Dusk]
    hide dr_amina_bhatt
    hide tomas_tommy_reyes
    hide mara_lin

    scene bg ch9_6b08b4_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet, the distant dull beat of the generators settling; someone hums a tune that used to be a lullaby]
    # play music "music_placeholder"  # [Music: Sparse piano; a minor key that doesn't resolve]
    "You come back to the Commons and find that the community's muscle has not stopped moving. Tents are pitched, tarps are patched, lists taped to a weathered board. The work is steady and humane in a way the official documents were not."
    "Rae sets up a small projection of images—faces, houses, smudged clay models of the replaced landscape—and people stay to watch in silence. Tommy carves a bench from driftwood and offers it to you; you sit together"
    "and the ocean makes the same ancient sound against the shoreline: indifferent, patient, a machine older than policy."
    "Elias Navarro appears at the edge of the light, not quite in the circle. He carries a stack of papers—amendments he'd been trying to push through, signatures he'd gathered from Dr. Amina and a few sympathetic council members."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "I… I got them to put enforceable language on temporary relocation. It's a start."
    show mara_lin at right:
        zoom 0.7

    mara_lin "A start that comes after people were moved. A start that recognizes harm but doesn't undo the harm."

    elias_navarro "I know. I keep thinking—if we had done more earlier. If I'd—"

    mara_lin "We keep making ifs, Elias. It gets tiring."
    "He takes a breath, like he's double-checking the phrase he needs to say."

    elias_navarro "Mara, I thought—maybe we could be partial to each other's methods. I thought we could keep the plan honest from the inside."
    "You look at him. The fatigue on his face is the same as yours, but the lines are drawn differently: his are the lines of someone who tries to translate grief into blueprints; yours are the map of someone who has carried people through storms."

    mara_lin "Maybe some bridges can't be rebuilt once the tide came through. Maybe we can only build new ones where the old ones are washed clean."
    "He reaches for your hand as if to test whether you'll rise to the same bridge. You pull your hand back."
    "There is a quiet that feels like surrender. Not a triumph, not a resolution—only the recognition that something fundamental has shifted."
    hide elias_navarro
    hide mara_lin

    scene bg ch9_6b08b4_8 at full_bg
    # [Narration]
    "You stay to coordinate the night shelters. You sign forms with a pen that smudges. You measure rations by the light falling on people's faces. You hold a child's cold hand and tell her a story that is the small thing you can still give."
    "The town moves forward in a way that will leave scars. The promenade will be built. There will be jobs, new lights, and a safer mainwalk for some. There will also be empty houses, lawsuits, and a community's sense of ownership eroded like the shoreline itself."
    "You find a quiet corner on the Rooftop Garden of the Old Mill later that night. The wind strips your hair across your face; salt spray tastes like iron. The rooftop's lanterns are dim, and the"
    "view of the newly framed promenade glows out of the darkness—an arc of polite light where people will walk and photograph the sea that used to belong to everyone in a different way."
    "You think of your sibling, the storm that took them, and the urgency that has lived in your hands since. You think of Elias Navarro and his careful equations and of Celeste Park and her smooth"
    "certainty. You have won some small victories—legal language, monitoring, money moved into accounts—but the cost has been a skyline of loss."
    "Rae finds you, sits without asking. She holds a roll of paper and unrolls a stencil she's been saving. On it, in thick block letters, it reads: REMEMBER."
    show rae_carter at left:
        zoom 0.7

    rae_carter "We keep the lists. We don't let them vanish behind ribbon-cuttings."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We keep the lists."
    "She looks at you, eyes fierce and aching. 'What now?'"

    mara_lin "Then we do what we do best. We rebuild where we can. We shelter who needs shelter. We pressure the clauses until they mean what they say. We don't stop telling the stories."
    "You stand, and the action is ordinary and immense—collecting flashlights, handing out soup, assigning watch shifts. The night is a work shift. The arousal—the panic, the fury, the frantic logistics—recedes into a worn, relentless determination. It's not triumph. It is survival braided with grief."
    hide rae_carter
    hide mara_lin

    scene bg ch9_6b08b4_9 at full_bg
    # play music "music_placeholder"  # [Music: A low, unresolved chord; the sound of wind entwined with the distant surf]
    "For a long while you let the tide of people carry you: making lists, distributing supplies, answering calls from a lawyer, sitting with a mother who cannot sleep. The community is restless but not broken. You"
    "are not untouched. You are changed—hardened not into someone cruel, but into someone who knows too well the anatomy of compromise."
    "You lay down on the rooftop boards after the night shift, your hands still smelling of soup and ink. The town hums below. You close your eyes on the plans you carried into and out of"
    "rooms, on the faces of those who will never quite trust the process again, and on the man who tried to hold two truths at once."
    "There is no neat promise in your chest. There is only a slow, steady resolve that the work continues."

    scene bg ch9_6b08b4_10 at full_bg
    # play music "music_placeholder"  # [Music: The soundtrack holds an unresolved minor chord]
    # [Narration]
    "You will not leave Solhaven. You will keep making lists, filling forms, stitching people into safety where you can. You will love in a way that is cautious now, marked by the memory of how easily"
    "hope can be co-opted into policy. You will keep fighting for the wetlands, for the gardens, for the little rituals that keep people grounded."
    "There is sorrow here—sharp, whole, and real. There is also a stubborn, aching care that will not let the Commons fall silent."

    scene bg ch9_6b08b4_11 at full_bg
    "THE END"
    # [GAME END]
    return
