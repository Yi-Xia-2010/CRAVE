label chapter6:

    # [Scene: Havenport Boardwalk | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A seagull keens. Distant engines hum. The low murmur of a gathered crowd is punctuated by someone beating a drum with measured desperation.]
    # play music "music_placeholder"  # [Music: Sparse piano notes, a low violin pulse; the atmosphere leans heavy.]
    "Narration"
    "You wake with the taste of salt already in your teeth, like the sea has stowed itself in the corners of your mouth. The dawn is thin and arranged against us — the light gives everything"
    "a brittle clarity. Your boots find the wet grain of the boardwalk without thinking. Rope grates between your palms; it smells faintly of diesel and tar. Someone has smeared a chant onto a piece of cardboard"
    "and tied it to the railing with fishing line."
    "Ivy's face is close by, no make-up left in her expression, only focus. Tomas stands a little apart, hands folded around the carved walking stick like a talisman. Lina Park moves through the edges, eyes sharp,"
    "a recorder flitting from her hand to her mouth. Ariana Voss is beside you, breath shallow in the cold, yellow boots planted in the same mud as everyone else."
    show marin_sato at left:
        zoom 0.7

    marin_sato "Hold the line. Eyes open. Don’t give them anything."
    "You hear your own voice as if from underwater — steadier than you feel. People lean into one another the way a net leans on a pole, closing gaps. The human chain is not romantic; it's"
    "a function, an angled geometry of bodies bracing against machines the way a breakwater braces a shore. Hands find hands. Arms lock."
    show ivy_morales at right:
        zoom 0.7

    ivy_morales "They said the crews start at first light. Don't let them take the Old Boathouse."
    "Ivy's words are a match struck on damp tinder; they spark more than resolve. Around you, faces set like gulls on the wire. You picture the lamps inside the boathouse, the jar of nails, the maps with curled corners — memory anchored to cedar."
    hide marin_sato
    hide ivy_morales

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens that might not be for us yet.]
    "Narration"
    "For the first hour, the world simplifies into rhythm: chant, hold, chant, hold. Adrenaline threads through you like electrical tape, numb and bright. Someone hands you a thermos; stale coffee gives you a moment of warmth you don't deserve."
    show lina_park at left:
        zoom 0.7

    lina_park "Marin, can you tell me what this blockade means for the broader plan?"
    show marin_sato at right:
        zoom 0.7

    marin_sato "It means we try to buy time. It means we show them what losing this place looks like. It means we refuse to become a footnote written by a company with a PR budget."

    lina_park "Some of your backers worried this would go sideways."

    marin_sato "We knew the risk."

    lina_park "And you still stood up. The town's voice... it will carry."
    "You can hear the friction under Lina Park's professional optimism — a tension between the story and the people who will live inside it. Her recorder clicks as if to puncture the moment."

    menu:
        "Kneel and rebreathe":
            "You sink to one knee on the plank, pressing the compass into your palm to quiet the quake in your chest. Ivy nudges your shoulder; no words, only the squeeze of solidarity."
        "Step forward and shout":
            "You fling your voice toward the contractors: 'This boardwalk remembers. You'll have to send a letter to history to erase it!' The shout gathers a surge; chants swell, and for a heartbeat we drown out the engines."
        "Scan the perimeter for cameras":
            "You raise your chin and sweep the edges, finding Lina Park, finding faces, finding a camera on a tripod. She meets your gaze and nods; she is listening, and that listening feels like a fragile safety net."

    # --- merge ---
    "Hours spread their weight across the morning. The sun climbs and collapses into a milky wash; breath condenses on collars. We hold. We take turns leaning back against the railing, catching whatever sleep we can in"
    "twenty-minute fragments. Conversations come and go in shards — childhood stories, quick lists of who needs water, jokes about seagulls stealing sandwiches. Those small human things keep the tide of panic from pulling under."
    "Narration"
    "Hours spread their weight across the morning. The sun climbs and collapses into a milky wash; breath condenses on collars. We hold. We take turns leaning back against the railing, catching whatever sleep we can in"
    "twenty-minute fragments. Conversations come and go in shards — childhood stories, quick lists of who needs water, jokes about seagulls stealing sandwiches. Those small human things keep the tide of panic from pulling under."
    show elder_tomas_hale at center:
        zoom 0.7

    elder_tomas_hale "When my hands shook the last time, I thought of my father. He'd have braided rope tighter. He'd have told us to sing louder."

    marin_sato "We sing for them. We sing because their names are still here."

    elder_tomas_hale "They teach us to make shelters from love. I'm afraid that'll look poetic and nothing else when the cameras leave."
    "Your throat tightens. You imagine the funeral the boathouse will become if it is taken: not an event but a slow disassembly of the places that taught people how to be here."
    hide lina_park
    hide marin_sato
    hide elder_tomas_hale

    scene bg ch6_601bcb_3 at full_bg
    "Narration"
    "The police come with an economy of movement. They do not shout. They hand a document to someone you recognize as Tideguard's local liaison; the seal and the paper's weight say the thing you feared but had not let yourself see: the court order."

    "Officer" "By order of the court, this site is to be cleared. You are obstructing construction that has lawfully been permitted."
    "Your breath is a held coin. Ivy spits a curse under her breath. Someone in the chain squeezes harder and a muffled sob escapes, an animal sound."
    "Cassian Rhee appears almost too late to be a presence and too early to be stubborn fate. He brings the professional neutrality of someone who has learned to thin the volume of human distress into reports."
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "Marin. Ivy. I didn't want this. I tried to... There's a legal framework here."
    show marin_sato at right:
        zoom 0.7

    marin_sato "You filed the framework, Cassian Rhee. You signed the orders."

    cassian_rhee "I believed we could stabilize the harbor if we moved quickly. I believed in protecting people."
    show ivy_morales at center:
        zoom 0.7

    ivy_morales "At the cost of our shelters?"

    cassian_rhee "You know trade-offs are inevitable."
    "The words fall like small, hard pebbles. He looks at you not with malice but with the clean, difficult clarity of someone who thinks in spreadsheets. You see the calculation in his jaw tighten."

    marin_sato "Trade-offs aren't your ledger. They're people."

    cassian_rhee "They're also the calculus of survival. I don't relish that choice."
    "There is no reconciliation in his voice — only an insistence that the world will be made to fit his criteria. The human edges are still casualties, collateral to a solution he imagines will save more lives than it costs. That arithmetic is a blade."
    hide cassian_rhee
    hide marin_sato
    hide ivy_morales

    scene bg ch6_601bcb_4 at full_bg
    show lina_park at left:
        zoom 0.7

    lina_park "Cassian Rhee, you told the regional board you would minimize cultural disruption. Do you stand by that now?"
    show cassian_rhee at right:
        zoom 0.7

    cassian_rhee "We made concessions where possible. This is a regional-scale infrastructure project. It cannot be built in fragments."

    lina_park "The boathouse—"

    cassian_rhee "Proximity to the reinforcement makes it a risk-engineered exclusion."
    show elder_tomas_hale at center:
        zoom 0.7

    elder_tomas_hale "You remove the place that remembers the storms and you expect us to remember nothing?"

    cassian_rhee "We remember and we protect what will shelter the most people. The rest is—unfortunate."
    "Narration"
    "'Unfortunate' hangs in the morning like smoke. The contractors start cataloguing us: names, faces, shoves recorded on phones. The cameras that Lina Park brought now become an instrument both of witness and of a history that will render you as spectacle. In the distance, bulldozer teeth glint like predatory birds."

    menu:
        "Refuse to be filmed":
            "You cover your face with your hands and step back, feeling the camera's lens slide over you like a judgment. Ivy comes to stand in front of you, blocking the frame with her small, furious body."
        "Step into the lens and speak":
            "You put yourself where the camera can find you. 'This is our town,' you tell every stranger's lens like a prayer. Lina Park holds the shot as if it matters, and the words tremble raw in your throat."
    "THE END"
    # [GAME END]
    return
