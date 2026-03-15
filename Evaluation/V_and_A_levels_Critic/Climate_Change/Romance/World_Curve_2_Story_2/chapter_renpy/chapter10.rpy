label chapter10:

    # [Scene: Rooftop Orchards | Late Afternoon]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the soft thump of irrigators; a creak of rigging]
    # play music "music_placeholder"  # [Music: Low, insistent percussion building tension]
    "You move through the narrow lanes between raised beds, the salt at the airline of your shirt a small, steady reminder of why you are here. From the Floodplain Market to the rooftop orchards, word has"
    "already spread: you decided to stage the living-reef demonstration yourself. The map in your head—parcels, homeowners, the old lighthouse marker—slides into the same rhythm as your breath. There is no turning this tide now."
    "Kai Navarro strides up alongside you, hands full of rope and a grin that fights with strain. Dr. Leila follows, a satchel of sensors clinking; she lets the equipment speak for her worries."
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "You look like you swallowed a gull. Nervous or… focused?"
    show mara_linh_alvarez at right:
        zoom 0.7

    mara_linh_alvarez "Both."
    "Kai Navarro chuckles, but it sounds too quick. He folds a coil of line into the satchel and looks out toward the kelp-platform—small squares of platform and modular reef cages bobbing on the brackish line, crews and volunteers already cutting lines and snapping on grow-bands."
    show dr_leila_osei at center:
        zoom 0.7

    dr_leila_osei "Tide window's narrow. Window's clean—salinity's where we predicted. Sensors green. Mooring tolerances in spec for calm surge, but—"

    dr_leila_osei "You know my but."

    mara_linh_alvarez "I know it. We hedge where we can. We can't wait for 'perfect.'"

    dr_leila_osei "Then we make this as resilient as our margin allows. I calibrated redundancy on the east moor. If the west takes load, we can shed modules in controlled sections."

    kai_navarro "Controlled shedding doesn't feel poetic, but it's honest. We'll mark the primary lines. I'll take the east bow—"

    kai_navarro "—and keep you anchored, Mara."
    "You feel the compass pendant against your sternum—cold brass against warm skin—a small, private steadying. The rooftop thrums with the quiet industry of people choosing to act. The Perfume of seaweed and compost mingles and steadies you; it's a smell you know like a language."

    menu:
        "Run a final line-check with Kai":
            "You drop into a crouch and run your fingers along the primary mooring. The fiber is creased but intact; Kai Navarro murmurs thanks and re-ties one knot with a practiced flick."
        "Give a short speech to steady the volunteers":
            "You climb a low planter edge, voice raised. Your words are short and raw—acknowledgement, call to care, a promise. Heads turn; the volunteers settle with a new pull in their shoulders."

    # --- merge ---
    "'You choose both—because silence feels like betrayal. You ratchet a quick speech into the air, then descend to double-check a line where Kai Navarro needs an extra hand. The options aren't mutually exclusive; they blur into"
    "the work. Dr. Leila hands you a sensor pod and points to a patch of fraying net. You patch it. You tie. You breathe.'"
    hide kai_navarro
    hide mara_linh_alvarez
    hide dr_leila_osei

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured prayers, laughter edged with nerves; a child's cry somewhere below]
    # play music "music_placeholder"  # [Music: Percussion swells slightly]
    "You choose both—because silence feels like betrayal. You ratchet a quick speech into the air, then descend to double-check a line where Kai Navarro needs an extra hand. The options aren't mutually exclusive; they blur into"
    "the work. Dr. Leila hands you a sensor pod and points to a patch of fraying net. You patch it. You tie. You breathe."
    # [Scene: Kelp Farm Platform | Golden Hour]

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wet slap of kelp, the thunk of a mallet, distant human voices sharpening into cheers]
    # play music "music_placeholder"  # [Music: A fragile, hopeful motif overlayed with mounting drums]
    "At first, it looks like success."
    "Kelp unfurls like banners of a slow-rolling victory. Tiny oyster spat cling to seeded frames, sending out pale tongues of life against plastic and rope. Community observers line the raised walkways, faces lit with a thin bloom of joy; someone from the market—Nita—waves a ragged flag."

    "Townsperson" "Look—there! It's actually taking!"
    show mara_linh_alvarez at left:
        zoom 0.7

    mara_linh_alvarez "This is what I pictured on paper, but better. It's messy and alive."
    show kai_navarro at right:
        zoom 0.7

    kai_navarro "Messier is the good kind of real. We should have you drawing diagrams for all of eternity."
    show dr_leila_osei at center:
        zoom 0.7

    dr_leila_osei "Sensors read a clear uptick in biomass accretion. Settlement rates are within predictive bands. If the moorings hold for another tide, we'll get two more data cycles before presentation."
    "You feel buoyed by the numbers—the small, rational scaffolding that leans toward hope. Around you, hands pass buckets, tie off lines, clap shoulders. The town's murmured approval threads into your chest like a belt—support that takes weight."
    "Across the channel, the Blackbrand development site sits like a gray moon on the horizon: cranes poised, chrome segments stacked, hazard lights blinking sterile rhythms. Evelyn Black stands on the site's edge—a shape—then lifts shading hands"
    "to watch. From here her expression is a silhouette of intent. You cannot read the creases at the corner of her mouth: in your mind, they flicker between a calculating thinness and something unreadably close to"
    "concern."
    "You remember the Schrödinger rule the town taught you in practice: where certainty is absent, interpret as complex. Evelyn Black looks…complex. Her figure does not break your spine, but it sits like a weight in your periphery."

    menu:
        "Signal Reverend Sol to temper the crowd":
            "Reverend Sol moves through the watchers with his cane tapping a steady rhythm; his voice softens the vibrations into patience. The crowd breathes with less edge."
        "Let the crowd cheer—ride the momentum":
            "They cheer. The sound swells like a wave you did not shape, and it shakes loose something in your throat: hope, or the start of something you cannot control."

    # --- merge ---
    "'The platform feels alive underfoot—almost breathing. You let the crowd cheer. You let the tide of hope lift you higher because you are trying not to be the person who shuts down possibility. The cheers are a hot thing you swallow, but it helps.'"
    "The platform feels alive underfoot—almost breathing. You let the crowd cheer. You let the tide of hope lift you higher because you are trying not to be the person who shuts down possibility. The cheers are a hot thing you swallow, but it helps."

    dr_leila_osei "Data collected at intervals—perfect. We'll loop the footage into the town presentation. This looks, scientifically, like a demonstrable prototype."

    kai_navarro "We did it."
    "In that pinch of time—fast and fragile—you almost believe it."
    # play sound "sfx_placeholder"  # [Sound: A low, distant hum, like a throat clearing in the sky]
    # play music "music_placeholder"  # [Music: Percussion tightens; elongated strings hint at something coming]
    "Then the weather shifts."
    "You feel it first as a pressure change against your eardrums, like the world inhaling and forgetting the next exhale. Someone curses softly. The sea's surface wrinkles where it should be steady; a bar of darker"
    "cloud moves over the sun like a hand smudging a lamp's glow. The salt wind goes hard."

    dr_leila_osei "That's not in the window—late-season swell. Everyone—secure lines now!"

    kai_navarro "Mara—east bow. Now."
    "You move before you think. Ropes bite your palms. A mooring groans like old wood remembering weight, then steadies. Underfoot, the platform shudders as if the sea undercuts it. You can hear the sound of synthetic fiber screaming."
    # play sound "sfx_placeholder"  # [Sound: A cacophony—metallic snaps, the wet slap of displaced water, shouts layering]
    # play music "music_placeholder"  # [Music: High-tempo drums, discordant strings—the arousal surges into panic]

    kai_navarro "We're seeing twice the predicted load!"

    dr_leila_osei "Automatic shedding—now—let the east modules free on command!"
    "You falter. Letting modules go feels like sacrificing a limb to save a body you cannot be sure will survive. Every knot you release sends a small life tossing into uncertain water."

    mara_linh_alvarez "No—hold for one more cycle!"

    dr_leila_osei "Mara, the sensors show mooring fatigue at sixty-two percent. If we wait—"

    kai_navarro "Then we lose the whole line. Do the math—do it, Mara!"
    "Your hands shake; rope burns your palms. The sound of the gulls is drowned in grit and hydraulic screams. Volunteers stumble as waves shove the platform side to side. A module capsizes in a choke of kelp; volunteers slip—someone cries out."
    "You reach for a secondary tether. The line snaps like a twig. A metallic thud—then the wall of water hits."
    hide mara_linh_alvarez
    hide kai_navarro
    hide dr_leila_osei

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single, long, keening whoosh; then impact—wood splintering, the grinding roar of heavy things dragging]
    # play music "music_placeholder"  # [Music: Collapsing chord; silence only punctuated by sharp, human sounds]
    "Moorings fail en masse."
    "You watch in suspended horror as a cluster of modules—weeks of work, hopes, grant dollars and the town's fragile future—are ripped free. Ropes unwind into the current. Cages spin, algae streaming like a living flag. One frame catches, then shreds. Oyster clusters wash out like clusters of ghosts."
    "Kai Navarro's shout cuts through the chaos—raw, raw—and you can hear the exact note of someone who has just seen a thing they love torn from them."
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "No—no, no—hold!"
    "You lunge. Your boot scrapes, the platform tilts, and your shoulder slams against a winch. Cold spray stings your eyes. You taste metal and the edge of fear."
    show dr_leila_osei at right:
        zoom 0.7

    dr_leila_osei "We can salvage some—if we act now. If we don't—this becomes the clip Evelyn Black uses."
    "Evelyn Black—across the channel—does nothing you can interpret as victory or gloating or pity. She remains a small statue against the crane, watching the modules' dispersed wake with an unreadable tilt to her head. Her mouth is a hard line. The ambiguity bruises you worse than any accusation."
    "Town voices fray into argument and grief. Someone hurls a rope—another rope misses. A child starts to cry and you hear it like an accusation."
    show mara_linh_alvarez at center:
        zoom 0.7

    mara_linh_alvarez "Pull—pull the north line! Drag them into the shallows—hold them until we can patch!"

    kai_navarro "I'm on it—Mara, watch the—"
    "A crash close enough to peel your vision makes you flinch; a platform connector shears with a sound like a bell breaking. Modules slip into the brackish channels, spinning away like small betrayals."
    "For a single, terrible heartbeat you watch the place where the reef should have held—where life should have been given shelter—and see only empty water swallowing plastic and rope and your conviction. The taste in your"
    "mouth is bitter and metallic. The optics will be merciless: footage of a failed demonstration can become propaganda for Blackbrand's case that only hard infrastructure can be trusted."
    "Someone—Dr. Leila, or maybe Reverend Sol—screams your name so loud that the noise ripples through the salt-slick air and finds purchase in your ribs."

    mara_linh_alvarez "Kai—status."

    kai_navarro "We saved a module. Maybe two. Mostly—it's scattered. People are—"
    "He stops. You hear his breath ragged, the sound of someone trying to summon steadiness they don't own."
    "You look out across the channel. The kelp, where it's still attached, whips like a tattered flag. A single panel, a small oyster cluster, holds on to a sliver of rope and bobs like a promise that might not exist."
    "Everything narrows to that bobbing speck."
    # play sound "sfx_placeholder"  # [Sound: Distant, indistinct shouts; an engine starting up; the metallic beep of a sensor failing]
    # play music "music_placeholder"  # [Music: A single descending cello note—sustained and unresolved]
    "You are soaked to the bone. Your hair plastered to your neck. Your palms ache with rope burns and the memory of knots that didn't hold. The town is stunned; some faces are shocked into movement—others into silence so complete you could swear it has weight."
    "Evelyn Black's silhouette remains at the edge of the development site—complex, unreadable—no immediate gesture of triumph, no gloating smile. The ambiguity of her stance presses like sea water against the teeth of the town's resolve."
    "You taste salt and a beginning you hadn't wanted: doubt. Not about the science—you feel certain about the principle—but about scale, timing, the cruelty of testing a prototype under the tyranny of a late-season surge. The"
    "image of modules drifting like flotsam will be the headline tomorrow. It could be the end of what you fought for, or a painful, public lesson."
    "You feel the compass against your sternum, a beaten circle of brass, and you wrap both hands around it as if to hold yourself in place."
    hide kai_navarro
    hide dr_leila_osei
    hide mara_linh_alvarez

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your breathing; a child's soft whimper; a camera somewhere clicks, steady and indifferent]
    # play music "music_placeholder"  # [Music: Tension holds—no resolution]
    "A volunteer staggers toward you, eyes wide with question and accusation and hope bundled together. Kai Navarro's shoulders heave with the effort of staying upright."
    "You have to choose what comes next."

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: A single held chord, aching and unresolved]
    "You stand on the brink—wet, furious, and not yet broken."

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
