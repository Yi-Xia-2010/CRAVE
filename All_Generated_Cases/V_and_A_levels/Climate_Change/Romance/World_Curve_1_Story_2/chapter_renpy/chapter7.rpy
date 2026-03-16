label chapter7:

    # [Scene: Seabreak Marshes | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of small, impatient waves; the slap of a distant boat hull; peat worms stirring beneath the mud]
    # play music "music_placeholder"  # [Music: Bright strings with driving percussion — hopeful, urgent]
    "You wake before your alarm, because the tide has a timetable that does not care for human schedules. Your boots leave soft imprints in the mud, and each step feels like a ledger entry: months of"
    "work balanced in salt and sediment. Where last year there was glassy open water, narrow rivulets now braid through a carpet of green—Spartina holding its ground, cattails learning the contours again. Juvenile fish dart like quicksilver"
    "signatures in the nursery channels you and the volunteers coaxed open."
    "Your notebook is heavier from use; laminated tide charts softened at the edges, a smear of clay on the cover that will not come clean. You run your thumb along a recent graph, the lines you"
    "plotted at night from core samples and salinity readings. Each peak and trough answers a question you used to carry alone. Now they answer the town."
    "You breathe in brackish air mixed with the bitter mineral of the bay and the sweet churn of wet earth. It tastes of work and of proof."
    "You crouch at the edge of a newly filled sod mattress—plant roots knotted into the old dock timbers—and feel the foliage when you smooth your hand across it. The blades whisper against your palm, rough and"
    "candid. A flock of starlings lifts and folds as if on cue; above them the gulls wheel in practiced tolerance."

    menu:
        "Trace the new channel with your finger":
            "You follow the shallow current with a fingertip, feeling the cool pull and imagining the path juvenile flounder will take in spring. The motion is small and reverent; you name the channel in your head, as fishers name boats."
        "Check the sediment cores locked in your notebook":
            "You flip to a page of recent cores, the ink smeared with salt. The numbers—accretion rate, organic content—read like a pulse. They tell you this is not luck. It's the cumulative rhythm of many hands."

    # --- merge ---
    "You continue your morning, carrying the quiet proof of the marsh with you."
    # [Scene: Community Rooftop Garden & Meeting Hall | Golden Hour]

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter rolling under the tin roof, the clink of plates, Lina's brush scratching across plaster]
    # play music "music_placeholder"  # [Music: A warm folk motif — mandolin and harmonies, quickening tempo]
    "The rooftop is a festival of small economies: jars of pickled marsh greens labeled in Lina's handwriting, Aiden's thermos sending out steady coffee steam, Priya handing a grant packet fingertip-to-fingertip to a volunteer coordinator. The mural"
    "on the community hall wall is becoming its own congregation—Lina steps back, squints, and adds a reed that looks almost alive."
    "You move through the crowd, offering quick directions—who will pick up seedlings tomorrow, which plot needs mesh reinforcement before high tide—and collecting updates. The cadence of months has taught you to listen for details that mean"
    "survival. A woman from the co-op squeezes your hand. 'The sea vegetable trial's doing better than we thought,' she says, voice thick with something like relief. She does not need to explain what that will do"
    "for the winter tables."
    "Aiden is near the edge, elbow on a crate, eyes on the water as if reading its temper. When he sees you he makes the usual exaggerated grimace that pretends to be critical and is really an invitation to a conversation that will never be public. You cross to him."
    show aiden_reyes at left:
        zoom 0.7

    aiden_reyes "You look like you've been up all night counting tides and saving the world."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "Maybe just counting tides. Saving the world would be dramatic."
    "Aiden Reyes smiles, then his expression softens. He leans in with that easy earnestness he reserves for moments that are not for show."

    aiden_reyes "We had three more people sign up for volunteer shifts today. Mateo taught two young fishers to weave cordgrass into mats. They're proud of it. They brought their tools."

    maya_kwon "Good. It matters. A lot."

    aiden_reyes "You did this. Not the charts—they helped—' (he nods at Priya who is elbow-deep in a grant form) '—but you started the way everyone would follow."
    "You hesitate, the reflexive part of you deflecting the praise. You remember the nights of maps and small indignities—snide council emails, sleep that slid through worry. You choose, for once, not to unpack that burden."

    maya_kwon "We did it. The town did it."

    menu:
        "Tell him, honestly, how scared you still are sometimes":
            "You lean closer, voice low. 'I still wake up thinking of that storm. It takes effort to not let that be the only story.' Aiden threads his fingers through yours and his grip says the rest."
        "Laugh it off and change the subject to Lina's mural":
            "You point to Lina's work and make a joke about the mussel-eyed heron she's painted. Aiden laughs, and for a breath the past's jagged edges smooth into paint and food and light."

    # --- merge ---
    "You stay there longer than you planned, because the night keeps offering small miracles—neighbors who used to argue over dock hours now trading seedlings; an elder swapping stories for the kids about when the marsh used"
    "to swallow whole winters and still give back. The music swells; someone lifts a tin cup and starts a chorus. Your chest softens in the way bedtime stories did when you were small: full, safe, charged."
    # [Scene: Community Hall | Afternoon — Council Vote]
    hide aiden_reyes
    hide maya_kwon

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur of clustered bodies, paper shuffling, a single gavel that will not go unused]
    # play music "music_placeholder"  # [Music: Tension-building strings underlaid with a steady drum — intensity peaking]
    "This is the day the town ratifies its decision. The room smells of wet wool and strong tea. Priya sits at your side, an island of competence, her tablet syncing minutes and stipulations. Mateo is onstage-like"
    "in his quiet way, leaning on his cane with a presence that tilts the room's history toward your side. Councilor Tomas Hale paces with a briefcase that seems to thump against his knee in panic; he"
    "is not used to losing momentum."
    "Dr. Elara Voss arrives mid-storm, trench coat dark with rain, hair plastered at the temple. She stands in the doorway for a long beat, watching the mural peeking from the corridor, then the maps you once"
    "brought to her—lines inked with work and tears. When she meets your eyes her expression is unreadable and, for once, not threatening. Just a complex human weighing evidence."
    show dr_elara_voss at left:
        zoom 0.7

    dr_elara_voss "I won't pretend it's all been my plan. The models show risk. But the data from your pilot—and Priya's legal buffers—are persuasive."
    "(She taps at her tablet; the slide she brings up is not blocks of concrete but nodes of support.)"

    dr_elara_voss "Living shorelines buy time in a different way. They carry ecosystem services. If the town insists on local control, I can offer guidance on where engineered nodes will stabilize access without swallowing the marsh."
    "There is a small intake of breath around the room; you can feel the arousal spike—years of friction compressed into a single sentence that sounds like truce."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "You surprised me, Elara."

    dr_elara_voss "You surprised me first. I expected resistance—driven walls, definitive answers. What you did was make the system measurable and social. That changes risk calculus."
    show priya_anand at center:
        zoom 0.7

    priya_anand "We mapped contingencies. We will monitor salinity, sediment, economic output. We have workforce agreements to transition boatmen into marsh harvests when needed. This plan is built to be adaptive."
    hide dr_elara_voss
    show councilor_tomas_hale at left:
        zoom 0.7

    councilor_tomas_hale "Adaptable sounds like a gamble. How do we ensure the docks don't lose access, the co-op doesn't lose revenue in the short term? Contractors guarantee—"

    "Mateo Reyes" "Guarantees sail off with the first bad wind. What we made here—what these hands did—was a place that takes the wind's temper into account. We still fish. We still make money. We just don't bury our future under a ribbon of concrete."
    "A cacophony of voices rises: one side calling for immediate, hard protections; another for the slow, relentless work of marsh reconnection. Lina speaks from the back like a trumpet of youth, voice clear."
    hide maya_kwon
    show lina_kwon at right:
        zoom 0.7

    lina_kwon "We painted the fish into the mural because they're coming back. We named the channels. This is our town."
    "The debate is not clean; it crackles with urgency, the very-high arousal you have been carrying like a drumbeat. Every rebuttal, every concession, is a shift in the town's future weight. You watch people's faces—some lined with fear, some bright with the flush of possibility."
    "You take a breath and stand. The room narrows to the world you want to protect. Your voice steadies even when your stomach wants to betray you with trembling."
    hide priya_anand
    show maya_kwon at center:
        zoom 0.7

    maya_kwon "This plan will not be perfect. It will require patience, it will require labor, and it will require all of us to stay honest when shortcuts tempt us. But the pilot showed us something engineers couldn't model: people will tend what they help build. The marsh will make waves softer and livelihoods broader if we let it. Priya and Elara and I have layered legal and technical safeguards so this doesn't become the naive choice of a nostalgic town. This is strategy with a spine."
    "A councilor leans forward, skeptical but not unkind."
    hide councilor_tomas_hale
    show councilor_tomas_hale at left:
        zoom 0.7

    councilor_tomas_hale "If we vote this through, will Vernon & Crow meddle? Will investors push their seawalls anyway?"
    hide lina_kwon
    show priya_anand at right:
        zoom 0.7

    priya_anand "We have clauses. Opening funding to contractors will be under town oversight; vendors will be prequalified to work within ecological parameters. Elara will consult on targeted nodes only under community direction."
    hide maya_kwon
    show dr_elara_voss at center:
        zoom 0.7

    dr_elara_voss "I will not allow the town to be used as a test case for a single model that breaks the next storm. If my name is on files, my reputation's on the line. I am accountable to the town now as much as to models."
    "The vote is called. Silence drops like a curtain, then a sound rises—chairs scraping, a woman's exhale, a child's small gasp outside the open door. The clerk reads the tally. You can hear your heart like"
    "a drum in your ear, the very-high intensity of build-up condensed into a fraction of breath."

    "Clerk" "The motion to adopt the hybrid marsh restoration plan with strategic engineered nodes—ayes have it."
    "For a second you are weightless; then the room erupts in the most human of storms—cheers, hands on shoulders, tears tracked in salt. People are hugging strangers, laughing in disbelief, and Tucak, the local crab vendor, is clapping so hard his gloves flop off."
    hide councilor_tomas_hale
    show maya_kwon at left:
        zoom 0.7

    maya_kwon "We did it."
    "You look for Aiden and find him at the doorway, the rain making little glass beads on his jacket. He pushes through the crowd and reaches for your hand without fanfare. It's the same steadying touch"
    "you've come to rely on through nights of mapping and days of slogging wet earth."
    hide priya_anand
    show aiden_reyes at right:
        zoom 0.7

    aiden_reyes "You were brilliant in there. Stubborn in the best way."

    maya_kwon "You mean my usual obstinance?"

    aiden_reyes "Call it stubbornness. Call it faith. Call it the part of you that won't let the town fold. Whatever it is, I'm glad you used it here."
    "You laugh, the sound high and fierce, and you let the moment hold all the pressure it has been carrying. Around you the town is a living thing—no, a community: messy, imperfect, renewed."
    # [Scene: North Pier | Night — After the Vote]
    hide dr_elara_voss
    hide maya_kwon
    hide aiden_reyes

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft revelry, a lone bell clanging once every few minutes, the tide whispering against pilings]
    # play music "music_placeholder"  # [Music: Piano motif returns, now full and luminous; a swelling chorus underlines the final beats]
    "After the vote, people drift toward the North Pier. Someone starts a small bonfire in an iron drum; the scent of fried fish tempers with smoke and salt. You stand at the rail, watching the reflection"
    "of string lights ripple, thinking of how many small hands turned charts into beds and beds into blue-fingered harvests."
    "Aiden comes up beside you and, with a quiet sincerity that has become his trademark, slips his braided rope bracelet into your hand. The driftwood charm—carved smooth by waves and his careful knife—rests against your palm like a promise already kept."
    show aiden_reyes at left:
        zoom 0.7

    aiden_reyes "I started bringing it to sea because it felt like a talisman. But it's really been for seeing you come back to fight for this place, day after day."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "It fits. It smells like you and the boat and rain."

    aiden_reyes "That's a selling point in Seabreak Hollow."
    "You close your fist around the bracelet. The rope is rough and familiar; the driftwood fits the hollow of your hand the way some histories fit the shape of grief."

    maya_kwon "Promise me something."

    aiden_reyes "Name it."

    maya_kwon "Promise you'll keep arguing with me when I'm too stubborn to see another way. Promise you'll let the place change us in ways we can't yet imagine."

    aiden_reyes "I promise. And you'll remind me when I want to compromise too fast. We'll be loud about the things we love and kind about the things we lose. We will show up."
    "The wind picks up, and the bracelet winds a little around your wrist, as if sealing the vow. The pier hums with the town's small victories: Lina leaning against Mateo, Priya debating funding timelines with someone"
    "on a clipboard, old vendors offering out fish and bread in a circle of makeshift tables. Dr. Voss stands a little apart, coat still damp, watching the marsh's outline. You catch her eyes and she nods—an"
    "acknowledgement with the currency of respect."
    show dr_elara_voss at center:
        zoom 0.7

    dr_elara_voss "You folks did something I didn't expect—built something that works. I'll keep working with you, if you'll have me."

    "Mateo Reyes" "To the marsh. To hands that mended it. To the kids who'll not have to move."
    "The cup is passed around like a shared witness; voices lift in verse and cheer. Your chest swells until it aches with a fierce, bright joy."
    "You close your eyes. For the first time in a long time, your grief does not feel like an anchor but like a seam—stitched, mended, part of a fabric stronger for being joined. The marsh will"
    "have storms. The town will have storms. But tonight, the tide that comes in feels like a reclamation, not a taking."
    "You open your eyes and meet Aiden's gaze. The promise between you is ordinary and enormous. He brushes his thumb across the driftwood charm, and the motion is private and whole."

    aiden_reyes "So—stay?"

    maya_kwon "Stay."
    "He smiles, and it is the kind of smile that rearranges the future into something kinder. Around you, your neighbors laugh and shout, hands in each other's shoulders, a tide of people that will tend and"
    "heal. The mural on the hall glows in the distance, Lina's reeds caught mid-sway, forever holding the shape of the town now."
    hide aiden_reyes
    hide maya_kwon
    hide dr_elara_voss

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestral closure — triumphant, tender, enduring]
    # play sound "sfx_placeholder"  # [Sound: The tide's constant whisper, overlayed with distant, sustained applause]
    "You tuck your battered notebook into your jacket, the pages filled with measurements, lists of names, sketches of future plantings, and, between margins, smudged ink of small love notes that read like maps. The field notes are no longer just data; they are testament."
    "You step back from the rail, hand in Aiden’s, feet rested in the mud of a place you fought to keep. The future is not a tidy thing; it is patient labor, shared risk, and evenings like this where promises are braided into rope and thrown hand-to-hand."
    "You think of the possible endings everyone fretted over—walls, loss, leaving—and how this one is quieter, more costly in days and hands than in headlines. It is, in the way that matters, real."
    # play music "music_placeholder"  # [Music: Fade to a single sustained piano note that resolves into silence]

    scene bg ch6_601bcb_6 at full_bg
    "THE END"
    # [GAME END]
    return
