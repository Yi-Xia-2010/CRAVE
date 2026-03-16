label chapter14:

    # [Scene: Aurelia Construction Site | Late Afternoon]

    scene bg ch14_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Diesel engines, the metallic ping of a hammer on rebar, a distant foghorn]
    # play music "music_placeholder"  # [Music: Percussive, driving rhythm — heartbeat tempo; strings layered thinly to lift the tension]
    "You stand at the edge of the exclusion tape with mud sucking at the soles of your boots, the salt of the bay settling into the fabric of your sleeves. The concrete edge beneath your knuckles is cold and sharp; it grounds you — anchors the decision to your skin."
    "Eli Navarro is to your left, close enough that your shoulders almost touch. His fingers cradle a trembling Polaroid; when he hands it to the reporter it shakes again, caught in the flash of cameras. Around"
    "you, neighbors press in: some with hands full of marsh plugs and biodegradable mesh, others simply watching, mouths set into thin lines."
    "You smell diesel and wet rope and the faint lemon of the crowd's breath; the air tastes like metal and intent. The living tissues you've been growing — cordgrass plugs, mussel clusters, coir logs seeded with"
    "eelgrass — feel absurd and holy beside the engineered steel. That absurdity is your statement."

    "Reporter" "Ms. Reyes, can you explain what you're doing here? Is this legal?"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We're showing a simple truth: living systems can be integrated. They soak up wave energy, they host life, and they keep people here.' (You press your thumb into the damp soil of a coir roll.) 'We're not just stopping tides — we're keeping memory."

    "Reporter" "Are you worried about safety? Aurelia claims you're trespassing."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "Safety is the reason we chose a visible, demonstrable approach. We're not reckless — we're demonstrative."

    menu:
        "Step forward and begin planting publicly":
            "You push the tape aside with fingers that smell of brine and go to work, the crowd swelling around you; a camera lands on your hands as if they were a treaty."
        "Stay behind the line and speak to the cameras":
            "You stay at the perimeter, voice steady, translating the science into phrases people can hold; your hands stay clean, but the people working in the mud need you to be loud."

    # --- merge ---
    "Continue at the next visual beat"
    hide maya_reyes
    hide eli_navarro

    scene bg ch14_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A reporter's recorder button clicks; nearby a security radio crackles]
    # play music "music_placeholder"  # [Music: Tempo increases — drums sharpen; brass underscores the approach of something larger]
    "A security guard steps forward, helmet catching the light. He is big and practiced, the kind of composure you recognize from many bureaucratic scripts."

    "Security Guard" "Ma'am, you need to stand back. This is an active construction zone."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We're in the intertidal. We're demonstrating non-destructive methods. We're asking —' (your voice narrows, polite but fierce) '—to be seen."

    "Security Guard" "You can't set up installations here. That's company property."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "We're not installing. We're showing. There's a difference."
    "The guard radios his supervisor. You feel the base notes of escalation rumble through the earth as a crane swings, shadowing the crowd like a slow pendulum."
    # play sound "sfx_placeholder"  # [Sound: A louder crackle from the security radio — a different voice, corporate-flat: "Hold position. Send a vehicle. Media on site?"]
    "Tomas is in the back of the crowd, half-hidden by a stack of pallets. You see him before he sees you: jaw clenched, hoodie pulled up, hands deep in his pockets. His posture is taut with"
    "a war between two loyalties — the shop he worries will be bought out and the person who has never stopped fighting for what keeps their town whole. He doesn't move forward. He watches, furious and"
    "reconciled all at once."
    hide maya_reyes
    hide eli_navarro

    scene bg ch14_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clunk of a camera shutter; a gull's cry cuts through the machinery noise]
    "A man in a crisp suit emerges from a pickup — an Aurelia project manager, eyes hard and measured. He wears the company's logo like armor. He walks to the security perimeter with engineers flanking him."

    "Project Manager" "This site is essential infrastructure. Any interference risks people. You need to leave."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We're not trying to interfere with people's jobs.' (You step closer; the crowd leans with you.) 'We're trying to protect them. Your wall might protect buildings, but it kills the shore that feeds the harbor."

    "Project Manager" "Those are technical claims. There are processes. File a complaint."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "No — we will not be pushed into paperwork while machines eat the shoreline.' (He lifts the Polaroid in the air like a flag.) 'We documented the system today. We documented the community."
    # play music "music_placeholder"  # [Music: Crescendo — fast strings and percussion; the air feels like it could break into sound]
    "A reporter pushes through, mic extended."

    "Reporter" "There are calls to the regulatory office — we have a live line. Are you prepared to be cited?"

    maya_reyes "Prepared for consequences is different from prepared to be silent."
    "Suddenly, a different sound: the blunt, official timbre of a regulator's voice on a handheld speaker. A vehicle with blue markings pulls up; two officials step out, badges glinting. The crowd parts with the collective inhale of a town holding breath."

    "Regulator" "This is the Coastal Management Office. We're here to assess claims and ensure compliance. Please stand by."
    "Relief and adrenaline collide inside you like waves. The demonstration, which had been a risky provocation, now has a witness whose authority matters. Cameras pivot. Phones light up. The tempo of the day flips from confrontation to scrutiny."

    menu:
        "Explain the ecological claims directly to the regulators":
            "You kneel in the mud, opening your field notebook and pointing to charts, tide gauges and community observations; the regulators' faces shift from neutral to rapt."
        "Call Asha and ask for a scientist on record":
            "You pull out your phone and put it on speaker; Asha's voice comes through, steadying and precise, and the regulators listen as if a lighthouse had spoken."

    # --- merge ---
    "Continue at the next visual beat"
    hide maya_reyes
    hide eli_navarro

    scene bg ch14_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Swell — hopeful brass underpins the urgency]
    "The regulator listens, pen poised. You hand over your sensor logs, your Polaroids, the printed lab notes Asha left in your vest. You think of the pier that vanished when you were a child — the"
    "one that taught you the shape of loss — and you fold that memory into the dataset. You make the empirical human."

    "Regulator" "We'll open an incident review. Until then, we'll be instituting a pause on pile operations pending independent monitoring."
    "A cheer rises from parts of the crowd like a wave breaking. Others mutter. You see faces transform: hope bright, fear darkening edges. The project manager's jaw tightens into an impossible line."

    "Project Manager" "That is an overreach."

    "Regulator" "It's temporary."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Temporary can be enough to stop something irreversible."
    # play sound "sfx_placeholder"  # [Sound: A phone rings loudly in Tomas's pocket; he stares at the screen, then into the mud where you've been planting. He lets the call go to voicemail.]
    hide eli_navarro

    scene bg ch14_601bcb_5 at full_bg
    "But the pause is not a triumph without cost. The mood in the crowd frays almost immediately: some neighbors clap and hug; others cross their arms, voices taut."

    "Neighbor (older woman)" "You put my son's job at risk. He can't afford a buyout — we need work."

    "Neighbor (young fisher)" "You risked fines. You could have been arrested. Do you know what that does to a family account?"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I know. I don't — I couldn't —' (Your sentences trip; the urgency makes you clumsy.) 'I thought the demonstration would draw attention. I didn't want anyone hurt."
    "Tomas steps forward from the shadows of the pallets. He is not shouting; fury has made his voice low and controlled."
    show tomas_reyes at right:
        zoom 0.7

    tomas_reyes "You made a spectacle in front of our livelihoods. You think putting plants in the mud is noble? You think applause pays the rent?"
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "Tomas, we—"

    tomas_reyes "Don't 'we' me. You stood with me when I fixed your boat. You stood with me when the pier collapsed. Where were you when Aurelia was giving out buyout checks two blocks over? Don't make this a virtue play."
    "A hush like the surface of a bay falls; your internal tide pulls tight. You hear the accusation in every syllable and the brotherly wound beneath it. The crowd splits into shards of loyalty and grievance."

    maya_reyes "I'm sorry. I didn't mean to make anyone choose me over their work."
    "Tomas's eyes are wet. For a moment he looks like the little brother who used to climb on your back while you planned tidal models for fun. Then he sets his jaw."

    tomas_reyes "Just don't make us choose in the dark."
    "Eli Navarro reaches for you; his hand finds yours in the muddle. Fingers intertwine, firm and human."

    eli_navarro "We didn't come to make enemies. We came to open options."

    tomas_reyes "Options don't pay the rent."
    # play music "music_placeholder"  # [Music: Tension remains high — strings minor; drums sharp but now threaded with a rising, hopeful motif]
    "Later that evening, an emergency council meeting is convened. The chamber is packed; lights are harsh; the air tastes like takeover and possibility. Councilor Marco calls the meeting to order with the careful voice of a man conscious of a tipping scale."
    hide maya_reyes
    show councilor_marco_lin at left:
        zoom 0.7

    councilor_marco_lin "We have a lot to unpack. Aurelia has agreed to a temporary pause and to fund independent monitoring. We'll need to decide how to manage this pause and how to communicate with residents."
    "June Park [composed, razor-sharp]: (sits near the front) Her mouth is a tight line. Across from her, Rosa speaks into the microphone, her shawl a flag of lineage and stubbornness."
    hide tomas_reyes
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "We must protect our people and our shore. We cannot be bought off by short-term solutions."
    hide eli_navarro
    show june_park at center:
        zoom 0.7

    june_park "We need infrastructure that protects property immediately. We must be pragmatic."
    "You rise. The room narrows into a corridor of attention aimed directly at you."
    hide councilor_marco_lin
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "This pause gives us leverage. Not a victory — leverage. We can insist on monitoring that the company can't spin away. We can demand community representation in the oversight. We can fund living prototypes that protect jobs and shorelines at once."

    june_park "And what if those prototypes fail? Will you take responsibility when a storm hits?"

    maya_reyes "I'll take responsibility for trying to keep the shore alive. For trying to keep us here without erasing what makes us a town."
    hide rosa_alvarez
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "We can design guardrails. Hybrid approaches. But the community needs a seat at the table, not just noise on the airwaves."

    june_park "Community control slows things. It also can save lives, if done well."
    "The room hums. Councilor Marco narrows his eyes at both of you, then at the gallery. In the end, he nods."
    hide june_park
    show councilor_marco_lin at center:
        zoom 0.7

    councilor_marco_lin "We'll accept Aurelia's temporary pause and the independent monitoring they fund. We'll form an oversight committee that includes community members. The details will be hashed in the coming days."
    "A sigh passes through the room — some relieved, some wary. The decision is partial; it is a hinge that will not solve everything but will open a new seam in how the town negotiates power."
    hide maya_reyes
    hide eli_navarro
    hide councilor_marco_lin

    scene bg ch14_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Crossfade to softer, warm strings — the tempo slows but the emotional charge remains high]
    "A week later, at the tidal steps that lead to the old lighthouse, you and Eli Navarro find each other. The stones are still wet; the fog is low and forgiving. The fight has left both"
    "of you with a strange glow — rawness wrapped in the knowledge that something changed."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Your hands still smell like mud."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And your Polaroid is still smudged."

    eli_navarro "It captured the moment.' (He holds it up between you; the image is grainy — your hands in the soil, Tomas at the edge, the sheet piles ghosting behind.) 'Sometimes a blur is better than a perfect shot."

    maya_reyes "Sometimes a blur is all we can do when things are moving too fast."

    eli_navarro "We pushed harder than either of us expected. Some people are angry. Tomas is angry. People were scared. But you moved a whole room to put monitoring on the table."

    maya_reyes "I couldn't have done it without you. You were steadier than I felt."

    eli_navarro "And you were the pulse. You made them see it wasn't a stunt."

    maya_reyes "We broke things."

    eli_navarro "And we mended some of them."

    maya_reyes "Will some stay broken?"

    eli_navarro "Maybe. We keep working. We keep asking for seats at the table. We keep planting. We keep listening."

    maya_reyes "I was afraid we'd lose you in the shouting."

    eli_navarro "I nearly lost you when I thought you weren't listening to the cost.' (He inhales; the tide answers.) 'But we rebuilt faster than we broke. Not because we ignored the cracks, but because we found each other at them."
    "You both look out at the water. The lighthouse is a silhouette — its beam a slow, patient promise."

    menu:
        "Promise to Tomas you'll work the oversight plan with him":
            "You turn your shoulder to the harbor and promise, feeling the weight of the words not as a burden but as a pact; Tomas will hear it, and it will matter."
        "Promise Eli you'll step back sometimes and listen":
            "You lean into Eli, hands still in his, and promise to step back from the fight when needed — to let people breathe — while keeping your convictions."

    # --- merge ---
    "Continue at the next visual beat"

    eli_navarro "We can't erase the bruises, Maya. But we can tend them. We can invite people into the repair."

    maya_reyes "Repair is messy."

    eli_navarro "We have calluses."

    maya_reyes "We have a town."
    hide eli_navarro
    hide maya_reyes

    scene bg ch14_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide moves; pebbles shift; a gull wheels once and is gone]
    # play music "music_placeholder"  # [Music: Warm, resolving chord — full strings and a gentle harp arpeggio]
    "Later, Tomas shows up at the oversight meeting. He sits across from you, not at your heel but as an equal and an interlocutor. He reads the monitoring data with skepticism and a craftsman's eye. He"
    "asks hard questions in a voice that still carries his hurt. You answer truthfully; you also ask him how repairs can look from his storefront. He offers ideas about hiring local crews for marsh planting, for"
    "combining living modules with temporary protections that let fishers work."
    "Asha and Rosa push for transparency; Councilor Marco negotiates process; June Park watches the committee like a player studying a chessboard. Aurelia's funded monitors show early signs of reduced sediment loss in one baylet where a"
    "living module took hold. The result is not victory — it is a beginning: scaffolded, fragile, real."

    scene bg ch14_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Triumphant but tempered — a bright woodwind flourishes into an undercurrent of calm]
    "At the market the next full moon, you and Eli Navarro walk under a canopy of string lights. People talk about the monitoring numbers over grilled fish and cilantro. A child points at a newly sprouted"
    "patch of cordgrass and laughs. Rosa hands you both cups of coffee — too bitter and perfect."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You shook the tide, but you gave it hands to hold. Don't forget us when it gets easy."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We won't. We will teach."
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "We will build things that hold both water and memory. We will make room for work and shore to exist together."

    maya_reyes "That will take years."

    eli_navarro "Good thing we're stubborn."
    "You rest your head against his shoulder as the harbor glows like a scattered constellation. The city's scars are visible — sheet piles rising, a few boarded storefronts — but there are also lines of green, small but relentless, threading the edges."
    hide rosa_alvarez
    hide maya_reyes
    hide eli_navarro

    scene bg ch14_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Full, conclusive motif — strings, brass, and a warm cello line carrying the final notes]
    "You think of the cost: the burns of argument, the people who will need time and aid, the streets that won't be the same. You also think of clarity: that your work made a visible argument"
    "that couldn't be unread. Aurelia paused; independent monitors are funded; the oversight committee exists; the community has a voice at the table. None of it is complete. All of it is an offer — to repair,"
    "to reconcile, to keep trying."
    "Your chest is full of tired. Your hands are streaked with salt and soil. You are both smaller and larger than you were at dawn. You have learned that love and resilience are not separate projects"
    "but the same work, done in different languages — some days with data, some days with hands in dirt, some days with a Polaroid that trembles into the right frame."
    "Eli Navarro squeezes your hand. 'We keep going,' he says."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We keep going."
    hide maya_reyes

    scene bg ch14_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: Resolve — a single, sustained chord that slowly fades into the sound of tide and wind]

    scene bg ch14_601bcb_11 at full_bg
    "THE END"
    # [GAME END]
    return
