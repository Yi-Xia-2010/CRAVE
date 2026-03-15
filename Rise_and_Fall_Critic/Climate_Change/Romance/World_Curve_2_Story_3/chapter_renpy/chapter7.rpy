label chapter7:

    # [Scene: Tideguard Pavilion — Private Meeting Room | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant traffic of maintenance pumps, the soft whir of climate controls; the sea is a muffled bass beyond the glass]
    # play music "music_placeholder"  # [Music: Low, sparse piano; a slow minor key that keeps time with the tide]
    "You stand in the doorway like someone who doesn't want to close it behind them. The pavilion's glass swallows the harbor light, sharpening the edges of everything inside — polished wood, a line of engineered greenery"
    "in planters that smell faintly of antiseptic and fresh soil, and Cassian sitting as if he had been waiting for you all day."
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "Marin."
    "His blazer is the same slate-gray cut you've seen at public hearings; his expression, under the clean lines of the suit, is softer. It's the kind of softness that makes you want to believe the words that follow."

    cassian_rhee "We can talk in private. No press. No spokespeople. Just the facts, and how we protect this town before the next season."
    "The table is deliberately empty except for his slim tablet. When he taps it, data blooms in layered charts — tide models, projected economic impacts, color bands that feel like inevitabilities. The numbers, the timelines, the"
    "neat lines of projected protection read like a story with a single ending: barriers up, water kept out, lives saved."
    "You smell something metallic under the plant-scent — the faint tang of ozone from the tablet, the corporate-clean air. Your fingers find the compass at your throat without thinking; it is warm with your pulse."
    show marin_sato at right:
        zoom 0.7

    marin_sato "You make it sound simple. Built fast, done right."
    "Cassian leans forward, voice even, the cadence of someone who has convinced himself of the virtue of expedience."

    cassian_rhee "Simple is the wrong word. Immediate. Targeted. Funded. We can mobilize prefabricated harbor barriers within months if permits are expedited. We'll create a corporate trust to manage funds and maintenance. Tideguard will shoulder the upfront costs — your community can have protection now, not after another storm erases what it wants to keep."
    "You can almost see the town behind his words: roofs, boats, Elder Tomas at the edge of the pier, Ivy balancing a crate into place. You can see the boathouse, the hand-lettered maps, the lamp-smudged timber."
    "You can also see blanker things — layoffs, sealed easements, people told to move with a compensation check that reads like a polite dismissal."

    marin_sato "And what does Tideguard ask in return?"
    "Cassian's face is careful now, the pitch measured into negotiable slices."

    cassian_rhee "Legal easements along key stretches for barrier foundations. Expedited permitting. Some symbolic cultural concessions — plaques, a preservation fund for the boathouse, curated access points. Minimal signage of corporate involvement. We won't bulldoze traditions, Marin. We'll stabilize them."
    "The words fall like tidy bricks. You try to build a counter-argument and find your hands empty."

    marin_sato "Easements are not symbolic when they shift who walks the shoreline and how. Expedited permits mean we don't debate who lives where. 'Symbolic' is for the things you can't replace."
    "Cassian watches you, not unkindly."

    cassian_rhee "I know what you've fought for. I went through the community briefings. But there is a choice here between a town that fights and loses, and a town that accepts help and survives. I'm not asking you to sell your soul. I'm asking you to choose life."
    "He speaks as if to a practical mind. His tablet flashes maps where neighborhoods are stamped with different levels of protection — green for immediate fortification, yellow for retrofitting later, red for relocation. In the red zones you can sense the ache of displacement, even without names."
    "A vibration against your thigh makes you glance down. A single-line message from Ariana Voss splits the room into two incoming realities: the pilot timeline, the sounding optimism she wears like armor."
    # play sound "sfx_placeholder"  # [Sound: Soft ping]
    hide cassian_rhee
    hide marin_sato

    scene bg ch7_453e40_2 at full_bg
    "Ariana Voss's hope is a map that draws different lines. She wants time to prove that living infrastructure works at scale. Cassian wants time to build steel fast. You can almost feel the town's breath held between those kinds of clocks."
    "Cassian notices your glance."
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "Ariana Voss's leadership there is promising. Parallel tracks could work — private fortifications where the risk is greatest, pilots where experimental approaches can prove themselves. I don't want to steamroll her work."
    "He says it plainly, with that taut, believable care. Which is what makes your next question heavy."
    show marin_sato at right:
        zoom 0.7

    marin_sato "Who holds the trust? Who audits it? Who gets a vote when maintenance decisions come up?"

    "Cassian flicks another screen and the words come up" "Tideguard Trust — oversight board with municipal representatives (initial seat allocation), third-party auditors, community liaison."

    cassian_rhee "We can make oversight structural. I would propose an independent audit clause, rotational seats for community leaders, and a transparent maintenance ledger available publicly."
    "You want to believe he means it. You want to press him on the details of those clauses — how binding they are, how permanent easements can be revoked, what happens if Tideguard sells the trust"
    "— but with every legal caveat you imagine, Cassian has a counter: a draft amendment, a clause, a feasibility window."
    "Dialogue stretches between you with careful, layered turns. You ask. He answers. You interrupt; he reframes. You accuse; he apologizes with economy."

    marin_sato "If this goes in and Tideguard changes hands, what prevents a new owner from prioritizing profit over small fisheries?"

    cassian_rhee "Governance is the guarantee. We can write performance bonds. We can create staggered transfer clauses. But there is always a risk. Do you want the risk of inaction or the risk of a contract with guardrails?"
    "You taste antiseptic on your tongue — not just the smell in the room but the metallicness of compromise."

    menu:
        "Press for a public clause: insist on a town ratification vote for any final agreement":
            "You push the tablet back slightly, voice tight. Cassian's jaw flexes; he makes a note and says the legal team prefers consensus-building first."
        "Ask for an independent escrow: demand a neutral third-party hold funds until safeguards are proven":
            "You suggest an escrow and how it should be linked to climate performance metrics. Cassian nods slowly, the first genuine concession forming in the air."

    # --- merge ---
    "Cassian softens, and there's an almost-human plea in it."
    "Cassian softens, and there's an almost-human plea in it."

    cassian_rhee "I am trying to buy time for people, Marin. I know the cultural loss that can come with change. But I've seen towns choose debate while the sea erased their options. I'm asking you to be decisive."
    "You remember Elder Tomas's hands — the way they held a carving knife and calmed a splintered hull. The memory is sharp, an accusation and a benediction at once. Ivy's bright vest, bright as an emergency"
    "flare, flashes in your mind. You feel culpability like a bruise forming inside your chest: if you take this deal, the town may be safe in the immediate sense, but some lives will be asked to"
    "move for that safety."
    "Your throat tightens. You think of Lina's pen cutting through statements in print. You think of how her headlines can make a plan a salvation or a sellout."
    "A second soft buzz — Lina's name in your messages. You don't open it. The room narrows to Cassian, the tablet, the plan."

    cassian_rhee "If we delay, funding windows close. Contractors book other projects. Deadlines are real. I have the capital and the engineers. You have the voice to make this palatable. We can memorialize the boathouse; we can fund Tomas's workshop. We can keep Ivy's jobs viable. We just need sign-off to move."

    marin_sato "And if the sign-off includes easements that prohibit small-scale fishing access or requires relocation?"

    cassian_rhee "We can prioritize access points. We can ensure compensation and relocation assistance. Not perfect, but not abandonment."
    "Your hands curl into fists beneath the table. The compulsion to protect the town warps into a trap: to be the person who saves people by giving away the thing that made them who they are. The word that rises, uninvited and hot, is culpability."

    marin_sato "I need guarantees. Public oversight. A clause that makes any permanent change subject to a community referendum within five years. And transparency — all contracts open to local review."
    "Cassian studies you for a long moment. The room seems to inhale."

    cassian_rhee "Those are negotiable. I can't promise everything you ask. But I will put on paper: auditors, community seats, an open ledger, and funding for cultural preservation. I want this to be right, Marin. I want Havenport to be viable."
    "You imagine the harbor with a line of concrete and steel, the gulls half-remembering their flight paths. You imagine people sleeping without the sound of water under them for the first time in years. You imagine other people boxed in by permits, boxed out by price."
    "You feel the rift inside you like a tide cutting the dune. The compass at your throat seems suddenly too small to hold the weight of both futures."

    menu:
        "Demand a written timeline for the living-seawall pilot to run in parallel":
            "You propose a binding pilot window and conditions; Cassian allows a clause, but his smile tightens — he wants the greenlight first."
        "Ask for a cooling-off period: request community review before any permits are filed":
            "You ask for time. Cassian's expression hardens a fraction; he warns funding risks but agrees to consider a short review window."

    # --- merge ---
    "Cassian reaches for a pen and places it between you. It is small, black, deliberate."
    "Cassian reaches for a pen and places it between you. It is small, black, deliberate. The pen looks like a hinge. You can sign a preliminary memorandum that launches the trust and the permits process; you"
    "can ask him to draft changes and return them to the town for ratification. Each option is a blade with a different edge."

    cassian_rhee "I can have counsel draw a memorandum that includes the oversight clauses you want. It would secure funding, begin procurement, and — if you approve — let us begin construction before the next high season. It protects what we can protect now."

    marin_sato "And if I refuse? If I bring this back to a town vote and they say no?"
    "Cassian studies the harbor through the glass, as if the answer is written in the water. His expression is almost apologetic."

    cassian_rhee "Then we wait. We fund what we can privately for the most critical stretches. But I can't guarantee that the protective window will remain open indefinitely."
    "Silence collects in the room like rain in a gutter. There are practical reasons to accept and moral reasons to refuse; both are waiting for the same consequence: the town changed — in some ways preserved, in others rearranged."
    "Your thumb brushes the pen. Your index finger hesitates above the paper where a preliminary remit could be initialed. There is a taste in your mouth that is not the sea nor the plant-scented air —"
    "it's the metallic tang of complicity. You imagine the headlines Lina could write praising the shields. You imagine the quiet list of families who will have to leave. You imagine Ariana Voss's face when she learns"
    "the pilot is sidelined in favor of concrete."
    "Your pulse beats against the brass of the compass at your throat, a small drum keeping time with a choice you were told you didn't have to make alone but somehow must make now."
    "How much autonomy do you trade for safety? How many voices are you authorized to speak for? Who gets to weigh the cost of a life saved against the cost of a history erased?"
    "The pen rests, the tablet waits, Cassian's gaze is patient and expectant. Your chest is a ledger with not enough columns."
    hide cassian_rhee
    hide marin_sato

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant harbor bell; the building's climate system sighs]
    "You lift the pen."
    "You pause with it poised over the paper — a suspended breath."
    "You feel the floor give a fraction as if the town is shifting beneath you in sympathy."
    "You close your eyes for a second and see two possible towns: one with walls and fewer ghosts; one with the shore in flux and more memory. Both demand power you're not sure you have."
    "You do not sign."
    # play music "music_placeholder"  # [Music: A single piano note held and unresolved]

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
