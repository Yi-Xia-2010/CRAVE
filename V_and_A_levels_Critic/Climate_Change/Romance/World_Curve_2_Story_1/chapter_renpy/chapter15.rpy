label chapter15:

    # [Scene: Wave Innovation Lab | Night — hours after the breach]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Alarms—short, insistent beeps—layered over the ocean's steady roar beyond the pilings]
    # play music "music_placeholder"  # [Music: Driving percussion with an underlying minor-key synth—relentless, urgent]
    "You come in wet. Salt flakes along your jacket collar, hair plastered to your forehead. The lab smells of ozone and solder and the faint, persistent tang of the sea. Your hands are black with grease"
    "where you gripped a buoy's casing; your palms still remember the cold bite of the water."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "We lost two anchors in the northwest channel when that flank hit. The modular clamps sheared—' (he cuts himself off, breath sharp) '—but the node mesh held. If we reroute the array we can compensate, at least until dawn."
    "The graphs on the screen spike and fold like a broken heartbeat. You read numbers as if they were tide lines on a body—where pressure rose, where it broke."
    "Your throat tightens. This is what you wanted: something that could be scaled, that could buy time. But the buying feels like bargaining with the sea itself—small victories traded for an uncertain tomorrow."

    mateo_alvarez "We need crews on the eastern piers now. Etta's pulling the nursery teams into assembly. Jun's out with the boats. I can keep the control loop stable if someone coordinates field teams without tripping the maintenance contracts."
    "You glance at the lab console; there, a blinking message from Elio Sato's firm — terse, polished, offering funds and an engineer liaison with a signature that shimmers corporate-blue. The note smells of investment and knots—solutions that come with strings."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "What does 'liaison' mean this time?"

    mateo_alvarez "It means they can give us the parts faster than we can fabricate. It means satellite uplink for the mesh. It means—' (he swallows) '—it means oversight, Ari. Contracts. Data-sharing clauses."
    "Mateo Alvarez's hands hover over the keyboard like he's holding an apology."

    ari_tanaka "We accepted community deployment. We promised the town control. We can't hand over everything because it keeps us afloat for one season."

    mateo_alvarez "I know.' (he turns, urgency sharpening him) 'But right now it's not about future clauses. It's about keeping fifty houses from flooding again tonight. We don't have the luxury of idealism when the next surge could wipe the docks clean."
    "Your chest hammers; the lab's neon light feels too thin to hold so many decisions. Outside, the sea hammers pilings with a force that makes the building vibrate. The teams are already moving—people you know by gait and name—dragging buoys across slick planks, shouting over the wind."
    hide mateo_alvarez
    hide ari_tanaka

    scene bg ch13_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo—percussion and synthetic swells—heightens the urgency]
    "Etta: (coming up the lab stairs, rain streaking her hair, voice like crushed paper) 'The eastern array can't be left undermanned. If that channel fails, the water will take the low blocks first—your mother's street will be the first to go, Ari.'"
    "You flinch at the mention of family; the image of the old Tanaka house, its porch warped by salt, flashes abrupt and raw."
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "Then we stop the eastern breach.' (your voice is steadier than you feel) 'Mateo, route me a team. I'll handle coordination on the ground. We can't let the fabric tear."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "And the contracts?"
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "I'll negotiate terms with Elio Sato. Short-term access. No proprietary lock. We keep community custody of the control protocols."
    "Etta studies you both, a slow, wary breath. 'You both say 'we' like you can make promises that don't rip people apart.'"

    ari_tanaka "We make the promises we can keep."

    menu:
        "Stay at the console":
            "You pull the lab console closer and keep the maps in your sightline, diverting signal traffic and issuing assignments over the radio. Your voice is precise; commands cut the noise into work."
        "Go to the eastern piers":
            "You grab a harness and sprint down the ramp, boots slapping planks. Saltwater hits your face; you shout, torque a clamp with hands that have started to shake, and help steady a buoy as it finds its hold."

    # --- merge ---
    "Whichever you picked—if you stayed, the monitors reflect your face, jaw clenched; if you went, cement and tar hiss under your boots, and a child's plastic toy bobbing in a pooled gutter reminds you why you move—both are intimate, both are costly."
    hide ari_tanaka
    hide etta_hargrove
    hide mateo_alvarez

    scene bg ch13_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Rapid staccato strings — the tempo quickens toward a peak]
    "The night becomes work and crisis braided together. The buoys lock systems into a fragile lattice that hums like a second heartbeat beneath the town. Volunteers rotate between hands-on wrestling with hardware and radio relays that"
    "sound like prayers. You hear names—Jun, Mara, Councilor Rosa—spoken into the dark, each one a weighted life. The lab's LED status bars flick green, then orange, then red, and everyone recalibrates hope."
    "Each time a buoy reports stable, something in your chest loosens—then tightens again as you remember the cost. These machines are stopgaps. They will need parts, money, institutional permission. In exchange, Elio Sato's message grows more"
    "insistent, asking for 'shared telemetry' and 'regional rollout.' His tone is that of a man trying to be kind while moving chess pieces."
    # [Scene: Tidebridge Harbor | Night — the surge hits]

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A roar that drowns radios for a breath; the lab's alarms spike into a continuous wail]
    # play music "music_placeholder"  # [Music: Full, chaotic timpani with a high, keening synth—panic reaches a fever pitch]
    "The ocean finds a weak seam. Water sluices past low-stacked sandbags, kisses thresholds of houses, and drags a rusted bicycle down the road like a child's ghost. Someone screams—maybe a warning, maybe a name—and it tears like something pulled wide."
    "You run. You move through a crowd that feels like a living chain—hands passing rope and tools, breath visible and ragged. You see Jun at the edge, hauling a buoy line, the set of his shoulders"
    "like iron. For a second he meets your eyes and there is a flash of accusation, of fear, and then a jerk of a smile that's not a laugh."
    "Jun: (shouting over the surf) 'Ari! The north block's water's jumped the break! We need a makeshift sill!'"
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "I know—pack the coir, wedge the logs—Etta's got the pattern. Mateo, can you stabilize the node there?"
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "I'm trying. The relay's flaring. If we reroute power we'll lose telemetry for ten minutes, but we can anchor the array manually."
    show jun_park at center:
        zoom 0.7

    jun_park "Ten minutes is a lifetime with this surf."

    mateo_alvarez "Then we do it now."

    ari_tanaka "Do it."
    "The world narrows to the work: hands, salt, the rope between you that keeps someone from washing away. Your body moves as if with muscle memory—torquing bolts, holding a buoy while others secure it—some primal choreography"
    "of survival. Noise is a physical thing: the ocean, the screech of metal, the shallow, panicked prayers."
    # play music "music_placeholder"  # [Music: Climactic peak—everything tight, relentless]
    "For a breath the buoys hold. A shudder passes through the line as if the sea tests and retracts, and the tide's roar eases like a released breath. Somewhere nearby, someone cries. You don't know if it's relief or grief."
    hide ari_tanaka
    hide mateo_alvarez
    hide jun_park

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lab's alarms shift to a long, lower tone. Radio chatter turns from sharp commands to muttered assessments.]
    "The immediate crisis eases enough to measure damage. The eastern blocks are sopped but standing. The north had a few basements flooded; one family lost the ground floor. A child’s toy floats in a flooded stoop like a small, stubborn buoy—untethered, refusing to sink entirely."
    "Etta: (sits on a crate, hands clasped, voice broken) 'We kept people from drowning. We kept roofs. But we lost a dozen small businesses and Mrs. Hargrove's bakery—gone.'"
    "You feel hollow. Everything you wanted: saved, fractured, compromised, expensive. The buoys bought time, yes—but they cost maintenance contracts, municipal oversight, and now a new kind of governance that smells faintly of brokerage."
    # [Scene: Wave Innovation Lab | Early Morning]

    scene bg ch13_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: A lower, grief-soft piano motif—heavy but unresolved]
    show elio_sato at left:
        zoom 0.7

    elio_sato "You did what needed to be done. The data you collected over the last twelve hours is...invaluable. Imagine scaling this across the whole estuary. We can underwrite production and deployment—fully funded, rapid rollout."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "At what cost?"

    elio_sato "Data access. Regional monitoring rights for optimization. A limited governance seat on maintenance protocols. We don't want to own the town—we want to make the system interoperable. We need telemetry to improve the models."
    "His eyes flick to Mateo Alvarez for reaction, then back to you. There's a tilt of the head that is almost humane, which somehow makes the offer worse: a man who understands softens the edges of a leash."
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "If we sign over live telemetry, they can decide when to shut down nodes, when to prioritize areas. They'll have decision weight."

    elio_sato "We'd build the system to protect the greatest number of assets. Public-private partnership models mean fewer failures and faster repairs. It isn't about power—it's about scale and lives saved."
    hide elio_sato
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "Scale that leaves people out is still a scale into erasure."
    hide ari_tanaka
    show elio_sato at right:
        zoom 0.7

    elio_sato "If you want total autonomy, you'll need sustained capital. Philanthropy dries up. Grants are limited. Corporations can provide a network effect that compresses response times."
    "The words are all calculus. Lives turned into functions. You look at the map of the town projected onto the wall—blocks colored by risk—and you see the math of what he proposes. Neighborhoods with higher assessed"
    "value cluster green; older, lower-income blocks sit orange and red. His model would maximize 'assets.' Your town is not a series of assets."
    hide mateo_alvarez
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "If we let you in, we risk prioritizing moneyed blocks over low-asset homes. We risk people waking up one day to find their node throttled because the return calculus says so."

    elio_sato "We can write safeguards into the agreement. Oversight committees. Community liaisons—"

    ari_tanaka "You mean appointed oversight with veto power."

    elio_sato "Ari, I'm offering stability. It's messy, yes, but your people can sleep without waiting for the next breach."
    hide etta_hargrove
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "They're offering what we don't have. Parts, manpower, redundancy. We can keep this town standing—if we take the deal."
    "You look at Mateo Alvarez as if seeing him for the first time tonight: wind-creased face, hands raw, an exhaustion so total it looks like a risk. Love and strategy knot messy in your chest."

    ari_tanaka "And in exchange?"

    mateo_alvarez "In exchange we take the maintenance contracts—guaranteed funding for teams from here. In exchange we accept joint governance, but we nail down clauses now that lock community veto on any regionally prioritized throttling."
    hide elio_sato
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "Words are sand when the tide comes."
    "Jun: (quiet, he has been listening) 'I'm moving up the ridge.'"
    "Heads swivel. Jun stands framed by the lab door, rain beading on his cap, face set like flint."

    ari_tanaka "Jun—"
    hide ari_tanaka
    show jun_park at center:
        zoom 0.7

    jun_park "My nets were gutted. My house is the kind that will be picked over first if the buyouts start. Council's been offering relocation aid. I can't keep patching a hole for someone who'll buy me out when it suits them."
    hide mateo_alvarez
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "We don't know that will happen—"

    jun_park "We know what happens when 'optimization' meets poor people. They get optimized out.' (his voice cracks) 'I can't watch Mom lose the shop because someone said it was less valuable. I hate the thought of leaving. But I can't gamble the next few years on promises."

    menu:
        "Reach for Jun's shoulder":
            "You step forward and place your hand on Jun's shoulder. He flinches, then relaxes into the contact for a moment. Your fingers find callus and salt, and for a second the storm's noise recedes."
        "Hold back and listen":
            "You let Jun speak without touching him. You watch his jaw work; you hear the decisions in his voice. Your restraint keeps the space between you honest—no soothing words, only listening."

    # --- merge ---
    "The lab is a furnace of decisions. People whom you love are making choices that will fracture the town into those who stay and those who leave, those who have power and those whom policy will"
    "categorize as expendable. The buoys kept water from swallowing every street, but they also created a dependency that invites actors with capital and leverage."
    "The lab is a furnace of decisions. People whom you love are making choices that will fracture the town into those who stay and those who leave, those who have power and those whom policy will"
    "categorize as expendable. The buoys kept water from swallowing every street, but they also created a dependency that invites actors with capital and leverage."
    # play music "music_placeholder"  # [Music: Tense low strings—the arousal doesn't drop; instead tension tightens into a hard, unbearable point]
    "You and Mateo Alvarez stand in the middle of it all—two people who have sewn plans together with wire and sweat. The world narrows to him: the way his hand trembles when he finally turns to you, how his eyes go soft when he tries to smile."
    hide etta_hargrove
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "I didn't sign anything yet. I wanted us to decide together. I wanted you."

    ari_tanaka "You wanted me.' (you repeat the words as if testing the sound) 'I wanted what we started to stay ours. But I also wanted to keep people from drowning tonight."

    mateo_alvarez "We saved people. We kept the harbor from becoming a grave. That matters."
    "Guilt pulls taut in your chest. The town looks to you to be the moral compass and the operator. You have failed in the purest sense and succeeded in the pragmatic one. It feels like walking"
    "a shoreline of broken glass and knowing only the soles of your boots will carry you."
    "You step toward him, and the lab's dim light bakes the salt in your eyelashes. He reaches for your hand—brief, hopeful, absolute."

    mateo_alvarez "If we make this commitment—if we sign a coalition agreement that keeps community veto and maintenance jobs local—I'll marry you, Ari."
    "You laugh—it's a small, sharp sound—and then you realize you are crying, the laugh curdled into salt."

    ari_tanaka "Don't make promises to fix the future with vows."

    mateo_alvarez "I'm not promising the future. I'm promising to be in it with you. To stand in it while we fight."
    "Ari Tanaka: (you breathe in) 'Then stand with me.'"
    "He does. It is not cinematic. It is two people standing in a lab that smells of grease and coffee, hands clasped for just long enough to make the promise—small and defiant."
    hide jun_park
    hide ari_tanaka
    hide mateo_alvarez

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Piano chord—soft but unresolved; underlying percussion still ticks—this is no closure, only the hush after the immediate storm]
    "The town will sleep in shifts. Repairs will become routine. Maintenance contracts will bind the buoys to paid technicians and bureaucratic reviews. Elio Sato will draft terms; the council will haggle; some clauses will pass, others"
    "will be fought tooth and nail. The stability you bought tastes metallic in your mouth: safety threaded with obligation."
    "You try to tally wins. Houses still stand. People still have roofs. Children woke up. But you feel a thousand small losses: a bakery gone, Jun leaving, the nursery's seedlings crushed in low places. The cost ledger will be long."
    "You and Mateo Alvarez walk together out toward the harbor at first light. The sky is a bruised watercolor—ash and the briefest hint of pink. The pilings are scattered with detritus; the buoys bob like tired"
    "sentries. The town looks both saved and altered, familiar in shape but changed at the edges."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "We did what we could."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "We did what we had to."
    "He squeezes your hand. There is no fireworks. There is a small, honest steadiness—knees bruised, hands filthy, hearts taxed. Around you, people clean, make lists, grieve. The political negotiations will come. Contracts will be signed. Some"
    "families will take offers, move to higher blocks with relocation aid. Others will stay and tend what remains."
    "In the end, the sea did not stop. You built a machine that held it back for a while and created a new set of rules for who gets protected and whose losses are catalogued as acceptable. That is the bitter truth."
    hide mateo_alvarez
    hide ari_tanaka

    scene bg ch13_601bcb_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant call of a gull; hammers in the distance; a child's laughter that sounds small and fierce]
    # play music "music_placeholder"  # [Music: A low, elegiac string note—final, not reconciled]
    "You lean your forehead against Mateo Alvarez's shoulder and let the salt dry on your cheek. He rests his chin on your head. It's an anchor that says you will not be alone carrying this weight. That is solace, but it does not erase the ledger."
    "The buoys bought time. They bought breaths, and breakfasts, and the warmth of sleeping children. They also opened a door to a future where data is currency and decisions are brokered. You made a choice that"
    "holds people now—and shifts risks onto the uncertain shoulders of governance and capital. You have a partner at your side. You have a town that is bruised and breathing."

    scene bg ch13_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, held chord—resigned and heavy]

    scene bg ch13_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
