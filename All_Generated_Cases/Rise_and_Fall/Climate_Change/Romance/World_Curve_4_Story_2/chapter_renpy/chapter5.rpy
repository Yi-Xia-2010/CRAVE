label chapter5:

    # [Scene: AquaWorks Research Station | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, rising piano with a warm pad that promises progress]
    # play sound "sfx_placeholder"  # [Sound: Low fluorescent hum, occasional drip of water from an overhanging pipe, the scrape of a chair leg on concrete]
    "The lab smells of metal and coffee — antiseptic glass softened by the oil and wet wool of people who have been awake too long. You step inside with your field journal heavy in your bag"
    "and the memory of yesterday’s dawn still warm behind your ribs. Momentum hums in your bones: volunteers showed up early, sensors started pinging, the dashboard lit green where it once blinked red. That tiny victory follows"
    "you like a buoy."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tablet tap; low murmur of voices]
    "Dahlia Kestrel stands at the head of the table with her tablet angled toward the room. Her suit is too clean for this space, but the light picks out the teal seams of her design overlays;"
    "the schematics slide and rotate with an assuring efficiency. She gestures with one gloved hand as if conducting the map itself."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "Our phased installation reduces immediate exposure across the most vulnerable sectors. Prefab segments drop into place — minimized downtime, measurable metrics, and demonstrable protection within months."
    "You step closer, palm against the cool edge of the table. The screen reflects in your hazel-green eyes; the modular segments look tidy and clinical, a promise in steel and algorithm. Your fingers itch to mark"
    "a tidal cut or a low channel that would, if sealed, strand fish and choke the marsh."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Prefab moves fast. It also risks cutting off connectivity. The marsh isn't a static bump — it's a series of flows. Tidal corridors need to breathe, or we lose nursery habitat and the sediment flow that rebuilds our shore."
    hide dahlia_kestrel
    hide maya_reyes

    scene bg ch5_4001e7_3 at full_bg
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "We can include hydraulic gates. They're programmable. You get seasonal exchange without sacrificing structure."
    "The word 'programmable' tastes of compromise. You know gates can fail, or be closed in a panic, or be managed without the town's knowledge. Your journal is a map of lived seasons; Dahlia Kestrel's tablet is a map of probabilities."
    # play sound "sfx_placeholder"  # [Sound: Footsteps at the doorway; a low, wind-worn voice arrives like a steady tide]
    show elias_kwan at right:
        zoom 0.7

    elias_kwan "If those gates don't line up with the lanes we use at dusk, people lose nets and income. How big are the openings? Where are you putting the haul zones?"
    "Elias Kwan fills the doorway in a way that makes the room breathe easier — a human-sized anchor. The oilskin coat is patched, the rope around his boot frayed. He crosses the lab and lays a"
    "hand on the table next to your sketch of a feeding shoal. You feel relief at his presence, and a fresh pressure too: whatever you choose now will shape both the town and him."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "We need open channels that match natural tidal heads, not just engineered openings. Size and timing matter. If the barrier shutters misalign with the tides, we destroy young fish runs before they can return."

    dahlia_kestrel "Your data is valuable, Maya. But the political reality is urgency. We can’t ask the town to wait for a two-year ecological cadence while storms keep coming. Visible results buy us social license."
    "You hear the logic and feel it — the media crews already circling, the mayor’s promises, the town's fragile patience. Visibility buys breathing room; but not if what you build kills what it intends to save."

    maya_reyes "My father used to say the tide remembers everything. If we build walls that the tide can't pass, the bay will remember our mistake. We can't be fast at the cost of erasing the thing we’re trying to protect."
    hide dahlia_kestrel
    hide elias_kwan
    hide maya_reyes

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Minor lift into hopeful strings; undercurrent of steady rhythm]
    "Dahlia Kestrel's face is unreadable in the fluorescent light — efficient, sharp, but not cruel. She's not an enemy; she is an acceleration. You sense the meeting is less an argument and more a negotiation between"
    "tempos: the quick beat of large-scale work and the slow, patient pulse of living systems."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "We can iterate. Start with the segments where risk is greatest, monitor exchange through embedded sensors, and adjust parameters remotely. We demonstrate impact and refine the detail as we go."
    show elias_kwan at right:
        zoom 0.7

    elias_kwan "Remote adjustments are fine until the net is on the line and the machine says it's closed. Who's liable when a season's catch is lost? Who's on the dock at three in the morning checking an app?"
    "You feel the room tighten around that question. It is not just technical — it is moral, legal, and intimately tied to the trust of the people who have lived by the bay for generations."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "Community oversight on operational triggers. Not just data feeds to a corporate dashboard. If we’re going to rely on gates, the people who fish these waters need real authority — trained operators, legal recourse, local employment tied to maintenance."

    menu:
        "Slide your journal's annotated channel overlay across the table toward Dahlia":
            "You push the paper gently; your tidal diagrams lie over the schematic like a counterargument made of ink. Dahlia Kestrel’s fingers hover over the margin notes, and for a beat you see curiosity in her face."
        "Tap the tablet and pull up a simulation of the deployment timeline":
            "You summon a timeline on the screen; the months stack like dominoes. She watches the blocks fall into place, then pauses, calculating how to compress them without breaking the sequence."

    # --- merge ---
    "Conversation continues with Dahlia Kestrel responding."

    dahlia_kestrel "Data and lived maps together — that's useful. If you can show me specific corridors that must remain open, I can model gate placement to reduce ecological impact while keeping install time short."
    "You feel a small, cautious optimism flare. The room had been set for a clash; instead, it shifts toward synthesis. The momentum that hums in you finds another beat in the lab — a shared problem, not a zero-sum game."

    elias_kwan "If she can make openings that line up with the old east channel at low tide, my brother’s nets will work. If you mark those on the plan, I'll bring people to help with the placements and the sea trials."
    "Your heart quickens at the offer. It's more than labor — it's a vote of faith from the docks. You think of the nights you and Elias Kwan have stayed late testing salinity probes, the quiet"
    "way his laughter steadies you. The choice you make now will test the seam of that trust — between urgency and careful repair, between your impatience and his steadiness."
    hide dahlia_kestrel
    hide elias_kwan
    hide maya_reyes

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Hopeful motif swells, synthesized strings threading through acoustic notes]
    "A lab tech appears with two steaming cups of coffee and a third in a travel mug with a faded floral sticker — your source of comfort left on the table earlier. Steam softens the hard"
    "edges of the schematics. For the first time in days, the design conversation feels like a rehearsal for something that could actually work: technical rigor braided to community stewardship."

    menu:
        "Accept Dahlia's invitation to model corridor placements together":
            "You dip your pen into the margin and start annotating known feeding lines. Dahlia Kestrel taps as you speak, the simulation redrawing with each mark. It feels like choreography."
        "Pause and insist on writing legal clauses for community oversight before modeling":
            "You draw a box around the operation triggers and sketch a clause outline. Elias Kwan nods slowly — it's slower, but the framework you create glows with the shape of accountability."

    # --- merge ---
    "Conversation continues with Dahlia Kestrel proposing milestones and integrated phases."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "I can work with corridors in the model and we can draft an operational charter. But we need milestones — visible milestones — for the town. How do we save lives and livelihoods now while building trust for the longer work?"
    "You stare at the schematic, at the places your pen trembled when you marked tidal cuts. The media will want a story: quick wins or principled delay? The mayor wants headlines. The volunteers want to know"
    "work is happening. Your hands feel both nimble and weighted as you trace a line that could become policy."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We design for both. Short-term protective geometry where risk is acute, and simultaneously finance and install living marsh buffers that rebuild the shoreline. Jobs today — restoration training tomorrow. That’s how we keep the town whole."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "That sounds like the kind of plan my neighbors can sign onto."
    "Dahlia Kestrel studies you both, then taps a stylus against the screen as if counting off possibilities."

    dahlia_kestrel "Operational milestones, integrated marsh phases, and a community advisory role written into the charter. It’s more complex, but plausible. It slows us a little. It also makes for a stronger proposal when you can promise jobs and local oversight."
    "The room exhales and inhales at once. There is friction, yes, but the friction sparks a clearer shape than either market logic or local lore could produce alone: a hybrid that might actually work."
    hide dahlia_kestrel
    hide maya_reyes
    hide elias_kwan

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum brightens — machines and people in sync]
    # play music "music_placeholder"  # [Music: Ascending strings resolve into a warm chord]

    "Your hand trembles when you underline the note. In your head your father's voice returns, calm as the tide" "Tides remember, Maya. Build for the remembering."
    "Everything narrows to the next tactical move. The room awaits your stance: Will you nudge the plan toward the rapid, visible deployment that buys political breathing room? Will you insist the marsh buffers are non-negotiable, even"
    "if they slow the timeline? Or will you press for legally binding community co-management before any breakground — risking Dahlia Kestrel’s patience but guaranteeing local control?"
    "You blink, tasting salt and coffee, and reach for your pen."

    jump chapter6
    return
