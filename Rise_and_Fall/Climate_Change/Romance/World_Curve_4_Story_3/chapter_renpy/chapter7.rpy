label chapter7:

    # [Scene: Tide Lab (Converted Research Ferry) | Pre-Dawn Rain]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, deliberate piano; a rising undercurrent of strings]
    # play sound "sfx_placeholder"  # [Sound: Quiet hum of pumps, distant gulls, rain drumming on metal]
    "You wake inside the decision you already made. It has a weight to it—less like a stone and more like a tide that will reshape everything it touches. The choice to confront NovaSeis isn't theatrical; it"
    "is a series of small, stubborn acts: printing, cross-checking, asking uncomfortable questions until the seams show."
    "You run your thumb along a wet margin of your notebook. Salt and ink mingle beneath your skin. The pages smell like sea—brine and old paper—and the smell steadies you. Around you, the Tide Lab breathes:"
    "fans whisper, a spectrometer clicks, and the projector throws slow-moving sediment models across a bulkhead."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We have a timeline. We have anomalies in their wave-modelling outputs and holes in the sediment retention data. If we sequence this right, it reads as pattern, not paranoia."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Pattern, not paranoia,' you repeat, tasting the phrase as if it were a knot you can untie. 'We need to show not only the numbers but the people those numbers erase."
    "Professor Asha looks at you the way she looks at a problem set—calm, exacting, and quietly proud."

    professor_asha_rao "Then we start with coastal transects and with testimony. The dossier should marry the geology and the memory."
    "Maya moves between a printer and a rack of leaflets, fingers stained with ink and tide-mud. She hums under her breath—an arranging of energy more like percussion than song."
    show maya_ellis at center:
        zoom 0.7

    maya_ellis "People will show if they think someone finally understands what gets lost when 'efficiency' is the only measure. They need to hear their story reflected back in hard paper."
    "Jonah Reyes stands near the rail, jacket zipped, camera strap across his chest like a talisman. He hasn't said much. His municipal connections are a bargaining chip you didn't know you would have to spend; he watches every face in the lab with an engineer's economy of movement."
    hide professor_asha_rao
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "I can give you shots from the southern breakwater—before and after NovaSeis installed their panels. Field notes, timestamps. But if this goes public, it draws lines that might make my office... uncomfortable."
    "You turn to him. Rain throws silver streaks across his hair; his eyes are patient and guarded."

    mara_ellis "We don't need sacrifice theatrics, Jonah. We need truth. If your notes make the case tighter, they save us from being dismissed as sentimental."
    "Jonah Reyes's jaw tightens. He rubs his thumb over the woven ring on his right thumb."

    jonah_reyes "I want to help. But know I won't be a prop. If this starts a fire, I'll stand with the community, not with any department that tries to quiet it."

    mara_ellis "Then stand. Help us light what needs to be seen."
    "The exchange is not neat; it never is. Jonah Reyes shifts from guarded to wry in a breath."

    jonah_reyes "Practical lighting then. No torches. Just evidence with good exposure."

    menu:
        "Emphasize the community testimony first":
            "You gather Maya's leaflets and scribble a cover letter: 'This is about what happens when living things are treated like variables.' The lab smells like ink and resolve."
        "Lead with the quantitative anomalies":
            "You stack the graphs in front of Asha and lay your pen along a jagged line. Numbers sharpen conversation. The room listens differently when the spikes are framed as risk, not rumor."

    # --- merge ---
    "The group continues assembling materials; evidence and testimony begin to take shape."
    "Professor Asha pulls up an overlay on the tablet—sites in two other cities where NovaSeis systems were installed. The overlay blurs; a cursor highlights a radius where shoreline retreat accelerated after intervention."
    hide mara_ellis
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "See here. Short-term gain, long-term export of sediment. Proprietary designs that don't account for littoral transport. If we can pair this with local erosion markers and persistent testimonials—"

    maya_ellis "—then the narrative can't be gaslighted away by glossy ads."
    "You stack a set of printed comparisons, the pages slightly curled from the humidity. Jonah Reyes feeds you a flash drive, the metal cool in your palm."

    jonah_reyes "These are raw. No filters. Photographs, timestamps, notes. One set is from last March, another from December. You can reproduce the hydrology models with these."
    hide maya_ellis
    show mara_ellis at center:
        zoom 0.7

    mara_ellis "Good. We need reproducible. We need threads more than accusations."

    professor_asha_rao "I'll annotate the dataset. We should also file a freedom-of-information request for their environmental impact statements and procurement notes."
    hide jonah_reyes
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "And I'll call the neighborhood groups. If the Promenade crowd shows, the council will have to act."
    "You feel the first crest of momentum—like a swell building in your chest. It is careful, but it exists. You have allies who carry different kinds of courage: Asha's academic steadiness, Maya's civic fire, Jonah Reyes's"
    "reluctant tether to the city, and your stubborn unwillingness to let a corporation write the coastline into forgetting."
    # [Scene: Promenade (Half-Submerged Boardwalk) | Late Morning]
    hide professor_asha_rao
    hide mara_ellis
    hide maya_ellis

    scene bg ch7_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Hopeful strings swell; a rhythmic underbeat mirrors the march of dozens]
    # play sound "sfx_placeholder"  # [Sound: Murmurs of a gathering crowd, boots on wet wood, distant traffic]
    "You stand with a stack of handouts, the paper damp at the corners. The Promenade smells of seaweed, frying oil from a nearby food cart, and the faint metallic tang of municipal salt. Faces lift as"
    "the slideshow begins: numbers, then people, then places. The order matters. When data meets grief, the room doesn't ask which to believe; it feels both."
    "A woman with a neon-yellow raincoat steps forward—an organizer you haven't met before. Her voice is a rasp smoothed by too many meetings."

    "Organizer" "We had a seawall here in 2022. They promised fewer floods. We got fewer floods but a narrower beach every month. My son's boat has nowhere to land."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "Tell me what you saw. Exact months help us tie it to their deployments."
    "She does. The account is small—dates, debris lines, a change in the algae that used to anchor the sand. You write, every word a bead on a string that will become evidence."
    show maya_ellis at right:
        zoom 0.7

    maya_ellis "This isn't about nostalgia. It's about how decisions are made, who is left out, and whether a dollar figure is the only thing that counts."

    "Someone in the back shouts, half-angry, half-afraid" "Is anyone gonna stop them?"
    "You look at Jonah Reyes. He gives a small, almost sheepish nod and thumbs his camera: the images will stop the gaslighting if presented in sequence. The projector shows a pair of photos: one with a broad fringing marsh, another months after installation with a bare, receding edge."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We can trace the sediment pocketing. If the council sees that sequence tied to municipal procurement—"
    "A man at the front cuts in, voice like gravel."

    "Man" "Elias Crowe already sent a glossy piece to every councilor. On the news this morning—oceanic safety, minimal disruption. He paints a future."

    mara_ellis "Then we paint another. We show what his 'minimal disruption' looks like where it happened."

    menu:
        "Lead the crowd in a call to demand an oversight hearing":
            "You step to the mic Maya hands you and say, 'We deserve a transparent hearing.' The crowd answers with a hum; people start to clap like rain starting to fall."
        "Encourage small, targeted petitions to the councilors first":
            "You ask for names and emails. Maya sets up a phone tree. The energy becomes organized; the crowd turns to lists and commitments."

    # --- merge ---
    "Volunteers and signatures begin to coalesce into a coordinated push for formal oversight."
    "Maya corrals volunteers, and soon people are filling in forms, signing petitions, sending emails. You feel the communal engine engage—tired hands pressing new pages into older palms, children poking at damp posters with curious fingers. The"
    "Promenade's reflection pools become mirrors for the protest signs. A mother tucks her child close; her expression is fierce in a way that is just like aching."
    "Meanwhile, Elias Crowe is already on the airwaves. A glossy video loops: sleek models, confident engineers, sailboats skimming calm water—no marsh, no rooted eelgrass. His voice is steady in the narrator track. He smiles with the practiced warmth of a man who has spent a lifetime polishing surfaces."
    hide mara_ellis
    show elias_crowe at left:
        zoom 0.7

    elias_crowe "We design for resilience. Our work keeps cities standing."
    hide maya_ellis
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Resilience that doesn't name what it lifts isn't resilience at all."
    "Jonah Reyes's shoulder brushes yours. He looks tired but resolute."

    jonah_reyes "They have PR and pocketed narratives. We have images, timelines, and people who will testify. That balances the scale."
    hide jonah_reyes
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "We've unsealed the procurement timeline and cross-referenced the sediment studies. If council orders oversight, we can subpoena the unredacted models."
    "You feel the swell again—this time larger and louder. The Promenade's crowd is no longer only locals; reporters begin to edge closer. The momentum doesn't roar; it accumulates like runoff collecting into a stream that chooses a channel and becomes inevitable."
    # [Scene: Tide Lab | Afternoon]
    hide elias_crowe
    hide mara_ellis
    hide professor_asha_rao

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Piano motif returns, higher and more insistent]
    # play sound "sfx_placeholder"  # [Sound: Printer stutters, a mobile phone buzzes with incoming messages]
    "The lab is now a hub for coordination. Asha's annotations grow into a narrative arc: causation maps, accessible timelines, red-flag markers. Maya organizes witnesses, collecting contact details and short statements she formats into a concise briefing."
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "If we put forward two or three strong witnesses and the photographic sequence, the oversight hearing has teeth."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "And we attach the matched municipal contracting dates. If those align with accelerated erosion, it's not just correlation."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "I'll testify about the field notes and chain-of-custody for the photos. I can stand there and say, 'These were taken at these times, by me.' It's honest and hard to dismiss."

    mara_ellis "Thank you. That means a lot."

    jonah_reyes "Means a lot to me, too. This could cost me. I need you to know that."

    mara_ellis "I do—and I want you there as yourself, not as someone forced into a corner. If things get rough, we don't throw anyone under the bus."
    hide maya_ellis
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We prepare for pushback. Elias will produce counter-studies and hire spokespeople. But we have a moral scaffolding that money can't easily dismantle: lived experience and reproducible data."
    "A wave of small, practical things follows: formatting the dossier, printing the copies for council members, preparing witness statements, marshaling legal contacts. You file the request to unseal procurement documents. Each click, each photocopy feels like a nail in a frame you're trying to build."

    menu:
        "Insist Jonah give an on-record statement today":
            "You press the urgency: 'If not now, then when?' Jonah exhales, shoulders squaring. He agrees to an on-record statement, and the camera shutter stabs like a promise."
        "Let Jonah choose the timing of his testimony":
            "You step back. Jonah nods slowly and says he'll speak when ready—his autonomy preserved. It gives him strength; he comes back to the table with renewed clarity."

    # --- merge ---
    "Jonah's participation is secured in a way that balances urgency and his agency."
    # [Scene: Council Chambers (Glass Civic Forum) | Early Evening — Public Notice]
    hide mara_ellis
    hide jonah_reyes
    hide professor_asha_rao

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings bloom optimistically; a single, hopeful chime]
    # play sound "sfx_placeholder"  # [Sound: Distant city rain, the murmur of online comments pinging phones]
    "You read the public notice twice because the city printing it is an act of permission. It is one thing to gather evidence; it is another to have the mechanisms of governance respond. The notice is"
    "not victory—it is invitation. You tape a copy to a corkboard in the Tide Lab, where its shadow lands over a cluster of graphs."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We made them listen enough to open a hearing. That is political entropy moving toward order."
    show maya_ellis at right:
        zoom 0.7

    maya_ellis "They opened a door. Now we walk through it together."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "This will be on record. If Elias goes full PR, we won't win hearts on aesthetics alone. We have to be clear, calm, and evidentiary."
    "You close your eyes for a single breath and let the shape of what's next come into focus: the schedule of witnesses, the order of presentation, the way you will stand and say the coastline matters because people do."
    "Your stubbornness feels less like obstinacy and more like a lever. The entries into the ledger of public life—names, dates, photographs—are small, precise movements that add up. The air tastes like possibility, not safety. That difference matters: possibility allows you to plan and hope at the same time."
    "Elias Crowe's counter-narrative will come with lights and polish, but the hearing is a place where data can be paraded under oath, where procurement can be examined and where community memory meets corporate explanation. That is where the crust of narrative might crack."
    "You pick up your damp notebook, feeling the ridges where your pen has pressed lines into memory. The page is streaked but legible. Outside, rain runs across the ferry's hull in a steady sheet."
    hide professor_asha_rao
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "We pull them into the light."
    hide maya_ellis
    hide jonah_reyes
    hide mara_ellis

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo into a hopeful chord; then a soft sustain]
    "You gather the dossier, the annotated timelines, Maya's witness list, and Jonah Reyes's images. The group forms a loose constellation around the workbench—each person a point of intention. No one celebrates yet. Instead there is a quiet, shared inhale: the kind that comes before a choir begins."
    "You glance out the porthole. The Promenade lights blur into long, patient reflections. The city is wet and awake, listening."
    "Page-turn thought: The hearing will not decide everything in one sitting, but it will make private choices public. That is enough to change the math. The next act asks you to translate evidence into persuasion—to stand under bright scrutiny and let the facts do the arguing."

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
