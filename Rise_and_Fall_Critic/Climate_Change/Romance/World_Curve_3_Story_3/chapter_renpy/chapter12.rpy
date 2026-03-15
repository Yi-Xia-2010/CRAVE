label chapter12:

    # [Scene: Dunes — After the Decision | Dusk]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind combing over sandbags; a distant horn from a fishing trawler]
    # play music "music_placeholder"  # [Music: Low, weathered cello; a steady, minor-key ache]
    "You chose the path no one asked for aloud. You chose to be the hand that draws the line under the town's maps and says which neighborhoods will stay, which will be let go, and how"
    "people will breathe after they move. The choice sits like a stone in your throat—heavy, necessary, and cold."
    "Finn is beside you, quiet in a way that makes the world shrink to the size of his shoulders and the wind between them. Elias Novak is halfway between the barricade and the dunes, lips pursed"
    "against the wind. Noah Kestrel stands a little apart, hands hidden, as if the math of compromise were something he keeps in his pockets. You feel all of them like heat and pressure on the same"
    "membrane."
    "You fold the page of your notebook back over the ink you wrote earlier—schemes, contingencies, supply chains. The compass at your throat presses, warm against the cord. The red thread around your wrist tugs at the promise you made and the weight you have now accepted."
    # [Scene: High Tide Laboratory | Night]

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The constant slap of ocean against hull; faint beeps of tide sensors]
    # play music "music_placeholder"  # [Music: A taut single violin — tension held just before release]
    "The lab smells of ozone and seaweed and the kind of coffee that has been reheated twice too many times. Dr. Hana Park moves through the light with small, efficient gestures, as if she can arrange"
    "data the way one arranges anchors. She sets a tablet down and taps; a projected map blooms over the metal table, tide-lines braided into layers like tree rings."
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "You came alone,' (she says, not accusation, more a cataloging of fact) 'and you brought conviction."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I brought a plan,' you answer, more steady than you feel. 'Or at least, the start of one."
    "Dr. Hana Park: (leaning in, fingers hovering over the projection) 'Tell me what you mean by 'plan.' Speak technically. I need the scaffolding under the rhetoric.'"
    "There it is—her request for scaffolding. The scientist in her wants the bones. The leader in you wants the warmth of people to soften them. You inhale the sterile air and lay out the bones anyway:"
    "phased relocation, living shorelines where possible, formalized buyouts for the most at-risk blocks, a Rooftop Sanctuary relay to hold people and supplies during peak tides, and floating caches that double as community pantries."
    "You watch Hana's face through the orange light—eyes shadowed, jaw working as she sorts the ethical weight."

    dr_hana_park "Phased relocation is the cleanest way to reduce mortal risk. But—' (she taps an area of the map and the buildings there bloom red) '—sacrificing historic blocks is not just urban planning. It's cultural amputation."

    maya_serrano "I know,' you whisper. 'People's memories are there. Lives folded into porches and family rooms. But if we don't move some lines voluntarily, the water will decide for us and we'll lose more than houses."
    "Dr. Hana Park: (quiet; she sets her hand flat on the table) 'There's a moral calculus here. Compulsory buyouts, staged evacuations—where you draw the line will define who survives and who remembers. Are you ready for that authority?'"
    "The question isn't rhetorical. You feel its teeth. Leadership has suddenly become a ledger and a weapon. Part of you wants to step back and let the slow politics bleed the edges of the crisis; another"
    "part, the part threaded with the neighbor you lost, will not let that be an option."

    dr_hana_park "If we go this way, we have to be surgical. Evacuation windows, redundancy in supply lines, real shelter capacity—not promises. The Rooftop Sanctuaries can be linked with solar pumps and desal units, but they'll need formal agreements with the building owners and a legal framing for temporary land use."

    maya_serrano "Rosa can mobilize café networks. Finn can—' (you stop, because naming people turns planning into risk) '—people will come if they can see a plan that keeps their kids and their dogs alive and gives them a place to sleep that isn't a wet school gym for months."
    "Dr. Hana Park: (a small, almost fond smile) 'You always think in people, Maya. It's why you'll be a good—but lonely—leader.'"
    "Her words fall like a recorded tide—predictable and inevitable. You grimace, feel the loneliness like cold steel at your ribs."

    menu:
        "Show the full, detailed map and data to the first volunteer cohort tonight":
            "You pull the tablet closer, flood the room with projection. Faces around you sharpen, awe mixed with fear. Volunteers understand the gravity; some step up immediately, others step back, eyes glassy. The room becomes a kiln where resolve hardens and fractures."
        "Simplify the briefing—show the human side and keep some technical specifics for later":
            "You fold the plans into a story: 'This is where we will sleep, this is where we will keep food.' The volunteers nod; their anger softens into practical questions. You keep the most volatile details—like which blocks are slated for buyout—off the table for now."

    menu:
        "Accept Elias's offer to co-lead community briefings":
            "You nod, letting the weight be shared. Elias's public energy pulls more faces into the room; the briefings swell with attendance, and anger sometimes quiets into questions. But you notice your name in the mouths of people less often, replaced by 'the organizers'."
        "Keep the logistics centralized—let Elias rally crowds, but keep plan control with you":
            "You shake your head, keep the tablet under your thumb. The meetings stay tidy, the plan stays precise. Still, Elias's disappointed look follows you out of every door, and some volunteers report feeling unheard."

    menu:
        "Tell Rosa and the rooftop volunteers that we'll start the first relay tonight—no more waiting":
            "You decide. Orders are given, anchors dropped. Volunteers move like an answering tide; boats are prepped, routes memorized. The town feels the shudder of action and, with it, a spike of fierce solidarity—then finger-pointing, then relief. The first night is long and cold, and some faces in the community remember how close they were to losing everything."
        "Delay public action one more day to finalize legal assurances with Hana and quiet fund-raising":
            "You ask for patience. Some understand, breathing out; others call you cowardly. The extra hours let you iron out paperwork and contingency plans, but the rumor mill accelerates: accusations that you're stalling for corporate deals begin to spread."

    menu:
        "Coordinate a controlled evacuation and Rooftop Sanctuary relays with Hana and Rosa.":
            jump chapter13
        "Sabotage Kestrel equipment to slow corporate construction and force renegotiation.":
            jump chapter15
        "Lead a mass blockade of development zones, prioritizing civil resistance.":
            jump chapter17
    return
