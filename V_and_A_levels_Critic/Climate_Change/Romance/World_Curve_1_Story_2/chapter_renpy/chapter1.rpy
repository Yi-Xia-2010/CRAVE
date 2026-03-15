label chapter1:

    # [Scene: Mariselle Boardwalk | Late Afternoon]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, low piano—each note like a dropped pebble]
    # play sound "sfx_placeholder"  # [Sound: The slow hiss of distant surf; gulls call once, then fall silent]
    "You step off the battered bus with a bag of tools slung over one shoulder and a Moleskine tucked against your ribs. The strap bites into the wet fabric of your jacket; the smell of brine"
    "and wet wood folds into the fibers. Your scarf is damp where the fog has leaned in and lingered. The town greets you the only way it knows—worn, stubborn, weathered into a certain silence."
    "Boards have been patched with mismatched planks; salt has crystallized in the seams like tiny fossils. Protest flyers flap under that persistent fog, their edges softened and half-blank by rain. Someone has tied a threadbare banner"
    "to a lamp post: HOLD THE LINE. Below, a child's handwriting has scrawled NO HOME FOR EPHRAIM in a shaky, permanent marker."
    "You breathe. The air tastes of iron and old storms. The bus doors hiss shut behind you and the engine coughs away, leaving a hush that feels too large for your shoulders."
    # [Scene: Co-op | Early Evening]

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation from the back; the soft clink of ceramic pots]
    # play music "music_placeholder"  # [Music: A quiet, sustained cello note under the ambient sound]
    "Maya is there before you—half-hidden beneath a fisher's raincoat, sun freckles a constellation across her nose. She looks smaller than memory, or else you are larger with all the things you carry. For a beat she doesn't recognize you, or pretends not to; then her mouth quirks."
    show maya_cruz at left:
        zoom 0.7

    maya_cruz "Look at you. Still carrying that Moleskine like it's a talisman. Come in, salt-sore. Sit."
    "You set the bag down, the tools making a soft metallic complaint. Your fingers trace the scratch on your fitness-watch—an old retrofit you calibrated yourself. It gives you the time and a barometric whisper. You find yourself reading it the way others read names carved into wood."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "It feels weird to be the one back in town, honestly. Like I'm wearing someone else's coat."

    maya_cruz "You always did borrow entire identities when you were a kid. Remember stealing my rain boots? You tried to declare yourself Mayor of the Canal for an afternoon."
    "You both laugh, small and brittle. The sound is a buoy, but it doesn't lift much."

    maya_cruz "Council's tomorrow. Lina's speech is rumor-thick already. Ephraim's people were seen unpacking something at the old pier. Sora's got a crew setting up by the plaza. It's—' (she presses a hand to her chest) '—it's a hornet's nest."

    ari_navarro "The levee-and-housing package?"

    maya_cruz "Exactly. Big numbers, smooth promises. They call it security; a lot of folks call it eviction by design."
    "You stare at the row of seed trays, small green shoots pushing stubbornly from mud. The co-op smells of wet peat and brewing tea; your scarf smells of smoke and salt and the faint grease of"
    "the boardwalk. You feel the old pressure yet again: the ghost of an evacuation plan that didn't work, a sibling's absence that is not absence but a hollowness in the map of your life. It tugs"
    "at you in slow, precise pulls."

    maya_cruz "No one can do the retrofit dance like you, Ari. You know those numbers. But—' (she glances away, fingers worrying at a seed packet) '—people are tired of spreadsheets."

    ari_navarro "I know. I still have a duty to make the numbers mean something for people, not just for reports."
    "Maya's hand finds yours—a quick, knotted squeeze—then withdraws. You both look at the tray of marsh grasses someone has labeled 'for living edges'. A child left a muddy bootprint on the table; the imprint is small, decisive."

    menu:
        "Help Maya hang the new protest flyers":
            "You climb the short ladder, arms steady, and the paper stutters in your hands until you smooth it flat; Maya hums, approving. The act is ordinary and it steadies something thin inside you."
        "Flip open your Moleskine and check tide notes":
            "The paper slides open to a cluster of inked curves and shorthand—dates, lag times, odd salinity spikes. Your thumb traces a line you had hoped you'd never read again; it feels like counting bones."

    # --- merge ---
    "Both outcomes converge back to the ongoing scene."

    maya_cruz "Whatever you do, don't let your head stay buried in the margins. People want to know there is care beyond the models."

    ari_navarro "People also need to survive the next supertide."

    maya_cruz "And they'll survive something that looks like hope. Neither is wrong. Both have to be true."
    "Her eyes are tired but fierce. It's the look of someone who has resurrected her optimism more than once."
    # [Scene: Mariselle Boardwalk — Walk toward Tidewatch Institute | Dusk]
    hide maya_cruz
    hide ari_navarro

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footfalls on wet wood, distant muted chanting]
    # play music "music_placeholder"  # [Music: Sparse wind-hummed tones; a single sustained pad]
    "You walk past the promenade, boots scuffing salt. Somewhere farther down, Sora Watanabe's crew is setting up placards—bright colors that conflict with the gray. Sora Watanabe is visible as a silhouette moving deftly among people, a"
    "long wave of hair catching a stray glare from an emergency lamp. Their presence is a small flare: intent, loud in its modesty."
    "You pause. The retrofit watch on your wrist ticks. Its barometric sensor whispers—no alarm, only the soft drop of pressure like a breath drawn and held. Your fingers narrow around the Moleskine. The page edges are"
    "softened by recent rain; the ink has feathered in places. You think of the failed evacuation: radios gone, channels clogged, people left waiting at the wrong pier. The image comes unbidden—rain-slashed sky, the high scream of"
    "wind, someone you should have seen and didn't."
    "Your hazel eyes feel tight, narrowing not out of focus but in concentration—calculation as grief."
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "Ari! You're back. About time you joined the flesh-and-bone side of town meetings."
    "You approach. Sora Watanabe's smile is quick, practiced for the camera of a crowd. Up close, there's a softer tremor in their jaw you don't see on distant stages."

    sora_watanabe "We were saving a sign for you. Says, 'Engineered, yes—but with us.'"
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "I didn't know if coming back would help. Or if I'd just make things harder."

    sora_watanabe "You always make things interesting. And sometimes harder is what wakes people up."
    "Sora Watanabe's hands are warm against the chilly air when they brush your hand to pass the rolled sign. There is an impatience under their earnestness—an insistence that action must be louder than policy. You sense the friction in it, the way their idealism can tilt toward risk."

    sora_watanabe "We're thinking of a human chain at the council steps. Visual, undeniable. Lina Moreau hates visuals that don't come with a ribbon and a press release."

    ari_navarro "A visual can also become a scene if it escalates. I don't want people hurt."

    sora_watanabe "Neither do I. That's why you're here, right? To keep things from becoming a headline about failure."
    "The words hang between you like a balance. Neither of you moves to clinch it; both of you measure."

    menu:
        "Offer to draft an emergency route plan for the demonstration":
            "You pull out your pen and sketch a quick route on the back of a flyer, nodding as Sora murmurs adjustments. The plan is small and careful—safety cordons, med points, ebb-tide awareness—and it steadies Sora's expression into something grateful and raw."
        "Stand with Sora and hand out flyers to the crowd":
            "You take a stack and fold them over your palm. The corrugated sound of paper is loud in the hush. Your voice, when you speak to passersby, is softer than protest chants but people listen anyway."

    # --- merge ---
    "Both outcomes converge back to the ongoing scene."

    sora_watanabe "Whatever you pick, we're glad you're here. Town needs you, Ari. Not just your numbers."
    "You swallow; the throat thickens. It is true—the town needs more than calculations. It needs someone to argue that calculations should be applied to people, not footnotes."
    # [Scene: Dunes near Tidewatch Institute | Early Night]
    hide sora_watanabe
    hide ari_navarro

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Whisper of wind through reeds; the distant murmur of set-up noises]
    # play music "music_placeholder"  # [Music: A single low sustained drone, then silence]
    "Dr. Noor steps out of the Institute like someone emerging from an old fact. Her silver-streaked hair is braided back; the field camera hangs at her side like an old friend. She does not offer a"
    "smile. When she reaches you, there is the soft friction of someone who settles into the weight of bad news before speaking it."
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Ari.' (her voice is gentle, not soft) 'You came back when I hoped you would."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "I couldn't stay away. Not when Council—"

    dr_noor_patel "Listen to me carefully. The sediment models—' (she presses a folded raft of papers into your palms) '—they changed. Not by a percentage point. The baseline shifted."
    "You take the papers. The corner is cold; the ink has a clinical smell. You can feel your heart negotiate with the slow clock of a breath. The models are dense: cross-sections, worst-case envelopes, runoffs calibrated"
    "to new data. Your fingers find the lines with the habit of someone who once read these things to comfort themselves."

    ari_navarro "How bad?"

    dr_noor_patel "Worse than the last public run. The channels are filling faster. Storm surge coupling with tidal amplification—we have a probability envelope that expands like a bruise. People will judge you by what you do next."
    "The sentence lands like a verdict. Around you, the town continues its preparation—voices, the thud of a hammer, a radio calling numbers. Everything seems mundanely alive and simultaneously suspended, as if the town is inhaling and part of it has forgotten to exhale."
    "You gesture at the watch again. The barometer edge is a hair lower than when you arrived. The drop is subtle but true; it makes your knuckles ache with foreknowledge rather than surprise."

    dr_noor_patel "I am sorry I couldn't tell you sooner. The data came in this afternoon."

    ari_navarro "Could this be mitigated? With living shorelines and retrofits—"

    dr_noor_patel "They will buy you time in places. But not everywhere. Not for everyone if the money flows the way Ephraim wants. The models won't lie. They only show us outcomes. The rest—' (she breathes in) '—the rest is politics and people's stubbornness."
    "You fold the papers into your coat like a small, cold relic. The line between numbers and real faces has never felt thinner."

    dr_noor_patel "People will judge you by what you do next."
    "You hold that sentence until it fits into the hollow place left by the disaster you already carry. It is not only instruction; it is accusation, and it is plea."
    "The greenhouse light spills down like an island against the dark; distant figures move like paper cutouts rehearsing for a show. The salt taste in your mouth is sharp. Your scarf clings damp to your neck, a small, domestic anchor."
    "You make a promise to yourself that is less a vow than a brimful of intention: This time, you will make a plan that saves more than statistics. You will try to keep the town from becoming a number in someone else's ledger."

    dr_noor_patel "I can brief you fully tonight. If you want—if you can bear it."
    "You look at the crease of paper in your hands, at the amber glow above, at the small lights where Sora Watanabe and volunteers are folding into ranks. You feel each layer of town and job"
    "and grief compress, then settle. The pressure around your ribs is a dull, steady ache—less sudden than a panic, more sustained like erosion."
    "You nod."
    "There is no triumphant uplift. Only the slow click of a decision being registered in the heavy machinery of your conscience."
    # play music "music_placeholder"  # [Music: The cello note resolves into a single, low harmonic that holds—no release]
    hide dr_noor_patel
    hide ari_navarro

    scene bg ch1_Start_5 at full_bg
    "You stand there under the amber glow, and the town hums its low, determined preparations. The hush is not peace. It is waiting."
    # [Scene Transition: Night settles; lamps glow; a thin rain begins]
    # play sound "sfx_placeholder"  # [Sound: Distant, muted chant; the sea breathing against its edges]
    "You feel the first, tiny climb of urgency in your chest—a restrained tightening rather than a shout. The emotional arc in the evening has edged upward from numbness to a quiet, resolute dread. The town waits with you, and your next move will be counted quietly and harshly."

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
