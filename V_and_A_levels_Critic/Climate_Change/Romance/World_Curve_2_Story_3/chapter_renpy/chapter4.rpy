label chapter4:

    # [Scene: Mariner's Row | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense strings under a brisk percussion pattern]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, muffled voices preparing folding tables]
    "You wake into the neighborhood the way you always do—by listening. The sound of someone hammering a last nail, Lina's laugh spilling from a doorway, the soft thud of a stack of handouts landing on a"
    "picnic table. The ledger in your head—your grandmother's hands, the names on the lists—ticks louder this morning because the calendar on Elias's tablet is ticking louder too."
    "You pull your patched olive jacket tighter against a salt breeze. The jacket has more stories than you do; neighbors nod as you pass, eyes searching for certainty that isn't there. For now there are meetings, sketches on butcher paper, the small stubborn work of coaxing policy into people-shaped shapes."

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, a child's crayon squeak; a municipal transit announcement faintly echoes from a distant street]
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "Morning. Looks like people turned up."
    show mira_santos at right:
        zoom 0.7

    mira_santos "They did. Lina's already turned three sketches into a manifesto."
    "Elias Moreno sets down his tablet and bends over the table, already translating municipal language into something the room can understand. His hands move as if drawing bridges—literally and figuratively."

    elias_moreno "We can phase construction. We can make tenancy guarantees binding. If we lock land-trust clauses into the first procurement package, it becomes part of the contract."
    "You watch him talk and a warmth grows—there's a sincerity there that steadies you. For a moment the political geometry rearranges itself into possibility. Living-shoreline cross-sections sit next to diagrams of gradual armoring. Dr. Arun's pen scratches an ecological note."
    show dr_arun_patel at center:
        zoom 0.7

    dr_arun_patel "These living shorelines can reduce wave energy and preserve habitat, but they require careful staging—if the procurement rushes everything, installation quality drops. That increases failure risk during heavy tides."

    mira_santos "We have to make tenure guarantees non-negotiable. People can't be slipped out because a timeline was accelerated."

    elias_moreno "I know. That clause is important. I'm pushing for it."

    menu:
        "Point to the timeline and say 'We need more time'":
            "You gesture at Elias's tablet; his jaw tightens, but he doesn't pull away. The room waits."
        "Quietly hand Lina an extra stack of flyers":
            "You press papers into Lina's hands; she grins and disappears into the crowd, and for a single second you feel like the work is catching on."

    # --- merge ---
    "The workshop continues; residents refine sketches and the conversation pivots to procurement mechanics."
    # [Scene: Workshop — Midday]
    hide elias_moreno
    hide mira_santos
    hide dr_arun_patel

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussive rhythm accelerates; piano notes staccato underneath]
    # play sound "sfx_placeholder"  # [Sound: The clatter of a folding chair, a camera shutter in the background (Tamiko)]

    "Initially, the room breathes as one. Residents sketch living-shoreline ideas—mollusk reefs, marsh terraces, community docks comfortable in higher water. Tamiko records everything with a camera that seems to search for truth in the seams. You moderate, translating technical jargon to human stakes" "If we do this wrong, people move. If we do this right, we stay."
    "Elias Moreno works through objections with a patience that feels like an offering. He explains procurement windows, federal funding timelines, the ways the city's funding formulas reward scale and speed."
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "If we miss this window, Cassian's consortium will step in. They have financing ready to deploy. That means a different approach—faster, but less community-led."
    show mira_santos at right:
        zoom 0.7

    mira_santos "And that 'different approach' looks like promenade, gated access, and people asked to leave. You know that."

    elias_moreno "I do. That's why I'm trying to thread guarantees into the contract now."
    show tamiko_sato at center:
        zoom 0.7

    tamiko_sato "Threading is what you do with cloth, not with legal power. We need teeth, Mira. Real teeth."

    mira_santos "We need binding language. We're not here to be poetic about hope—we need enforceable mechanisms."
    hide elias_moreno
    show dr_arun_patel at left:
        zoom 0.7

    dr_arun_patel "Legalese can be precise, but also brittle. If the clause isn't matched with procurement oversight—"

    "You cut in, because the urgency has a tidal rhythm and you can feel it. Mira Santos" "We can't let brittle be the only shape left."
    "Conversation folds and unfolds—ideas proposed and struck down. The room's attention pivots every time the municipal timeline is mentioned. You can sense a pressure front approaching: funding calendars, council votes, Cassian's public relations machine humming like a low tide."
    # [Scene: Mariner's Row — Late Afternoon]
    hide mira_santos
    hide tamiko_sato
    hide dr_arun_patel

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Nearby, a municipal press notice blares from a speaker; footsteps cross a boardwalk]
    # play music "music_placeholder"  # [Music: Tension ratchets; string ostinatos push forward]
    "As you and Elias walk the Row, you point out sites for demonstration plantings. His fingers trace a fence where mangroves might be introduced; his expression is open, intent."
    show mira_santos at left:
        zoom 0.7

    mira_santos "If we get the land-trust language in, and we tie procurement to a participatory oversight committee, then the community actually has a seat."
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "We can specify oversight membership. We can—"
    "He pauses because a notification buzzes on his tablet. He reads, his brow drawing shadow."

    elias_moreno "Cassian's team just proposed an alternate procurement model to the council—'fast-track coastal defense'—with a guarantee of delivery in eighteen months."
    "Your stomach drops. Eighteen months: the number hits like a wave. It sounds like salvation at first—that immediacy—but you know the trade: speed for consent."

    mira_santos "And Vale's terms?"

    elias_moreno "They'd require the city to grant a prioritized contracting clause—short-circuiting public bidding. They frame it as an emergency measure."

    mira_santos "Emergency for whom?"

    elias_moreno "For the city, Mir—"

    mira_santos "For the waterfront, not for the people who live on it."
    "His face tightens. This is where the seams show. Elias Moreno's impulse to fix with plans bumps against your impulse to protect with people-shaped protections."

    menu:
        "Ask Elias, 'Do you see how this sounds?'":
            "You say it bluntly; his hand lifts in reflex, as if to measure the words. He answers, quieter: 'I do. But I also see lives that could be saved if we move.'"
        "Stay silent and press your palm against the wooden fence":
            "Your palm rests on sun-worn grain. The wood is cool, splintered—anchoring you while the city's machines hum in the distance."

    # --- merge ---
    "The conversation continues, tension unresolved as legal and political complications deepen."
    # [Scene: A makeshift legal clinic inside a community center | Evening]
    hide mira_santos
    hide elias_moreno

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Rhythmic, urgent; a low synth underscores building pressure]
    # play sound "sfx_placeholder"  # [Sound: A murmuring crowd, a kettle whistles softly in the corner]
    "You bring in a municipal lawyer Elias has pulled into the circle and Dr. Arun lays out ecological risks with a clarity that makes the stakes feel medical. The lawyer's pencil scratches as she reads drafts of proposed guarantees."

    "Lawyer" "This clause is problematic. As written, 'priority protections' are advisory, not enforceable. The procurement process can override advisory language during an emergency grant."
    show mira_santos at left:
        zoom 0.7

    mira_santos "So they can wave 'em aside."

    "Lawyer" "Not technically. But the political pressure to accept Vale's expedited procurement could make advisory protections meaningless in practice."
    "Your throat tightens. You flip through the draft until a line about land-trusts seems like it's been edited into a weaker form—'where feasible'—words that hollow the promise."
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "We can push to reword. We can demand 'mandatory' instead of 'where feasible.'"

    "Lawyer" "It's not that simple. Funding formulas have covenants. If federal or state funds limit modifications, the city might not be able to attach conditions without jeopardizing the whole package."
    "The room feels smaller. The air tastes metallic. For the first time since you started working with Elias, you see his optimism meeting not just political friction but legal architecture designed to privilege scalers and speed."

    mira_santos "Why are the rules set up like this? Why do people have to pay with their homes to make timelines work?"

    elias_moreno "Because the system rewards outcomes in a certain way. I'm trying to change the outcome."

    mira_santos "But changing the outcome might require changing the system."

    elias_moreno "We don't have the luxury of changing the system on the timeline the tide gives us."
    "The words hit the room like a cold wave. Around the table, neighbors’ faces hollow in quiet computation: tradeoffs, sacrifices, promises."
    # [Scene: Mariner's Row — Night]
    hide mira_santos
    hide elias_moreno

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: High-tension strings; rapid rhythm building toward a climax]
    # play sound "sfx_placeholder"  # [Sound: A distant protest chant, Tamiko's camera clicks; the hum of late-night traffic]
    "Word of Vale's fast-track pitch spreads quickly. Tamiko posts a grainy clip to her channel—Cassian smiling in a press clip, speaking of 'swift protection.' Comments flare into heated threads. Lina, exhausted, finds you on a porch and does not beat around the bush."
    show lina_cortez at left:
        zoom 0.7

    lina_cortez "Mira. People are scared. They want the seawall now if it means their kids aren't swept away. They're asking—did you bargain away our souls for this?"
    show mira_santos at right:
        zoom 0.7

    mira_santos "I didn't bargain anyone away. I'm fighting for guarantees."

    lina_cortez "But you said you'd work with Elias. Now he says some things he can't change, the lawyer says clause language is fragile, and I'd swear I saw his eyes on that tablet when Cassian's timeline popped up."

    mira_santos "You think I'm negotiating for myself? You think I'm making deals at your expense?"

    lina_cortez "I don't know what to think. All I know is the people who stayed behind because they believed in us are looking at us like we'll be gone tomorrow."
    "Tamiko joins, camera lowered. Her skepticism is a steady blade."
    show tamiko_sato at center:
        zoom 0.7

    tamiko_sato "Compromise is one thing. Capitulation is another. Mira, if you're the one arguing to give up protective mechanisms for speed, you need to say why."
    "You feel your spine straighten, every tendon an argument you haven't voiced. Elias appears at the edge of the porchlight, coming in from the street. He looks tired—a planner exhausted by the world's impatience—but earnest."
    hide lina_cortez
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "I didn't come here to capitulate. I came here to protect people faster."

    mira_santos "Faster for some, Elias. Faster at the cost of others' ability to stay."

    elias_moreno "If we stall, Cassian steps in. Do you understand what that looks like? Rapid construction, yes, but also corporate contracting, displacement, sanitized promenades—"

    mira_santos "So what do we do? Let him have the field? Or do we force a public fight that could blow your career apart?"

    elias_moreno "If calling Cassian out publicly keeps his consortium from securing the fast-track, and that keeps us at the table...I will do it. But if it makes my position untenable and the city swings to Vale because I'm gone, then we lose everything."
    "Your chest tightens. The night smells like wet pavement and the iron taste of possibilities. The pressure, which had been a slow boil all day, becomes a sharp pressure now—like someone turning a valve."

    mira_santos "You've always believed in systems to fix things for people. I believed we could slow systems down for people. Now those visions are pulling—hard."

    elias_moreno "I want both. I want safety and justice. But right now, the calendar punishes perfect justice."
    hide mira_santos
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "Then pick which of you is right, Mira. Choose."
    # play music "music_placeholder"  # [Music: Reaches a jagged peak; strings and percussion collide]
    # play sound "sfx_placeholder"  # [Sound: A lone boombox plays a protest chant far off; a window slams somewhere in the Row]
    "You feel every face on the Row like a prying tide. Trust—between you and Elias, between you and the neighborhood—shows hairline cracks: small things that could spiderweb into rupture. The legal walls, funding constraints, and Cassian's enticements have dialogued into consequences you can no longer delay."
    "Your fingers clench around your scarf. The hood of your jacket is wet with spray from a passing truck; it beads like attention on your sleeve. This is the fulcrum: press for a political showdown that"
    "risks Elias professionally, accept a compromised guarantee that buys immediate protection but weakens tenure, or delay and bring in Dr. Arun and outside counsel to rework the guarantees at the risk of losing the city's political"
    "momentum."
    "Your chest pounds; the air tastes like iron and wet paper. You know this will fracture something—alliances, trust, perhaps a relationship. The arousal that has been building all day now slams into your center: high, insistent, unforgiving."
    "You lift your chin and speak, the sound small but carved by necessity."
    hide tamiko_sato
    show mira_santos at center:
        zoom 0.7

    mira_santos "We can either force a public reckoning with Vale now, accept a compromised guarantee for speed, or take time to build something legally unassailable that might cost us the window."
    "Elias Moreno's eyes search yours, pleading and proud in the same beat. Lina watches like a coiled wire. Tamiko looks like a judge and a comrade folded into one. Dr. Arun's face is unreadable—steady, concerned."

    menu:
        "Insist Elias take Vale to task publicly to preserve leverage.":
            jump chapter5
        "Accept a compromised legal guarantee for quicker construction.":
            jump chapter6
        "Delay and bring in Dr. Arun and outside counsel to rewrite guarantees.":
            jump chapter6
    return
