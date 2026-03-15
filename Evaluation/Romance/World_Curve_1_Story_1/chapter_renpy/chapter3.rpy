label chapter3:

    # [Scene: Old Dockside Neighborhood | Early Evening — Storm Window]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain percussion on tin, distant gull calls cut short by wind, a faint municipal siren wailing far off.]
    # play music "music_placeholder"  # [Music: Low, steady guitar motif underscored by hopeful hand-drums]
    "You stand where the lane narrows and the houses lean toward each other like people sharing an umbrella. The air tastes of salt and wet rope; it clings to your cheeks and the seam of your"
    "collar. Somewhere a kettle hisses; a dog barks once and subsides. Rosa's patchwork sandbags—stitched, re-stitched, apologetic in their sag—are stacked along a threshold, a hand-lettered sign wedged into the top that reads KEEP THE DOCKS HOME."
    "Theo is hunched next to a battered sensor array beneath a tarpaulin, breath fogging as he toggles a palm-sized reader. Lightning softens into a bright wash behind the clouds; the reader bleeps like a throat clearing."
    show theo_baines at left:
        zoom 0.7

    theo_baines "This cluster drifted overnight.' (He taps a screen; the glow throws a pale map across his glasses.) 'Calibration's off by a fraction that becomes...notable when you compound it over tidal cycles. It's not just noise. The baseline creep's real, Maya."
    "You feel that word, real, like a weight settling in familiar places—your shoulders, the place where your cuff braids press into the skin. You've been expecting a storm to test plans. You weren't expecting the timeline to speed up."
    show maya_calder at right:
        zoom 0.7

    maya_calder "How much earlier are we talking?"

    theo_baines "Days. Maybe less than a week before the next major window. These misreads masked an uptick. If we don't move fast, higher tides will lap at the worst of the docks during the storm surge. And—' (He swallows, chooses words like tools.) 'Sienna pushed a motion through for an accelerated vote next week. She's framing it as emergency governance."
    "Your mouth tastes of iron and salt. Emergency governance: two words that flatten the world to a map of winners and losses. Sienna's seawall, so often a distant policy diagram in the lab, becomes a machine with teeth that could chew up footpaths and tenancy."
    "From the direction of the promenade, voices splinter into sharper shapes—elders arguing, a younger woman calling for immediate sandbag training, a municipal megaphone that keeps clipping like a skipping record. You move toward the sound because"
    "that's what you do: go where the noise gathers, because that is where people need anchors."
    # [Scene: Community Meeting — Makeshift Tent on the Boardwalk | Night]
    hide theo_baines
    hide maya_calder

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on tarp, murmured disagreement, hands gesturing against the glow of phone screens.]
    # play music "music_placeholder"  # [Music: Guitar motif rises, notes bright and forward]
    "The meeting has exploded into a pressure cooker. Asha is standing on an overturned crate, voice sharpened into organizer-tempo. Elias 'Eli' Maren is near the back, harmonica sheathed but eyes bright; when you glance his way"
    "he squeezes your hand—soil-warm and grounding—and doesn't say anything, which in itself is an answer."
    show asha_patel at left:
        zoom 0.7

    asha_patel "We show what gardens do. We show—' (She points toward the rooftop map.) '—how distributed resilience feeds people and keeps families here. They can't sell us a plan if we don't show an alternative."

    "A woman you recognize from the fish market—her palms flecked with scales—cuts in, voice trembling" "But what if there isn't time to build enough roofs? What if the water rises while we're still proving it works?"
    "The room tilts like a boat in a wake; voices pick up and collide. Someone calls for calm. Someone calls Dr. Sienna Kade a savior; someone calls her a bulldozer. You want to thread each voice into a single fabric, but the fabric is being tugged in too many directions."
    "Dr. Sienna Kade arrives with the light, a set of aides, and a look that's precise as a blueprint. She thanks the room for their time with the soft authority of someone practiced in address. Her"
    "presence narrows into a clean line of policy talk about timelines, metrics, and emergency powers. Her words are efficient; her hands move like a conductor excluding stray notes."
    show dr_sienna_kade at right:
        zoom 0.7

    dr_sienna_kade "An accelerated vote ensures the city can secure funding and deploy protective measures before the next storm window.' (She tilts her head, surveying faces without singling anyone out.) 'I am proposing a plan that prioritizes lives."
    "You study her as you listen. That sentence—prioritizes lives—lands like a stone dropped into a shared pool. You want to believe it. You also smell, under her control, the metallic tang of political expedience."
    show maya_calder at center:
        zoom 0.7

    maya_calder "What about displacement? What about maintaining tenure for long-term residents?"
    "Dr. Sienna Kade's expression is complex; it sits on her face like a closed book. Not a look of anger, not warmth—something that contains both reassurance and something unreadable."

    dr_sienna_kade "There will be provisions. Temporary relocation, compensation frameworks—' (She measures each phrase.) '—but we cannot risk the entire coast stagnating in paralysis because of fear. The votes must move quickly."
    hide asha_patel
    show theo_baines at left:
        zoom 0.7

    theo_baines "Quickly doesn't mean well.' (He steps forward, fingers brushing his coffee cup as though it steadies him.) 'We have data that shows alternatives reduce local risk and preserve occupation. We can overlay green infrastructure and strategic walls."

    dr_sienna_kade "Data helps. Implementation helps more."
    "The room exhales, the debate folding into smaller pockets. Your lungs fill with cool damp. You think of the braided cuff pressing into your wrist, each braid a reminder of what brought you home—Rosa's hands, packed"
    "lunches after long days on water, the smell of mending oil. You will not let those braids be an artifact in a museum of what used to be. They are living threads."
    hide dr_sienna_kade
    show rosa_calder at right:
        zoom 0.7

    rosa_calder "We can teach people to fold a sandbag right. We can teach them to read tide marks. But teaching isn't enough if the sea takes more than we can teach against."

    maya_calder "Then we make the teaching part of the plan. We teach and build and negotiate. Nothing should take home from a family unless we all agree and have a plan to bring them back."
    "Elias 'Eli' Maren moves to the whiteboard, his hands honest and quick. He sketches a rooftop diagram—barrels for rain, raised beds, tie-downs for furniture. He speaks the language of possibility."

    "Elias 'Eli' Maren" "If we get a few signature roofs built, visible, now—people see it, donors see it, and we have a living demonstration instead of a theoretical line graph."
    hide maya_calder
    show asha_patel at center:
        zoom 0.7

    asha_patel "Exactly. A flash demo on the rooftops. We pull a group tonight, film it, and push it to the channels. Show, don't just tell."
    "You feel a small, fierce warmth in your chest. The idea of making something tangible suddenly makes the room quieter, as if everyone has caught the same thread."

    menu:
        "Offer to speak at the flash demo, lead with practical fixes":
            "You volunteer your voice. Asha's face lights with fierce gratitude; Elias 'Eli' Maren claps once, quiet. People look to you for a name to rally behind, and your throat tightens with the weight of it."
        "Stay back and coordinate data logistics with Theo":
            "You step away toward the tech table, and Theo exhales sharply, then grips your shoulder. 'Bring the numbers, we'll build the argument,' he says. Your hands push cold into the reader; the rhythm of the data steadies you."

    # --- merge ---
    "The micro-decision is small but it reframes the immediate action: visibility vs. verification. Both feel necessary. The room fractures into teams, hands sorting tape, people stealing tarps for the roofs. Hope isn't naive; it's practiced, sweaty, and wet from the rain."
    # [Scene Transition: Rooftop Gardens — Night, Wind Picking Up]
    hide theo_baines
    hide rosa_calder
    hide asha_patel

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through leaves, the soft slap of water into barrels, a chorus of murmured cameraphone recordings.]
    # play music "music_placeholder"  # [Music: Guitar motif brightens; percussive hand-drums emphasize forward motion]
    "The flash demo is kinetic. You climb the narrow stair with a hammer and a kit of quick fittings; Elias 'Eli' Maren moves beside you, tying down a wooden crate to a bench with practiced knots."
    "His hands smell of earth and lemon peel. When he leans close to tie a loose string, his breath brushes your ear."

    "Elias 'Eli' Maren" "We make something that shows what staying looks like."
    show maya_calder at left:
        zoom 0.7

    maya_calder "And what staying without getting washed out looks like."
    "He hums, a little tune that could be a promise or a plan. Nearby, cameras are trained on the beds as Asha narrates, her voice crisp and charged with possibility. Theo paces the perimeter with a"
    "laptop, monitoring signal strength. You watch people—neighbors, volunteers, a couple of students from the lab—arriving to help. The scene feels like stitching a community quilt in a storm: hurried, precise, full of love."

    "Someone in the crowd asks a pointed question about scale" "How do you feed everyone when roofs are small? How do you protect people in a surge?"
    "You step forward because the question is real and deserves a real answer. You say what you know—how layered approaches add up, how rain capture prolongs irrigation, how community labor can amplify small plots into networks."
    "You show them a compact model of how a clustered system reduces neighborhood-level risk. Words tumble out—technical and tender."
    "After you speak, Dr. Sienna Kade appears at the edge of the rooftop, hands in coat pockets, watching the demonstration. Her mouth flattens into a line that suggests calculation. She doesn't interject immediately; instead she allows"
    "the audience to see her as listener. When she finally speaks, her voice is measured, possibly testing, possibly finding openings."
    show dr_sienna_kade at right:
        zoom 0.7

    dr_sienna_kade "This is compelling—visceral, even. You build resilience from the ground up. There is merit in the demonstration, Ms. Calder.' (She looks at you in a way that feels like weighing a scale.) 'I would invite you to consider shaping policy from the inside. Work with my team; help map where modular green infrastructure can replace unnecessary sections of wall."
    "The offer is both hand and trap: access to levers you longed for, and the implicit bargain that comes with proximity to power. You sense the room tilting—some faces hopeful, some suspicious. Theo tightens his jaw;"
    "Elias 'Eli' Maren's jaw clenches but his fingers never leave a planting stake. Asha's eyes flash in a way that says calculation and cold-fire optimism."
    "Your chest rocks with an odd hunger: the chance to steer the great machine, to thread the city's official power through the patchwork you are making. But you think of displacement clauses, of boarded-up alleys after"
    "other projects, of the smell of varnish on deals made without reverence. You also think of the children who will not have to move if the right compromises are struck in time."

    menu:
        "Ask Sienna for explicit relocation safeguards before you accept":
            "You ask the question directly; Sienna's face tightens, then smooths. 'We can draft enforceable clauses,' she says, gloved in professional persuasion. The crowd murmurs—some relieved, some skeptical."
        "Thank her, but insist on a joint community-lab pilot before any formal engagement":
            "You propose a hybrid: pilot first, then policy. Asha beams; Theo exhales like someone who has been holding his breath. Dr. Sienna Kade inclines her head—interested, not giving ground."

    # --- merge ---
    "Those micro-choices are small pivots; they do not resolve the massive decision at your ribs, but they offer textures of how you want to be seen—cautious, combative, collaborative. The rooftop hums with practical work, laughter, and the shared clink of toolboxes."
    "You walk the perimeter, hands damp with rain and soil. You think of Rosa's hands folding sandbags—how patient and stubborn she was, how she taught you to fold, press, and knot so that the sand would"
    "stay where it was needed. You think of Theo's red-checked hoodie, of his penchant for metaphors that made data sound like weather. You think of Elias 'Eli' Maren's laugh, the way it fills spaces and makes"
    "them safer."
    "Your internal monologue runs in layered threads: if you join Dr. Sienna Kade, you could embed protections into the wall—actual clauses that tie compensation to return rights, to transitional housing within the neighborhood. If you push"
    "the grassroots route, you could build power of a different kind—narrative, presence, proof by example. If you scale decentralized adaptation, you could keep doors open tonight and mobilize neighbors into immediate safety, but you might lose"
    "voice in the larger infrastructure decisions."
    "None of these choices feel clean. They all promise progress and demand cost. You breathe in the salt-and-earth air and taste the future like rain on your tongue."
    "Elias 'Eli' Maren catches your eye again, and in the brief private exchange there is a small solidarity. He doesn't tell you what to do; he hands you a piece of cloth and says, quietly, 'Tie"
    "it to the railing if you choose. It's a way to promise you'll come back, whatever you decide.'"
    "You blink, the piece of cloth a ridiculous and tender token. Promises are not policy, but they are anchors for the heart."
    "You stand at the edge of the rooftop, rain and possibility on your face. The city is a constellation of small resistances and large machines. The storm will test both. You can feel the decision settling into your ribs—the weight of one lever pulled over another."
    "There is no answer yet. Only the horizon, thick with rain, and the hum of people making things hold."
    # play music "music_placeholder"  # [Music: The guitar motif swells with steady, rising warmth]

    menu:
        "Take Sienna's offer to work inside the lab and shape the seawall.":
            jump chapter4
        "Lead a community-first mobilization with Eli and Asha to force an inclusive plan.":
            jump chapter7
        "Scale decentralized adaptation—build demonstrable rooftop and micro-farm resilience, prioritize local safety.":
            jump chapter10
    return
