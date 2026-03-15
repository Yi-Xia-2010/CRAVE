label chapter9:

    # [Scene: Main Street | Noon]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Rapid strings underscoring a rising heartbeat — urgent, bright]
    # play sound "sfx_placeholder"  # [Sound: Mic feedback, the murmur of a gathered crowd, gulls distant]
    "You step up to the temporary podium with the town behind you and the bay like a living mirror at your back. The glare off wet boards paints everyone with a high, unforgiving light; it feels like the whole town is being photographed at once."
    "Your notebook is in your hand, pages damp at the corners. The brass compass at your throat is warm against your windbreaker. For a beat you feel the old automatic ache — the 'not enough' that used to tighten around your ribs. Then Asha's calm voice anchors you."
    show asha_malik at left:
        zoom 0.7

    asha_malik "We paired three years of sediment data with before-and-after imaging of the mudflats. The change isn't hypothetical — it's measurable and accelerating."
    "You hear Eli Navarro before you see him: a soft curse, the click of his camera closing, then the rough comfort of his presence as he reaches for your shoulder. His fingers are paint-speckled and steady."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "Those photos tell it plain. Where the piles go in, life goes quiet. Where we build back with the land, the tide learns to carry less harm."
    "You inhale and let the salt air fill your lungs. You did not come here to be perfect; you came to be heard. The reporter's light is a heat on your face. You imagine Tomas in"
    "the audience — the repair-shop bell you can almost hear in memory — and you let that tether you to the words."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "What we're asking for is simple: transparency, a pause on permits that will irreversibly alter the shore, and an independent study before any irreversible construction starts. We can protect lives and livelihoods without erasing the systems that support them."
    # play sound "sfx_placeholder"  # [Sound: A single camera shutter, then a swell in the crowd noise — a rising current]
    hide asha_malik
    hide eli_navarro
    hide maya_reyes

    scene bg ch9_3be532_2 at full_bg

    "Reporter (TV)" "June Park, Aurelia Holdings has called your group's claims 'alarmist.' Will you respond?"
    "June Park steps forward, composed and practiced. On live feed she is all smooth lines and cool logic — the kind of voice that makes hard choices sound inevitable."
    show june_park at left:
        zoom 0.7

    june_park "We appreciate community concerns. Our project aims to secure immediate protection for homes at risk. Engineering solutions have a proven track record of saving lives when time is short."
    "You watch the cameras pick at every inflection. June Park's words are precise; there is no malice, only a sharp belief in her method. But the narrative is shifting. The juxtaposition — Asha's slow, patient graphs,"
    "Eli Navarro's quiet Polaroids, Rosa's trembling hands holding an old photograph of Main Street before the first seawall — makes a picture no amount of corporate polish can clean."

    menu:
        "Adjust your notes one last time":
            "You smooth the page with a damp thumb, realigning the figures until they look like something tangible rather than a plea."
        "Fold the notebook away and look at the crowd":
            "You tuck the notebook into your vest and let your eyes travel over familiar faces—each glance adds weight to what you say next."

    # --- merge ---
    "The scene continues as the crowd reacts."
    "A hush passes as the footage runs on social channels; phones alight like fireflies. Within hours, Aurelia’s stock begins to wobble on the live tickers rolling across news feeds. The market doesn't care for nuance, only momentum — and momentum has turned toward scrutiny."
    # play sound "sfx_placeholder"  # [Sound: The distant electronic ping of browsers refreshing; then an audible murmur that becomes a cheer]
    # play music "music_placeholder"  # [Music: Brass surging — victory notes threaded with tension]
    "Eli Navarro moves beside you, hand finding yours with the ease of a practiced map-reader finding north. His palm is warm, rough with clay and plans. That small contact steadies you in a way words can't."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "They'll listen. People will look."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "They already are."
    "Later, off-camera, you and Asha argue through phrasing—how to phrase 'pause,' what legal language buys time without alienating those who need immediate assurance. The back-and-forth is fierce and intimate: two minds carving a way through specifics while the whole town waits on the other side of the glass."
    hide june_park
    show asha_malik at left:
        zoom 0.7

    asha_malik "We need conditional language that forces an independent panel. That gets the council to delay without shutting down community input."

    maya_reyes "Conditionals are slow. People need breathing room today. Tomas needs to know whether to sign the declaration or close up."

    asha_malik "You always fold people's stomachs into your plans. It's why you make them work."
    "The news cycle moves fast. By mid-afternoon, local anchors replay Eli Navarro's photos with Asha's overlays; national outlets pick up the human stories the reporter framed — Tomas stooping behind a cluttered counter that smells of"
    "oil and coffee, Rosa tracing a waterline on a tattered menu where she once stored recipes for storms. The footage is clean but raw. It turns what might have been abstract into a series of faces"
    "the public can name."
    # [Scene: Pier | Late Afternoon]
    hide eli_navarro
    hide maya_reyes
    hide asha_malik

    scene bg ch9_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussive tribal rhythm — the sound of many hands working together]
    # play sound "sfx_placeholder"  # [Sound: Spade against crate, laughter cutting through exertion, waves lapping]
    "You walk the pier as the sky is a softened gold. Volunteers bend into synchronized motion—cordgrass plugs lined like stitches along the shore—planting in patterns you drew up months ago with Eli Navarro at a chalkboard"
    "table. Rosa hands out bowls of hot stew; the scent of cumin and salt fills the air."
    "Tomas stands with a pen shaking only a little as he signs a slim document: a declaration to stay, to adapt, to resist buyouts that would flatten the town’s memory for short-term convenience. When he looks"
    "up, his jaw has the stubborn set your mother's taught you. Pride, hot and private, loosens in your chest."
    show tomas_reyes at left:
        zoom 0.7

    tomas_reyes "Figured I'd do my bit. Can't watch this place get boxed into a memory book."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You staying means everything. It tells other people they don't have to leave yet."

    tomas_reyes "Seems you and Eli Navarro did a thing that gets folks to listen. Don't get smug."
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "Smug is her natural habitat."
    "You laugh, the sound a clean break of sunlight through cloud. The day has been too loud and too long; your eyes sting. Not from salt or wind, but from an emotion that finally has room to breathe: pride, bright and practical."

    menu:
        "Kneel and plant a cordgrass plug with the volunteers":
            "You bend into the mud, fingers learning the new, forgiving rhythm of seeding: push, nestle, pat. The earth takes it in like forgiveness."
        "Stand and hand out bowls with Rosa":
            "You take a ladle, pass steam and sustenance to strangers who are suddenly neighbors in a new way. Rosa squeezes your hand like payment."

    # --- merge ---
    "Evening falls and the council announces a delay pending review."
    "As dusk threads itself along the horizon, council aides call an emergency session: permits will be delayed pending an independent ecological review. It is not the end you wanted — the legal fights will come — but it is a reprieve, a crack in the inevitability Aurelia tried to sell."
    hide tomas_reyes
    hide maya_reyes
    hide eli_navarro

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Rising choir — hopeful, trembling]
    "June Park watches from the edge of the site; she is not defeated. On the contrary, her composure is a line of iron. She catches your eye and gives the faintest of nods — an acknowledgment"
    "that the shape of the battle has changed. There's a hint of something like respect in it, or mere calculation; either way, you accept it as a shift in the tide."
    show june_park at left:
        zoom 0.7

    june_park "This town is resilient. We'll adapt. The methods differ."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We both want people safe. We disagree on what safety asks of the shore."

    june_park "Perhaps. Time will tell. For now, let's ensure any action is informed."
    "Those words are an olive branch and a gauntlet at once. You do not know if she will soften, or simply rearm with finer arguments. The future is still crowded with storms. But victory is not"
    "only about stopping a machine today; it's about changing the terms of the conversation. Today, the terms have changed."
    # [Scene: Old Lighthouse & Tidal Steps | Night]
    hide june_park
    hide maya_reyes

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Warm cello, heartbeat slowing but full]
    # play sound "sfx_placeholder"  # [Sound: Close, regular breaths; the call of a single distant gull]
    "The planting continues in pockets of light beneath strings of bulbs. Volunteers slow; hands are raw. Maya Reyes and Eli Navarro wander past the tidal steps, past the place where you once sketched cross-sections on napkins and argued quietly until the stars came out."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You were brilliant today. Terrifying, but brilliant."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You were the one with photos that made ears perk. And you kept my hands from shaking on that podium."

    eli_navarro "Trade-off. You keep the data honest; I keep people interested."
    "You both stop beneath the lighthouse shadow. For a moment the world narrows to salt, the thud of your pulse, the warmth of his fingers still entwined with yours. The day's triumph — partial, fierce, precarious — settles into something quieter but no less electric."
    "His hand cups your cheek with the sort of care that reads as promise and question all at once. You think of the months of maps and midnight conversations, of the bitterness you once felt when"
    "your science had to be shepherded into palatable language. You think of the town — fragile, stubborn, alive — and how, for today, you helped keep it that way."

    eli_navarro "Stay with me here. Not just in plans. With the planting, with the stubborn parts."

    maya_reyes "I already am."
    "He closes the distance. The kiss is not an erasure of struggle but its seal: a compact between two people who have chosen, against tides and machinery and the gnaw of guilt, to believe in each"
    "other and in the town they love. It is quick, then long; it tastes faintly of sea and stew and the dust of construction. When you part, the lighthouse seems to exhale."
    hide eli_navarro
    hide maya_reyes

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings, then soft resolve]
    "You stand there a while longer, watching teams plant the living shoreline you proposed, watching Rosa pass bowls and Tomas laugh with a neighbor he used to argue with. The fight is far from over: Aurelia's"
    "influence still exists, funding will have to be wrestled to the ground, and policy debates will become the long, grinding work of months and years."
    "Yet something lighter has replaced the old leaden guilt. It is not freedom from responsibility — that will never leave you — but a loosening, a room opening in the chest where pride can sit without"
    "feeling like arrogance. You earned this with other people's hands and with sleepless nights; you can accept it without shame."

    scene bg ch9_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet—distant laughter, the soft slap of tide]
    "You tuck the photograph into your vest and feel Eli Navarro's hand slip into yours once more, easy and sure."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We will keep doing this."
    # play music "music_placeholder"  # [Music: Resolve — a warm, final chord with a hint of open horizon]
    hide maya_reyes

    scene bg ch9_3be532_8 at full_bg

    scene bg ch9_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
