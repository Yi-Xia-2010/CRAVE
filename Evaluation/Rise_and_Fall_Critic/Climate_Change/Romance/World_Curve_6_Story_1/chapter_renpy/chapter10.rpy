label chapter10:

    # [Scene: Highland Cliffs Overlook | Dawn]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Slow, ascending strings; a single bright piano motif]
    # play sound "sfx_placeholder"  # [Sound: Wind whispering over grass; gulls calling faintly below]
    "You are here because you chose the middle path—the compromise that keeps both hands in the water. The choice still feels new in your mouth, as if you had just put a coin on a table"
    "and the town might take it or push it away. Dawn presses salt and chill into your hair; the damp loosens the knot you usually tie when you work. Your chest is an odd mixture of"
    "ledger and tide chart: calculations and names, margins of error beside family plots."
    "You step closer to the cliff's edge and let the camera of your mind pan the harbor—solar canopies, the thin line where marsh gives way to open water, the scaffolds where a contractor tentatively measures out"
    "a berm. The light is honest and lean; it highlights the places you want to keep. You touch the compass at your throat without thinking—a small, private ritual that steadies you. It is warm against your"
    "skin."
    "You think of Asha's voice in the council chamber—the clipped logic, the infuriating clarity—and of Jonah's hands in the mud the day he showed you how they planted cordgrass. Your decision was a promise of experiments,"
    "time limits, governance rules, and public dashboards; it is a promise you can both measure and betray. But for now the cliffs smell of sea glass and new rain, and hope tastes like blue morning."

    menu:
        "Call Jonah and walk the northern plots together":
            "You tap his number, hesitating only a second before you press. Jonah answers with a sleep-rough laugh; his voice is an anchor. He tells you he'll meet you at the northern access in twenty minutes, and the line goes soft with that small, ordinary agreement."
        "Sit and wait — make notes in silence":
            "You take the field notebook from your jacket and let the pen find the page. The first lines are messy, but they are yours; they map wind directions, solar angles, and a quiet list of things to say to Asha and to the town. You feel the logic of it arranging itself into a shape you can carry."

    # --- merge ---
    "Continue main narrative"

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell softly, then settle into a steady rhythm]
    "Jonah Reyes arrives smelling of coffee and diesel, cheeks windburned. He does not break your silence with a speech; instead he offers you a thermos and the smallest, wry grin you know well."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You always pick the coldest, windiest places to think. Did you bring me along to keep me from talking you into building a fortress?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I brought you to make sure I don't build a fortress that nobody will live behind. Compromise isn't architecture, Jonah. It's paperwork and patience."

    jonah_reyes "Paperwork is fine. It's the patience part I'm not sure we'll have. People get tired of trials when the tide keeps coming."

    mira_kestrel "Then we'll measure faster. We'll prove what works so the patience has reason."
    "The exchange is small but deep. Words between you are like stakes in sand—easily disturbed, but when placed with care they hold for a season."
    # [Scene: Greenhouse Collective | Morning]
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled laughter, the rustle of soil, a radio playing a cautious upbeat tune]
    # play music "music_placeholder"  # [Music: Light acoustic guitar; optimistic undertones]
    "Dr. Lian Zhou is already there, knees dirty, looking at tethered sensor arrays as if they were delicate instruments of an orchestra."
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "If we pair the berm with a living shoreline, we can run matched comparisons: erosion rates, invertebrate colonization, bird usage. We set identical monitoring windows and…"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "And the governance terms lock in community control of the data and hiring preferences. Evelyn insisted on a public dashboard and Bento wanted veto powers written into the pilot terms."

    dr_lian_zhou "Open data will encourage replicability. If Tidehaven's dashboard is transparent, other towns can adapt faster."
    "You feel the thrill of language aligning—science, law, and local memory forming a single sentence."
    "Evelyn arrives mid-sentence, hands full of petition copies and a thermos tag on her coat that smells faintly of the town hall's lamp oil."
    show evelyn_sato at center:
        zoom 0.7

    evelyn_sato "Dawn meetings will always be my favorite. Less performative, more honest. The council signed off on the seed funding for the paired plots this morning—conditional on the timeline and the dashboard. People want to watch this work."

    mira_kestrel "We'll give them metrics and stories, Evelyn. We'll make the dashboards show more than numbers—photos, weekly notes, a place for neighbors to post observations."

    evelyn_sato "That’s what will make it stick."
    "Kai sweeps in, energy like compressed spring: flyers in one hand, seed trays in the other."
    hide dr_lian_zhou
    show kai_tan at left:
        zoom 0.7

    kai_tan "We're running a planting drive Saturday. If we get the collective to plant the living shoreline, it's harder to hand it off to private interests later."

    mira_kestrel "We seed it together. The Greenhouse seeds both plots—cordgrass for the living edge, salt-tolerant sedges for the berm transition strips. We label everything so the dashboard can show the exact day each plug went in."

    menu:
        "Pick the cordgrass packet with the oldest provenance":
            "You choose the packet with the handwriting you recognize from Old Bento's notes—heritage strains he swore performed well here. It feels like a small, sacred trust put back into the soil."
        "Pick the experimental mix Dr. Lian recommends":
            "You pick the experimental mix. Dr. Lian's eyes light up; she tucks the packet into your palm like a promise. It is science betting on resilience."

    # --- merge ---
    "Continue main narrative"
    # play sound "sfx_placeholder"  # [Sound: Hands digging, the soft slap of soil; someone hums tunelessly]
    # play music "music_placeholder"  # [Music: Guitar picks a hopeful motif; strings return]
    "Bento arrives a little later, slower in his movements but precise in what he says and where he puts his hands. He runs them over a chart, lays a palm on the proposed governance draft."
    hide mira_kestrel
    show bento_old_bento_morais at right:
        zoom 0.7

    bento_old_bento_morais "If you put the word 'veto' in there, make sure it's real. People who remember storms don't want their traditions listed as footnotes. And if the town's hiring preference becomes a paragraph, make sure it isn't just a paragraph."
    hide evelyn_sato
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "We wrote hiring provisions and a community oversight board into the draft. We made the veto process layered—transparent triggers. Not a unilateral 'no,' but a process for adjudication that centers local knowledge."

    bento_old_bento_morais "Good. Memory and method. That might keep it from feeling like another thing taken from us."
    hide kai_tan
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "And we'll publish the first datasets weekly. Photographs from Jonah's camera and community-submitted observations will sit beside the tide and turbidity numbers."
    hide bento_old_bento_morais
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "If you put my photos up, I get to write the captions. 'Jonah’s daily hero shots'—that's a public service."
    "Mira Kestrel laughs, and the sound feels like a practical stitch. The greenhouse smells of damp peat and something green and living—the precise aroma of a thing someone can still nurture."
    # [Scene: Paired Pilot Plots | Afternoon to Dusk (series of montages)]
    hide mira_kestrel
    hide dr_lian_zhou
    hide jonah_reyes

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Heavy machinery muted to a steady thrum; community chatter, the clink of shovels, gulls returning in arcs]
    # play music "music_placeholder"  # [Music: Rhythmic strings, rising in tempo and warmth]
    "Dr. Lian and you place sensor nodes along the two plots. Each node clicks into place, a small electronic heart that will pulse and tell a story across seasons. The sea-gate contractor—an efficient woman in a"
    "high-visibility jacket—comes to talk compromise: dampening her original plan, elongating the berm to leave tidal corridors, and incorporating vegetated setbacks where feasible."

    "Sea-gate Contractor" "We can phase the gate. Test the mechanical thresholds as the living edge develops. We don't have to hardline this from day one."
    "Asha Verma appears, sleeves rolled, the lines around her eyes softer than they had been in the council chamber."
    show asha_verma at left:
        zoom 0.7

    asha_verma "A time-limited trial is acceptable if we retain the capacity to scale up. I want defined success metrics."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Then metrics we will give you—erosion change, habitat return, maintenance costs, and social measures: job creation, community satisfaction. We commit to reporting monthly."
    "Asha Verma: [brief, unreadable] 'Then begin.'"
    "The exchange is tight, professional, and not without friction—but the friction is refining, not breaking. It is the sound of metal being filed into useful shapes."
    hide asha_verma
    hide mira_kestrel

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, song, the slap of boots in mud; someone plays an old sea shanty on a battered radio]
    # play music "music_placeholder"  # [Music: Layered harmonies, a hopeful chorus under the montage]
    "Night settles with work lights humming. Jonahs' camera clicks—Polaroids taped to a temporary board—with hand-scrawled dates. Mira Kestrel and Jonah Reyes share a late-night bowl of something rich and salty during a break between surveys. Your conversation loops like the tide: practical details, then small flashes of memory."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You remember when Bento taught me to knot net lines? He said a good knot makes a small promise. Maybe we need more good knots."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Knots hold when everything else pulls. Maybe that's what we're building—connections that can take a load."

    jonah_reyes "And people. That's the part I was scared the most about losing. If this is going to be for the town, it has to be of the town."

    mira_kestrel "It is. That's the whole point."
    "You both fall quiet, fed and tired, and the silence is companionable. It is the kind of evening that feels like repair—gradual, mutual, deliberate."
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls; the tide moves in with a soft, steady hush]
    # play music "music_placeholder"  # [Music: Piano motif returns, gentle and luminescent]
    "Weeks pass in a braided rhythm: data streams in, code and human notes side by side on the dashboard; Dr. Lian pilots a model update; Kai organizes a volunteer planting day that fills the living plot"
    "with neighbors; Evelyn posts weekly summaries on the town's noticeboard. The first gulls begin to use the restored marsh as a roost—a small, unequivocal sign of life returning."
    "You go home with mud under your nails more often than you would have expected. Your notebook blossoms with apologies written and unread, with minutes, with tide charts, and the plain record of work. The town is busy and fragile and, importantly, moving."

    menu:
        "Upload a Polaroid to the dashboard with a personal note":
            "You scan Jonah's Polaroid and write a short note: 'Day 34: first gulls returning to the restored marsh. Small things, held together.' The dashboard shows it under 'Field Notes' and receives a handful of comments—thank-yous, memories, and one small worried question. It is exactly the conversation you wanted."
        "Let the data speak alone — post only the metrics":
            "You post the tide and turbidity graphs without commentary. The numbers look clean and professional; the town's reply is sparse but analytical. It is useful, but not warm. You tuck the Polaroid into your notebook instead."

    # --- merge ---
    "Continue main narrative"
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings; a sense of steady momentum]
    "The pilot, for a while, works. The berm shows reduced overtopping in one scenario; the living shoreline binds sediment and hosts small invertebrates earlier than the models predicted. The sea-gate contractor finds a design compromise; Asha"
    "Verma, who had insisted on precise triggers, sits in the field one afternoon with a thermos and says quietly:"
    show asha_verma at left:
        zoom 0.7

    asha_verma "You backed me into a limit I hadn't wanted to accept—time. Now I can see the value of trying things where we can observe them."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "And you kept the option to act if the data points the wrong way."

    asha_verma "Yes."
    "Her reaction is compact—professional, layered—what you have learned to translate as respect in her language. It is not warmth, but it carries the quiet pressure of someone who has come to believe in a process she once mistrusted."
    "Bento watches the first public meeting to review pilot data and taps his fingers against the council table. His thumbs brush a Polaroid Jonah has taken of a child planting cordgrass."
    show bento_old_bento_morais at center:
        zoom 0.7

    bento_old_bento_morais "Careful with these images in documents,' he says. 'They are not only evidence, they are claims."

    mira_kestrel "Exactly. Which is why we include people's voices. Not just numbers."

    bento_old_bento_morais "Good. Let them be claims then—claims of care."
    # play music "music_placeholder"  # [Music: Crescendo to a bright chord; then a held, hopeful note]
    # play sound "sfx_placeholder"  # [Sound: A chorus of community voices fades into the breeze]
    "You record more than metrics in your notebook now. You record moments: a contractor altering a blueprint, an elder pointing to a line on a map and saying, 'We remember when that house used to be"
    "on stilts,' a school group naming a restored patch 'Mira's Meadow' in a child's handwriting that makes you ache in a good way. You find yourself smiling more in the margins."
    "The work is still hard. There are hiccups—sensor malfunctions, one patch of cordgrass that fails, a late council member who wants to accelerate the gate. But the overall curve is up. The pilot gives everyone something they can touch: data, photographs, living roots."
    # [Scene Transition: Dusk at the Paired Plots | The air is cool; the lights of the town begin to blink awake]
    hide asha_verma
    hide mira_kestrel
    hide bento_old_bento_morais

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Piano and strings, a single luminous chord that suggests continuation rather than conclusion]
    # play sound "sfx_placeholder"  # [Sound: Night insects, the distant ring of a bell]
    "You stand at the edge of the living plot, palms dirty, heart steady. The dashboard shows a modest but meaningful trend. Jonah Reyes stands beside you, shoulders relaxed in a way they hadn't been weeks before."
    "Asha Verma's clipped messages have become fewer and more collaborative. Evelyn posts the weekly dashboard link to the council and the town listserv; people comment and sometimes argue, but they do so on the same page."
    "You allow yourself a rare, deliberate inhale. This is not triumphal—it's pragmatic. It is a day of small victories stitched into a larger fabric. The town moves in a direction you can quantify and defend, and you have a hand in steering it."
    # [Page-Turn Moment]
    "You run a finger along the salt-stained edge of your notebook, tracing the spiral of meetings and misgivings, the signatures and the coffee rings. Outside, the harbor breathes in and out like a living thing, and"
    "somewhere beyond the immediate warmth of lamps and timers, the political wind shifts. There will be votes and press and people who demand faster answers. For now, though, tide and trial are in your favor; for"
    "now, the work is visible and the town is participating."
    "You make a note: 'Prepare briefing for council—highlight metrics, human stories, escalation triggers.' You close the notebook and feel an unexpected calm. There will be crosswinds ahead—politics will stir the trial into something louder—but tonight the community has a scaffold it can stand on."
    # play music "music_placeholder"  # [Music: A single bright piano chord held, then tapering into a hopeful hush]

    scene bg ch10_453e40_8 at full_bg

    scene bg ch10_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
